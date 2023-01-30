def sortPeople(names, heights):
    i=1
    while i < len(heights):
        temph=heights[i]
        tempn=names[i]
        j=i
        while j > 0 and temph > heights[j-1]:
            heights[j]=heights[j-1]
            names[j]=names[j-1]
            heights[j-1]=temph
            names[j-1]=tempn
            j-=1
        i+=1
    return names