HH_NONE = "int  0"
HH_BLUR = "int  1"
HH_BRIGHTEN = "int  2"
HH_GRAYSCALE = "int  3"
HH_SHARPEN = "int  4"
HH_INVERT_COLORS = "int  5"
HH_CUSTOM = "int  6"
def ():
    '''returns IlvManager\n\n
    ()\n
    (final int n)\n
    (final int n, final int n2)\n
    (final IlvManager ilvManager)\n
    (final IlvInputStream ilvInputStream)\n
    '''
def setDebugBoundingBoxes():
    '''returns None\n\n
    setDebugBoundingBoxes(final boolean b)\n
    '''
def isDebugBoundingBoxes():
    '''returns boolean\n\n
    isDebugBoundingBoxes()\n
    '''
def setNameImpl():
    '''returns None\n\n
    setNameImpl(final String nameImpl)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final IlvGraphic key, int n, boolean b)\n
    addObject(final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final IlvGraphic key, final boolean b)\n
    '''
def replaceObject():
    '''returns None\n\n
    replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)\n
    '''
def isManaged():
    '''returns boolean\n\n
    isManaged(final IlvGraphic ilvGraphic)\n
    '''
def getObject():
    '''returns IlvGraphic\n\n
    getObject(final String key)\n
    getObject(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)\n
    getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)\n
    getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)\n
    '''
def setObjectName():
    '''returns boolean\n\n
    setObjectName(final IlvGraphic value, final String s)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName(final IlvGraphic ilvGraphic)\n
    '''
def applyToObject():
    '''returns None\n\n
    applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    '''
def applyToObjects():
    '''returns None\n\n
    applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)\n
    applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)\n
    '''
def moveObject():
    '''returns None\n\n
    moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)\n
    '''
def reshapeObject():
    '''returns None\n\n
    reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)\n
    '''
def addLayer():
    '''returns None\n\n
    addLayer(final IlvManagerLayer ilvManagerLayer, int n)\n
    addLayer(final int n)\n
    '''
def removeLayer():
    '''returns None\n\n
    removeLayer(final int n, final boolean b)\n
    '''
def setOptimizedLayerThreshold():
    '''returns None\n\n
    setOptimizedLayerThreshold(final long r)\n
    '''
def getOptimizedLayerThreshold():
    '''returns long\n\n
    getOptimizedLayerThreshold()\n
    '''
def setNumberOfLayer():
    '''returns None\n\n
    setNumberOfLayer(int n)\n
    '''
def getLayersCount():
    '''returns int\n\n
    getLayersCount()\n
    '''
def swapLayers():
    '''returns None\n\n
    swapLayers(final int n, final int n2, final boolean b)\n
    '''
def addManagerLayerListener():
    '''returns None\n\n
    addManagerLayerListener(final ManagerLayerListener l)\n
    '''
def removeManagerLayerListener():
    '''returns None\n\n
    removeManagerLayerListener(final ManagerLayerListener l)\n
    '''
def setLayerName():
    '''returns None\n\n
    setLayerName(final int n, final String name)\n
    '''
def getLayerName():
    '''returns String\n\n
    getLayerName(final int n)\n
    '''
def getLayer():
    '''returns int\n\n
    getLayer(final String anObject)\n
    '''
def getManagerLayer():
    '''returns IlvManagerLayer\n\n
    getManagerLayer(final String anObject)\n
    '''
def setLayer():
    '''returns None\n\n
    setLayer(final IlvGraphic obj, final int n, final boolean b)\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final int n, final boolean b, final boolean b2)\n
    setVisible(final IlvManagerView ilvManagerView, final int n, final boolean b, final boolean b2)\n
    setVisible(final IlvGraphic ilvGraphic, final boolean visible, final boolean b)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final int n)\n
    isVisible(final IlvManagerView ilvManagerView, final int n)\n
    isVisible(final IlvGraphic ilvGraphic)\n
    isVisible(final IlvGraphic ilvGraphic, final IlvManagerView ilvManagerView)\n
    '''
