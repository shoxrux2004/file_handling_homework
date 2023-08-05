def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open("data/data10.txt")
    data=f.readline()
    a=data.replace(' ','')
    return len(a)
print(main("data10.txt"))