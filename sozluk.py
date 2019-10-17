

tel = {'jack': 4098, 'sape': 4139}

print(tel['jack'])
#print(tel[0]) bu şekilde değil, erişilecek değer ile aranır
# key , value ikilsi (anahtar, değer)
print(tel['sape'])

d2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print (d2)


print( ( 1 , 2 , 3 )              > ( 1 , 1 , 1 ))
print( [ 1 , 2 , 3 ]              < [ 1 , 2 , 0 ])
print( 'ABC' < 'C' < 'Pascal' < 'Python')
print( ( 1 , 2 , 3 , 4 )           < ( 1 , 2 , 4 ))
print( ( 1 , 2 )                 < ( 1 , 2 , - 1 ))
print( ( 1 , 2 , 3 )             == ( 1.0 , 2.0 , 3.0 ))
print( ( 1 , 2 , ( 'aa' , 'ab' ))   < ( 1 , 2 , ( 'abc' , 'a' ), 4 ))

# yukarda dıkkat edılmesı gereken pyhon sırayla karsılastırır ve cevabı buldugu an ıslemı 
# sonlandırır. mısal (1,2,3) < (1,1,3) ılk 1lere bakar esıtler sıradıkıler bakar
# ılkde 2 var 2cıde 1 var kosul bıter dırek ekrana basar 3 elemanları kontrol etmez.
