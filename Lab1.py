#1
a = int(input("a = "))
b = int(input("b = "))
c = (a**2 + b**2)**(0.5)
print(c)

#2
n = int(input("n = " ))
n1 = n%100//10
print(n1)

#3
n = int(input("n = "))
print(n+2-(n%2))

#4
n = int(input("n = "))
m = n*45+(n//2)*5+((n+1)//2-1)*15
print(m//60+9, m%60)

#5
n = int(input("n = "))
m = int(input("m = "))
if n>m:
	print(n)
elif n<m:
	print(m)
else:
	print(0)

#6
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a>b and a>c:
	print(a)
elif b>a and b>c:
	print(b)
elif c>a and c>b:
	print(c)

#7
x = int(input())
y = int(input())
x1 = int(input())
y1 = int(input())
if x==x1 or y==y1:
	print("YES")
else:
	print("NO")

#8
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if (a+b)>c or (a+c)>b or (b+c)>a:
	print("YES")
else:
	print("NO")

#9
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a==b and a==c and b==c:
	print(3)
elif (a!=b and a!=c and b==c) or (a==b and a!=c and b!=c) or (a!=b and a==c and b!=c):
	print(2)
else:
	print(0)

#10
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a<=b and b<=c and a<=c:
	print(a,b,c)
elif a<=b and c<=b and a<=c:
	print(a,c,b)
elif b<=a and b<=c and c<=a:
	print(b,c,a)
elif b<=a and b<=c and a<=c:
	print(b,a,c)
elif c<=a and b<=a and c<=b:
	print(c, b, a)
elif c<=b and a<=b and c<=b:
	print(c, a, b)
else:
	print(a,b,c)

abc = [a, b, c]
print(sorted(abc))

	


