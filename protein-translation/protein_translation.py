translation={"AUG" :"Methionine" ,**dict.fromkeys(['UUU', 'UUC'],'Phenylalanine'),
**dict.fromkeys(['UUA', 'UUG'],'Leucine'),**dict.fromkeys(['UCU', 'UCC', 'UCA', 'UCG'],'Serine'),
**dict.fromkeys(['UAU', 'UAC'],'Tyrosine'),**dict.fromkeys(['UGU', 'UGC'],'Cysteine'),"UGG":"Tryptophan",
**dict.fromkeys(['UAA', 'UAG', 'UGA'],'STOP')}


def proteins(strand):
    acids=aminoacid(strand)
    translated=[]
    for i in acids:
        if translation[i]=='STOP':
            break
        translated.append(translation[i])
    return translated


def aminoacid(sequence):
    acid=[]
    for i in range(0,len(sequence),3):
        acid.append(sequence[i:i+3])
    return acid



print(proteins('UAU'))
