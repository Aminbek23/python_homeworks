#task 1
fruits=['apple','banana','lemon','orange']
print(fruits[2])

#task 2
my_list1=[1,3,5]
my_list2=[2,4,6]
print(my_list1+my_list2)

#task 3
my_list=[1,2,3,4,5,6,7]
first=my_list[0]
middle=my_list[len(my_list)//2]
last=my_list[-1]
new_list=[first,middle,last]
print(new_list)

#task 4
movies=['Avangers', 'Mr Ben', 'Spiderman','Weapons','Joker']
movie_tuple=tuple(movies)
print(movie_tuple)

#task 5
cities=['London','Paris','New York','Los Angels']
if 'Paris' in cities:
    print('yes')
else:
    print('no')

#task 6
num=[1,2,3,4,5]
new_n=num*2
print(new_n)

#task 7
num=[1,2,3,4,5]
num[0],num[-1]=num[-1],num[0]
print(num)

#task 8
num=1,2,3,4,5,6,7,8,9,10
print(num[3:7])

#task 9
colors='yellow','blue', 'black','orange', 'blue'
print(colors.count('blue'))

#task 10
animals="sheep",'snake','lion','monkey'
print(animals.index('lion'))

#task 11
num1='a','b','c'
num2=[1,3,5]
print(num1+tuple(num2))

#task 12
my_list=[23,45,43,54,67,65]
my_tuple=12,23,34,45
print('List lenght:' ,len(my_list))
print('Tuple lenght:', len(my_tuple))

#task 13
my_tuple= 13,17,23,26,20
my_list=list(my_tuple)
print(my_list)

#task 14
num=20,26,17,13,33
num=list(num)
num.sort()
print("MIN:",num[0])
print("MAX:",num[-1])

#task 15
num="apple","iphone","milk","chocolate","cofee"
num=list(num)
num.sort(reverse=True)
print(num)