def setInsertionAdjusting():
    '''returns None\n\n
    setInsertionAdjusting(final boolean b)\n
    '''
def isInsertionAdjusting():
    '''returns boolean\n\n
    isInsertionAdjusting()\n
    '''
def addManagerContentChangedListener():
    '''returns None\n\n
    addManagerContentChangedListener(final ManagerContentChangedListener l)\n
    '''
def removeManagerContentChangedListener():
    '''returns None\n\n
    removeManagerContentChangedListener(final ManagerContentChangedListener l)\n
    '''
def addManagerTreeContentChangedListener():
    '''returns None\n\n
    addManagerTreeContentChangedListener(final ManagerContentChangedListener l)\n
    '''
def removeManagerTreeContentChangedListener():
    '''returns None\n\n
    removeManagerTreeContentChangedListener(final ManagerContentChangedListener l)\n
    '''
def setContentsAdjusting():
    '''returns None\n\n
    setContentsAdjusting(final boolean b)\n
    setContentsAdjusting(final boolean contentsAdjusting, final boolean b)\n
    '''
def addManagerViewsListener():
    '''returns None\n\n
    addManagerViewsListener(final ManagerViewsChangedListener l)\n
    '''
def removeManagerViewsListener():
    '''returns None\n\n
    removeManagerViewsListener(final ManagerViewsChangedListener l)\n
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
def reDrawObj():
    '''returns None\n\n
    reDrawObj(final IlvGraphic ilvGraphic)\n
    '''
def reDrawRegion():
    '''returns None\n\n
    reDrawRegion(final IlvRegion ilvRegion)\n
    '''
def invalidateRegion():
    '''returns None\n\n
    invalidateRegion(final IlvGraphic ilvGraphic)\n
    invalidateRegion(final IlvRect ilvRect)\n
    invalidateRegion(final IlvManagerView ilvManagerView, final IlvRect ilvRect)\n
    '''
def initReDraws():
    '''returns None\n\n
    initReDraws()\n
    '''
def isInvalidating():
    '''returns boolean\n\n
    isInvalidating()\n
    '''
def abortReDraws():
    '''returns None\n\n
    abortReDraws()\n
    '''
def reDrawViews():
    '''returns None\n\n
    reDrawViews()\n
    '''
def blinkingReDraw():
    '''returns None\n\n
    blinkingReDraw()\n
    '''
def reDraw():
    '''returns None\n\n
    reDraw()\n
    '''
def computeBBox():
    '''returns IlvRect\n\n
    computeBBox(final IlvTransformer ilvTransformer)\n
    computeBBox(final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def draw():
    '''returns None\n\n
    draw(final Graphics graphics, final IlvManagerView ilvManagerView)\n
    draw(final Graphics graphics, final IlvTransformer ilvTransformer)\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics graphics, final IlvRect ilvRect, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def processEvent():
    '''returns boolean\n\n
    processEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)\n
    '''
def setHoverHighlightingImageOperation():
    '''returns None\n\n
    setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation bq)\n
    '''
def getHoverHighlightingImageOperation():
    '''returns IlvHoverHighlightingImageOperation\n\n
    getHoverHighlightingImageOperation()\n
    '''
def setHoverHighlightingMode():
    '''returns None\n\n
    setHoverHighlightingMode(final int n)\n
    '''
def getHoverHighlightingMode():
    '''returns int\n\n
    getHoverHighlightingMode()\n
    '''
def shortCut():
    '''returns boolean\n\n
    shortCut(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)\n
    '''
def processHoverHighlightingEvent():
    '''returns boolean\n\n
    processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)\n
    processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView, final IlvGraphic ilvGraphic)\n
    '''
def dispatchToObjects():
    '''returns boolean\n\n
    dispatchToObjects(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)\n
    '''
def addAccelerator():
    '''returns None\n\n
    addAccelerator(final IlvAccelerator e)\n
    '''
def removeAccelerator():
    '''returns None\n\n
    removeAccelerator(final IlvAccelerator o)\n
    '''
def getAccelerators():
    '''returns IlvAccelerator[]\n\n
    getAccelerators()\n
    '''
def setAccelerators():
    '''returns None\n\n
    setAccelerators(final IlvAccelerator[] array)\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll(final boolean b)\n
    deleteAll(final int n, final boolean b)\n
    '''
def allowMoving():
    '''returns boolean\n\n
    allowMoving(final IlvGraphic ilvGraphic)\n
    '''
def isMovable():
    '''returns boolean\n\n
    isMovable(final IlvGraphic ilvGraphic)\n
    '''
def setMovable():
    '''returns None\n\n
    setMovable(final IlvGraphic ilvGraphic, final boolean movable)\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable(final IlvGraphic ilvGraphic)\n
    '''
def setEditable():
    '''returns None\n\n
    setEditable(final IlvGraphic ilvGraphic, final boolean editable)\n
    '''
def isSelectable():
    '''returns boolean\n\n
    isSelectable(final IlvGraphic ilvGraphic)\n
    isSelectable(final int n)\n
    '''
def objectIsSelectable():
    '''returns boolean\n\n
    objectIsSelectable(final IlvGraphic ilvGraphic)\n
    '''
def setSelectable():
    '''returns None\n\n
    setSelectable(final IlvGraphic ilvGraphic, final boolean selectable)\n
    setSelectable(final int n, final boolean b)\n
    '''
def getAllObjects():
    '''returns IlvGraphicVector\n\n
    getAllObjects(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)\n
    getAllObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b, final boolean b2)\n
    '''
def getCollapseExpandObject():
    '''returns IlvObjectWithSelection\n\n
    getCollapseExpandObject(final IlvPoint p4, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def getSelectableObject():
    '''returns IlvGraphic\n\n
    getSelectableObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def getAllSelectableObjects():
    '''returns IlvGraphicVector\n\n
    getAllSelectableObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)\n
    '''
def getSelection():
    '''returns IlvSelection\n\n
    getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)\n
    getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final IlvGraphic ilvGraphic)\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)\n
    setSelected(final IlvGraphic ilvGraphic, final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)\n
    '''
def addManagerSelectionListener():
    '''returns None\n\n
    addManagerSelectionListener(final ManagerSelectionListener l)\n
    '''
def removeManagerSelectionListener():
    '''returns None\n\n
    removeManagerSelectionListener(final ManagerSelectionListener l)\n
    '''
def addManagerTreeSelectionListener():
    '''returns None\n\n
    addManagerTreeSelectionListener(final ManagerSelectionListener l)\n
    '''
def removeManagerTreeSelectionListener():
    '''returns None\n\n
    removeManagerTreeSelectionListener(final ManagerSelectionListener l)\n
    '''
def setSelectionEventSource():
    '''returns None\n\n
    setSelectionEventSource(final Object ac)\n
    '''
def setSelectionAdjusting():
    '''returns None\n\n
    setSelectionAdjusting(final boolean b)\n
    '''
def isSelectionAdjusting():
    '''returns boolean\n\n
    isSelectionAdjusting()\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll(final IlvManagerView ilvManagerView, final boolean b)\n
    selectAll(final boolean b)\n
    selectAll(final boolean b, final boolean b2)\n
    '''
def deSelectAll():
    '''returns None\n\n
    deSelectAll(final boolean b)\n
    deSelectAll(final boolean b, final boolean b2)\n
    deSelectAll(final int n, final boolean b)\n
    '''
def setSelectionFactory():
    '''returns None\n\n
    setSelectionFactory(final IlvSelectionFactory ay)\n
    '''
def getSelectionFactory():
    '''returns IlvSelectionFactory\n\n
    getSelectionFactory()\n
    '''
def write():
    '''returns None\n\n
    write(final IlvOutputStream ilvOutputStream)\n
    write(final OutputStream outputStream, final boolean b)\n
    write(final OutputStream outputStream)\n
    write(final String name, final boolean b)\n
    write(final String s)\n
    '''
def writeIt():
    '''returns None\n\n
    writeIt(final IlvOutputStream ilvOutputStream)\n
    '''
def writePrefix():
    '''returns None\n\n
    writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)\n
    '''
def writeSuffix():
    '''returns None\n\n
    writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)\n
    '''
def readPrefix():
    '''returns None\n\n
    readPrefix(final IlvInputStream ilvInputStream, final boolean b)\n
    '''
def readSuffix():
    '''returns None\n\n
    readSuffix(final IlvInputStream ilvInputStream, final boolean b)\n
    '''
def setFileName():
    '''returns None\n\n
    setFileName(final URL a9)\n
    '''
def getFileName():
    '''returns URL\n\n
    getFileName()\n
    '''
def read():
    '''returns boolean\n\n
    read(final InputStream inputStream)\n
    read(final String name)\n
    read(final URL az)\n
    '''
def setStreamFactory():
    '''returns None\n\n
    setStreamFactory(final IlvManagerStreamFactory a7)\n
    '''
def getStreamFactory():
    '''returns IlvManagerStreamFactory\n\n
    getStreamFactory()\n
    '''
def check():
    '''returns None\n\n
    check(final boolean b)\n
    '''
def getSelectedMovingObjects():
    '''returns IlvGraphicEnumeration\n\n
    getSelectedMovingObjects(final boolean[] array)\n
    '''
def translateSelections():
    '''returns None\n\n
    translateSelections(final float n, final float n2, final IlvManagerView ilvManagerView)\n
    '''
def translateObjects():
    '''returns None\n\n
    translateObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final float n, final float n2, final IlvTransformer ilvTransformer)\n
    '''
def deleteSelections():
    '''returns None\n\n
    deleteSelections(final boolean b)\n
    deleteSelections(final boolean b, final boolean b2)\n
    '''
def duplicateSelections():
    '''returns None\n\n
    duplicateSelections(final int n, final int n2)\n
    duplicateSelections(final float n, final float n2, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def map():
    '''returns None\n\n
    map(final IlvApplyObject ilvApplyObject, final Object o)\n
    map(final IlvApplyObject ilvApplyObject, final Object o, final boolean b)\n
    '''
def mapIntersects():
    '''returns None\n\n
    mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)\n
    mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def mapInside():
    '''returns None\n\n
    mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)\n
    mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)\n
    '''
def pasteSelection():
    '''returns IlvGraphicEnumeration\n\n
    pasteSelection(final IlvPoint ilvPoint, final boolean b)\n
    '''
def copySelection():
    '''returns None\n\n
    copySelection()\n
    '''
def lostOwnership():
    '''returns None\n\n
    lostOwnership(final Clipboard clipboard, final Transferable transferable)\n
    '''
def removeProperty():
    '''returns boolean\n\n
    removeProperty(final String key)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String key, final Object value)\n
    '''
def replaceProperty():
    '''returns boolean\n\n
    replaceProperty(final String key, final Object value)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String key)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final String key, final Object o)\n
    '''
def zoomable():
    '''returns boolean\n\n
    zoomable()\n
    '''
def applyTransform():
    '''returns None\n\n
    applyTransform(final IlvTransformer ilvTransformer)\n
    '''
def moveResize():
    '''returns None\n\n
    moveResize(IlvRect obj)\n
    '''
def setGraphicBag():
    '''returns None\n\n
    setGraphicBag(final IlvGraphicBag graphicBag)\n
    '''
def addManagerExpansionListener():
    '''returns None\n\n
    addManagerExpansionListener(final ManagerExpansionListener l)\n
    '''
def removeManagerExpansionListener():
    '''returns None\n\n
    removeManagerExpansionListener(final ManagerExpansionListener l)\n
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
def setSelectionInvariantSubManagerBounds():
    '''returns None\n\n
    setSelectionInvariantSubManagerBounds(final boolean b)\n
    '''
