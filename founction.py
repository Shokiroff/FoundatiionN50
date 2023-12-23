def ekub(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    print(a)
def royxat(ls:list):
    ls.sort(key= lambda x: x[1], reverse=True)
    print(ls)
def sonlar(st:str):
    for x in st:
        if x.isdigit():
            print(x,end=" ")
    print()
def kvadrat(ls):
    ls,lambda x:x**2
    print(ls)
    
ekub(12,28)
ls=[("diyor",12),("siroj",48),("baxtiyor",24),("abbos",22),("johongir",23),("og'abek",19)]
royxat(ls)
sonlar(st="adss123sf4eddf5dds4w342wd0c")
ls1=[12,343,21,4,65,89,0,21]
kvadrat(ls)
