t = int(input())
while t:
    n1, n2 = [int(e) for e in input().split()]
    lcs = [[0 for col in range(n1)] for row in range(n2)]

    arr1 = input()
    arr2 = input()

    for j in range(0, n2, 1):
        for k in range(0, n1, 1):
            if arr2[j] == arr1[k]:
                lcs[j][k] = 1
                if j and k:
                    lcs[j][k] += lcs[j-1][k-1]
            else:
                lcs[j][k] = max(lcs[j - 1][k], lcs[j][k - 1])

    print(lcs[n2 - 1][n1 - 1])
    t -= 1