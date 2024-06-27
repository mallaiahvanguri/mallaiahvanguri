#Write a Program To REVERSE content of the given String by using while loop?
def reverse(s):
    res=''
    i=len(s)-1
    while i>=0:
        res=res+s[i]
        i=i-1
    return res
s="Mallaiah M.Tech CSE Hyderabad"
res=reverse(s)
print('the reverse string is ',res)

def reverse_list_string(lst):
    res=[]
    for i in range(len(lst)):
        if isinstance(lst[i],str):
            lst[i]=lst[i][::-1]
    #return res

list=[0, 1, 2, 3, 4, 'mallaiah', 6, 7, 8, 9]
#list=['apple', 'banana', 'cherry']
lst=reverse_list_string(list)
print("reverse list is",lst)