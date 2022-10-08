import random
def wrongtable(number):
    wrong = random.randint(1,9)
    table = [i*number for i in range(1,11)]
    table[wrong]= table[wrong]+ random.randint(0,10)
    return table

def correcttable(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1
    return None

if __name__ == '__main__':
    #print(wrongtable(7))
    number = int(input("enter a number : "))
    mytable=wrongtable(number)
    print(mytable)
    wrongindex=correcttable(mytable,number)
    print(wrongindex)
