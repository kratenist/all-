a =  input("İSMİNİ GİR : ")
b = int(input("YAŞINI GİR : "))

print((a),"TAM BİR MAL VE GİRDİĞİ YAŞ : ")
if b < 18 :
    print("VELET YAŞI : ",(b))
else :
    print(b)
c = int(input("OKUL ORT Girin : "))
if c == 0 or c <= 49:
    print("BAŞARISIZ")
elif c == 50 or c <= 59:
    print("GEÇER")
elif c == 60 or c <= 69:
    print("ORTA")
elif c == 70 or c <= 84:
    print("İYİ")
elif c == 85 or c <= 100:
    print("PEKİYİ")
elif c < 0 or c > 100:
    print("HATALI NOT")

