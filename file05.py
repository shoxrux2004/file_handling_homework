def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    r=[]
    h=[]
    for i in range(len(data)):
        if data[i].isdigit():
            r.append(data[i])
            x=(len(r))
        else:
            h.append(data[i])
            y=len(h)
    return x,y
f=open("data/data05.txt").read()
print(main(f))