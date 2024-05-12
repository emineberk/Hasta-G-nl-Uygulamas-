import random # rastgele bir öneri almak için randomu import edip randint metodunu kullandık
yasak_kelimeler = ["alışveriş", "tekrar", "kumar", "içki", "bahis"]#Bu listede yasaklı kelimeleri yazdık

kontrol_kelimeler= False #Yasaklı kelimeler için bayrak olarak kullandık.
girdi = input(" bugünün günlüğünü yazınız:")#Kullanıcıdan girdi alırız.

kelimeler = girdi.split()#Girdideki kelimeler bir listeye ayrılır

oneriler=["yürüyüşe çıkmalıyız","kitap okuyabiliriz","müzik dinleyebiliriz","sohbet edebiliriz"]
#Eğer bu listede yasaklı kelimeler varsa öneride bulunur.

for i in kelimeler:#kullanıcının girdiği her bir kelimeyi bu döngü ile kontrol ederiz.
    if i in yasak_kelimeler:#
        kontrol_kelimeler= True
        break#Yasaklı kelimler bulunduğunda döngü sonlandırılır.
        
if ( kontrol_kelimeler == True):#Eğer yasaklı kelime bulunduysa ,kullanıcıya bir uyarı ve öneri verir.
    print (" Bu konuda gerçekten biriyle konuşmanız gerekiyor, veya {}".format(oneriler[random.randint(0,len (oneriler)-1)]))
       #random.randint(0, len(oneriler)-1)  ile öneriler listesinden rastgele bir öneri seçiyoruz.   
else:
    print(" Blogunuzu güncellediğiniz için teşekkür ederiz")
#Yasaklı kelime bulunmuyorsa bu çıktıyı alırız