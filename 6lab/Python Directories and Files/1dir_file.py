import os

def list_content(path):
    if not os.path.exists(path):
        print("Invalid path! Please enter a valid directory path.")
        return
    
    print("Directories:")
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    for directory in directories:
        print(directory)
    
    print("\nFiles:")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    for file in files:
        print(file)
    
    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)

if __name__ == "__main__":
    path = input("Enter the directory path: ")
    list_content(path)