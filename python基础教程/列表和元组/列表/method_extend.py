#-----------------------------------
# 列表方法 追加元素
#-----------------------------------

arr = ['a', 'b', 'c', 'd', 'e', 'f']

arr.extend(['1', '2', '3', '4', '5'])
# 在列表后追加多个元素， 注意append是只追加一个元素， extend追加多个元素
print(arr)

arr = ['a', 'b', 'c', 'd', 'e', 'f']

arr[len(arr):] = ['1', '2', '3', '4', '5']
# 使用切片赋值的效果与extend相同， 但不推荐这么写， 可读性变差
print(arr)
