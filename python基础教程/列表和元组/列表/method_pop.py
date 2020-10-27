#-----------------------------------
# 列表方法 弹出末位元素或弹出指定索引的元素
#-----------------------------------

arr = ['a', 'b', 'c', 'd', 'e', 'f']
# 默认弹出列表最后一个元素， 并返回这个元素
print(arr.pop())
print(arr)

arr = ['a', 'b', 'c', 'd', 'e', 'f']
# 使用切片赋值空序列达到相同效果， 但代码可读性变差
arr[len(arr) - 1:] = []
print(arr)

arr = ['a', 'b', 'c', 'd', 'e', 'f']
# 传递元素索引，则弹出该元素， 并返回该元素
print(arr.pop(1))
print(arr)
