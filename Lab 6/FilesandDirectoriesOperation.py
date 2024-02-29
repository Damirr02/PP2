import os

# Ex 1
def list_directories_files(path):
    print("Directories:")
    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)

    print("\nFiles:")
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)

def list_all_directories_files(path):
    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        for file_name in files:
            print(os.path.join(root, file_name))

if __name__ == "__main__":
    specified_path = input("Enter the path: ")

    list_directories_files(specified_path)
    list_all_directories_files(specified_path)
    
# Ex 2
def check_access(path):
    print(f"Existence: {'Exists' if os.path.exists(path) else 'Does not exist'}")
    print(f"Readability: {'Readable' if os.access(path, os.R_OK) else 'Not readable'}")
    print(f"Writability: {'Writable' if os.access(path, os.W_OK) else 'Not writable'}")
    print(f"Executability: {'Executable' if os.access(path, os.X_OK) else 'Not executable'}")

if __name__ == "__main__":
    specified_path = input("Enter the path: ")

    print("\nChecking access to specified path:")
    check_access(specified_path)
    
# Ex 3
def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

if __name__ == "__main__":
    specified_path = input("Enter the path: ")

    print("\nTesting the given path:")
    test_path(specified_path)
    
# Ex 4
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

if __name__ == "__main__":
    filename = input("Enter the path to the text file: ")
    line_count = count_lines(filename)
    print(line_count)
    
# Ex 5
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
    print(filename)

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    filename = input("Enter the filename to write the list to: ")
    write_list_to_file(filename, my_list)
    
# Ex 6
def generate_text_files():
    for i in range(65, 91): 
        letter = chr(i) 
        filename = f"{letter}.txt"
        with open(filename, 'w') as file:
            pass  
        print(filename)

if __name__ == "__main__":
    generate_text_files()
    
# Ex 7
def copy_file(source_file, destination_file):
    with open(source_file, 'r') as source:
        with open(destination_file, 'w') as destination:
            destination.write(source.read())

if __name__ == "__main__":
    source_file = input("Enter the source file path: ")
    destination_file = input("Enter the destination file path: ")

    copy_file(source_file, destination_file)

# Ex 8
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)

if __name__ == "__main__":
    specified_path = input("Enter the file path to delete: ")

    delete_file(specified_path)