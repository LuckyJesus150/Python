def average():

    A = list(map(int,input('Enter a list: ').split()))

    print(A)

    avr = sum(A) / len(A)

    print ('Average is:',avr)

    return avr

average()