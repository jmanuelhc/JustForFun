print("Type in something and I'll check whether or not it is palyndrome:\n ")
uinput = input()
uinput = uinput.split()
uinput = "".join(uinput)
uinput = uinput.upper()
counter = 1

for letter in uinput:
    letter = letter.upper()
    if letter == uinput[-counter] and counter <= len(uinput)/2:
        counter +=1
        continue
    elif counter > len(uinput)/2:
            print("Its palindrome!")
            quit()
    else:
        print("Its not palindrome.")
        quit()

        

