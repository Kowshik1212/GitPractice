import multiprocessing

square_numbers = [1,2]
def cal_squares(numbers,result):
    print(str(square_numbers))
    for idx,i in enumerate(numbers):
        result[idx] = i*i

def speakLoud():
    print("I'm speaking")

def writeFast():
    print("I'm writing")

def singSweat():
    print("I'm singing")

def hear():
    print("I'm hearing")

def walk():
    print("I'm walking")

numbers = [1,2,3]

if __name__ == "__main__":
    result = multiprocessing.Array("i", 3)
    p1 = multiprocessing.Process(target = cal_squares, args = (numbers,result))
    p1.start()
    p1.join()
    print(result[:])


