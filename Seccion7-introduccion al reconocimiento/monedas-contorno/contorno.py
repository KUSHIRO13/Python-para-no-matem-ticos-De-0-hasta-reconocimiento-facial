import cv2

#Imagenes
imagen = cv2.imread("contorno.jpg")
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY_INV)
contorno,jerarquia = cv2.findContours(umbral,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(251,60,50),3)

cv2.imshow("Image original",imagen)
#cv2.imshow("Image en grises",grises)
#cv2.imshow("Image en umbral",umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()