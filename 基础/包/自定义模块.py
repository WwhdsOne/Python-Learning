# 测试模块
# 在实际开发中，当一个开发人员编写完一个模块后，为了让模块能够在项目中达到想要的效果，
# 这个开发人员会自行在py文件中添加一些测试信息，例如，在my_module.py文件中添加测试代码test(1,1)

# 问题: 
# 此时，无论是当前文件，还是其他已经导入了该模块的文件，在运行的时候都会自动执行`test`函数的调用

# 解决方案
# 只在当前文件中调用该函数，其他导入的文件内不符合该条件，则不执行test函数调用
import mymodule
if __name__ == '__main__':
    mymodule.test (1, 1)
    
# 注意事项：当导入多个模块的时候，且模块内有同名功能. 当调用这个同名功能的时候，调用到的是后面导入的模块的功能
from mymodule import test
from mymodule01 import test
print(test(2, 3))  # 输出：1

# __all__
# 如果在模块中定义了__all__变量，当使用from...import *导入模块时，只有__all__中的函数、类、变量会被导入，其他的都不会被导入。
from mymodule01 import *
print(hide(2, 3))  # 输出：1


    

    


