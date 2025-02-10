# 异常并不一定语法错误
try:
    num1 = 10
    num2 = 0
    res = num1 / num2
except Exception as e:
    # 捕获异常
    print(f'捕获异常，异常是{e}')
print('程序继续运行...')
