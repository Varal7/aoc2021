@cache
def f(i, j):
    if i == n-1 and j == m-1:
        return tab[i][j]
    if i == n-1:
        return tab[i][j] + f(i, j+1)
    if j == m-1:
        return tab[i][j] + f(i+1, j)
    return tab[i][j] + min(f(i+1, j), f(i, j+1))



