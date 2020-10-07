# -------------------------Q.2------1 max-----------------------------
'''a=int(input())
b=int(input())
c=int(input())
if a>=b:
	if a>=c:
		print(a)
	else:
		print(c)
if b>=a:
	if b>=c:
		print(b)
	else:
		print(c)
		'''

# --------------Q.3--------------2nd max-------------------------
'''

a=int(input())
b=int(input())
c=int(input())


if a>=b>=c:
	print(b)
else:
	if a>=c>=b:
		print(c)
	else:
		if b>=a>=c:
			print(a)
		else:
			if b>=c>=a:
				print(c)
			else:
				if c>=b>=a:
					print(b)
				else:
					if c>=a>=b:
						print(a)

'''

# ---------------------------Q.4---------------------------
'''a=int(input())
b=int(input())
a=b+a
b=a-b
a=a-b
print("a-",a)
print("b-",b) '''

# ------------------Q.5-------------------------------------------------------------
'''a=int(input())
b=int(input())
if a%b==0:
	print("completely divisible by",b)
else:
	c=a%b
	a=a-c
	print(a,"completely divisible by",b)'''
# --------------------Q.6-------------------------------------------
'''
n=int(input())
if n%2==0:
	if n>200 :

		print("Bingo")
	else:
		print("Codechef")

else:
	if n%2!=0:
		if n<200:
			print("Ringo")
		else:
			print("Codechef")
'''
# -----------------------Q.9-------------------
'''
n=int(input())
if n%5==0:
	if n%11==0:
		print("divisible by Both")
	else:
		print("divisible by 5")
else:
	if n%11==0:
		print("divisible by 11")
	else:
		print("None")

'''
# ----------------------Q.10----------------------
'''a=int(input())
b=int(input())
c=int(input())
if a+b>c:
	if b+c>a:
		if a+c>b:
			print("Tringle is possible")
		else:
			print("invalid")
	else:
		print("invalid")
else:
	print("invalid")
'''
# ---------------------Q.11-----------------
'''n=int(input())
if n%2==1:
	if n%3==0:
		print("Odd multiple of 3")
	else:
		print("Odd not multiple of 3")
else:
	if n%3==0:
		print("No Odd multiple of 3")
	else:
		print("none")
	'''


# -----------------------Q.12---------------------------
'''a=int(input())
b=int(input())
c=int(input())
if a==b==c:
	print("equilateral")
else:
	if a!=b!=c:
		print("scalene")
	else:
		print("isosceles")
		'''

# ----------------Q.13-------------------------------------
'''
a=int(input())
b=int(input())
c=int(input())
if a+b>c:
	if b+c>a:
		if a+c>b:
			if a==b==c:
				print("equilateral,valid Tringle")
			else:
				if a!=b!=c:
					print("scalene and valid Tringle")

				else:

					print(" isosceles and valid Tringle")
		else:
			print("invalid")
	else:
		print("invalid")
else:
	print("invalid")

'''
# --------------Q.14----------------------------------
'''
a=int(input())
b=int(input())
c=int(input())
if a+b+c==180:
	print("Tringle")
else:
	print("invalid")
'''

# --------------------Q.15--------------
'''

a=int(input())
b=int(input())
c=int(input())

if a>90 or b>90 or c>90 and a+b+c==180:
	print("obtuse")
else:
	if a<90 and b<90 and c<90 and a+b+c==180:
		print("Acute")
	else:
		if a==90 or b==90 or c==90 and a+b+c==180:
			print("Right")
		else:
			print("invalid")
			'''

# ----------------------Q.16----------------------

# -------------------Q.17-------------------
'''
a=20
while a!=0:
	print(a)
	a-=1
	'''
# ------------------Q.18--------------------------
'''
a=10
s=1
while a!=0:
	s=s*a
	a-=1
print(s)
	'''

