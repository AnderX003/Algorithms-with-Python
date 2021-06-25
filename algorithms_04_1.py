if __name__ == '__main__':
    file_name = "04_Text_file_1.txt"
    s = "----------------------------------------"
    try:
        print(f"{s}\nopening the file {file_name}...")
        file = open(file_name, "r")
        file_text = file.read()
        print(f"existing text from file {file_name}:\n{s}")
        print(file_text + f"\n{s}")
        file.close()
    except:
        print(f"file {file_name} didn't exist")
        file = open(file_name, "w")
        file.close()
        print(f"file {file_name} created")

    print(f"now you are adding text to the file {file_name}")
    print(f'to end editing enter "__end__"')
    print(f'to input break line use Enter key\n{s}')
    file = open(file_name, "a")
    while True:
        text = input()
        if text == "__end__":
            break
        file.writelines(text + "\n")

    file.close()
    print(f'{s}\nediting of the file {file_name} ended successfully\n{s}')
