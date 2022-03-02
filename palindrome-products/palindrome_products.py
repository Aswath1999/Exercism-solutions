def largest(min_factor, max_factor):
    pal=1
    fac=[]
    for a in range(min_factor,max_factor+1):
        for i in range(a,max_factor+1):
            if str(a*i)==str(a*i)[::-1]:
                if a*i>pal:
                    pal=a*i
                    fac+=[{a,i}]
    return (pal,fac[0])


def smallest(min_factor, max_factor):
    pal=max_factor**2
    factors=[]
    for a in range(min_factor,max_factor+1):
        for i in range(a,max_factor+1):
            s=a*i
            if str(a*i)==str(a*i)[::-1]:
                if s<pal:
                    pal=a*i
                    factors=[{a,i}]
    return (pal,factors)

print(smallest(1000,9999))