def ():
    '''returns IlvLine\n\n
    ()\n
    (final IlvPoint ilvPoint, final IlvPoint ilvPoint2)\n
    (final float n, final float n2, final float n3, final float n4)\n
    (final IlvLine ilvLine)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def pointsInBBox():
    '''returns boolean\n\n
    pointsInBBox()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def getFrom():
    '''returns IlvPoint\n\n
    getFrom()\n
    '''
def getTo():
    '''returns IlvPoint\n\n
    getTo()\n
    '''
def setTo():
    '''returns None\n\n
    setTo(final IlvPoint ilvPoint)\n
    '''
def setFrom():
    '''returns None\n\n
    setFrom(final IlvPoint ilvPoint)\n
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
def setForeground():
    '''returns None\n\n
    setForeground(final Color c)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int i, final IlvTransformer ilvTransformer)\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int i, final float n, final float n2, final IlvTransformer ilvTransformer)\n
    '''
def allowsPointMove():
    '''returns boolean\n\n
    allowsPointMove(final int n)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
