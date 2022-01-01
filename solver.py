
e = ["a","b","c","d"]

affected_e = [0,1,2,3]


temp_e_p = e[affected_e[3]]
for i in range(len(affected_e) - 1):
    e[affected_e[3-i]] = e[affected_e[2-i]]
e[affected_e[0]] = temp_e_p

print(e)