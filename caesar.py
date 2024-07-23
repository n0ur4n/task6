message=input("Enter your message ")
shift= int  (input("Input shift value "))
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
output=""

for i in message : 
    if i in alphabet:
        index=((alphabet.index(i))+ (shift))%26
        output+=alphabet[index]
    else:
        output+=i
        
print(output)

    
        