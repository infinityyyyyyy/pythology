"""W3 schools ile ilerlemeye devam ettim
print("hello")
x=5
print("Merhaba Dünya")
if 5> 2:
    print("Five is greater than two")
if 5 < 2:
    print("Five is greater than two!")
x = 5
y = "john"

print(x)
print(y)

x = 4
x= "sgdrtgher"
print(x)

x = str(3)
y = int(3)
z= float(3)
print(x)
print(y)
print(z)
print(x,y,z)  #print ile 3 değerimi sırasıyla yazabiliyorum
*ALTTA DEĞİŞKENLERİN VERİ TÜRÜNÜ ÖĞRENDİK
x = 5
y= "john"

print(type(x))
print(type(y))
*BURADA DİZE DEĞİŞKENLERİN TEK VEYA ÇİFT TIRNAK İŞSRETLER İÇERSİİNDE GÖSTEREBİLECEĞİMİZİ GÖSTERDİK

x= "John"
# is the same as

y= ' John'

print(x,y)
*DEĞİŞKEN ADLARI BÜYÜK VE KÜÇÜK HARFLERE DUYARLIDIR

a = 4
A ="Sally"
print(a,A)

# A will not overwwrite a
*DEĞİŞKEN ADLARI NASIL YAZILIR? AŞAĞIDAKİ VERSİYONLAR KABUL EDİLEBLİR

myvar = "John"
my_var ="John"
_my_var ="John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print()
***DEVE KILIFI YÖNTEMİ -->İLKİ HARİÇ KELİME BÜYÜK HARFLE YAZILIR
myVariableName = "John"

***PASCAL KILIFI YÖNTEMİ--> HER KELİME BÜYÜK HARFLE BAŞLAR
MyVariableName ="John"

***YILAN KILIFI --> HER SÖZCÜK BİR ALT ÇİZGİ KARAKTERİYLE AYRILIR

my_variable_name = "john"  

*Birden çok değişkene birçok değer

x,y,z = "orange","banana","cherrry"
print(x)
print(y)
print(z)
Birden çok değişkene aynı değer
x=y=z="banana"
print(x)
print(y)
print(z)
Bir Koleksiyonu Paketinden Çıkarma

fruits = ["apple","banana","cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
çıktıları almak için print kullanılır

x= "python is Awesome"
print(x)
GLOBAL DEĞİŞKENLER

x = "awesome"
def myfunc():
    print("python is " + x)

myfunc()  #burada fonksiyonumuzu çağırıyoruz

x = "awesome"

def myfunc():
    x = "fantastic"  #Bu değişken yerel olur ve yalnızca değişken için kullanılır

    print("python is " + x)

myfunc()
print("python is "  + x)

GLOBAL ANAHTAR KELİME

def myfunc():
    global x  # Bir değişkenin içinde global değişkenin değiştirmek istiyorsan anahtar kelime kullanılır
    x= "fantastic"
myfunc()

print("python is " + x)


x = "awesome"
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x )

Tür Dönüşümü

x= 1
y= 2.8
z= 1j

a =float(x)
b =int(y)
c=complex(x)
print(a)  #
print(b)
print(c)


print(type(a))  # Türünü değiştirdik
print(type(b))
print(type(c))"""

import random
print(random.randrange(1,10))


