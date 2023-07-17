def product(z):
    p = 1
    for i in z:
        if i!=0:
            p *= i
    return p


print(product([12,2,1,0]))
