
liste=[1,2,3,1,2,3]               #Liste
tuuple=(1,2,3)               #Tuple
kume = {1,2,3,2,1,3}      # kumelerde aynı olanlar sadece 1 defa gecer


print(liste)
#  cıkıs -->    [1, 2, 3, 1, 2, 3]
print(tuuple)
#  cıkıs --> (1, 2, 3)
print (kume)
#   cıkıs -->   {1,2,3}    rastgele sırayla yazdırır kumeler

kume2=set(liste)        # listeyı kumeye cevırmeye yarar set komutu

kume3=set([1,2,3,1,5,32])

print(kume2)
#   cıkıs --> {1,2,3}        yukarda yazdıgımız gıbı kumeler aynı elemanda yanlızca sadece 1nı alır
print(kume3)
# cıkıs --> {32, 1, 2, 3, 5}  toplamda 4 tane 1 olmasına ragmen sadec 1 tanesını alır rastgele yazar

kume4=set('Umutgecer')  # Kumeye cevırmek ıcın set komutunu kullanıyorduk
kume5=set("murıyeksel")

print(kume4)    # Buyuk ve kucuk harfı aynı saymaz dıkkat edılmesı gerekır
#   cıkıs -->   {'g', 't', 'U', 'm', 'e', 'c', 'r', 'u'}

print(kume5)
#   cıkıs -->   {'e', 's', 'l', 'ı', 'u', 'k', 'r', 'm', 'y'}

print(kume4|kume5)      # iki kumeyı bırlestırme ıslemi yapar tekrarlı elemanları atar.
#   cıkıs -->   {'e', 's', 'l', 'u', 'g', 'c', 't', 'k', 'y', 'ı', 'r', 'm'}

print(kume4-kume5)      # kume4 olup kume5 olmayanı alır. kume farkı
#   cıkıs -->   {'t', 'U', 'c', 'g'}  

print(kume4&kume5)      #kume4 ve kume5 ortak olanları alır.
#   cıkıs -->   {'m', 'u', 'e', 'r'}

print(kume4^kume5)      #kume4 ve kume5 arasında bır bırınde olmayanları alır
#    cıkıs -->   {'k', 'ı', 's', 'l', 't', 'U', 'g', 'y', 'c'}




