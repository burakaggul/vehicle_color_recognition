import cv2
from PIL import Image
image_color = cv2.imread('C:/Users/MacBookPro/Desktop/uakk/test (57).jpg',cv2.IMREAD_COLOR)
cv2.imshow("Orjinal", image_color)
image_color = cv2.resize(image_color, (600,450))
cv2.imshow("Resize Image", image_color)
yukseklik = image_color.shape[0]
genislik = image_color.shape[1]
print('Resim Yüksekliği (px):', yukseklik)
print('Resim Genişliği  (px):', genislik)
cropped = image_color[150:int(yukseklik-100), 100:int(genislik-100)]
b_1 = int(cropped.item(150, 100, 0))
g_1 = int(cropped.item(150, 100, 1))
r_1 = int(cropped.item(150, 100, 2))   
cv2.imshow("Crop_Image", cropped)
ort_b = int(b_1)
ort_g = int(g_1)
ort_r = int(r_1)
if (180<=ort_b and ort_b<255 and 180<=ort_g and ort_g<255 and 160<=ort_r and ort_r<255):
    arac_r = "Beyaz"
    print("Aracın Rengi         :",arac_r)   
elif (110<ort_b and ort_b<150 and 110<ort_g and ort_g<150 and 110<ort_r and ort_r<150):
    arac_r = "Füme"
    print("Aracın Rengi         :",arac_r)      
elif (150<ort_b and ort_b<180 and 150<ort_g and ort_g<180 and 150<ort_r and ort_r<160):
    arac_r = "Gri"
    print("Aracın Rengi         :",arac_r)          
elif (130<ort_b and ort_b<255 and 25<ort_g and ort_g<150 and 0<ort_r and ort_r<150):
    arac_r = "Lacivert"
    print("Aracın Rengi         :",arac_r)
elif (0<ort_b and ort_b<150 and 0<ort_g and ort_g<150 and 100<ort_r and ort_r<255):
    arac_r = "Kırmızı"
    print("Aracın Rengi         :",arac_r)      
elif (ort_b<=110 and ort_g<110 and ort_r<110):
    arac_r = "Siyah"
    print("Aracın Rengi         :",arac_r)   
print("Ortalama BGR Değeri  :",ort_b,ort_g,ort_r,)
cv2.waitKey(0)
cv2.destroyAllWindows()



