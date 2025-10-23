# a-z, A-Z, 0-9, _
# you can not start a variable name with a number

# firstName = "Sadiqul"

# num1 = -5

# roll = 8

# x = 5.6
# y = 4 + 2j
# name = "Roman"
# is_the_2nd_class = True

# nums = [4, 3, 2, 7, 8, 0]
# names = ("rony", "abid", "arif")
# fruits = {"apple", "banana"}
# users = {
#     'id': 3,
#     "name": "sultanan"
# }



# x = input("Enter any number: ")

# print("The output is x")


# x = 4
# y = 2

# print(x / y)

# a = 10

# b = float(a)
# print(b)


# num = input("Enter any number: ")


# print(type(num))


# x = 5
# y = 2

# z = x * y

# print(z)

# =, +=, -=, *=, /=, %=, **=

# x = 9
# x = x + 1
# x = x - 1
# x = x * 1
# x = x / 1
# x = x ** 1
# x = x % 1


# ==
# !=
# >
# >=
# <
# <=

# x = 5
# y = 8

# if x != y:
#     print("Valid.")
# else:
#     print("Invalid.")


a = 4
b = 6
c = 8

if a > b and a > c:
    print("The largest number is = ", a)
    
elif b > c and b > a:
    print("The largest number is = ", b)
    
else:
    print("The largest number is = ", c)
    
balance = 60

amount = int(input("Enter your amount: "))


if amount <= balance:
    print(f"Your recharge is successful. Your current balance is {balance - amount} Taka.")
    
else:
    print(f"Insufficient balance. Your current balance is {balance} Taka.")