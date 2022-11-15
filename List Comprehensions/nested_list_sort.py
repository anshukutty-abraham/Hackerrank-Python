if __name__ == '__main__':
    records=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
    records.sort()    
    records1=dict(records)
    val_list=sorted(set(records1.values()))
    #print(val_list)
    second_lowest_score=val_list[1]
    #print(second_lowest_score)
    for key,val in records1.items():
        if val==second_lowest_score:
            print(key)