# -------------------Q.19-----------------------
'''
n=2
c=10
while c!=0:
	print(n)
	n+=2
	c-=1
	'''

# -----------------Q.20-----------------
'''
n=3
c=14

while c!=0:
	print(n)
	n+=2
	c-=1
	'''
# -----------------------Q.21----------------------
'''
n=5
while n!=0:
	print("Hello")
	n-=1
	'''
# ----------------------------Q.22-----------------------
'''
n=(input("Enter the name :) "))
c=20
while c!=0:
	print("Hello",n)
	c-=1
'''
# ----------------------Q.23-----------------------
'''
n=2
c=1
while c<=10:
	print(n,"*",c,"=",n*c)
	c+=1
	'''
# --------------------------Q.24---------------------------
'''
n=int(input("Enter the Number "))
c=1
while c!=11:
	print(n,"*",c,"=",n*c)
	c+=1
	'''
# --------------------------Q.25---------------------
'''
n=int(input("Enter the Number "))
s=0
while n!=0:
	s+=n
	n-=1
print(s)
'''
# --------------------Q.26------------------------
'''
n=int(input("Enter the Number "))
while n!=0:
	print(n)
	n-=1
	'''
# ------------------------------Q.27-----------------
'''
n=int(input("Enter the Number for how many times you want take input:) "))
while n!=0:
	n1=int(input("Enter the Number"))
	if n1%2==0:
		print("Even")
	else:
		print("Odd")
'''
# -----------------Q.28-----HCF-----------------
'''
a=int(input())
b=int(input())
while a!=b:
	if a>b:
		a-=b
	else:
		b-=a

print(a)
'''
# --------------------Q.29-----LCM---------------------
'''
a=int(input())
b=int(input())

find_lcm=a*b
while a!=b:
	if a>b:
		a-=b
	else:
		b-=a

find_lcm//=a
print(find_lcm)
'''
# ----------------------------Q.30---------------------------
'''
n=int(input())
if n%10==7:
	print("yes")
else:
	print("No")
'''
# ------------Q.31-------------------------------

'''
n=int(input())
n1=n//10
if n1%10==7:
	print("yes")
else:
	print("No")
'''
# ------------Q.32--------------------------
'''
# optimize loop:-
n=int(input())
i=1
while i<=n**.5:
	m=n%i==0
	if n%i==0:
		print(i)
		if i!=n**.5 and m!=i:
			print(n//i)
	i+=1
'''
# or
'''
n=int(input())
i=1
while i<=n//2+1:
	if n%i==0:
		print(i)
	i+=1
print(n)
'''

