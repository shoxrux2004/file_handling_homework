def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l=[]
    for i in range(len(data)):
        if data[i].isalpha:
            l.append(data[i])
    return l
f=open("data/data04.txt").read()
print(main(f))