#Calculating the cost of food items

int def add(a,b):
	res = a+b
	return res

int def sub(a,b):
	res = a-b
	return res

int def prod(a,b):
	res = a*b
	return res
	
int def div(a,b):
	res = a/b
	return res
	
print("=========================/n/t WELCOME TO THE CALCULATOR APP!/t/n=========================")
item1 = int(input())
item2 = int(input())
symbol = input()

ans = 0

if symbol == '+':
	ans = add(a,b)

if symbol == '-':
	ans = sub(a,b)
	
if symbol == '*':
	ans = prod(a,b)
	
if symbol == '/':
	ans = div(a,b)
	
print(ans)
