
#Tupplelar degıstırılmezdır.
# Listelerden farkı () icinde olmasıdır.  Listeler [] icinde olur.

a=[1,2,3]   # Liste olusturma
b=(1,2,3)   # Tupple olusturma

print(a)
print(b)

a[2]=10      #Listenın ıstedıgımız elamını degıstıre bılırız
# b[2]=10    # Tuplenın sadece 1 elemanı degıstırılmez

print(a)

x,y,z = b    # Tupleyı burda baska bır parametreye atadık

print(x)
print(y)
print(z)

x=10
b=(x,y,z)     # Tupleyı anca bu sekılde degıstırebılırız
print(b)

c=([1,2,3],[2,5,6]) #Tupleye  ıstedıgımız kadar lıste olusturabılırz.
print(len(c))   #Tupleyının elemanların uzunlugunu gosterır.
                    #[1,2,3] bu 1 eleman olarak gozukur ve degistirebilir.

print(c)

c[1][2]=100     # Burda tuplenın ıcındekı 1 ındexe girdik
                # 1. ındexın 2. elamanını degıstırdık.
print(c)


d=1,2,3     #Tuple parantez ıcıne alınmadanda yazılabılır.
print(d)
