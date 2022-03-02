def distance(strand_a, strand_b):
    count=0
    if len(strand_a)!=len(strand_b):
        raise ValueError("+.")
    else:
        for i,(k,v) in enumerate(zip(strand_a,strand_b)):
            if k!=v:
                count+=1
        return count
   
