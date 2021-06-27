import numpy as np
import PIL
from PIL import Image
from array import array


class ArrayMake:
        def createPix(fileName):
            pix = np.array(fileName)


print('Hello, world!')



I = np.array(PIL.Image.open(r"Image editor first functions add visual\Coding Py\2.jpg"))
#print(I)
#I.setflags(write=1)



def creepyPic():
    redAddForLighterPic= 175
    greenAdd = 1
    blueAdd = 1

    print(I[1500][2000])
    #columns
    for t in range(0,3000):
        #rows
        for x in range(0,4000):
                    
                    #first color filter
                        if ((I[t][x][0] > 245 or I[t][x][0] < 205) and
                            (I[t][x][1] > 190 or I[t][x][1] < 150) and
                            (I[t][x][2] > 160 or I[t][x][2] < 120)):
                    # if (I[t][t][0] < 220):                 
                                I[t][x][0] += redAddForLighterPic


    img = Image.fromarray(I, 'RGB')
    img.save('my.jpg')

                
creepyPic()


def blackGraph():

    #simplest formula y = x*x
    array1 = []
    #Making de y values change array
    for i in range(0,10):
        k = [i,i*i]
        array1.append(k);
    
    print(array1)

    
    
    
    redAddForLighterPic= 175
    greenAdd = 1
    blueAdd = 1

    
    #in comparison to de standart creepy pic gonna be added de block of pixels to
    #make de graph more fat

    
    #cycle of de previous one for de future usages

    #columns
   # for t in range(250,500):
        #rows
    #    for x in range(250,500):
                    
      #              if (t == 250 and x == 250):
    for l in range(0,10):
                        
                            u = 250+array1[l][0]
                            I[u][250+array1[l][1]] = [0,0,0]
                                #making it fat 4 sides
                            I[u+1][250+array1[l][1]] = [0,0,0]
                            I[u-1][250+array1[l][1]] = [0,0,0]
                            I[u+1][250+array1[l][1]] = [0,0,0]
                            I[u-1][250+array1[l][1]] = [0,0,0]
                                #a bit more fat
                           # I[250+array1[l][0]+2][250+array1[l][1]+2] = [0,0,0]
                           # I[250+array1[l][0]-2][250+array1[l][1]+2] = [0,0,0]
                          #  I[250+array1[l][0]+2][250+array1[l][1]-2] = [0,0,0]
                           # I[250+array1[l][0]-2][250+array1[l][1]+2] = [0,0,0]


    img = Image.fromarray(I, 'RGB')
    img.save('blacGgraph.jpg')

                
        #lets try to add de formula of de pixelz black blank graph
    #firstExperiment make de pic a bit brighter hm
    #if 0 element last arrays groupd 255 - number is > 40 add +35


#blackGraph()
    #    print(t[500])
    #    r = t[0,1,2]
    #    g = t[1,2,3]
    #b = t[2]

    #    print("red: " + r + " green: " + g + " blue: " + b)
        

def beautifullPic():
    redAddForLighterPic= 175
    greenAdd = 1
    blueAdd = 1

    #columns
    for t in range(0,4000):
        #rows
        for x in range(0,3000):
                    


                    # if (I[t][t][0] < 220):   
                    # 
                    # 
                    # 
                    # 
                    # 
                    #               
                        I[t][x][0] += 150
                        I[t][x][1] += 150
                        I[t][x][2] += 150   

    img = Image.fromarray(I, 'RGB')
    img.save('newStyle.jpg')

                
#beautifullPic()
        



#C:\Users\xXx\Desktop\Day0-Day73\Projects folder\Django\First project\Image editor first functions add visual\Coding Py\2.jpg
"""array1 = ArrayMake.createPix("/images/2.jpg")
print(array1)"""