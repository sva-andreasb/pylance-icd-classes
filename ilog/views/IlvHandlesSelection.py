FILLED_SQUARE_SHAPE = "int  0"
SQUARE_SHAPE = "int  1"
FILLED_CIRCLE_SHAPE = "int  2"
CIRCLE_SHAPE = "int  3"
def ():
    '''returns IlvHandlesSelection\n\n
    (final IlvGraphic ilvGraphic)\n
    '''
def getHandlesColor():
    '''returns Color\n\n
    getHandlesColor()\n
    '''
def setHandlesColor():
    '''returns None\n\n
    setHandlesColor(final Color c)\n
    '''
def getActiveHandlesColor():
    '''returns Color\n\n
    getActiveHandlesColor()\n
    '''
def setActiveHandlesColor():
    '''returns None\n\n
    setActiveHandlesColor(final Color d)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def getHandle():
    '''returns int\n\n
    getHandle(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def drawWithoutHandles():
    '''returns None\n\n
    drawWithoutHandles(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def onEnter():
    '''returns None\n\n
    onEnter(final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
def onExit():
    '''returns None\n\n
    onExit(final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
