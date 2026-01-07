# input("What is your name brother ? ")
# age=21
# print("your age is :"+str(age))


#float

# height=250.5
# print(type(height))



# message='Hey Asalbek how are u doing?'
# new_message=message.replace('Asalbek', 'Rahmon')
# print(new_message)



# greeting="Hey mate!"
# name="Asalbek"

# message=f" {greeting}, {name.upper()}. Welcome! "
# print(message)


#Integers and Floats
#smth=3//2   #butun sonni chiqaradi
#a=3%2  #qoldiqni chiqaradi              
#print(smth)
#print(a)


# print(round(3.75,1)


#LISTS, TUPLES AND SETS

# courses=['Math', 'english', 'Algebra', 'Computer Science']
# courses_2=["geo", "other"]
# print(courses[2:])
# courses.append("Art")
# print(courses)
# courses.extend(courses_2)
# print(courses)
# popped=courses.pop()
# print(popped)
# print(courses)
# print(courses.index("Computer Science"))

# for index, course in enumerate(courses, start=1):
#     print(index, course)  

# course_str=' - '.join(courses)
# print(course_str)
# new_list=course_str.split(' - ')
# print(new_list)



#SETS

# cs_courses={'History', 'Algebra', 'Java', 'OS', 'Math'}
# art_courses={'music', 'Dance', 'History', 'Algebra'}
# print(cs_courses.intersection(art_courses))


#EMPTY
#list
# empty_list=[]
# empty_list=list()

#tuple
# empty_tuple=()
# empty_tuple=tuple()

#set
# empty_set={}
# empty_set=set()


#DICTIONARIES

# student={'name': 'John', 'age': 25, 'courses': ['Math', 'CompScience']}
# print(student['age'])

# for k in student.items():
#     print(k)
# print(student.values())


#IF CONDITIONALS

# language='Python'
# if language=="Python":
#     print('Conditional was true')

# user='Admin'
# logged_in=False

# if user=="Admin" or logged_in==False:
#     print("Admin Page ")
# else:
#     print(" Bad creds")


# condition='SMTH'

# if condition:
#     print("That's True")
# else:
#     print('That is false')



#LOOPS AND ITERATIONS

nums=[3,2,4,5,5,7]

# for num in nums:
#     if num==3:
#         print("Found!")
#         continue
#     print(num)

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)
# x=0
# while True:
#     if x==5:
#         break
#     print(x)
#     x+=1




#FUNCTIONS

def hello_func(greeting):
    return 'Hello World'

print(hello_func().upper())
