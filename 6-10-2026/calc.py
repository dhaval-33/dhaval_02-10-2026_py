a=30
b=40
c=int(input("Enter your choice : "))
print("Press 1 for addtion")
print("Press 2 for sub")
print("Press 3 for mul")
print("Press 4 for div")
print("Press 5 for mod")

if c==1:
    print(f"addition ofr {a} + {b} = {a+b}")
elif c==2:
    print(f"sub fr {a} - {b} = {a-b}")
elif c==3:
    print(f"mul ofr {a} * {b} = {a*b}")
elif c==4:
    print(f"div ofr {a} / {b} = {a/b}")
elif c==5:
    print(f"mod ofr {a} % {b} = {a%b}")

else:
    print("Enter valid number")