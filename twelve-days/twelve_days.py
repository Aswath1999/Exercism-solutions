def recite(start_verse, end_verse):
    days=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth",
 "eleventh","twelfth"]
    gifts = ["a Partridge in a Pear Tree.", "two Turtle Doves, and ", "three French Hens, ", "four Calling Birds, ", "five Gold Rings, ", "six Geese-a-Laying, ", "seven Swans-a-Swimming, ", "eight Maids-a-Milking, ", "nine Ladies Dancing, ", "ten Lords-a-Leaping, ", "eleven Pipers Piping, ", "twelve Drummers Drumming, "]
    lyrics=[]
    for i in range(start_verse-1,end_verse):
        verse=f"On the {days[i]} day of Christmas my true love gave to me: {''.join(gifts[i::-1])}"
        lyrics.append(verse)
    return lyrics
        

    # return [f"On the {days[verse]} day of Christmas my true love gave to me: {''.join(gifts[verse::-1])}" for verse in range(start_verse-1, end_verse)]
