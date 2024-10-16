
#Shifting Functions:

#function to left shift the message
def shift_left(input, d):
    # slice string in two parts for left
    Lfirst = input[0: d]
    Lsecond = input[d:]
    return Lsecond + Lfirst

#function to right shift the message
def shift_right(input, d):
    # slice string in two parts for right
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]
    # now concatenate two parts together
    return (Rsecond + Rfirst)

#function for encrypt the message
def encrypt_text(plaintext: str, shift: int, rotation: int) -> str:
    l = []
    r = []
    string = ""
    shift = 3
    rotate = 2
    shifted_text = shift_right(plain_text, shift)
    for i in shifted_text:
        l.append(ord(i))
    for j in l:
        rotated = (j+ rotate -32) %94 + 32
        r.append(rotated)
    for k in r:
        if(k < 48):
            string += "~"
        else:
            string += chr(k)
    hash_no = hash(plain_text)
    print("Encrypted string: {} \nHash number: {}".format(string, hash_no))

#function for decrypt the message 
def decrypt_text(encrypted: str, shift: int, rotation: int) -> str:
    l = []
    r = []
    string = ""
    shift = 3
    rotate = 2

    for i in plain_text:
        l.append(ord(i))
    for k in l:
        if (k < 48):
            l.remove(k)
    for rotated in l:
        j = (rotated - 32) %94 + 32 - rotate
        r.append(j)
    for s in r:
        string += chr(s)
    decrypted = shift_left(string, shift)
    hash_no = hash(decrypted)
    if(hash_no == has_n0):
        print("Decrypted message: {}".format(decrypted))
    else:
        print("invalid Hash Number")


#function for determine the hash number
def hash_text(hash: str, base: int, hash_size: int) -> int:
    l = []
    h = []
    sum = 0
    for i in plain_text:
        l.append(ord(i))
    for j in l:
        new_value = (l.index(j) + 31)**j
        h.append(new_value)
    for k in h:
        sum += (k%1000000000)
    return sum

#main function
def main():
    inpt = input("enter your choice(for encrypt enter e and for decrypt enter d:")
    if(inpt == "e"):
        message = input("enter the message:")
        encrypt_text(plaintext)
    elif(inpt == "d"):
        message = input("enter encryted message:")
        hash_no = int(input("enter hash number:"))
        decrypt_text(message, hash_no)
    else:
        print("invalid choice")
main()