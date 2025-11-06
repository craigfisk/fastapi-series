
# see https://docs.python.org/3/library/typing.html#typing.get_type_hints


from typing import Annotated, get_type_hints

def double(x: Annotated[int, (0,100)]) -> int:
    type_hints = get_type_hints(double, include_extras=True)
    print(type_hints)
    return x * 2

result = double(511155) 

print(result)  # This will print 1022230

