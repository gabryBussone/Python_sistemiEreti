import cv2

# Carica il classificatore preaddestrato per il riconoscimento del corpo intero
body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Inizializza il modulo di acquisizione video
cap = cv2.VideoCapture(0)  # 0 indica la fotocamera predefinita

while True:
    # Leggi il frame dalla fotocamera
    ret, frame = cap.read()

    # Converti il frame in scala di grigi
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Rileva i corpi nel frame
    bodies = body_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Disegna i rettangoli intorno ai corpi rilevati
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostra il frame con i rettangoli disegnati
    cv2.imshow('Body Detection', frame)

    # Interrompi il loop quando si preme 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia le risorse quando il programma termina
cap.release()
cv2.destroyAllWindows()
