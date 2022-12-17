def getFrom():
    '''returns IlvPoint\n\n
    getFrom()\n
    '''
def getTo():
    '''returns IlvPoint\n\n
    getTo()\n
    '''
def ():
    '''returns IlvPolyline2D\n\n
    (final IlvPoint from, final IlvPoint to)\n
    (final IlvPolyline2D ilvPolyline2D)\n
    (final IlvPoint[] array, final boolean b)\n
    (final IlvPoint[] array)\n
    '''
def setNumberOfSegments():
    '''returns None\n\n
    setNumberOfSegments(final int numsegments)\n
    '''
def setSegment():
    '''returns None\n\n
    setSegment(final int n, final IlvPoint ilvPoint, final IlvPoint ilvPoint2)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getNumberOfSegments():
    '''returns int\n\n
    getNumberOfSegments()\n
    '''
def getSegment():
    '''returns IlvLineSegment\n\n
    getSegment(final int n)\n
    '''
def getSegments():
    '''returns IlvLineSegment[]\n\n
    getSegments()\n
    '''
def getNumberOfPoints():
    '''returns int\n\n
    getNumberOfPoints()\n
    '''
def getPoint():
    '''returns IlvPoint\n\n
    getPoint(final int n)\n
    '''
def getPoints():
    '''returns IlvPoint[]\n\n
    getPoints()\n
    '''
def getClosestSegment():
    '''returns int\n\n
    getClosestSegment(final IlvPoint ilvPoint)\n
    '''
def getBounds():
    '''returns Rectangle\n\n
    getBounds()\n
    '''
def getBounds2D():
    '''returns Rectangle2D\n\n
    getBounds2D()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final double n, final double n2)\n
    contains(final Point2D point2D)\n
    contains(final double n, final double n2, final double n3, final double n4)\n
    contains(final Rectangle2D rectangle2D)\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final double n, final double n2, final double n3, final double n4)\n
    intersects(final Rectangle2D rectangle2D)\n
    '''
def getPathIterator():
    '''returns PathIterator\n\n
    getPathIterator(final AffineTransform affineTransform)\n
    getPathIterator(final AffineTransform affineTransform, final double n)\n
    '''
def currentSegment():
    '''returns int\n\n
    currentSegment(final double[] array)\n
    currentSegment(final float[] array)\n
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
def getMedian():
    '''returns PointAndDirection\n\n
    getMedian()\n
    '''
def computeParallel():
    '''returns IlvPolyline2D\n\n
    computeParallel(final float n)\n
    computeParallel(final float n, final boolean b)\n
    '''
def computeThickLinkShape():
    '''returns TwoPolylines\n\n
    computeThickLinkShape(final float n)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def reverse():
    '''returns None\n\n
    reverse()\n
    '''
def insertPoint():
    '''returns None\n\n
    insertPoint(final int n, final IlvPoint ilvPoint)\n
    insertPoint(final IlvPoint ilvPoint)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int n, final IlvPoint ilvPoint)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(final int n)\n
    '''
def removeRedundantPoints():
    '''returns None\n\n
    removeRedundantPoints()\n
    '''
def adjustForFromArrow():
    '''returns None\n\n
    adjustForFromArrow(final float n, final float n2)\n
    '''
def adjustForToArrow():
    '''returns None\n\n
    adjustForToArrow(final float n, final float n2)\n
    '''
def adjustForArrow():
    '''returns IlvPoint[]\n\n
    adjustForArrow(final IlvLineSegment ilvLineSegment, final float n, final float n2)\n
    '''
