#Starting up PIL
from PIL import Image
import os,platform

#Asking questions for the file
file = input ("File name?: ")
#loading the image and setting up lists
filepath = os.path.join(file)
im = Image.open(filepath)
pix = im.load()
width, height = im.size#take image size and stores it as variable
RGBchannel = []
#getting a list of rgb
for a in range (height):
        for b in range (width):
                pixelcolour = pix[a,b]
                for c in range (3):
                        RGBchannel.append(pixelcolour[c])
#Minecraft MAP ART 51 different RGB and Names
#stored as [R1,B1,G1,R2,B2,G2]
blockcolor = [127,178,56,247,233,163,199,199,199,255,0,0,160,160,255,167,167,167,0,124,0,255,255,255,164,168,184,151\
,109,77,112,112,112,64,64,255,143,119,72,255,252,245,216,127,51,178,76,216,178,76,216,102,153,216,229,229,51,127,204,25,242,127,165\
,76,76,76,153,153,153,76,127,153,51,76,178,102,76,51,102,127,51,153,51,51,25,25,25,250,238,77,92,219,213,74,128,255,0\
,217,58,129,86,49,112,2,0,209,177,161,159,82,36,149,87,108,112,108,138,186,133,36,103,117,53,160,77,78,57,41,35,135,107,98\
,87,92,92,122,73,88,76,62,92,76,50,35,76,82,42,142,60,46,37,22,16]
#all the names of the blocks at respective positions
block = ["Grass Block","Birch Planks","Mushroom Stem","Redstone Block","Ice","Iron Trapdoor","Fern","White Wool"\
,"Clay","Grass Path","Cobblestone","Water","Oak Planks","Diorite","Acacia Planks","Magenta","Light Blue","Yellow"\
,"Lime","Pink","Gray","Light Gray","Cyan","Purple","Blue","Dark Oak Planks","Green","Red","Black","Gold Pressure Plate"\
,"Dark Prismarine","Lapis Block","Emerlad Block","Spruce Planks","Netherrack","White Terracotta","Orange Terracotta"\
,"Magenta Terracotta","Light Blue Terracotta","Yellow Terracotta","Lime Terracotta","Pink Terracotta","Gray Terracotta"\
,"Light Gray Terracotta","Cyan Terracotta","Purple Terracotta","Blue Terracotta","Brown Terracotta","Green Terracotta"\
,"Red Terracotta","Black Terracotta"]

conv = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
convblock = []
convrgb = []
#RGB offset
pixels = int(len(RGBchannel)/3)
for a in range (pixels):
        #emptying lists
        score = []
        dif = []
        #calculate difference
        for b in range (51):
                for c in range (3):
                #putting each difference value into a buffer
                        if RGBchannel[(a*3)+c] > blockcolor[(b*3)+c]:
                                dif.append((RGBchannel[(a*3)+c]) - (blockcolor[(b*3)+c]))
                        else:
                                dif.append(blockcolor[(b*3)+c] - RGBchannel[(a*3)+c])

        #calculate the score
        for b in range (51):
                score.append(dif[(b*3)] + dif[(b*3)+1]+ dif[(b*3)+2])
        #assigns minscore
        cnt = -1
        #finds position of the best score
        while min(score) != score[cnt]:
                cnt = cnt + 1
        convblock.append(block[cnt])
        for b in range(3):
                convrgb.append(blockcolor[(cnt*3)+b])
        conv[cnt] = cnt
        
img = Image.new( "RGB", (height,width), "white")
imgpix = img.load()
for y in range(width):
        for x in range(height):
               imgpix[y,x] = (convrgb[(width*y*3)+(x*3)],convrgb[(width*y*3)+(x*3)+1],convrgb[(width*y*3)+(x*3)+2])
img.show()
