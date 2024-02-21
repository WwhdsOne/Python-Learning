from my_utils import str_util
print(str_util.str_reverse("hello"))

print(str_util.substr("hello", 1, 3))

from my_utils import file_util
file_util.print_file_info("test.txt")

from my_utils import file_util
file_util.append_to_file("test.txt", "hello world")