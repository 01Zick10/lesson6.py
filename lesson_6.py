a = int(input('first-number'))
b = int(input('second-number'))
c = 0

for i in range(a, b + 1):
    c += i
    print(c)

 #2
a = int(input())
sum1 = 0
count = 1
while a >= count:
    sum2 = 0
    for i in range(0, count +1):
        sum2 += i
    count += 1
    sum1 += sum2
print(sum1)

#3
a = int(input('a => '))
b = int(input('b => '))
c = int(input('c => '))
x = int(input('x => '))
print(a * x ** 2 + b * x + c)


#4
def Numbers_To_Words (number):
    dictionary = {'0': "zero",'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
                  '7': "seven", '8': "eight", '9': "nine", '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen',
                  '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen',
                  '19': 'nineteen', '20': 'twenty'}
    print(dictionary[number])


print (Numbers_To_Words('19'))
