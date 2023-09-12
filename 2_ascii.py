size=int(input("Enter the size of the dictonary:"))
ascii_dict={}
if size==26:
    alphabet = [chr(ord('a')+i)for i in range(26)]
    ascii_value = [ord(char)for char in alphabet]
    for i in range(26):
        ascii_dict[alphabet[i]]=ascii_value[i]
    print("Dictionary:",ascii_dict)
else:
    print("invalis size")