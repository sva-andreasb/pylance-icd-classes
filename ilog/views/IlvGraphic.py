def ():
    '''returns IlvGraphic\n\n
    ()\n
    (final IlvGraphic ilvGraphic)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def getCenter():
    '''returns IlvPoint\n\n
    getCenter(final IlvTransformer ilvTransformer)\n
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
def move():
    '''returns None\n\n
    move(final float n, final float n2)\n
    move(final IlvPoint ilvPoint)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(IlvRect a)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2)\n
    '''
def rotate():
    '''returns None\n\n
    rotate(final IlvPoint ilvPoint, double degreesToRadians)\n
    '''
def scale():
    '''returns None\n\n
    scale(final double n, final double n2)\n
    '''
def resize():
    '''returns None\n\n
    resize(final float n, final float n2)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag b)\n
    '''
def setForeground():
    '''returns None\n\n
    setForeground(final Color color)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color color)\n
    '''
def setFillOn():
    '''returns None\n\n
    setFillOn(final boolean b)\n
    '''
def setStrokeOn():
    '''returns None\n\n
    setStrokeOn(final boolean b)\n
    '''
def reDraw():
    '''returns None\n\n
    reDraw()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String nameImpl)\n
    '''
def setNameImpl():
    '''returns None\n\n
    setNameImpl(final String s)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def removeProperty():
    '''returns boolean\n\n
    removeProperty(final String s)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def replaceProperty():
    '''returns boolean\n\n
    replaceProperty(final String s, final Object o)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String s, final Object o)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible()\n
    '''
def isMovable():
    '''returns boolean\n\n
    isMovable()\n
    '''
def isSelectable():
    '''returns boolean\n\n
    isSelectable()\n
    '''
def processActionEvent():
    '''returns None\n\n
    processActionEvent(final ActionEvent actionEvent)\n
    '''
def makeSelection():
    '''returns IlvSelection\n\n
    makeSelection()\n
    '''
def getDefaultInteractor():
    '''returns String\n\n
    getDefaultInteractor()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def getTransferDataFlavors():
    '''returns DataFlavor[]\n\n
    getTransferDataFlavors()\n
    '''
def isDataFlavorSupported():
    '''returns boolean\n\n
    isDataFlavorSupported(final DataFlavor dataFlavor)\n
    '''
def getTransferData():
    '''returns Object\n\n
    getTransferData(final DataFlavor flavor)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setBlinkingAction():
    '''returns None\n\n
    setBlinkingAction(final IlvBlinkingAction a)\n
    '''
def getBlinkingAction():
    '''returns IlvBlinkingAction\n\n
    getBlinkingAction()\n
    '''
def setBlinkingOnPeriod():
    '''returns None\n\n
    setBlinkingOnPeriod(long c)\n
    '''
def getBlinkingOnPeriod():
    '''returns long\n\n
    getBlinkingOnPeriod()\n
    '''
def setBlinkingOffPeriod():
    '''returns None\n\n
    setBlinkingOffPeriod(long d)\n
    '''
def getBlinkingOffPeriod():
    '''returns long\n\n
    getBlinkingOffPeriod()\n
    '''
def getBlinkingObjectOwner():
    '''returns IlvBlinkingObjectOwner\n\n
    getBlinkingObjectOwner()\n
    '''
def setToolTipText():
    '''returns None\n\n
    setToolTipText(final String s)\n
    '''
def getToolTipText():
    '''returns String\n\n
    getToolTipText()\n
    getToolTipText(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer)\n
    '''
def setToolTipBaseTextDirection():
    '''returns None\n\n
    setToolTipBaseTextDirection(final int value)\n
    '''
def getToolTipBaseTextDirection():
    '''returns int\n\n
    getToolTipBaseTextDirection()\n
    '''
def setPopupMenu():
    '''returns None\n\n
    setPopupMenu(final JPopupMenu popupMenu)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu()\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvTransformer ilvTransformer, final IlvManagerView ilvManagerView, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def setPopupMenuName():
    '''returns None\n\n
    setPopupMenuName(final String s)\n
    '''
def getPopupMenuName():
    '''returns String\n\n
    getPopupMenuName()\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def isLocaleSensitive():
    '''returns boolean\n\n
    isLocaleSensitive()\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final ULocale uLocale, final ULocale uLocale2)\n
    '''
def getComponentOrientation():
    '''returns ComponentOrientation\n\n
    getComponentOrientation()\n
    '''
def isComponentOrientationSensitive():
    '''returns boolean\n\n
    isComponentOrientationSensitive()\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def getResolvedBaseTextDirection():
    '''returns int\n\n
    getResolvedBaseTextDirection()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def usesBidiMarkers():
    '''returns boolean\n\n
    usesBidiMarkers()\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int n, final int n2)\n
    '''
def addNamedPropertyListener():
    '''returns None\n\n
    addNamedPropertyListener(final NamedPropertyListener l)\n
    '''
def removeNamedPropertyListener():
    '''returns None\n\n
    removeNamedPropertyListener(final NamedPropertyListener l)\n
    '''
def setNamedProperty():
    '''returns IlvNamedProperty\n\n
    setNamedProperty(final IlvNamedProperty value)\n
    '''
def getNamedProperty():
    '''returns IlvNamedProperty\n\n
    getNamedProperty(final String key)\n
    '''
def removeNamedProperty():
    '''returns None\n\n
    removeNamedProperty(final String key)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def viewChanged():
    '''returns None\n\n
    viewChanged(final ManagerViewsChangedEvent managerViewsChangedEvent)\n
    '''
