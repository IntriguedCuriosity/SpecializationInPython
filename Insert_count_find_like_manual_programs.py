def count(lst,count_element):
    accum=0
    for i in lst:
        if i == count_element:
            accum= accum+1
    return accum

def in_exist(lst,element):
    for i in lst:
        if i == element:
            return True
        else:
            return False

def reverse(lst):
    rev=[]
    for i in lst:
        rev= [str(i)] + rev
    return rev

def index(lst,element):
    index=0
    for i in lst:
        index =index +1
        if i == element:
            return index -1

def insert(lst,element,pos):
    if len(lst) > pos + 1:
        return lst[:pos] + [element] + lst[pos:]
      
lst=[1,23,4,5,'arshad','shaikh','arshad',1,2,11,1]
print(count(lst,1))
print(in_exist(lst,6))
print(reverse(lst))
print(index(lst,1))
print(lst)
print(insert(lst,3,3))