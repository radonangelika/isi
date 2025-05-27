import math

def method1():
    print("Sposób 1 (math):")
    for i in range(1, 257):
        if i % 2 == 0:
            print(f"sqrt({i}) = {math.sqrt(i)}")

def method2():
    print("\nSposób 2 (list comprehension):")
    wyniki = [math.sqrt(i) for i in range(2, 257, 2)]
    print(wyniki)

if __name__ == '__main__':
    method1()
    method2()
