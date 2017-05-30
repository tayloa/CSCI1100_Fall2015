def reverse(number):
    if len(number) == 3:
        reversed_number = number[2]+number[1]+number[0]
    if len(number) < 3:
        reversed_number = number
    return reversed_number
   

number = raw_input("Enter a value ==> ") 
print number
new_number = reverse(number)
value_a = abs(int(new_number) - int(number))
value_b = reverse(str(value_a))
value_c = int(value_b) + int(value_a)
print
print "Here is the computation:"
print new_number,"-",number,"=",value_a
print value_a,"+",value_b,"=",value_c
if number == new_number:
    print "Are you sure your input is valid?"
else:
    print "You see, I told you."
