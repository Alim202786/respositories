import os

def check_path(path):
    if not os.path.exists(path):
        print("Invalid path")
        return
    print(f"Check access {path}")
    print(f"Exists {'Yes' if os.path.exists(path) else 'No'}")
    print(f"Readability {'Yes' if os.access(path, os.R_OK) else 'No'}")
    print(f"Writability {'Yes' if os.access(path, os.W_OK) else 'No'}")
    print(f"Executability {'Yes' if os.access(path, os.X_OK) else 'No'}")
    
if __name__ == "__main__":
    path = input("Enter access: ")
    check_path(path)