import requests
print(a+"[*]ايجاد الارقام الفرديه\n")

z=int(input("Enter Your First number: "))
print()
x=int(input("Enter Your list number: "))
start = z
end = x
 

for num in range(start, end + 1):
     
    if num % 2 != 0:
        print(num, end = " ")
