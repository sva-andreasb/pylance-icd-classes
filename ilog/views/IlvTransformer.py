def ():
    '''returns IlvTransformer\n\n
    ()\n
    (final IlvTransformer ilvTransformer)\n
    (final double a, final double b, final double c, final double d, final double e, final double f)\n
    (final AffineTransform affineTransform)\n
    (final IlvPoint ilvPoint, double degreesToRadians)\n
    (final double n, final double n2, final IlvPoint ilvPoint)\n
    (final IlvPoint ilvPoint)\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final double a, final double b, final double c, final double d)\n
    setValues(final double a, final double b, final double c, final double d, final double e, final double f)\n
    '''
def setAffineTransform():
    '''returns None\n\n
    setAffineTransform(final AffineTransform affineTransform)\n
    '''
def getAffineTransform():
    '''returns AffineTransform\n\n
    getAffineTransform(final AffineTransform affineTransform)\n
    '''
def getx0():
    '''returns double\n\n
    getx0()\n
    '''
def gety0():
    '''returns double\n\n
    gety0()\n
    '''
def getx11():
    '''returns double\n\n
    getx11()\n
    '''
def getx12():
    '''returns double\n\n
    getx12()\n
    '''
def getx21():
    '''returns double\n\n
    getx21()\n
    '''
def getx22():
    '''returns double\n\n
    getx22()\n
    '''
def isIdentity():
    '''returns boolean\n\n
    isIdentity()\n
    '''
def isTranslation():
    '''returns boolean\n\n
    isTranslation()\n
    '''
def isScale():
    '''returns boolean\n\n
    isScale()\n
    '''
def isBad():
    '''returns boolean\n\n
    isBad()\n
    '''
def getDeterminant():
    '''returns double\n\n
    getDeterminant()\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvPoint ilvPoint)\n
    apply(final IlvRect ilvRect)\n
    '''
def applyFloor():
    '''returns None\n\n
    applyFloor(final IlvPoint ilvPoint)\n
    applyFloor(final IlvRect ilvRect)\n
    '''
def boundingBox():
    '''returns None\n\n
    boundingBox(final IlvRect ilvRect, final boolean b)\n
    '''
def deltaApply():
    '''returns None\n\n
    deltaApply(final IlvPoint ilvPoint)\n
    '''
def inverse():
    '''returns boolean\n\n
    inverse(final IlvPoint ilvPoint)\n
    inverse(final IlvRect ilvRect)\n
    '''
def compose():
    '''returns None\n\n
    compose(final IlvTransformer ilvTransformer)\n
    '''
def postCompose():
    '''returns None\n\n
    postCompose(final IlvTransformer ilvTransformer)\n
    '''
def computeInverse():
    '''returns boolean\n\n
    computeInverse(final IlvTransformer ilvTransformer)\n
    '''
def translate():
    '''returns None\n\n
    translate(final double n, final double n2)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double n, final double n2, final double n3, final double n4)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final double n, final double n2, double degreesToRadians)\n
    '''
def zoomFactor():
    '''returns double\n\n
    zoomFactor()\n
    '''
def zoomXFactor():
    '''returns double\n\n
    zoomXFactor()\n
    '''
def zoomYFactor():
    '''returns double\n\n
    zoomYFactor()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
