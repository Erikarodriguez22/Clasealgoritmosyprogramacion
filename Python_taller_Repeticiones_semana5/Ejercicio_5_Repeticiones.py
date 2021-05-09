for k in range(1,1001):
    sigma=(k**2+1)/k
    if(sigma>=999):
        break
print(sigma,k)