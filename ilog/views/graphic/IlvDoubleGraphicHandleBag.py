def ():
    '''returns IlvDoubleGraphicHandleBag\n\n
    (final IlvGraphic ilvGraphic, final IlvGraphic ilvGraphic2)\n
    (final IlvDoubleGraphicHandleBag ilvDoubleGraphicHandleBag)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def setObject1():
    '''returns None\n\n
    setObject1(final IlvGraphic f)\n
    '''
def setObject2():
    '''returns None\n\n
    setObject2(final IlvGraphic g)\n
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
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def move():
    '''returns None\n\n
    move(final float n, final float n2)\n
    move(final IlvPoint ilvPoint)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
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
    setObjectName(final IlvGraphic ilvGraphic, final String nameImpl)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String s)\n
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
