try:
    with open("sample.txt", "r") as file:
        line_number = 1
        while True:
            line = file.readline()
            if not line: #this ensures that if the end of file comes then the loop will break
                break
            print("line", line_number, ":", line)
            line_number += 1
except FileNotFoundError:
    print("Custom Error: The file 'sample.txt' does not exist.")
