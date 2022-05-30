from itertools import product


def multiply_and_greet(*args, **kwargs):
    product=1
    for x in args:
        product*=x
    print(product)
    keys=kwargs.keys()
    if "country" in keys:
        print(f"Hello {kwargs ['name']} you are from {kwargs ['country']}")
    elif "name" in keys:
        print(f"Hello {kwargs ['name']}")
    elif "age" in keys:
        year=2022-age
        print(f"Hello {kwargs ['name']} you were born in {kwargs ['year']}")
    else:
        print(f"Hello world")                

    