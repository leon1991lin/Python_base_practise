#list 分組

def grouping_list(group, data):

    """
        將輸入的序列化物件分組
    :param group: int, 一組要有幾個元素
    :param data: iterable object, 欲分組之物件
    :return: list
    """
    
    #將欲分組之物件建立為iterator

    data_1 = iter(data)
    ans = []

    for i in range(len(data)//group):
        item = [] 
       
        for j in range(group):
            item.append(next(data_1))
            
        #用 for 迴圈將  iterator 輸出指定數量的元素，建立為 list  
        ans.append(item)
    return ans

    

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grouping_list(3, a)

# output : [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#不適用於物件元素數量無法整除每組指定數量的狀況
