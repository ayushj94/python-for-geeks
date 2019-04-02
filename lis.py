#code
t = int(input())
while t:
    n = int(input())
    arr = []
    lis = [1] * n
    max_so_far = 1
    arr = [int(e) for e in input().split()]
    for j in range(n-2, -1, -1):
        for k in range(j+1, n, 1):
            if arr[j] < arr [k]:
                lis[j] = max(lis[j], lis[k] +1)
                if lis[j] > max_so_far:
                    max_so_far = lis[j]
                    break
    print(max_so_far)
    t -= 1