import cv2
import sys

#Resmi Oku
zarresmi = cv2.imread(sys.argv[1])
cv2.imshow(sys.argv[1], zarresmi)

#Yüzler
zarınyüzü = ['BiR','iKi','UC','DORT','BES','ALTI']

# Resmi Gri Tonlamaya Çevir
griresim = cv2.cvtColor(zarresmi, cv2.COLOR_BGR2GRAY)

# Gri Tonlama Resmi Bulanıklaştır - Gaussian Blur
bulanıkresim = cv2.GaussianBlur(griresim, (7,7), 0)

# Canny algoritması ile kenarları belirle
kenarbelirlenmiş = cv2.Canny(bulanıkresim, 30, 100)

im, contours, hierarchy= cv2.findContours(kenarbelirlenmiş, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

t = len(contours)
print("Zarın Gelen Yüzü = ", t)

cv2.drawContours(zarresmi, contours, -1, (0,255,0), 2)
cv2.imshow(zarınyüzü[t-1], zarresmi)
cv2.waitKey(0)
