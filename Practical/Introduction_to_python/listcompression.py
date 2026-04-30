# create list of songs with their ratings
songlist = [("S1", 3), ("S2", 5), ("S3", 2), ("S4", 4), ("S5", 1)]
# syntax [what to print    for statement   if condition]
goodsongs = [x for x in songlist if x[1]>3]
print(goodsongs)