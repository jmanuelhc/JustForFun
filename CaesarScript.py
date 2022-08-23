#Code to encrypt data as the Caesar encryption method, will honor spaces and numbers, all encrypted text will come in upper case
print("Insert a text to encrypt:")
ptext = input()
print("Enter a shift value for the encryption (not bigger than 25):")
shifter = int(input())

etext = ""
for ch in ptext:
    try:
        int(ch)
        if ch.isdigit:
            etext += str(ch)
    except:
        ch = ch.upper()

    if type(ch) == "int":
        continue
    if ch.isspace():
        etext += ch 
    elif ch.isalpha():
        ch = ord(ch) + shifter
        if ch > ord("Z"):
            ch = ch - 26
            etext += chr(ch)
        else:
            etext+=chr(ch)
    else:
        continue
    
print(etext)
