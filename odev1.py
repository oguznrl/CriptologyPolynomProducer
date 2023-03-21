polynom=[4,1,0]

border_limit=max(polynom)
mod=[]

for i in polynom:
    if(i==border_limit):
        pass
    else:
        mod.append(i)
def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

polynom_subvalues=[]
def expand_result(value):
    count_of_border=int(value/border_limit)
    else_multipiler=value-(count_of_border*border_limit)
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
                for j in range(len(expanded_mod)):
                    temp_mod.append(expanded_mod[j]+else_multipiler)
            else:
                temp_mod.clear()
                count_of_border-=1
                for j in range(len(expanded_mod)):
                    for k in range(len(mod)): 
                        temp_mod.append(expanded_mod[j]+mod[k])
            expanded_mod.clear()
            for j in range(len(temp_mod)):
                expanded_mod.append(temp_mod[j])
            

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
            max_res=max(expanded_res)
            while(max_res>=border_limit):
                for j in range(len(expanded_res)):
                    if(expanded_res[j]>=4):
                        res=expand_result(expanded_res[j])
                        expanded_res[j]=res[0]
                        for k in range(1,len(res)):
                            expanded_res.append(res[k])
                odd_number=list()
                for j in range(len(expanded_res)):
                    if(expanded_res.count(expanded_res[j])%2==0):
                        odd_number.append(expanded_res[j])
                expanded_res=unique(expanded_res)
                odd_number=unique(odd_number)
                for j in odd_number:
                    if(j in odd_number):
                        expanded_res.remove(j)
                max_res=max(expanded_res)
            polynom_subvalues.append(expanded_res)

equal_value=[]
for i in range(len(polynom_subvalues)-1):
    res=0
    for j in polynom_subvalues[i]:
        res+=pow(2,j)
    equal_value.append(res)

print(equal_value)
