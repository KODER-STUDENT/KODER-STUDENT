from math import  sqrt , cos ,  log as ln , sin

x = (input('Enter your x here:' , ))
while not x.isdigit():
   x = input('Please enter nteger, not string, try again:')

x = int(x)

if x < 3:
   print("x < 3")
elif  3 <= x < 6:
   print("3 <= x < 6")
elif  x >= 3:
   print("x >= 3")

print("sqrt(x4 + ln(x)) =", sqrt(x*4 + ln(x)))
print("abs(ln(x))*5 =", abs(ln(x))*5)
print("(cos(x))x =", cos(x)**x)
 

x = input('Enter your x here second time: ', )

while not x.isdigit():
   x = input('Please enter nteger, not string, try again:')
x = int(x)

n = input('Enter your n here: ',)

while not n.isdigit():
   n = input('Please enter nteger, not string, try again:')

n = int(n)

sum_result = x
for n in range(1, n + 1):
    sum_result += n * x**2 * sin(n*x)
print("sum_result:", sum_result)
