polynom=[4,1,0]

border_limit=max(polynom)
mod=[]

for i in polynom:
    if(i==border_limit):
        pass
    else:
        mod.append(i)

polynom_subvalues=[]
def expand_result(value):
    count_of_border=i-border_limit
    else_multipiler=i-count_of_border*border_limit
    is_first=False
    expanded_mod=[]
    temp_mod=list()
    if(count_of_border==1):
        for j in range(len(mod)):
            temp_mod.append(mod[j]+else_multipiler)
    else:
        while(count_of_border>0):
            if(not is_first):
                is_first=True
                count_of_border-=2
                for j in range(len(mod)):
                    for k in range(len(mod)): 
                        expanded_mod.append(mod[j]+mod[k])
            else:
                count_of_border-=1
                for j in range(len(mod)):
                    for k in range(len(mod)): 
                        temp_mod.append(mod[j]+mod[k])
                expanded_mod.clear()
                for j in temp_mod:
                    expanded_mod.append(j)
                temp_mod.clear()
            for j in range(len(expanded_mod)):
                temp_mod.append(expanded_mod[j]+else_multipiler)

    expanded_mod.clear()
    for j in temp_mod:
        expanded_mod.append(j)
    temp_mod.clear() 
    return expanded_mod

for i in range(pow(2,border_limit)):
    if(i<border_limit):
        polynom_subvalues.append([i])
    else:
        if(i==border_limit):
            polynom_subvalues.append(mod)
        else:
            expanded_res=[i]
            while(max(expanded_res)>border_limit):
                for j in range(len(expanded_res)):
                    if(expanded_res[j]>=4):
                        res=expand_result(expanded_res[j])
                        expanded_res[j]=res[0]
                        for k in range(1,len(res)):
                            expanded_res.append(k)
                for j in range(len(expanded_res)):
                    temp_val=None
                    if(expanded_res.count(expanded_res[j])>1):
                        temp_val=expanded_res[j]
                        expanded_res.remove(expanded_res[j])
                        expanded_res.append(temp_val)
            polynom_subvalues.append(expanded_res)


            
            
                   
                
                        

