import os

def generate_text(path):
    for letter in range(65, 91):
        file_name = f"{chr(letter)}.txt"
        file_path = os.path.join(path, file_name)
        file = open(file_path, 'w', encoding='utf-8')
        file.write(f"the file {file_name}\n")
        file.close()
    
    print("(A-Z)")

if __name__ == "__main__":
    dir = input("Enter: ")
    generate_text(dir)