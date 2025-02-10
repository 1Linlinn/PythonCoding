print('---下面对象布尔值皆为False---')
print(bool(False))
print(bool(0))
print(bool(''))
print(bool([]))
print('...')


# 每一个都有一个布尔值，有些代码可以直接使用对象的布尔值做判断
content = 'hello'
if content:
    print(f"hi {content}")
else:
    print("空字符串")

lst = [1, 2]
if lst:
    print(f"lst: {lst}")
else:
    print("空列表")

content = ''
if content:
    print(f"hi {content}")
else:
    print("空字符串")