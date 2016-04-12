import optparse

def sortString():
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
sortString()

