def simple_yield_func():
    yield "Mani"
    yield "Sahar"
    yield "Mehdi"
    yield 2


itr = simple_yield_func()
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
