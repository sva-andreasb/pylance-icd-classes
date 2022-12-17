def ():
    '''returns DelegateObjectInteractor\n\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvGraphic ilvGraphic, final double a)\n
    (final IlvFullZoomingGraphic ilvFullZoomingGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    ()\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def getInitialZoom():
    '''returns double\n\n
    getInitialZoom()\n
    '''
def setInitialZoom():
    '''returns None\n\n
    setInitialZoom(double a)\n
    '''
def setAlpha():
    '''returns None\n\n
    setAlpha(final float b)\n
    '''
def getAlpha():
    '''returns float\n\n
    getAlpha()\n
    '''
def setAlphaBufferEnabled():
    '''returns None\n\n
    setAlphaBufferEnabled(final boolean c)\n
    '''
def isAlphaBufferEnabled():
    '''returns boolean\n\n
    isAlphaBufferEnabled()\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer()\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final IlvTransformer ilvTransformer)\n
    '''
def isDelegateObjectInteractor():
    '''returns boolean\n\n
    isDelegateObjectInteractor(final IlvObjectInteractor ilvObjectInteractor)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
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
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def intersects():
    '''returns boolean\n\n
    intersects(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def inside():
    '''returns boolean\n\n
    inside(final IlvRect ilvRect, final IlvRect ilvRect2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
