def ():
    '''returns IlvLinkImage\n\n
    (final IlvGraphic a, final IlvGraphic b, final boolean c)\n
    (final IlvLinkImage ilvLinkImage)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom(final IlvGraphic a)\n
    '''
def setTo():
    '''returns None\n\n
    setTo(final IlvGraphic b)\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def allowsPointInsertion():
    '''returns boolean\n\n
    allowsPointInsertion()\n
    '''
def allowsPointRemoval():
    '''returns boolean\n\n
    allowsPointRemoval()\n
    '''
def allowsPointMove():
    '''returns boolean\n\n
    allowsPointMove(final int n)\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int i, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int n, final float n2, final float n3, final IlvTransformer ilvTransformer)\n
    '''
def setIntermediateLinkPoints():
    '''returns None\n\n
    setIntermediateLinkPoints(final IlvPoint[] array, final int n, final int n2)\n
    '''
def pointsInBBox():
    '''returns boolean\n\n
    pointsInBBox()\n
    '''
def getConnectionReferencePoint():
    '''returns IlvPoint\n\n
    getConnectionReferencePoint(final boolean b, final IlvTransformer ilvTransformer)\n
    '''
def getConnectionPoints():
    '''returns None\n\n
    getConnectionPoints(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def isSpline():
    '''returns boolean\n\n
    isSpline()\n
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
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def isOriented():
    '''returns boolean\n\n
    isOriented()\n
    '''
def setOriented():
    '''returns None\n\n
    setOriented(final boolean c)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color d)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def getLineWidth():
    '''returns float\n\n
    getLineWidth()\n
    getLineWidth(final IlvTransformer ilvTransformer)\n
    '''
def setLineWidth():
    '''returns None\n\n
    setLineWidth(final float f)\n
    '''
def getEndCap():
    '''returns int\n\n
    getEndCap()\n
    '''
def setEndCap():
    '''returns None\n\n
    setEndCap(final int n)\n
    '''
def getLineJoin():
    '''returns int\n\n
    getLineJoin()\n
    '''
def setLineJoin():
    '''returns None\n\n
    setLineJoin(final int n)\n
    '''
def getMaximumLineWidth():
    '''returns float\n\n
    getMaximumLineWidth()\n
    '''
def setMaximumLineWidth():
    '''returns None\n\n
    setMaximumLineWidth(final float f)\n
    '''
def getLineStyle():
    '''returns float[]\n\n
    getLineStyle()\n
    '''
def setLineStyle():
    '''returns None\n\n
    setLineStyle(final float[] array)\n
    '''
def getLinkPoints():
    '''returns IlvPoint[]\n\n
    getLinkPoints(final IlvTransformer ilvTransformer)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
