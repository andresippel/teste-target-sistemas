def fibonacci(n):
    fib_seq = [0, 1]
    while fib_seq[-1] < n:
        next_value = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_value)
    return fib_seq

def is_fibonacci(num):
    fib_seq = fibonacci(num)
    return num in fib_seq

def main():    
    num = int(input("Informe um número positivo: "))
    
    if (num < 0):
        print(f"Por favor, digite um número positivo (maior que zero)")
    elif is_fibonacci(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
