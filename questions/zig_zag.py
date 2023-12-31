def findZigZagSequence(a, n):
    a.sort()
    mid = n//2
    a[mid], a[n-1] = a[n-1], a[mid]

    st = 0
    ed = n - 1
    while(st <= mid):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
# findZigZagSequence([1,2,3,4,5,6,7], 7)
findZigZagSequence([2,3,5,1,4], 5)