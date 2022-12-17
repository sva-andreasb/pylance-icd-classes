def ():
    '''returns IlvGeneralPath\n\n
    ()\n
    (final Shape z)\n
    (final IlvGeneralPath ilvGeneralPath)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def getShape():
    '''returns Shape\n\n
    getShape()\n
    '''
def setShape():
    '''returns None\n\n
    setShape(final Shape y)\n
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
def setStroke():
    '''returns None\n\n
    setStroke(final Stroke t)\n
    '''
def getStroke():
    '''returns Stroke\n\n
    getStroke()\n
    '''
def setMaximumStrokeWidth():
    '''returns None\n\n
    setMaximumStrokeWidth(float ac)\n
    '''
def getMaximumStrokeWidth():
    '''returns float\n\n
    getMaximumStrokeWidth()\n
    '''
def setFillPaint():
    '''returns None\n\n
    setFillPaint(final Paint q)\n
    '''
def getFillPaint():
    '''returns Paint\n\n
    getFillPaint()\n
    '''
def setStrokePaint():
    '''returns None\n\n
    setStrokePaint(final Paint s)\n
    '''
def getStrokePaint():
    '''returns Paint\n\n
    getStrokePaint()\n
    '''
def isPaintZoomed():
    '''returns boolean\n\n
    isPaintZoomed()\n
    '''
def setPaintZoomed():
    '''returns None\n\n
    setPaintZoomed(final boolean b)\n
    '''
def isPaintAbsolute():
    '''returns boolean\n\n
    isPaintAbsolute()\n
    '''
def setPaintAbsolute():
    '''returns None\n\n
    setPaintAbsolute(final boolean b)\n
    '''
def isContainsWhenNotFilled():
    '''returns boolean\n\n
    isContainsWhenNotFilled()\n
    '''
def setContainsWhenNotFilled():
    '''returns None\n\n
    setContainsWhenNotFilled(final boolean b)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color strokePaint)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color fillPaint)\n
    '''
def setClip():
    '''returns None\n\n
    setClip(final Shape pSrc)\n
    '''
def getClip():
    '''returns Shape\n\n
    getClip()\n
    '''
def setAlpha():
    '''returns None\n\n
    setAlpha(final float ad)\n
    '''
def getAlpha():
    '''returns float\n\n
    getAlpha()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getShapeBounds():
    '''returns IlvRect\n\n
    getShapeBounds(final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(final IlvRect ilvRect)\n
    '''
def resize():
    '''returns None\n\n
    resize(float n, float n2)\n
    '''
def setShapeBounds():
    '''returns None\n\n
    setShapeBounds(final IlvRect obj)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def isMovePointAllowed():
    '''returns boolean\n\n
    isMovePointAllowed()\n
    '''
def setMovePointAllowed():
    '''returns None\n\n
    setMovePointAllowed(final boolean b)\n
    '''
def isPointEditionAllowed():
    '''returns boolean\n\n
    isPointEditionAllowed()\n
    '''
def setPointEditionAllowed():
    '''returns None\n\n
    setPointEditionAllowed(final boolean movePointAllowed)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
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
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getPointsCardinal():
    '''returns int\n\n
    getPointsCardinal()\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(final int n, float x, float y, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int n, float x, float y, final IlvTransformer ilvTransformer)\n
    '''
def pointsInBBox():
    '''returns boolean\n\n
    pointsInBBox()\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(int n, final IlvTransformer ilvTransformer)\n
    '''
def setTransformedShapeMode():
    '''returns None\n\n
    setTransformedShapeMode(final boolean ab)\n
    '''
def isTransformedShapeMode():
    '''returns boolean\n\n
    isTransformedShapeMode()\n
    '''
def getApplyTransformer():
    '''returns IlvTransformer\n\n
    getApplyTransformer()\n
    '''
def getOriginalShape():
    '''returns Shape\n\n
    getOriginalShape()\n
    '''
