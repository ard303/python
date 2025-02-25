def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]

    return result 





students=[[1,"ayan","XII"],[2,"furqan","X"],[3,"usman","VI"],[4,"suffyan","XIII"],[4,"rahim","VII"]]
print(test(students))