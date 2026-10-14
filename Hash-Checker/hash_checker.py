#built-in library for cryptographic hash function
import hashlib 

#create function to calculate the SHA256 hash
def calculate_hash(filepath): 
    
    #empty sha256 object created
    sha256 = hashlib.sha256() 
    
    #opens file that needs hashing
    with open(filepath, "rb") as file: 

        while True:
            #reads a chunk of the file to avoid storing it all in memory
            data = file.read(4096) 

            if not data: #checks if data is empty
                break #exits loop

            #feeds the data chunk into the active sha256 calculation
            sha256.update(data) 
            
    #converts the hash data into readable hexidecimal text
    return sha256.hexdigest() 

#asks user for the filepath
filepath = input("Enter file path: ")

try:
    #calculates the file hash and displays it to user
    file_hash = calculate_hash(filepath) 
    print("\nSHA256 Hash:")
    print(file_hash)
    
#error message is file not found
except FileNotFoundError:
    print("File not found.")
