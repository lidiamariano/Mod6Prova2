import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

input_dir = '../frames'
output_dir = '../frames_detected/'

os.makedirs(output_dir, exist_ok=True)

for i in range(189): 
    img_path = os.path.join(input_dir, f'{i}.png')
    img = cv2.imread(img_path)

    if img is None:
        print(f'Não foi possível ler a imagem: {img_path}')
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    output_path = os.path.join(output_dir, f'{i}_detected.png')
    cv2.imwrite(output_path, img)

    print(f'Processada e salva: {output_path}')
