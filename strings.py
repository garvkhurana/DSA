def removingnumber(s1,ch):
    if len(s1)==0 or s1=="":
        return s1
    elif s1[0]==ch:
        return removingnumber(s1[1:],ch)
    return s1[0] + removingnumber(s1[1:],ch)



s="good morningssssss"
answer=removingnumber(s,'g')
print(answer)
    
    