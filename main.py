# functionality to select relevant data from a R&S FSH8 Spectrum Analyzer sweep and store only the value pairs of the actual measurement in a csv file
for x in range(1, 11):

    # file paths of existing and new file
    exPath = "E:/Clara/Studium/Master/MA/Messungen/20190613_Kalibrierung/WLAN/20190624/SA/21m2/20190624_2432MHz_40MHz_21m_" + str(
        x).zfill(2) + ".txt"
    newPath = "E:/Clara/Studium/Master/MA/Messungen/20190613_Kalibrierung/WLAN/20190624/SA/21m2/20190624_2432MHz_40MHz_21m_" + str(
        x).zfill(2) + ".csv"
    print(exPath)
    # open existing and new file
    ef = open(exPath, 'r')
    nf = open(newPath, 'w')

    # read lines of existing file
    ef_lines = ef.readlines()
    # some helpful variables
    counter = 0
    counter2 = 0
    check = False
    value = ''
    # got through the read lines, line by line
    for line in ef_lines:
        counter += 1
        # show current line
        # print(line)
        # find 'Freq.' in line to find start of relevant data
        result = line.find('Freq.')
        # when 'Freq.' was found, set variables
        if (result != -1):
            check = True
            counter2 = counter
        # filter data, when criteria meet (every line of data after 'Freq.' line
        if (check and counter > counter2):
            tmp = ''
            # go through line, char by char
            counter3 = 0
            for char in line:
                # when special char, save help2 into value and reset
                if (char == '\t'):
                    if (counter3 == 0):
                        tmp += ';'
                        value += tmp
                        counter3 = 1
                        tmp = ''
                elif (char == '\n'):
                    # print('tmp: ', tmp)
                    tmp += char
                    value += tmp
                    tmp = ''
                elif (char == ','):
                    tmp += '.'
                    value += tmp
                    tmp = ''
                else:
                    # save char in help2
                    tmp += char
            # write value (relevant data) into new file
            nf.write(value)
            # print('value: ', value)
            value = ''
    # close all open files
    ef.close()
    nf.close()
    print("New file written: ", newPath)
