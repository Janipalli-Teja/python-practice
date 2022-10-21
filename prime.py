# # printing primes upto given number
# first_num=int(input("enter first number required:"))
# last_num=int(input("enter the last number required:"))
# for n in range(first_num,last_num+1):
#     if n>1:
#         for i in range(2,n):
#           if n%i==0 :
#            break
#         else:
#            print(n)

x=int(input("enter a numbe:"))
for i in range(2,x):
  if x%i==0 : 
    print("not a prime")
    break
  else:
    print("prime")
    break
 

