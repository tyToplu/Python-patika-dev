def flatten_array(list1,list2):
    for i in list1:
        if isinstance(i,list):
            flatten_array(i,list2);
            pass
        else:
            list2.append(i)
    return

#### """test case"""###
#list2 = []; # list2 is nothing but an auxiliary variable.
#flatten_array([[1,'a',['cat'],2],[[[3]],'dog'],4,5],list2);
#print(list2);

def reverse_nested_lists(list1,list2):
    for i in list1:
        if isinstance(i,list):
            i.reverse();
            flatten_array(i,list2);
            pass
        else:
            list2.append(i)
    return
### """ list2 is an auxiliary variable for resulting list"""###
list2 = [];
reverse_nested_lists([[1, 2], [3, 4], [5, 6, 7]],list2)
print(list2)
