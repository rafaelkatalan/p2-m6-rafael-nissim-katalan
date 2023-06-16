import cv2
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

# Abre o arquivo de video
cap = cv2.VideoCapture('./arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not cap.isOpened():
    print("Error opening video file")
    exit(1)
    
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv2.VideoWriter( './final.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model.predict(frame, save = False, conf=0.7, classes = 0, hide_labels = True)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow("frame", annotated_frame)

        output_video.write(annotated_frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(30) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
output_video.release()
cv2.destroyAllWindows()