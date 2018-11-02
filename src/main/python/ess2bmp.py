import sys, os.path
#TODO Make readable
def ess2bmp(savefile, thumbnail):
    #begin ess data retrieval
    ess = open(savefile, 'rb')
    init = 13

    ess.seek(init)
    headerSize = int.from_bytes(ess.read(4), byteorder='little')

    ess.seek(init+4)
    version = int.from_bytes(ess.read(4), byteorder='little')

    headerByteSize = 4

    widthLocation = init + headerByteSize + headerSize - 8
    ess.seek(widthLocation)
    shotwidth = int.from_bytes(ess.read(4), byteorder='little')

    heightLocation = init + headerByteSize + headerSize  - 4
    ess.seek(heightLocation)
    shotheight = int.from_bytes(ess.read(4), byteorder='little')
    #ess.close()

    #end ess data retrieval
    #begin write bmp
    bmp = open(thumbnail, 'wb')
    #beging file header
    bmp.write(b'BM')
    bmp.write((2147483648).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(2, byteorder='little'))
    bmp.write((0).to_bytes(2, byteorder='little'))
    bmp.write((54).to_bytes(4, byteorder='little'))

    #end file header
    #begin image header
    bmp.write((40).to_bytes(4, byteorder='little'))
    bmp.write((shotwidth).to_bytes(4, byteorder='little'))
    bmp.write((shotheight).to_bytes(4, byteorder='little'))
    bmp.write((1).to_bytes(2, byteorder='little'))
    bmp.write((24).to_bytes(2, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    bmp.write((0).to_bytes(4, byteorder='little'))
    #end image header
    ## OPTIMIZE: Dump Pixels into BMP
    for rgbValue in range(3*shotwidth*shotheight, 0, -3):
        for rgbIndex in range(0,3):
            if rgbIndex == 0:
                ess.seek(init + headerByteSize + headerSize + rgbValue+2)
            elif rgbIndex == 1:
                ess.seek(init + headerByteSize + headerSize + rgbValue+1)
            else:
                ess.seek(init + headerByteSize + headerSize + rgbValue)
            pixelRGB = int.from_bytes(ess.read(1), byteorder='little')
            bmp.write((pixelRGB).to_bytes(1, byteorder='little'))

    print(version)
    print(headerSize)
    print(shotheight)
    print(shotwidth)

def displayFormat():
    print("Use the following format when using ess2bmp.py \n>python ess2bmp.py [Save File Path].ess [Output File Path].bmp")

def isCorrectFormat(thumbnail, savefile):
    if(savefile.endswith(".ess") and thumbnail.endswith(".bmp")):
        return True
    if(not savefile.endswith(".ess")):
        print("The second parameter must be of type .ess")
        displayFormat()
        return False
    elif(not thumbnail.endswith(".bmp")):
        print("The second parameter must be of type .bmp")
        displayFormat()
        return False
    else:
        displayFormat()
    return False

if __name__ == '__main__':
    if(len(sys.argv) == 3):
        savefile = sys.argv[1]
        thumbnail = sys.argv[2]
        if(isCorrectFormat(thumbnail,savefile)):
            if(not os.path.isabs(savefile)):
                savefile = os.path.abspath(savefile)
            if(not os.path.isabs(thumbnail)):
                thumbnail = os.path.abspath(thumbnail)
            ess2bmp(savefile, thumbnail)
    else:
        displayFormat()
