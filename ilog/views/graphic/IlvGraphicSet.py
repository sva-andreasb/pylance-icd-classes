def ():
    '''returns IlvGraphicSet\n\n
    ()\n
    (final IlvGraphicSet set)\n
    (final IlvGraphicSet set, final boolean b)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def addObjectAt():
    '''returns None\n\n
    addObjectAt(final IlvGraphic ilvGraphic, final int n, final boolean b)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def removeObjectAt():
    '''returns None\n\n
    removeObjectAt(final int n, final boolean b)\n
    '''
def removeAll():
    '''returns None\n\n
    removeAll(final boolean b)\n
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
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String key)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final IlvGraphic ilvGraphic)\n
    '''
def setObjectName():
    '''returns boolean\n\n
    setObjectName(final IlvGraphic value, final String s)\n
    '''
def setClip():
    '''returns None\n\n
    setClip(final Shape shape)\n
    '''
def getClip():
    '''returns Shape\n\n
    getClip()\n
    '''
def setAlpha():
    '''returns None\n\n
    setAlpha(final float b)\n
    '''
def getAlpha():
    '''returns float\n\n
    getAlpha()\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def firstContains():
    '''returns IlvGraphic\n\n
    firstContains(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def addGraphicBagHierarchyListener():
    '''returns None\n\n
    addGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)\n
    '''
def removeGraphicBagHierarchyListener():
    '''returns None\n\n
    removeGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)\n
    '''
def enableGraphicBagHierarchyEventForwarding():
    '''returns None\n\n
    enableGraphicBagHierarchyEventForwarding()\n
    '''
def needsGraphicBagHierarchyEvent():
    '''returns boolean\n\n
    needsGraphicBagHierarchyEvent()\n
    '''
def fireGraphicBagHierarchyEvent():
    '''returns None\n\n
    fireGraphicBagHierarchyEvent(final GraphicBagHierarchyEvent graphicBagHierarchyEvent)\n
    '''
def addManagerViewsHierarchyListener():
    '''returns None\n\n
    addManagerViewsHierarchyListener(final ManagerViewsChangedListener l)\n
    '''
def removeManagerViewsHierarchyListener():
    '''returns None\n\n
    removeManagerViewsHierarchyListener(final ManagerViewsChangedListener l)\n
    '''
def enableManagerViewsHierarchyEventForwarding():
    '''returns None\n\n
    enableManagerViewsHierarchyEventForwarding()\n
    '''
def needsManagerViewsHierarchyEvent():
    '''returns boolean\n\n
    needsManagerViewsHierarchyEvent()\n
    '''
def fireManagerViewsHierarchyEvent():
    '''returns None\n\n
    fireManagerViewsHierarchyEvent(final ManagerViewsChangedEvent managerViewsChangedEvent)\n
    '''
def isLocaleSensitive():
    '''returns boolean\n\n
    isLocaleSensitive()\n
    '''
def isComponentOrientationSensitive():
    '''returns boolean\n\n
    isComponentOrientationSensitive()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n, final boolean b)\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int n2)\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def processEvent():
    '''returns boolean\n\n
    processEvent(final IlvGraphic ilvGraphic, final AWTEvent awtEvent, final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
def handleExpose():
    '''returns None\n\n
    handleExpose(final IlvGraphic ilvGraphic, final Graphics graphics, final IlvObjectInteractorContext ilvObjectInteractorContext)\n
    '''
