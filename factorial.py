try:num=int(input("Enter a number:"))
except ValueError as e:
    print("Invalid input")
    exit()
res=1
if num==0:
    res=1
elif num>=0:
 for i in range(1,num+1):
    res=res*i
else:
    res=None
print(f"Factorial of {num} is:",res)