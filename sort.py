import optparse

def sortString(sortBy):
    with open("sort.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)

    
    array.sort(reverse=sortBy)
    for element in array:
        print(element)

def main():
    parser = optparse.OptionParser()
    parser.add_option('-n', dest='num', type='int')
    (options,args) = parser.parse_args()
    if (options.num > 0):
        sortString(True)
    else:
        sortString(False)

if __name__ == '__main__' :
    main()
