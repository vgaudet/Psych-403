# -*- coding: utf-8 -*-
"""
Gaudet, Vernon
"""

import numpy as np

# Variable operations exercises
def vopex():
    print("\nVariable operation exercises:")
    
    sub_code = "sub"
    subnr_int = 2
    subnr_str = "2"
    
    print(sub_code+ subnr_str)
    print(sub_code + " " + subnr_str)
    print(sub_code + " " + (subnr_str * 3))
    print((sub_code + subnr_str) *3)
    print(sub_code * 3 + subnr_str * 3)
    
    return sub_code, subnr_int, subnr_str

# List operations exercises
def lopex():
    print("\nList operation exercises:")
    numlist = [ 1, 2, 3] * 2
    numarr = np.array([1, 2, 3]) *2
    
    print(numlist)
    print(numarr)
    
    strlist = ["do", "re", "mi", "fa"]
    for i in range(0,4):
        strlist[i] = strlist[i]+ strlist[i]
    print(strlist)
    
    strlist = ["do", "re", "mi", "fa"]
    strlist.extend(strlist)
    print(strlist)
    
    strlist = ["do", "re", "mi", "fa"]
    for i in range(0,3):
        strlist[i] = strlist[i]+ strlist[i]
    
    strlist = ["do", "re", "mi", "fa"]
    for i in range(0, len(strlist)*2, 2):
        strlist.insert(i, strlist[i])
    print(strlist)
    
    strlist = ["do", "re", "mi", "fa"]
    print([[s]*2 for s in strlist])
    
    return numlist, numarr, strlist

# Zipping exercises
def zipex():
    print("\nZipping exercises:")
    
    face = list(range(1,6)) *10
    face = ["face" + str(i) + ".png" for i in face]
    
    house = sorted(list(range(1,6)) * 10)
    house = ["house" + str(i) + ".png" for i in house]  
    
    img1 = face + house
    img2 = house + face
    
    cue = (["cue1"] *5 + ["cue2"] *5) * 10
    
    trial = list(zip(img1, img2, cue))
    np.random.shuffle(trial)
    
    print(trial)
    
    return trial

# Indexing exercises
def inex():
    print("\nIndexing exercises:")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    print(colors)
    print(colors[-2])
    print(colors[-2][2], colors[-2][3])
    
    colors.remove("purple")
    colors.insert(6,"indigo")
    colors.insert(7, "violet")
    
    print(colors)

    return colors

# Slicing exercises
def slicex():
    print("\nSlicing exercises:")
    list100 = list(range(0, 101))
    
    print(list100)
    print(list100[0:10])
    print(list100[99::-2])
    print(list100[:-5:-1])
    
    
    print("\n\tBoolean operation: \n\t list100[39:44] == list(range(39, 44)")
    print('\t', list100[39:44],'==', list(range(39, 44)), '=',
         (list100[39:44] == list(range(39, 44))))

    return list100


def main():
    vopex()
    lopex()
    zipex()
    inex()
    slicex()
    return

if __name__ == "__main__":
    main()
    

