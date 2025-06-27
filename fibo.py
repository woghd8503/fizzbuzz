
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)

def main():
    print(fibo(4))

if __name__ == "__main__":
    main()

