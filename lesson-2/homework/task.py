#task 1
ism=input("Ismingizni kiriting: ")
t_yil=int(input("Tug'ilgan yilingizni kiriting: "))
from datetime import date
hozirgi_yil=date.today().year
yosh=hozirgi_yil-t_yil
print(f'{ism} siz {yosh} yoshdasiz')

#task 2
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])

#task 3
txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[-1::-2])

#task 4
txt = "I'am John. I am from London"
print(txt.split("from")[-1].strip())

#task 5
a=input("Matinni kiriting: ")
print(a[::-1])

#task 6
a=input("Matinni kiriting: ")
print(a.lower().replace("e","a").replace("i","a").replace("o","a").replace("u","a").replace("o'","a").count("a"))

#task 7
a=input("Sonlarni kiriting: ")
sonlar=[int(x) for x in a.split(",")]
print("Eng katta son: ", max(sonlar))

#task 8
txt=input("So'zni kiriting: ")
if txt==txt[::-1]:
   print("Palindrom so'z")
else:
   print("Palindrom so'z emas")

#task 9
gmail=input("Elekron pochta manzilizni kiriting:")   
print(gmail.split("@")[-1].strip())

#task 10
import random
import string
uzunlik=int(input("Parol uzinligini kiriting: "))
belgilar=string.ascii_letters+string.digits+string.punctuation
parol=' '.join(random.choice(belgilar) for i in range(uzunlik))
print("yaratilgan parol: ", parol)
