import optparse

def sortString(sortBy):
    with open("sort.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line)
    array.sort(reverse=sortBy)
    return array
 
def main():
    parser = optparse.OptionParser()
    parser.add_option('-n', dest='num', type='int', help='Enter 0 or 1 to sort array desc or asc')
    parser.add_option('-o', dest='out', type='string', help='Specify output file')
    (options,args) = parser.parse_args()

    if (options.num > 0):
        result = sortString(True)
    else:
        result = sortString(False)

    for i in result:
        print(i)
        if(options.out != None and options.out!='sort.txt'):
            f = open(options.out, 'a')
            f.write(str(result)+'\n')

    

if __name__ == '__main__' :
    main()
