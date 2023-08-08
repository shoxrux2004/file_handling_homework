def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    l=[]
    for i in range(len(data)):
        if data[i].isdigit()==True:
            l.append(data[i])
    a=min(l)
    return a
f=open("data/data09.txt").read()
print(main(f))