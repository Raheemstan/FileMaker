import os


def create_files(directory, name, num):
    # Create the specified directory if it doesn't exist
    if not os.path.exists(directory):
        os.mkdir(directory)

    for i in range(num):
        # Generate the file name in the format "i-name.py"
        file_name = f"{i}-{name}.py"

        # Create and write content to the file
        with open(os.path.join(directory, file_name), "w") as file:
            # You can customize the content of the files here
            file.write(f"# This is file {file_name}\n")
            file.write(f'print("Hello from {file_name}")\n')


if __name__ == "__main__":
    directory = input("Enter the directory to create files (relative path): ")
    name = input("Enter the name for the files: ")
    num = int(input("Enter the number of files to create: "))

    create_files(directory, name, num)
    print(f"{num} files named {name} have been created in the directory {directory}.")
