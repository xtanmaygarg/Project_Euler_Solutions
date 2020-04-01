# Please Download Keylog File Also
File = open("keylog.txt", "r").read().split("\n")
File.pop()
Result = []

for Data in File:
    Num_List = list(Data)
    
    if Num_List[0] not in Result:
        Result.insert(0,Num_List[0])
    
    for i in range(1,3):
        fi = Result.index(Num_List[i-1])
        if Num_List[i] not in Result:
            Result.insert(fi + 1,Num_List[i])
        si = Result.index(Num_List[i])
        if fi > si:
            Result[fi],Result[si] = Result[si],Result[fi]

print("".join(Result))
