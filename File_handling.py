# file_handling_assignment.py

def create_and_write_file():
    try:
        # Create a new file and write initial lines
        with open('my_file.txt', 'w') as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("End of initial content, line 3.\n")
        print("File created and initial content written successfully.")
    except PermissionError:
        print("Permission denied: unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_and_display_file():
    try:
        # Read the content of the file and display it
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("Reading content from the file:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")
    except PermissionError:
        print("Permission denied: unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        # Append additional lines to the file
        with open('my_file.txt', 'a') as file:
            file.write("This is an appended line 4.\n")
            file.write("Another appended line 5 with a number: 99.\n")
            file.write("Final appended line 6.\n")
        print("Content appended to the file successfully.")
    except PermissionError:
        print("Permission denied: unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_and_write_file()
    read_and_display_file()
    append_to_file()
    read_and_display_file()  # To display the final content after appending

if __name__ == '__main__':
    main()
