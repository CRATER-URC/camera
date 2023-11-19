
import cv2
import time


camera = cv2.VideoCapture(0)
prev_time = time.time()

while True:
    
    ret, frame = camera.read()
    cv2.imshow('Camera Feed', frame)
    current_time = time.time()
    elapsed_time = current_time - prev_time

    # frames per second fps
    fps = 1 / elapsed_time

    #assuming 8 bits per channel
    print(f"FPS: {fps:.2f}, Bandwidth: {fps * frame.size * 3 / 1024 / 1024:.2f} Mbps")
   
    prev_time = current_time

    # Break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


camera.release()
cv2.destroyAllWindows()
