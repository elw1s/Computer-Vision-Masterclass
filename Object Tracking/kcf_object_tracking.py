import cv2

tracker = cv2.TrackerKCF_create()

video = cv2.VideoCapture('race.mp4')

ret, frame = video.read()

bbox = cv2.selectROI(frame)

ok = tracker.init(frame, bbox)

while True:
  ret, frame = video.read()
  if not ret:
    break
  ret, bbox = tracker.update(frame)

  if ret:
    (x, y, w, h) = [int(v) for v in bbox]
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2, 1)
  else:
    cv2.putText(frame, 'Error', (100,80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

  cv2.imshow('Frame',frame)

  if cv2.waitKey(1) & 0xFF == 27:
    break