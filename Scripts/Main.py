print("Operator '+' is addition, operator '-' is substraction, operator '/' is division, operator '*' is multiplication, operator '**' is power.")

print("")

num_1 = input("First Input:  ")
num_2 = input("Sceond Input: ")
operator = input("Operator ")

if operator == ("+"):
    sum = (float(num_1) + float(num_2))

if operator == ("-"):
    sum = (float(num_1) - float(num_2))

if operator == ("/"):
    sum = (float(num_1) / float(num_2))

if operator == ("*"):
    sum = (float(num_1) * float(num_2))

if operator == ("**"):
    sum = (float(num_1) ** float(num_2))

print("The sum is: " + str(sum))