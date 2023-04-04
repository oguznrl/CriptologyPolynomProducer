polynom=[]

print("Please enter your polynom exponantial values:(Press 'e' for exit )")
val=0
while(1):
    val=input()
    if(val=='e'):
        break
    polynom.append(int(val))

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
def expand_result(value,expand_value):
    count_of_border=int(value/border_limit)
    else_multipiler=value-(count_of_border*border_limit)
    is_first=False
    expanded_mod=[]
    temp_mod=list()
    if(count_of_border==1):
        for j in range(len(expand_value)):
            temp_mod.append(expand_value[j]+else_multipiler)
    else:
        while(count_of_border>0):
            if(not is_first):
                is_first=True
                count_of_border-=2
                for j in range(len(expand_value)):
                    for k in range(len(expand_value)): 
                        expanded_mod.append(expand_value[j]+expand_value[k])
                for j in range(len(expanded_mod)):
                    temp_mod.append(expanded_mod[j]+else_multipiler)
            else:
                temp_mod.clear()
                count_of_border-=1
                for j in range(len(expanded_mod)):
                    for k in range(len(expand_value)): 
                        temp_mod.append(expanded_mod[j]+expand_value[k])
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
                    if(expanded_res[j]>=border_limit):
                        res=expand_result(expanded_res[j],mod)
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
                    if(j in expanded_res):
                        expanded_res.remove(j)
                max_res=max(expanded_res)
            polynom_subvalues.append(expanded_res)

equal_value=[]
for i in range(len(polynom_subvalues)-1):
    res=0
    for j in polynom_subvalues[i]:
        res+=pow(2,j)
    equal_value.append(res)

print("\n\nGenerated Values:")
print(equal_value)

print("\n\nEnter a value for finding matrix of coresponded that:")
matrix_in=int(input())

value_ind=equal_value.index(matrix_in)

sub_pol=polynom_subvalues[value_ind]

prefix_polynom=list()
result_matrix=list()

for i in range(border_limit):
    prefix_polynom.append([[i],i])
    sub_list=list()
    for j in range(border_limit):
        sub_list.append(0)
    result_matrix.append(sub_list)

prefix_polynom=prefix_polynom[::-1]

for i in range(len(prefix_polynom)):
    temporary_list=list()
    extended_list=list()
    reduced_list=list()
    for j in range(len(prefix_polynom[i][0])):
        for k in range(len(sub_pol)):
            temporary_list.append(prefix_polynom[i][0][j]+sub_pol[k])
    if(max(temporary_list)<border_limit):
        prefix_polynom[i][0]=temporary_list
    else:    
        for j in temporary_list:
            if(j>=border_limit):
                for k in polynom_subvalues[j]:
                    extended_list.append(k)
            else:
                extended_list.append(j)
        
        odd_number=list()
        for j in range(len(extended_list)):
            if(extended_list.count(extended_list[j])%2==0):
                odd_number.append(extended_list[j])
        if(len(odd_number)==0):
            prefix_polynom[i][0]=extended_list
            continue
        reduced_list=unique(reduced_list)
        odd_number=unique(odd_number)
        for j in odd_number:
            if(j in reduced_list):
                reduced_list.remove(j)
        
        prefix_polynom[i][0]=reduced_list
    

for i in prefix_polynom:
    for j in range(len(i[0])):
        result_matrix[i[0][j]][i[1]]=1
print("Coresponing Matrix:\n\n")

for i in result_matrix:
    print(i)

    
    


