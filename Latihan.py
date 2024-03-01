# FIBONACCI 1, 1,  2,  3,  5,  8,  13,  21,  34,...
#          0+1,1+1,1+2,2+3,3+5,... 
print("\t<<<\tFIBONACCI\t>>>\t")
print("Deret angka Fibonacci")
print("-"*15)
n = int(input("Masukan angka : "))
print("-"*15)
# Non-List Comprehesion (Manual)
# Fibonacci = [1]
# y = 0
# for i in range(n-1):
#     x = Fibonacci[-1] + y
#     Fibonacci.append(x)
#     y = Fibonacci[-2]
# print(f"{Fibonacci}")

# list Comprehesion
def fibonacci(n):
    x = 1
    y = 1
    for i in range(n):
        yield x
        x, y = y, x + y
Fibonacci = [ fib for i, fib in enumerate(fibonacci(n))]
print(f"{Fibonacci}")