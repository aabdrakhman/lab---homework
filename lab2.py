#1
a = int(input())
b = int(input())
if (a%2==0 and b%2==1):
    num = list(range(a, b, 2))
elif (a%2==1 and b%2==1) or (a%2==1 and b%2==0):
    num = list(range(a+1, b+1, 2))
elif (a%2==0 and b%2==0):
    num = list(range(a, b+1, 2))
else:
    print('ERROR')
for i in num:
    print(i, end=" ")

#2
x = int(input())
for i in range(2, x+1):
    if (x%i==0):
        print(i)
        break

#3
x = int(input())
for i in range(1, x+1):
    if (x%i==0):
        print(i, end = " ")

#4
n = int(input())
s = 0
for i in range(n):
    i = int(input())
    s += i
print(s)

#5
x = int(input())
b = []
while x>0:
    b.append(x%10)
    x = x//10
s = 0
for index, i in enumerate(b):
    s+=(2**index)*i
print(s)

#6
def power(a: float, n: int) -> float:
    return a**n

a = input().split()
print(double_power(float(a[0]), int(a[1])))

#7
def election(x: int, y: int, z: int)->int:
    match x, y, z:
        case (0, 0, 1) | (0, 1, 0) | (1, 0, 0) | (0, 0, 0):
            return 0
        case (0, 1, 1) | (1, 0, 1) | (1, 1, 0) | (1, 1, 1):
            return 1

a = input().split()
print(election(int(a[0]), int(a[1]), int(a[2])))

#8

def add_to_bank_account(sum:float, bank:float)->float:
    bank += sum
    return bank


def substract_from_bank_account(sum:float, bank:float)->float:
    bank -= sum
    return bank


def money_conversation(sum:float, convfrom: str, convto: str) -> float:
    match convfrom, convto:
        case "USD", "KZT":
            return sum*470
        case "KZT", "USD":
            return sum/470
        case _:
            return "Please, input correctly"

bank = 0
bank = add_to_bank_account(float(input()), bank)
result = substract_from_bank_account(float(input()), bank)
print(f'{result=}')

print(money_conversation(float(input()), str(input()).upper(), str(input()).upper()))

