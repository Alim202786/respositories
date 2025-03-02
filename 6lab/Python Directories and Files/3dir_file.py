import os

def check_path(path):
    if not os.path.exists(path):
        print("the path does not exist.")
        return
    
    print(f"Path Exists Yes")
    print(f"Directory portion {os.path.dirname(path)}")
    print(f"Filename portion {os.path.basename(path)}")
    
if __name__ == "__main__":
    path = input("Enter path: ")
    check_path(path)