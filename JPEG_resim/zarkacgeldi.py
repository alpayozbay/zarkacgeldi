import cv2
import sys

#Resmi Oku
zarresmi = cv2.imread(sys.argv[1])

#Resim Eşiğini Al
ret,thresh = cv2.threshold(zarresmi,75,75,75)

#Yüzler
zarınyüzü = ['BiR','iKi','UC','DORT','BES','ALTI']

# Eşik Resmi Bulanıklaştır - Gaussian Blur
bulanıkresim = cv2.GaussianBlur(thresh, (7,7), 0)

# Canny algoritması ile kenarları belirle
kenarbelirlenmiş = cv2.Canny(bulanıkresim, 10, 525)

im, contours, hierarchy= cv2.findContours(kenarbelirlenmiş, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

t = len(contours)
print("Zarın Gelen Yüzü = ", t)

cv2.drawContours(zarresmi, contours, -1, (0,255,0), 2)
cv2.imshow(zarınyüzü[t-1], zarresmi)




cv2.waitKey(0)
