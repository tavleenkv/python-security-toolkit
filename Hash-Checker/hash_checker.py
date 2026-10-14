import hashlib 

def calculate_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as file:

        while True:

            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


filepath = input("Enter file path: ")

try:

    file_hash = calculate_hash(filepath)

    print("\nSHA256 Hash:")
    print(file_hash)

except FileNotFoundError:

    print("File not found.")
