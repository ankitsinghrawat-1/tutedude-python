with open("output.txt", "r+") as file:
    data = input("Enter text to write to the file: ")
    file.write(data + "\n")
    print("Data successfully written to output.txt")
    xdata = input("Enter additional text to append: ")
    file.write(xdata + "\n")
    file.seek(0)
    rdata = file.read()
    print("Final contents of the output.txt: ", rdata)