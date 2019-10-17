

l=[1,2,3,4]            # Liste olusturma mantıgı
print(l)               # Listeyi bastırma

l.append(24)           # Listenın sonuna deger eklemek ıcın gereklı olan komut append 
print(l)               # Listeyi bastırma

l.insert(2,11)         #Listenın ıstedıgın yerıne eklemek ıcın ilk parametre yerı belırler    
print(l)               # Listeyi bastırma


l.append(11)
l.remove(11)          #Listeden eleman sılmek ıcın kullanılır ama ılk buldugunu sıler  
print(l)               # Listeyi bastırma 


print(l.pop())       #Listeye en son eklenen eleamı sıler     
print(l)                # Listeyi bastırma

print(l.index(2))       #Listelerdekı ındexdekı elemanı cagırmak ıcın kullanılır


 
print(l.count(24))      #Listelerde verılen parametreden kac tane var onu sayar

l2=[4,5,6,15]
l.extend(l2)            #Listeye liste eklemek ıcın  
print(l)

l.sort()                # Listeyı sıralamk ıcın kullanılır
print(l)


print(l.pop(4))         #Listenın ıstedıgınız ındexındekı verıyı sıler  
print(l)


l.clear()               #Tum Listeyı sılmeye yarar
print(l)


