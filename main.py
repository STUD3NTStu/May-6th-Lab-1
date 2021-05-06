#print('What is your first name?')
#name=input() #takes the input of first name
#print('What is your last name?')
#surname=input() #takes input of last name
#print('Hello, '+surname++' 'name+'!') #prints the  last name before the first

#print('Give me a number to check if it's even, odd, or 0.')
#number=int(input())
#if number%2==0 and number!=0: #checks to see ithe input is divisible by 2 and is not 0 so that a false positive doesn't register
  #print('This number is even.')
#elif number%1==0 and number!=0: #same as with 2 in that it checks to make sure that there is no false positive if the number inputted is 0
  #print('This number is odd.')
#else: #and finally, if the number is 0, this prints because there are no other possible numbers that it could be, so no code is needed.
  #print('This number is 0.')

#print('What day of the year is it?')
#day=int(input())
#if day<=31:
  #print('Janurary'+' '+str(day))
#elif day<=59 and day>31: #checks to make sure the day provided falls within the days that make up the month, this goes for the rest of the code as well.
  #print('Febuary'+' '+str(day%31))
#elif day<=90 and day>59:
  #print('March'+' '+str(day%59))
#elif day<=121 and day>90:
  #print('April'+' '+str(day%90))
#elif day<=151 and day>121:
  #print('May'+' '+str(day%121))
#elif day<=182 and day>151:
  #print('June'+' '+str(day%151))
#elif day<=212 and day>182:
  #print('July'+' '+str(day%182))
#elif day<=243 and day>212:
  #print('August'+' '+str(day%212))
#elif day<=273 and day>243:
  #print('September'+' '+str(day%243))
#elif day<=304 and day>273:
  #print('October'+' '+str(day%273))
#elif day<=334 and day>304:
  #print('November'+' '+str(day%304))
#elif day<=365 and day>334:
  #print('December'+' '+str(day%334))

n=int(input())
for i in range(n, 0, -1):
    for x in range(i, 0, -1):
     print(x, end='')
    print() 