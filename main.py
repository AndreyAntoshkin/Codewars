def narcissistic(a):
    a = int(input())
    mas = []
    temp = 0
    c = a
    while (a%10!=0):

        mas.append(a%10)
        a = a//10

    mas.sort()
    b = len(mas)
    #print(b)
    for i in mas:
        temp = temp + (i**b)
    #print(temp)
    #print(c)
    if temp == c:
       return True
    else:
       return False

def main():
    print(narcissistic())

main()