from art import logo

#Addition
def add(n1,n2):
  return n1+n2

#Subtract
def subtract(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  '+':add,
  '-':subtract,
  '*':multiply,
  '/':divide
}
should_continue = True
def calculate():
  print(logo)
  global should_continue
  num1=float(input("What's the first number ?: "))
  for key in operations:
    print(key)
  while should_continue==True: 
    operation_symbol=input("Pick an operation from the above options :")
    num2=float(input("What's the second number ?: "))
    calculation_symbol=operations[operation_symbol]
    value=calculation_symbol(num1,num2)
    print(f"{num1}{operation_symbol}{num2}={value}")
    num1=value
    repeat=input(f"Type 'y' if you want to continue calculation with {value}., type 'n' to start a new calculation or 'e' to exit.")
    if repeat[0]=='n':
      calculate()
    if repeat[0]=='e':
      should_continue=False

calculate()