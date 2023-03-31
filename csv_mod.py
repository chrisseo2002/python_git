'''
How to use:
1. Scrap the information into excel.
2. Save it into .csv format.
3. Put the .csv file and csv_mod.py in the same directory.
4. Modify 'num' into number of columns you want to sort.
5. Run 'python csv_mod.py' in terminal.
6. Open 'result.csv' file.

'''
import csv

def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
    for i in reader:
        output.append(i)
    return output

def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
        a = csv.writer(f, delimiter = ',')
        a.writerows(the_list)

def sortcsv(input, num):
    output = []

    for i in range(0,len(input)-1,num):
        output.append([])
        for j in range(num):
            output[i//num].append(input[i+j][0])
    return output

def main():
    num = 3 #number of columns you want to sort
    input = opencsv('excel_test.csv')
    output = sortcsv(input, num) 
    writecsv('result.csv', output)

if __name__ == "__main__":
    main()
