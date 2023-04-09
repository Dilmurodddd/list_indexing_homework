def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=0
    while a<len(list1):
        if list1[a]>=1:
            list1[a]=1
        else:
            list1[a]=False
        a+=1
    return list1
print(main([1,0,1,0,1,0,1,0]))