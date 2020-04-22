def square(x):
    return x * x

def main():
    for index in range(10):
         print("{} sqaured is {}".format(index,square(index)))

if __name__ == '__main__':
    main()