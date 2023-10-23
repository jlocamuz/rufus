import cv2

# Cargar la imagen
img = cv2.imread("/Users/julialocamuz/Documents/rufus/menus/WhatsApp Image 2023-05-07 at 15.01.08.jpeg", cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Realizar la umbralización
umbral = 128  # Ajusta este valor según tus necesidades
_, img_expuesta = cv2.threshold(gray, umbral, 255, cv2.THRESH_BINARY)

# Convertir la imagen de umbralización a RGB
img_expuesta_rgb = cv2.cvtColor(img_expuesta, cv2.COLOR_GRAY2BGR)

# Fusionar la imagen original y la imagen de umbralización
img_fusionada = cv2.addWeighted(img, 0.5, img_expuesta_rgb, 0.5, 0)

cv2.imshow("Región de Texto Recortada", img_fusionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
