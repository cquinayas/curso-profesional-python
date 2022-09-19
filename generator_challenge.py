import time
def fibo_max(max:int):
    n1,n2 = 0,1
    counter = 0
    while True:
        if counter <= max:
            yield n1
            aux = n1+n2
            n1,n2 = n2, aux
            counter += 1
        else:
            raise StopIteration

if __name__ == "__main__":
    fibonacci = fibo_max(20)
    for element in fibonacci:
        print (element)
        time.sleep(1)
        
        