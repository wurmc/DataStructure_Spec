# file paths of existing and new file
exPath = 'E:/Clara/Studium/Master/MA/201905_SpecAnalyzer/20190524_24125GHz_20MHz_01.txt'
newPath = 'E:/Clara/Studium/Master/MA/201905_SpecAnalyzer/20190524_24125GHz_20MHz_01.csv'

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
    print(line)
    # find 'Freq.' in line to find start of relevant data
    result = line.find('Freq.')
    # when 'Freq.' was found, set variables
    if (result != -1):
        check = True
        counter2 = counter
    # filter data, when criteria meet (every line of data after 'Freq.' line
    if (check and counter > counter2):
        help = ''
        # go through line, char by char
        for char in line:
            # when special char, save help2 into value and reset
            if (char == '\t'):
                help += ';'
                value += help
                help = ''
            elif (char == '\n'):
                help += char
                value += help
                help = ''
            else:
                # save char in help2
                help += char
        # write value (relevant data) into new file
        nf.write(value)
        print('value: ', value)
        value = ''
# close all open files
ef.close()
nf.close()
