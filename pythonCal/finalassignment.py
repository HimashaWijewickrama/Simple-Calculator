# assign a empty array to collect calculations(past calculations)
past_calcs=[]
# function for adding numbers
def add(a,b):
  return a+b
# function for substract numbers
def subtract(a,b):
  return a-b
# function for multiply numbers
def multiply (a,b):
  return a*b
# function for dividing numbers
def divide(a,b):
  try:
    return a/b
  except Exception as e:
    print(e)
# function for calculate power of numbers    
def power(a,b):
  return a**b
# function for remainder numbers
def remainder(a,b):
  return a%b
# function for history
def history():
    
    if past_calcs:
        for i,calc in enumerate(past_calcs):
            print(calc)
    else:
        print("No past calculations to show")
        return 0
    
             
def select_op(choice):
    #return calculation history 
  if (choice=='?'):
      return history()
    # terminate the program 
  if (choice == '#'):
    return -1
   # reset
  elif (choice == '$'):
    return 0

  elif (choice in ('+','-','*','/','^','%')):
    while (True):
          #inputed first number converts to the string value  
      num1s = str(input("Enter first number: "))
      #display the converted string value
      print(num1s)
      #if the string value ends with '$'sign, program will stop the session
      #start another session form the begining
      if num1s.endswith('$'):
        return 0
      #if the string value ends with '#' sign. program will terminate 
      if num1s.endswith('#'):
        return -1
      #if any case, program wants float numbers, convert string value into the float value 
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
        
      if num2s.endswith('#'):
        return -1
        
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number,please enter again")
        continue
    
    result = 0.0
    last_calculation = ""
 

#according to the operator calculations are happened
    if choice == '+':
      result = add(num1, num2)
    elif choice == '-':
      result = subtract(num1, num2)
    elif choice == '*':
      result = multiply(num1, num2)
    elif choice == '/':
      result =  divide(num1, num2)
    elif choice == '^':
      result = power(num1, num2)
    elif choice == '%':
      result = remainder(num1, num2)
    
    else:
      print("Something Went Wrong")
      
    last_calculation =  "{0} {1} {2} = {3}".format(num1, choice, num2, result)

#adding calculations and print them to the empty array
    print(last_calculation)
    past_calcs.append(last_calculation)
    
  else:
    print("Unrecognized operation")
    
# operators   
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  print("8.History  : ? ")

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$,?): ")
  print(choice)
  
  
  if(select_op(choice) == -1):
      #program ends here
      print("Done. Terminating")
      exit()


    


