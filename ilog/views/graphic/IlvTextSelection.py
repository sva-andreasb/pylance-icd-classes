def ():
    '''returns Range\n\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvGraphic ilvGraphic, final boolean resizable)\n
    (final IlvGraphic ilvGraphic, final boolean resizable, final boolean editable)\n
    ()\n
    (final int from, final int to)\n
    (final int n)\n
    '''
def setResizable():
    '''returns None\n\n
    setResizable(final boolean a)\n
    '''
def supportsResize():
    '''returns boolean\n\n
    supportsResize()\n
    '''
def getRange():
    '''returns Range\n\n
    getRange()\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final Range range)\n
    setRange(final int from, final int to)\n
    setRange(final Range range)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def isOnBorder():
    '''returns boolean\n\n
    isOnBorder(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def drawWithoutHandles():
    '''returns None\n\n
    drawWithoutHandles(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def getDefaultInteractor():
    '''returns String\n\n
    getDefaultInteractor()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def isCollapsed():
    '''returns boolean\n\n
    isCollapsed()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
