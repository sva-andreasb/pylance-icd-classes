IlvMarkerSquare = "int  1"
IlvMarkerDiamond = "int  2"
IlvMarkerCircle = "int  4"
IlvMarkerCross = "int  8"
IlvMarkerPlus = "int  16"
IlvMarkerFilledSquare = "int  32"
IlvMarkerFilledCircle = "int  64"
IlvMarkerFilledDiamond = "int  128"
IlvMarkerTriangle = "int  256"
IlvMarkerFilledTriangle = "int  512"
def ():
    '''returns IlvMarker\n\n
    ()\n
    (final IlvPoint point, final int type, final int size)\n
    (final IlvPoint ilvPoint, final int n)\n
    (final IlvMarker ilvMarker)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def getPoint():
    '''returns IlvPoint\n\n
    getPoint()\n
    '''
def setPoint():
    '''returns None\n\n
    setPoint(final IlvPoint ilvPoint)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int b)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final int c)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color d)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
