import time
# import argparse

# Fibonacci series without memoization
def fib(n):
    if n <= 2: return 1
    return fib(n-1) + fib(n-2)

# Fibonacci series with memoization
def fib_memoized(n, mem_dict={}):
    if n <= 2: return 1
    if n not in mem_dict: 
        mem_dict[n] = fib_memoized(n-1,mem_dict) + fib_memoized(n-2,mem_dict)
    return mem_dict[n]

if __name__ == "__main__":
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--Input", help="Number to be calculated")
    # args = parser.parse_args()
    # # n = input("Enter number : ")
    n = 500 #or int(args.Input)
    start = time.time()
    print(fib(n))
    print("LRU_CACHE took %s seconds" % (time.time() - start))
    start_ = time.time()
    print(fib_memoized(n))
    print("Manual memoization of took %s seconds" % (time.time() - start_))
