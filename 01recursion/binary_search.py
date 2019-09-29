# 二分查找 在一个含有n个元素的有序序列中有效地定位目标值

def binary_search(data, target, low, high):
    """ return True if target is found in indicated potion of a Python list
    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False
    mid = (low + high) // 2
    if data[mid] == target:
        return True
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, high)
    else: 
        return binary_search(data, target, low, mid - 1)

if __name__ == '__main__':
    print('my name is %s' % ('xiaoming'))
    data = [1, 4, 7 ,10, 23, 37, 69, 82]
    bFound = binary_search(data, 37, 0, len(data))
    bNotFound = binary_search(data, 38, 0, len(data))
    print(f'bFound = {bFound}, bNotFound = {bNotFound}')