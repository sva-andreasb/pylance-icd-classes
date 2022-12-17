def ():
    '''returns IlvDefaultGraphicManagerFrame\n\n
    (final IlvGraphic a, final IlvGraphic b, final int c, final float d, final float e, final float f, final float g, final boolean i)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def getFrameGraphic():
    '''returns IlvGraphic\n\n
    getFrameGraphic()\n
    '''
def copy():
    '''returns IlvManagerFrame\n\n
    copy()\n
    '''
def getTopMargin():
    '''returns float\n\n
    getTopMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    '''
def getBottomMargin():
    '''returns float\n\n
    getBottomMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    '''
def getRightMargin():
    '''returns float\n\n
    getRightMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    '''
def getLeftMargin():
    '''returns float\n\n
    getLeftMargin(final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    '''
def isOpaque():
    '''returns boolean\n\n
    isOpaque(final IlvManager ilvManager)\n
    '''
def draw():
    '''returns None\n\n
    draw(final IlvManager h, final IlvRect ilvRect, final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def resizeGraphic():
    '''returns None\n\n
    resizeGraphic(final IlvTransformer ilvTransformer, final IlvRect ilvRect)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvManager h, final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def getObjects():
    '''returns IlvGraphicEnumeration\n\n
    getObjects()\n
    '''
def reDrawObj():
    '''returns None\n\n
    reDrawObj(final IlvGraphic ilvGraphic)\n
    '''
def reDrawRegion():
    '''returns None\n\n
    reDrawRegion(final IlvRegion ilvRegion)\n
    '''
def reshapeObject():
    '''returns None\n\n
    reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)\n
    '''
def moveObject():
    '''returns None\n\n
    moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)\n
    '''
def applyToObject():
    '''returns None\n\n
    applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    '''
def setObjectName():
    '''returns boolean\n\n
    setObjectName(final IlvGraphic ilvGraphic, final String s)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String s)\n
    '''
def getGraphicBag():
    '''returns IlvGraphicBag\n\n
    getGraphicBag()\n
    '''
