from queues.array_stack import ArrayStack

def is_matched(expr):
    """在算术表达式中分隔符匹配算法"""
    left = '({['
    right = ')}]'
    S = ArrayStack()
    for c in expr:
        if c in left:
            S.push(c)
        elif c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()

def is_matched_html(raw):
    """HTML文本是否匹配标签"""
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1:k]
        if not tag.startswith('/'):
            if not tag.endswith('/'):
                S.push(tag)
        else:
            if S.is_empty():
                return False
            if tag[1:] != S.pop():
                return False
        j = raw.find('<', k+1)
    return S.is_empty()

if __name__ == '__main__':
    matched = is_matched('[(5 + x) - (y + z)]')
    print(matched)
    print(is_matched_html('<a><div/><p>Test duan</p><b/></a>'))