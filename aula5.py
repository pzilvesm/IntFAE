a=range(10)
i=1 
while i<10:
	print(a[i]+a[i-1])
	i+=1



l=[54, 44, 27, 79, 91, 41]
l[1]=l[4]
del l[4]
l.insert(5,l[1])
print(l)


tup=(11, 22, 33, 44, 55, 66)
new_tup=(tup[3],tup[4])
print(new_tup)


s1= 'abcde'
s2= '12345'
sn=s1[0]+s1[2]+s1[-1]+s2[0]+s2[2]+s2[-1]
print(sn)



h = input("Please enter the height of the rectangle:")
w = input("Please enter the width of the rectangle:")
def recper(x,y):
		return x+x+y+y
perimeter=recper(int(h),int(w))
print(perimeter)

c = int(input("Please enter a temperature in Celsius, and receive in Fahrenheit:"))
def CtoF(x):
	return (9*x/5)+32
f= CtoF(c)
print(f)