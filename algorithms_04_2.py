if __name__ == '__main__':
    golosni = "qeyuioajQEYUIOAJ"
    prygolosni = "wrtpsdfghklzxcvbnnmWRTPSDFGHKLZXCVBNM"
    file_name_1 = "input.txt"
    file_name_2 = "output.txt"

    file = open(file_name_1, "r")
    file_text = file.read()
    file.close()

    arr, word, g, p = [], "", 0, 0
    word_is_started = False

    for i in file_text:
        if i not in golosni + prygolosni:
            if word_is_started:
                arr.append([word, g <= p])
                arr.append([i, True])
                word_is_started = False
                word, g, p = "", 0, 0
            else:
                arr.append([i, True])
        elif i in golosni:
            word_is_started = True
            g += 1
            word += i
        elif i in prygolosni:
            word_is_started = True
            p += 1
            word += i

    file = open(file_name_2, "w")
    for i in arr:
        if i[1]:
            file.write(i[0])
    file.close()

