 
toplam=0
while True:
  sayi = float(input("Bir sayı girin: "))
  if sayi ==0:
    break
  toplam+=sayi
print("Girdiğiniz sayıları toplamı: ",toplam)

"""
from random import randint
 
rand=randint(1, 100)
sayac=0
 
while True:
    sayac+=1
    sayi=int(input("1 ile 100 arasında değer girin (0 Çıkış):"))
    if(sayi==0):0
    
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < rand:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > rand:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print("Rastele seçilen sayı {0}!".format(rand))
        print("Tahmin sayınız {0}".format(sayac))

#SINAV NOT
a = int(input("Sınav Notuzu Girin : "))
if a == 0 or a <= 49:
    print("BAŞARISIZ")
elif a == 50 or a <= 59:
    print("GEÇER")
elif a == 60 or a <= 69:
    print("ORTA")
elif a == 70 or a <= 84:
    print("İYİ")
elif a == 85 or a <= 100:
    print("PEKİYİ")
elif a < 0 or a > 100:
    print("HATALI NOT")





#TEKMİ ÇİFTMİ
sayi = int(input("Sayı Girin : "))
if sayi%2 == 0 :
    print((sayi),"Bu Sayı ÇİFT")
else:
    print((sayi)," , Bu Sayi TEK")
"""
