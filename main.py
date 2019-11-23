import numpy as np

mat = [[0, 999, 999, 999, -1, 999],
       [1, 0, 999, 2, 999, 999],
       [999, 2, 0, 999, 999, -8],
       [-4, 999, 999, 0, 3, 999],
       [999, 7, 999, 999, 0, 999],
       [999, 5, 10, 999, 999, 0]]

for row in mat:
    print(row)


print()
for k in range(0, 6):
    print("K = " + str(k+1) + ":")
    for i in range(0, 6):
        for j in range(0, 6):
            if i == j:
                continue
            if k == i or k ==j:
                continue
            tmp = mat[i][j]
            tmp2 = mat[i][k] + mat[k][j]
            m = np.minimum(tmp, tmp2)
            if m > 500:
                continue
            mat[i][j] = m
            # pi[i][j] =
            if tmp != mat[i][j]:
                print("D^" + str(k+1) + " [" + str(i+1) + ", " + str(j+1) + "] = " + str(mat[i][j]))
                # print("was: " + str(tmp) + "  became: " + str(mat[i][j]))
    for r in mat:
        print(r)
    print()
print()
for row in mat:
    print(row)
