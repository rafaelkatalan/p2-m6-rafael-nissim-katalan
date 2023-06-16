import cv2

# Abre o arquivo de video
video_capture = cv2.VideoCapture('./final.avi')

# Checa se foi possivel abrir o arquivo
if not video_capture.isOpened():
    print("Error opening video file")
    exit(1)

# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = video_capture.read()

    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break

    # Exibe o frame
    cv2.imshow('Video Playback', frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
video_capture.release()
cv2.destroyAllWindows()