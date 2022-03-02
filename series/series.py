def slices(series, length):
    a=[]
    if len(series)>=length and length>0:
        for i in range(len(series)+1-length):
            a.append(series[i:i+length])
        return a
    raise ValueError("Valueerror")
