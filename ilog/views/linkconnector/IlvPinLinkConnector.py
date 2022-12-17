IlvPinSquare = "int  1"
IlvPinDiamond = "int  2"
IlvPinCircle = "int  4"
IlvPinCross = "int  8"
IlvPinPlus = "int  16"
IlvPinFilledSquare = "int  32"
IlvPinFilledCircle = "int  64"
IlvPinFilledDiamond = "int  128"
IlvPinTriangle = "int  256"
IlvPinFilledTriangle = "int  512"
def ():
    '''returns IlvPinLinkConnector\n\n
    ()\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvLinkImage ilvLinkImage, final boolean b)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    write(final IlvOutputStream ilvOutputStream, final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def read():
    '''returns None\n\n
    read(final IlvInputStream ilvInputStream, final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def setPinColor():
    '''returns None\n\n
    setPinColor(final Color c)\n
    '''
def setPinXORColor():
    '''returns None\n\n
    setPinXORColor(final Color b)\n
    '''
def setPinType():
    '''returns None\n\n
    setPinType(final int d)\n
    '''
def getPinType():
    '''returns int\n\n
    getPinType()\n
    '''
def setPinSize():
    '''returns None\n\n
    setPinSize(final int e)\n
    '''
def getPinSize():
    '''returns int\n\n
    getPinSize()\n
    '''
def calcConnectionPoint():
    '''returns IlvPoint\n\n
    calcConnectionPoint(final IlvLinkImage ilvLinkImage, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def getClosestConnectionPoint():
    '''returns IlvPoint\n\n
    getClosestConnectionPoint(final IlvPoint ilvPoint, final Object o, final Object o2, final Object o3, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def getClosestConnectionPin():
    '''returns IlvGrapherPin\n\n
    getClosestConnectionPin(final IlvPoint ilvPoint, final Object o, final Object o2, final Object o3, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def connectLink():
    '''returns None\n\n
    connectLink(final IlvLinkImage ilvLinkImage, final IlvGrapherPin ilvGrapherPin, final boolean b)\n
    connectLink(final IlvLinkImage ilvLinkImage, final IlvPoint ilvPoint, final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def disConnectLink():
    '''returns None\n\n
    disConnectLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def disconnectLink():
    '''returns None\n\n
    disconnectLink(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def getPin():
    '''returns IlvGrapherPin\n\n
    getPin(final IlvLinkImage ilvLinkImage, final boolean b)\n
    '''
def linkRemoved():
    '''returns None\n\n
    linkRemoved(final IlvLinkImage ilvLinkImage)\n
    '''
def drawGhost():
    '''returns None\n\n
    drawGhost(final Graphics graphics, final IlvTransformer ilvTransformer, final Object o, final Object o2, final Object o3, final boolean b)\n
    drawGhost(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def getGhostBoundingBox():
    '''returns IlvRect\n\n
    getGhostBoundingBox(final IlvTransformer ilvTransformer)\n
    '''
def supportsDrawGhost():
    '''returns boolean\n\n
    supportsDrawGhost()\n
    '''
