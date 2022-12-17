def ():
    '''returns IlvPolyPoints\n\n
    (final IlvPoint[] array)\n
    (final IlvPoint[] array, final boolean b)\n
    (final IlvPolyPoints ilvPolyPoints)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def recomputeBBox():
    '''returns None\n\n
    recomputeBBox()\n
    '''
def inBBox():
    '''returns boolean\n\n
    inBBox(final IlvPoint ilvPoint)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
    '''
def getPointAt():
    '''returns IlvPoint\n\n
    getPointAt(final int n, final IlvTransformer ilvTransformer)\n
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
    insertPoint(final int i, final float n, final float n2, final IlvTransformer ilvTransformer)\n
    '''
def removePoint():
    '''returns None\n\n
    removePoint(final int i, final IlvTransformer ilvTransformer)\n
    '''
def movePoint():
    '''returns None\n\n
    movePoint(final int i, final float x, final float y, final IlvTransformer ilvTransformer)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
