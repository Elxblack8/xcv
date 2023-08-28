#ايجاد الارقام الفرديه
G= '\033[95m' 
a= '\033[94m' 
d= '\033[96m' 
f= '\033[92m'
c= '\033[93m' 
x= '\033[91m' 
v= '\033[0m' 
h= '\033[1m' 
k= '\033[4m' 

print(a+"[*]ايجاد الارقام الفرديه\n")

z=int(input(c+"Enter Your First number: "))
print()
x=int(input(f+"Enter Your list number: "+d))
start = z
end = x
 

for num in range(start, end + 1):
     
    if num % 2 != 0:
        print(num, end = " ")
