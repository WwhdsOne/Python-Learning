"""
Python的类型注解是Python 3.5版本引入的一个新特性,它允许你为函数的参数和返回值添加类型信息。
这些类型信息对Python解释器没有任何影响,但可以帮助开发者理解函数的预期输入和输出。
也可以被一些工具用来进行类型检查和自动补全。
以下是一个使用了类型注解的Python函数的例子:
"""
def greet(name: str) -> str:
    return f"Hello, {name}!"
# 基础类型的类型注解如下
def add_numbers(a: int, b: int) -> int:
    return a + b

def concatenate_strings(a: str, b: str) -> str:
    return a + b

def get_length(s: str) -> int:
    return len(s)

def is_even(n: int) -> bool:
    return n % 2 == 0

def divide_numbers(a: float, b: float) -> float:
    return a / b

from typing import List, Tuple, Dict, Set

def sum_list(numbers: List[int]) -> int:
    return sum(numbers)

def first_element(elements: Tuple[int, ...]) -> int:
    return elements[0]

def get_value(my_dict: Dict[str, int], key: str) -> int:
    return my_dict[key]

def add_to_set(my_set: Set[int], value: int) -> Set[int]:
    my_set.add(value)
    return my_set

# 除了使用 变量: 类型， 这种语法做注解外，也可以在注释中进行类型注解。
# 语法：
# type: 类型
var1 = 1 # type: int
var2 = "hello" # type: str
var3 = 1.0 # type: float

"""
在Python的typing模块中，Union类型表示一个值可以是多种类型中的一种。
以下是一些使用Union的例子：
"""
from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b

def print_string_or_list(data: Union[str, List[str]]) -> None:
    if isinstance(data, str):
        print(data)
    else:
        print("\n".join(data))
print_string_or_list("hello") # hello
print_string_or_list(["a", "b", "c"]) # a\nb\nc