def isSelectionInvariantSubManagerBounds():
    '''returns boolean\n\n
    isSelectionInvariantSubManagerBounds()\n
    '''
def boundingBox():
    '''returns IlvRect\n\n
    boundingBox(final IlvTransformer ilvTransformer)\n
    '''
def copy():
    '''returns IlvGraphic\n\n
    copy()\n
    '''
def getFrame():
    '''returns IlvManagerFrame\n\n
    getFrame()\n
    '''
def setFrame():
    '''returns None\n\n
    setFrame(final IlvManagerFrame bg)\n
    '''
def getTransformer():
    '''returns IlvTransformer\n\n
    getTransformer()\n
    getTransformer()\n
    '''
def getDrawingTransformer():
    '''returns IlvTransformer\n\n
    getDrawingTransformer(final IlvManagerView ilvManagerView)\n
    '''
def getTopLevelTransformer():
    '''returns IlvTransformer\n\n
    getTopLevelTransformer()\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def setULocale():
    '''returns None\n\n
    setULocale(final ULocale uLocale)\n
    setULocale(final ULocale bs, final boolean b)\n
    '''
def isLocaleSensitive():
    '''returns boolean\n\n
    isLocaleSensitive()\n
    '''
def getComponentOrientation():
    '''returns ComponentOrientation\n\n
    getComponentOrientation()\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final ComponentOrientation componentOrientation)\n
    setComponentOrientation(final ComponentOrientation bt, final boolean b)\n
    '''
def isComponentOrientationSensitive():
    '''returns boolean\n\n
    isComponentOrientationSensitive()\n
    '''
def isBaseTextDirectionSensitive():
    '''returns boolean\n\n
    isBaseTextDirectionSensitive()\n
    '''
def containsFrame():
    '''returns boolean\n\n
    containsFrame(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final IlvPoint ilvPoint, final IlvPoint p3, final IlvTransformer ilvTransformer)\n
    '''
def getIntersectionWithOutline():
    '''returns IlvPoint\n\n
    getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)\n
    '''
def setSizeLimitToDrawSubmanagerContents():
    '''returns None\n\n
    setSizeLimitToDrawSubmanagerContents(final float bm)\n
    '''
def getSizeLimitToDrawSubmanagerContents():
    '''returns float\n\n
    getSizeLimitToDrawSubmanagerContents()\n
    '''
def componentOrientationChanged():
    '''returns None\n\n
    componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)\n
    '''
def localeChanged():
    '''returns None\n\n
    localeChanged(final ULocale uLocale, final ULocale uLocale2)\n
    '''
def baseTextDirectionChanged():
    '''returns None\n\n
    baseTextDirectionChanged(final int d, final int baseTextDirection)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n, final boolean b)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def repaint():
    '''returns None\n\n
    repaint(final IlvRect ilvRect)\n
    '''
def getGraphics():
    '''returns Graphics\n\n
    getGraphics()\n
    '''
def getGrid():
    '''returns IlvGrid\n\n
    getGrid()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final Cursor cursor)\n
    '''
def getCursor():
    '''returns Cursor\n\n
    getCursor()\n
    '''
def isCursorSet():
    '''returns boolean\n\n
    isCursorSet()\n
    '''
def ensureVisible():
    '''returns None\n\n
    ensureVisible(final IlvPoint ilvPoint)\n
    '''
def snapToGrid():
    '''returns None\n\n
    snapToGrid(final IlvPoint ilvPoint)\n
    '''
def getDefaultXORColor():
    '''returns Color\n\n
    getDefaultXORColor()\n
    '''
def getDefaultGhostColor():
    '''returns Color\n\n
    getDefaultGhostColor()\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns IlvGraphic\n\n
    nextElement()\n
    '''
