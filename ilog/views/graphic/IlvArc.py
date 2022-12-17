def ():
    '''returns IlvArc\n\n
    ()\n
    (final IlvRect ilvRect, float a, float b)\n
    (final IlvRect ilvRect, final float n, final float n2, final boolean strokeOn, final boolean fillOn)\n
    (final IlvArc ilvArc)\n
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
def getDefinitionTransformer():
    '''returns IlvTransformer\n\n
    getDefinitionTransformer()\n
    '''
def getAnnulusThickness():
    '''returns float\n\n
    getAnnulusThickness()\n
    '''
def setAnnulusThickness():
    '''returns None\n\n
    setAnnulusThickness(final float n)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def getCenter():
    '''returns IlvPoint\n\n
    getCenter(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, final double n)\n
    '''
def symmetry():
    '''returns None\n\n
    symmetry(final int n)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color c)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color d)\n
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
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
