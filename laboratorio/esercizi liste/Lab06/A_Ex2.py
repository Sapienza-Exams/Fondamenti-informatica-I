from tester import tester_fun

def A_Ex2(start,n):
    l=[]
    somma=0
    for i in range(start,start+(2*n)):
        if i%2!=0:
            somma=somma+i
            print(somma)
    return somma




###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""
counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [4,3], 21)
counter_test_positivi += tester_fun(A_Ex2, [4,1], 5)
counter_test_positivi += tester_fun(A_Ex2, [2,3], 15)
counter_test_positivi += tester_fun(A_Ex2, [4,0], 0)
counter_test_positivi += tester_fun(A_Ex2, [5,5], 45)

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
