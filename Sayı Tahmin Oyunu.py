"""
Kod tarafından rastgele atanan bir sayıyı
klavyeden girilen sayılar aracılığıyla
tahmin eden ve doğru sonuca kaç adımda varıldığını
yazan alg.
"""
import random

sayı=random.randint(1, 100)
sayac=5
print("1-100 arasında bir sayı tuttum tahmin et")

yanıt=int(input("1-100 arası bir sayı girin: "))
while sayac>0:
    
    if yanıt>sayı:
        print("daha kucuk bir sayı girmelisin\n")
        sayac=sayac-1
        print(sayac,"hakkın kaldı")
        yanıt=int(input("yeni tahmininizi giriniz:"))
    elif yanıt<sayı:
        print("daha buyuk bir sayı girmelisin\n")
        sayac=sayac-1
        print(sayac,"hakkın kaldı")
        yanıt=int(input("yeni tahmininizi giriniz:"))
    else:
        print("tebrikler tuttugum sayıyı bildin") 
        break
    
print("\nbilemedin")
    