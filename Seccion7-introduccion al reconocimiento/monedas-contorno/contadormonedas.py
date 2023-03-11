import cv2
import numpy as np

varGauss = 3
varkernel = 3

origen = cv2.imread("monedas-colombianas.jpg")
gris = cv2.cvtColor(origen,cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris,(varGauss,varGauss), 0)
borde = cv2.Canny(gauss,60,100)
kernel = np.ones((varkernel,varkernel),np.uint8)
cierre = cv2.morphologyEx(borde,cv2.MORPH_CLOSE,kernel)

contorno,jerarquia = cv2.findContours(cierre.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print("Monedas escontradas: {}".format(len(contorno)))
cv2.drawContours(origen,contorno,-1,(0,0,255),2)

#Mostrar
cv2.imshow("Monedas",origen)
cv2.imshow("Grises",gris)
cv2.imshow("Gauss",gauss)
cv2.imshow("Canny",borde)
cv2.imshow("Cierre",cierre)
cv2.waitKey(0)
cv2.destroyAllWindows()
