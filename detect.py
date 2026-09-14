import argparse, json, time
from pathlib import Path
import cv2
from ultralytics import YOLO

VEHICLES = {"car", "motorcycle", "bus", "truck"}

def level(n, low, high):
    return "LOW" if n < low else "MEDIUM" if n < high else "HIGH"

def inside(x, y, r):
    rx, ry, rw, rh = r
    return rx <= x <= rx+rw and ry <= y <= ry+rh

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", default="data/road.mp4")
    p.add_argument("--model", default="yolo11n.pt")
    p.add_argument("--conf", type=float, default=0.35)
    p.add_argument("--low", type=int, default=8)
    p.add_argument("--high", type=int, default=18)
    p.add_argument("--show", action="store_true")
    a = p.parse_args()

    source = int(a.source) if str(a.source).isdigit() else a.source
    out = Path("outputs"); out.mkdir(exist_ok=True)
    model = YOLO(a.model)
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise FileNotFoundError("Could not open source. Add data/road.mp4 or use --source 0.")

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) or 1280
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) or 720
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    writer = cv2.VideoWriter(str(out/"annotated_output.mp4"), cv2.VideoWriter_fourcc(*"mp4v"), fps, (w,h))
    zone = (0, int(h*.72), w, int(h*.28))

    frames = total = peak = 0
    levels = {"LOW":0,"MEDIUM":0,"HIGH":0}
    start = time.time()

    while True:
        ok, frame = cap.read()
        if not ok: break
        frames += 1
        px,py,pw,ph = zone
        cv2.rectangle(frame,(px,py),(px+pw,py+ph),(0,165,255),2)
        cv2.putText(frame,"ROADSIDE PARKING ZONE",(10,py+28),cv2.FONT_HERSHEY_SIMPLEX,.7,(0,165,255),2)

        count = parked = 0
        result = model(frame, conf=a.conf, verbose=False)[0]
        if result.boxes is not None:
            for b in result.boxes:
                name = model.names[int(b.cls[0])]
                if name not in VEHICLES: continue
                conf = float(b.conf[0])
                x1,y1,x2,y2 = map(int,b.xyxy[0].tolist())
                cx,cy=(x1+x2)//2,(y1+y2)//2
                count += 1
                is_parked = inside(cx,cy,zone)
                parked += int(is_parked)
                color=(0,165,255) if is_parked else (0,220,0)
                label=f"{name} {conf:.2f}" + (" | PARKING ZONE" if is_parked else "")
                cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
                cv2.putText(frame,label,(x1,max(25,y1-8)),cv2.FONT_HERSHEY_SIMPLEX,.5,color,2)

        traffic = level(count,a.low,a.high)
        levels[traffic]+=1; total+=count; peak=max(peak,count)
        for i,t in enumerate([f"Vehicles: {count}",f"Parking-zone vehicles: {parked}",f"Congestion: {traffic}"]):
            cv2.putText(frame,t,(20,40+i*35),cv2.FONT_HERSHEY_SIMPLEX,.85,(255,255,255),3)
            cv2.putText(frame,t,(20,40+i*35),cv2.FONT_HERSHEY_SIMPLEX,.85,(20,20,20),1)

        writer.write(frame)
        if a.show:
            cv2.imshow("SmartRoad AI",frame)
            if cv2.waitKey(1)&0xFF==ord("q"): break

    cap.release(); writer.release(); cv2.destroyAllWindows()
    summary={"frames_processed":frames,"processing_seconds":round(time.time()-start,2),
             "average_vehicle_detections_per_frame":round(total/max(frames,1),2),
             "peak_vehicles_in_frame":peak,"congestion_frame_counts":levels,
             "thresholds":{"low":a.low,"high":a.high},
             "note":"Per-frame detections are not unique tracked vehicles."}
    (out/"summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
