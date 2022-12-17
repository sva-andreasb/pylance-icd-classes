def ():
    '''returns IlvEllipse\n\n
    ()\n
    (final IlvRect ilvRect)\n
    (final IlvPoint ilvPoint, final int n)\n
    (final IlvPoint ilvPoint, final float n)\n
    (final IlvRect ilvRect, final boolean strokeOn, final boolean fillOn)\n
    (final IlvEllipse ilvEllipse)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
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
