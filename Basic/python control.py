#if statement

# val = input("Enter no: ")
# flout_value=float(val)

# if(flout_value>100):
#     print("The no is greter than 100")


#ages 

# age=int(input("Enter you Age :"))

# if(age<18):
#     print("Minor Age")
# elif(age>18 and age<=35):
#     print("Adult")
# elif(age>35 and age<=60):
#     print("Senior Mid-Age")
# else:
#     print("Senior Sitizen")

#LOOP Statement
# for loop, while loop

# lst = [1,2,3,4,5,6,7,8]
# for i in lst:
#     print(i**3)


##find the sum of all the element in the list

# lst = [1,2,3,4,5,6,7,8]
# sum1=0
# for i in lst:
#     sum1=sum1+i

# print(sum1)

##find the sum of even and odd number 

# lst = [1,2,3,4,5,6,7,8]
# i = lst
# even_sum=0
# odd_sum=0

# for i in lst:
#     if(i%2==0):
#         even_sum=even_sum+i
#         # print("Enter Even no {}".format(i))
#     else:
#         odd_sum=odd_sum+i
        # print("Enter Odd no {}".format(i))

# print("Even Sum is {}".format(even_sum))
# print("Odd Sum is {}".format(odd_sum))

##While Looop

# i=0
# even_sum=0
# odd_sum=0

# while(i<=10):
#     if(i%2==0):
#         even_sum=even_sum+i
#     else:
#         odd_sum=odd_sum+i

#     i=i+1
# print(even_sum,odd_sum)

##break and continue 

# x=1
# while (x<7):
#     print(x)
#     if x==4:
#         break
    
#     x=x+1

x=0
while x<7:
    x=x+1
    if x==4:
        continue #to skp the statement
    
    print(x)
