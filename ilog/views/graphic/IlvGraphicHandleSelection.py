def ():
    '''returns IlvGraphicHandleSelection\n\n
    (final IlvGraphic ilvGraphic, final IlvSelection selection)\n
    '''
def setSelection():
    '''returns None\n\n
    setSelection(final IlvSelection a)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def isOptimizedDrawingEnabled():
    '''returns boolean\n\n
    isOptimizedDrawingEnabled()\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def drawWithoutHandles():
    '''returns None\n\n
    drawWithoutHandles(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
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
def setForeground():
    '''returns None\n\n
    setForeground(final Color foreground)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color background)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def onEnter():
    '''returns None\n\n
    onEnter(final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
def onExit():
    '''returns None\n\n
    onExit(final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
def getHandleCardinal():
    '''returns int\n\n
    getHandleCardinal()\n
    '''
def getHandle():
    '''returns IlvPoint\n\n
    getHandle(final int n, final IlvTransformer ilvTransformer)\n
    '''
def getDefaultInteractor():
    '''returns String\n\n
    getDefaultInteractor()\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
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
    setObjectName(final IlvGraphic ilvGraphic, final String name)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String s)\n
    '''
