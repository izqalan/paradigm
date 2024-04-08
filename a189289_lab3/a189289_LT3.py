
#1

for i in range(1,11):
  print(i)
  if (i == 5):
    print("Python")
    
#2
sum = 0
tally = 0

while tally < 10:
  try:
    number = float(input("Enter a number (float): "))
    sum += number
    tally += 1  
  except ValueError:
    print("Invalid input")
    continue

    
print("The sum of the numbers is: ", sum)
print("The average of the numbers is: ", sum/10)
print("The product of the numbers is: ", sum*10)

#3
def make_sandwich(*ingredients):
  print("\nYour order: ")
  if len(ingredients) == 0:
    print("No ingredients")
  else:
    # ya, I know you probably wanted me to use a for loop here, 
    # but I wanted to try this out
    print(*ingredients, sep = ", ")
    
  
make_sandwich("bread", "chicken slice", "cheese", "lettuce", "tomato")
make_sandwich("bread", "tuna", "cheese", "pepperoni", "tomato")
make_sandwich("bread")
make_sandwich()

