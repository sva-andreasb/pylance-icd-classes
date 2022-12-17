STROKE_ONLY = "int  0"
FILL_ONLY = "int  1"
STROKE_AND_FILL = "int  2"
def ():
    '''returns IlvGraphicPath\n\n
    (final IlvPoint[] array, final boolean b)\n
    (final IlvPointArray[] array, final boolean b)\n
    (final IlvGraphicPath ilvGraphicPath)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def setDrawRule():
    '''returns None\n\n
    setDrawRule(final int a)\n
    '''
def getDrawRule():
    '''returns int\n\n
    getDrawRule()\n
    '''
def getNumPaths():
    '''returns int\n\n
    getNumPaths()\n
    '''
def setPaths():
    '''returns None\n\n
    setPaths(final IlvPoint[] array, final boolean b)\n
    setPaths(final IlvPointArray[] array, final boolean b)\n
    '''
def getPaths():
    '''returns IlvPointArray[]\n\n
    getPaths()\n
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
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color e)\n
    '''
def getForeground():
    '''returns Color\n\n
    getForeground()\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color f)\n
    '''
def getBackground():
    '''returns Color\n\n
    getBackground()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
