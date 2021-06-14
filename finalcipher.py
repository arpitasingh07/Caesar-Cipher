
class CaesarCipher: 
   
    def encrypt(string,key):
        result = ""
        for char in string:
            if char == " ": 
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += chr((ord(char)+ key - 65) % 26 +65)
          
        
        return result
  
        



    def decrypt(string,key):
        result = ""
        for char in string:
            if char == " ":
                result += " "
                continue
            if ord(char) > 96 :
                result += chr((ord(char) - key - 97) % 26 + 97)
            else:
                result += chr((ord(char) - key -65) % 65 +65)
      
        return result



if __name__ == "__main__":    
    def main():
        String = input("Enter the message: ")
        key = int(input("Enter the number of shifts you want: "))
        crypt = input("Do you want to encrypt or decrypt the message? : ")
        encrypted = CaesarCipher.encrypt(String,key)
        decrypted = CaesarCipher.decrypt(String,key)    
        print("Plain Text : ", String)
        if crypt == 'encrypt':
            print("Encrypted : ", encrypted)
        elif crypt == 'decrypt':
            print("Decrypted : ", decrypted)
        else:
            print("Invalid input")
        cont = input("Do you want to continue (y/n): ")
        if cont == 'y':
            main()
        else:
            return 0
    main()