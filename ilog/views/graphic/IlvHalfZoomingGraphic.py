def ():
    '''returns DelegateObjectInteractor\n\n
    (final IlvGraphic ilvGraphic, final int n, final IlvPoint ilvPoint, final double a, final double b, final double c)\n
    (final IlvGraphic ilvGraphic, final IlvPoint ilvPoint, final double n, final double n2, final double n3)\n
    (final IlvGraphic ilvGraphic, final int n, final double n2, final double n3, final double n4)\n
    (final IlvHalfZoomingGraphic ilvHalfZoomingGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    ()\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def getMinZoom():
    '''returns double\n\n
    getMinZoom()\n
    '''
def setMinZoom():
    '''returns None\n\n
    setMinZoom(final double a)\n
    '''
def getMaxZoom():
    '''returns double\n\n
    getMaxZoom()\n
    '''
def setMaxZoom():
    '''returns None\n\n
    setMaxZoom(final double b)\n
    '''
def getInitialZoom():
    '''returns double\n\n
    getInitialZoom()\n
    '''
def setInitialZoom():
    '''returns None\n\n
    setInitialZoom(double c)\n
    '''
def setUnzoomedForeground():
    '''returns None\n\n
    setUnzoomedForeground(final Color d)\n
    '''
def getUnzoomedForeground():
    '''returns Color\n\n
    getUnzoomedForeground()\n
    '''
def setUnzoomedBackground():
    '''returns None\n\n
    setUnzoomedBackground(final Color e)\n
    '''
def getUnzoomedBackground():
    '''returns Color\n\n
    getUnzoomedBackground()\n
    '''
def setGrayedWhenUnzoomed():
    '''returns None\n\n
    setGrayedWhenUnzoomed(final boolean f)\n
    '''
def isGrayedWhenUnzoomed():
    '''returns boolean\n\n
    isGrayedWhenUnzoomed()\n
    '''
def setRotatable():
    '''returns None\n\n
    setRotatable(final boolean i)\n
    '''
def isRotatable():
    '''returns boolean\n\n
    isRotatable()\n
    '''
def setAlpha():
    '''returns None\n\n
    setAlpha(final float g)\n
    '''
def getAlpha():
    '''returns float\n\n
    getAlpha()\n
    '''
def setAlphaBufferEnabled():
    '''returns None\n\n
    setAlphaBufferEnabled(final boolean h)\n
    '''
def isAlphaBufferEnabled():
    '''returns boolean\n\n
    isAlphaBufferEnabled()\n
    '''
def isDelegateObjectInteractor():
    '''returns boolean\n\n
    isDelegateObjectInteractor(final IlvObjectInteractor ilvObjectInteractor)\n
    '''
def computeTransformer():
    '''returns IlvTransformer\n\n
    computeTransformer(final IlvTransformer ilvTransformer)\n
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
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
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
