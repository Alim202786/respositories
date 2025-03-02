import os

def write_list(path, data):
    file = open(path, 'w', encoding='utf-8')
    for s in data:
        file.write(str(s) + '\n')
    file.close()
    print(f"list written {path}")
    
if __name__ == "__main__":
    path = input("Enter path: ")
    data = input("Enter list: ").split()
    write_list(path, data)