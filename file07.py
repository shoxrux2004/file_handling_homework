def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    sum=0
    i=0
    l=[]
    for i in range(len(data)):
        if data[i].isdigit()==True:
            l.append(data[i])
        a="".join(l)
        x=int(a)
    while x>0:
        r=x%10
        i+=0
        sum+=r
        x//=10
    return sum
f=open("data/data07.txt").read()
print(main(f))