# ---------Q.33--------------
'''
n=int(input())
if n>1:
	c=2
	while c<n:
		if n%c==0:
			print("Not prime Number")
			break
		c+=1
		
	else:
		print("prime Number")
else:
	print("Not prime Number")
'''
# ----------------Q.34------------------------------
# optimize loop:-
'''
n=int(input())
i=1
while i<=n**.5:
	m=n%i==0
	if n%i==0:
		print(i)
		if i!=n**.5 and m!=i:
			print(n//i)
	i+=1
print(n)
'''
# ------------------------Q.35------------------------------
'''
n=int(input("Enter the Number "))
s=0
while n!=0:
	r=n%10
	s+=r
	n//=10
print(s)
'''
# -------------------------Q.36----------------------------
'''
n=int(input("Enter the Number "))
s=0
while n!=0:
	r=n%10
	s=s*10+r
	n//=10
print(s)
'''
# -----------------------------Q.37----------------
'''
n=int(input("Enter the Number "))
m=n
sum_fac=0
while n!=0:
	r=n%10
	s=1	
	while r!=0:
		s=s*r
		r-=1
	sum_fac+=s
	n//=10
if m==sum_fac:
	print("strong no")
else:
	print("Not strong no")
'''
# -----------------Q.38----------------
'''n=int(input("Enter The Number "))
i=1
sum_factor=0
while i<=n**.5:
	m=n%i==0
	if n%i==0:
		sum_factor+=i
		if i!=n**.5 and m!=i:
			sum_factor+=n//i
	i+=1
if n==sum_factor:
	print("perfect no")
else:
	print("not perfect")
#          ---or--
n=int(input("Enter The Number "))
i=2
sum_factor=1
while i<=n**.5:
    if n%i==0:
        sum_factor+=i+n//i
    i+=1
if n==sum_factor:
	print("perfect no")
else:
	print("not perfect")


'''
# ------------------Q.39-------Armstrong No--------------
'''for i in range(0,999):
	n=i
	sum1=0
	while i!=0:
		re=i%10
		sum1+=re**3
		i//=10
	if sum1==n and sum1!=0:
		print(sum1)
'''
#---------------Q.40-----------Fibonacci series-------------------------
'''
n=int(input("enter the number "))
a=1
b=1
while n!=0:
	fib=a
	d=a+b
	a=b
	b=d
	n-=1
print(fib)
'''
#-----------------Q.41-----------Prime number optimized---checking(if else)-----
'''
n=int(input("enter the no "))
if n==2 or n==3:
    print("prime no",n)
else:
	if n>2 and n%2==0 or n%3==0:
		print("Not a prime no",n)
	else:
		if n%int(n**.5)==0:
			print("Not a prime no",n)
		else:
			print("Prime no",n)'''
#-------------------Q.42---Prime number ---------------------
'''
n=int(input("enter "))
i=2
c=0
while True:
	for j in range(2,int(i**.5)+1):
		if i%j==0:
			break		
	else:
		print(i)
		c+=1
		if n==c:
			break
	i+=1
'''
#-------------Q.43----------Palindrome No-------------------
'''N=int(input())
N1=N
sum1=0
while N!=0:
	re=N%10
	sum1=sum1*(10)+re
	N//=10
if sum1==N1:
	print("YES")
else:
	print("NO")
'''
#----------------------Q.44-----------------------
'''
N=int(input())
a=1
while a<=N:
	c=1
	while c<=N:
		print(c,end=" ")
		c+=1
	print()
	a+=1
'''
#-------------------------Q.45---------------------------
'''
i=1
while i<=5:
	j=1
	while j<=5:
		print("*",end="")
		j+=1
	print("\n")
	i+=1
'''
#------------Q.46----------------------------
#Q.1
'''
 a=1
 b=1
 while b<=10:
 	print(a,end=" ")
 	a+=b
 	b+=1
'''
#Q.2
'''
a=1
b=10
c=1
while a<=10:
	print(c,end=" ")
	c+=b
	b+=10
	a+=1
'''
#Q.3
'''
a=1
b=2
c=1
while a<=10:
	print(c,end=" ")
	c+=b
	b+=2
	a+=1
'''
#-------------------------Q.47--------------------------
'''
N=int(input())
a=1
while a<=N:
	b=1
	while b<=a:
		print("*",end=" ")
		b+=1
	print("\n")
	a+=1
'''
-----------------------------Q.48----------------------
'''
N=int(input())
a=1
while a<=N:
	b=1
	while b<a:
		print(b,end=" ")
		b+=1
	while b>=1:
		print(b,end=" ")
		b-=1
	a+=1
	print("\n")
'''
#----------------Q.49---------------------------------
'''
N=int(input("Enter the number "))
k = 2 * N -2
i=0
while i<N:
	print(" "*k,end=" ")
	k = k - 2
	j=0
	while j<=i:
		print("*", end=" ")
		j+=1
	i+=1
	print("\n")
'''
#-----------------Q.50-----------------------------------------
'''
a=1
N=int(input())
c=10
while a<=N:
	if a%2==0:
		print(a,end=" ")
		c+=10
		a+=1
	a+=1
	print(c,end=" ")
'''
#-------------------------Q.51--------------------------

