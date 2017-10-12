# Backend-Python-Interview

<div align="center">
  <a href="https://dribbble.com/shots/3831443-Tech-Interview-Handbook">
    <img src="https://cdn.rawgit.com/yangshun/tech-interview-handbook/master/assets/book.svg" alt="Tech Interview Handbook" width="400"/>
 </a>
</div>


## Required Skills

- 数据结构和算法
- Git

### 数据结构

#### 一. 线性表

1. 线性表（简称表）就是一组元素（的序列）的抽象。一个线性表是某类元素的一个集合，还记录着元素之间的一种顺序关系。是最基本的数据结构之一。
2. ADT List:                     # 一个表抽象的数据类型
       - List(self)              # 表构造操作， 创建一个新表
       - is_empty(self)          # 判断self是否为一个空表
       - len(self)               # 获得self的长度
       - prepend(self, elem)     # 将元素elem加入表中作为第一个元素
       - append(self, elem)      # 将元素elem加入表中作为最后一个元素
       - insert(self, elem, i)   # 将elem加入表中作为第i个元素，其他元素的顺序不变
       - del_first(self)         # 删除表中的首元素
       - del_last(self)          # 删除表中的尾元素
       - del(self, i)            # 删除表中第i个元素
       - search(self, elem)      # 查找元素elem在表中出现的位置， 不出现时返回-1
       - forall(self, op)        # 对表中的每个元素执行操作op
2.1 


。


