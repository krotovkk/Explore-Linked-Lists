import time 
from linked_list import node, linked_list
from random import randint
import sys

sys.setrecursionlimit(100000)
T  = 1000


def benchmark(func):

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("{:s}: {:f} ms".format(func.__name__,(end - start) * 1000))
    return wrapper

@benchmark
def insert_bench():
    l = linked_list()
    head = None
    for i in range(T):
        data = randint(1, 100)
        head = l.insert(head, data)

@benchmark
def lib_insert_bench():
    l = []
    for i in range(T):
        l.append(i)

insert_bench()	
lib_insert_bench()