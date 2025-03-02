import os

def count_number(path):
    if not os.path.exists(path):
        print("the file does not exist")
        return
    
    file =open(path, 'r', encoding='utf-8')
    count = sum(1 for _ in file)
    file.close()
    print(f"Number line in the file: {count}")
    
if __name__ == "__main__":
    path = input("Enter path: ")
    count_number(path)