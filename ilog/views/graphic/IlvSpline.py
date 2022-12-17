def ():
    '''returns IlvSpline\n\n
    (final IlvPoint[] array)\n
    (final IlvPoint[] array, final boolean b)\n
    (final IlvPoint[] array, final boolean b, final boolean closed)\n
    (final IlvSpline ilvSpline)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
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
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color b)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color c)\n
    '''
def getBackground():
    '''returns Color\n\n
    getBackground()\n
    '''
def isFillOn():
    '''returns boolean\n\n
    isFillOn()\n
    '''
def setFillOn():
    '''returns None\n\n
    setFillOn(final boolean b)\n
    '''
def isStrokeOn():
    '''returns boolean\n\n
    isStrokeOn()\n
    '''
def setStrokeOn():
    '''returns None\n\n
    setStrokeOn(final boolean b)\n
    '''
def setClosed():
    '''returns None\n\n
    setClosed(final boolean b)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
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
def setSmoothness():
    '''returns None\n\n
    setSmoothness(final float a)\n
    '''
def getSmoothness():
    '''returns float\n\n
    getSmoothness()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
