VerticalLink = "int  0"
HorizontalLink = "int  1"
def ():
    '''returns IlvDoubleLinkImage\n\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b)\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final int a, final boolean b)\n
    (final IlvDoubleLinkImage ilvDoubleLinkImage)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setOrientation():
    '''returns None\n\n
    setOrientation(final int a)\n
    '''
def getOrientation():
    '''returns int\n\n
    getOrientation()\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getConnectionReferencePoint():
    '''returns IlvPoint\n\n
    getConnectionReferencePoint(final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def getConnectionPoints():
    '''returns None\n\n
    getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvTransformer ilvTransformer)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
