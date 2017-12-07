def my_generator():
    try:
        yield 'something'
    except ValueError:
        yield 'dealing with the exceptions'
    finally:
        print("ok let's clean")


gen = my_generator()
next(gen)


print(gen.throw(ValueError('mean mean mean')))

gen.close()
