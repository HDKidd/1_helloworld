# !usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter

# collections 提供许多有用的集合类

# 1.1 namedtuple (优化tuple）: 一个函数，用来创建一个自定义的tuple对象，并且规定了元素的个数，并可以用属性而不是索引来引用tuple的某个元素
print('========1.1========')

# tuple 表示不变集合，例如一个点的二维坐标表示为：
p1 = (1, 2)

# 但是光看（1,2）很难看出tuple是表示一个坐标，因此引用Namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])
p2 = Coordinate(1, 2)

print(p2.x)
print(p2.y)

# 表示创建的Coordinate对象是tuple的一个子类
print(isinstance(p2, Coordinate))
print(isinstance(p2, tuple))


# 1.2 用namedtuple定义一个圆
print('========1.2========')

Circle = namedtuple('Circle', ['x', 'y', 'r'])
c1 = Circle(1, 2, 5)

print(c1.r)


# 2.1 deque（优化list): 为了高效实现插入和删除操作的双向列表，适合用于队列和栈
print('========2.1========')

q1 = deque(['a', 'b', 'c'])
q1.append('x')       # 默认往尾部添加元素
q1.appendleft('y')   # 往头部添加元素
print(q1)

q1.pop()             # 删除尾部元素
q1.popleft()         # 删除头部元素
print(q1)


# 3.1 defaultdict (优化dict）: 使 dict 引用的key不存在时抛出keyerror 改为抛出设定值
print('========3.1========')

d1 = defaultdict(lambda: 'N/A')
d1['key1'] = 'abc'
print(d1['key1'])
print(d1['key2'])


# 4.1 orderedDict (优化dict）: 使 dict 的 Key 无序性改为有顺序
print('========4.1========')

d2 = dict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(d2)

d3 = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
print(d3)  # 根据插入的顺序排序，而不是key本身排序

d4 = OrderedDict()
d4['z'] = 1
d4['y'] = 2
d4['x'] = 3
print(list(d4.keys()))  # 按照插入key的顺序排序


# 4.2 orderedDict 实现FIFO的dict，当容量超限时删除最早的key
print('========4.2========')


class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)

# 本节暂未解决


# 5.1 Counter: 计数器，统计字符出现的个数
print('========5.1========')

c1 = Counter()
for ch in 'programming':
    c1[ch] = c1[ch] + 1

print(c1)                    # 统计字符出现了几次
