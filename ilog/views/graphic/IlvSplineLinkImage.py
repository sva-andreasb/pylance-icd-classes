def ():
    '''returns IlvSplineLinkImage\n\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2, final boolean b, final IlvPoint[] array)\n
    (final IlvSplineLinkImage ilvSplineLinkImage)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvTransformer ilvTransformer)\n
    '''
def setIntermediateLinkPoints():
    '''returns None\n\n
    setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int a)\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
    '''
def allowsPointInsertion():
    '''returns boolean\n\n
    allowsPointInsertion()\n
    '''
def allowsPointRemoval():
    '''returns boolean\n\n
    allowsPointRemoval()\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(int i, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int i, final float n, final float n2, final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def pointsInBBox():
    '''returns boolean\n\n
    pointsInBBox()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setSmoothness():
    '''returns None\n\n
    setSmoothness(final float b)\n
    '''
def getSmoothness():
    '''returns float\n\n
    getSmoothness()\n
    '''
def isSpline():
    '''returns boolean\n\n
    isSpline()\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
