TOP_LEFT = "int  1"
BOTTOM_LEFT = "int  2"
TOP_RIGHT = "int  4"
BOTTOM_RIGHT = "int  8"
def ():
    '''returns IlvRectangle\n\n
    ()\n
    (final IlvRect ilvRect)\n
    (final IlvRect ilvRect, final boolean strokeOn, final boolean fillOn)\n
    (final IlvRect ilvRect, final boolean b, final boolean b2, final int radius)\n
    (final IlvRectangle ilvRectangle)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setDefinitionRect():
    '''returns None\n\n
    setDefinitionRect(final IlvRect ilvRect)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(final IlvRect definitionRect)\n
    '''
def resize():
    '''returns None\n\n
    resize(final float n, final float n2)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    contains(final double n, final double n2)\n
    contains(final Point2D point2D)\n
    contains(final double n, final double n2, final double n3, final double n4)\n
    contains(final Rectangle2D rectangle2D)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color a)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color b)\n
    '''
def getBackground():
    '''returns Color\n\n
    getBackground()\n
    '''
def setRadius():
    '''returns None\n\n
    setRadius(final int c)\n
    '''
def getRadius():
    '''returns int\n\n
    getRadius()\n
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
def getCorners():
    '''returns int\n\n
    getCorners()\n
    '''
def setCorners():
    '''returns None\n\n
    setCorners(final int e)\n
    '''
def isCornersZoomable():
    '''returns boolean\n\n
    isCornersZoomable()\n
    '''
def setCornersZoomable():
    '''returns None\n\n
    setCornersZoomable(final boolean b)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def getBounds():
    '''returns Rectangle\n\n
    getBounds()\n
    '''
def getBounds2D():
    '''returns Rectangle2D\n\n
    getBounds2D()\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final double n, final double n2, final double n3, final double n4)\n
    intersects(final Rectangle2D rectangle2D)\n
    '''
def getPathIterator():
    '''returns PathIterator\n\n
    getPathIterator(final AffineTransform affineTransform, final double flatness)\n
    getPathIterator(final AffineTransform affineTransform)\n
    '''
def getWindingRule():
    '''returns int\n\n
    getWindingRule()\n
    '''
def isDone():
    '''returns boolean\n\n
    isDone()\n
    '''
def next():
    '''returns None\n\n
    next()\n
    '''
def currentSegment():
    '''returns int\n\n
    currentSegment(final float[] array)\n
    currentSegment(final double[] array)\n
    '''
