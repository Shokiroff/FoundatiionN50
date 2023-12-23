def ekub(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print(a)
def royxat(ls:list):
    ls.sort(key= lambda x: x[2], reverse=True)
    print(ls)
ekub(12,28)
ls=[("diyor",12),("siroj",48),("baxtiyor",24),("abbos",22),("johongir",23),("og'abek",19)]
royxat(ls)