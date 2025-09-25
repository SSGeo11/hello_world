def bin_search(n, t):
    l = -1
    r = len(n)
    m = (l+r)//2
    while(n[m]!=t and l<=r):
        if(t > n[m]):
            l = m+1
        else:
            r = m-1
        m = (l+r)//2
    if l>r:
        return -1
    else:
        return m

num = [-1, 2, 3, 5, 6, 8, 11]
target = 5

print(bin_search(num, target))
    
