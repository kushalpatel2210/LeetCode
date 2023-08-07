import os

def main():
    folder_names = [name for name in os.listdir() if os.path.isdir(name)]
    for folder_name in folder_names:
        print(folder_name)

if __name__ == "__main__":
    main()
