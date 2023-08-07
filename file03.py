def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    for i in range(len(data)):
        if data[i].isdigit()==True:
            l.append(data[i])
    return l
f=open("data/data03.txt").read()
print(main(f))