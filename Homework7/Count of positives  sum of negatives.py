def count_positives_sum_negatives(arr):
    sum=0
    count=0
    list=[]
    if arr != []:
        for i in arr:
            if i > 0:
                count+=1
            elif i < 0:
                sum +=i
        list.append(count)
        list.append(sum)
    return list