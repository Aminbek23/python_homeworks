#Dictionary Exercises
#task 1
my_dict={'firstname': 'Karl','lastname':'Mark', 'age' : 40, 'adrees':'Paris'}
my_dict = {'a': 12, 'b': 5, 'c': 18, 'd': 9}
values=my_dict.values()
increase=sorted(values)
decrace=sorted(values, reverse=True)

print("O'sish tartibida: ",increase)
print("Kamayish tartibida: ",decrace)

#task 2
my_dict={0:10, 1:20}
my_dict[2]=30
print('Uptaded my_dict: ', my_dict)

#task 3
dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
total=dict1|dict2|dict3
print(total)

#task 4
n=int(input('sonni kiriting: '))
print(n)
kvadratlar={}
for i in range(1,n+1):
    kvadratlar[i]=i**2
print(kvadratlar)

#task 6
kvadratlar={}
for i in range(1,16):
    kvadratlar[i]=i**2
print(kvadratlar)

#Set Exercises
#task 1
my_set={3,4,5,1,3}
print(my_set)

#task 2
my_set={23,43,68,79,16}
for i in my_set:
    print(i)

#task 3
my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print("new set: ", my_set)

#task 4
my_set = {10, 20, 30, 40}
my_set.remove(30)
print("new set: ", my_set)

#task 5
my_set = {10, 20, 30, 40}
my_set.discard(50)
print("new set:", my_set)


