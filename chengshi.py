st = [{"beijing":{"mianji":1290,"renkou":123123},"shanghai":{"mianji":12331,"renkou":123123}}]


for i in st:
    for j in i.keys():
        for k in i[j].keys():
            print(j,k,i[j][k])


    
    
