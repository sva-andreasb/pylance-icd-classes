THREADED_REDRAW = "int  0"
DIRECT_REDRAW = "int  1"
BLINKING_AUTOMATIC = "int  0"
BLINKING_ENABLED = "int  1"
BLINKING_DISABLED = "int  2"
def ():
    '''returns LayerCache\n\n
    (final IlvManager o, final IlvTransformer ilvTransformer, final ULocale uLocale)\n
    (final IlvManager ilvManager, final IlvTransformer ilvTransformer)\n
    (final IlvManager ilvManager)\n
    ()\n
    ()\n
    ()\n
    '''
def hierarchyChanged():
    '''returns None\n\n
    hierarchyChanged(final HierarchyEvent hierarchyEvent)\n
    hierarchyChanged(final HierarchyEvent hierarchyEvent)\n
    '''
def addManagerChangedListener():
    '''returns None\n\n
    addManagerChangedListener(final ManagerChangedListener l)\n
    '''
def removeManagerChangedListener():
    '''returns None\n\n
    removeManagerChangedListener(final ManagerChangedListener l)\n
    '''
def setInteractor():
    '''returns None\n\n
    setInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)\n
    '''
def pushInteractor():
    '''returns None\n\n
    pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor, final AWTEvent awtEvent)\n
    pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)\n
    '''
def popInteractor():
    '''returns IlvManagerViewInteractor\n\n
    popInteractor()\n
    '''
def removeAllInteractors():
    '''returns None\n\n
    removeAllInteractors()\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)\n
    '''
def setDoubleBufferFrozen():
    '''returns None\n\n
    setDoubleBufferFrozen(final boolean g)\n
    '''
def isDoubleBufferFrozen():
    '''returns boolean\n\n
    isDoubleBufferFrozen()\n
    '''
def createImage():
    '''returns Image\n\n
    createImage(final int n, final int n2)\n
    '''
def setRegisteredAtToolTipManager():
    '''returns None\n\n
    setRegisteredAtToolTipManager(final boolean bv)\n
    '''
def isRegisteredAtToolTipManager():
    '''returns boolean\n\n
    isRegisteredAtToolTipManager()\n
    '''
def imageUpdate():
    '''returns boolean\n\n
    imageUpdate(final Image image, final int n, final int n2, final int n3, final int n4, final int n5)\n
    '''
def update():
    '''returns None\n\n
    update(final Graphics graphics)\n
    '''
def repaint():
    '''returns None\n\n
    repaint(final IlvRect ilvRect)\n
    repaint(final long n, final int x, final int y, final int width, final int height)\n
    '''
def paint():
    '''returns None\n\n
    paint(final Graphics graphics)\n
    paint(final Graphics graphics, final IlvManagerView ilvManagerView)\n
    '''
def print():
    '''returns None\n\n
    print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)\n
    '''
def isOpaque():
    '''returns boolean\n\n
    isOpaque()\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final int x, final int y, final int width, final int height)\n
    '''
def isVisible():
    '''returns boolean\n\n
    isVisible(final int n)\n
    '''
def setVisible():
    '''returns None\n\n
    setVisible(final int n, final boolean b)\n
    '''
def isContributingToViewBBox():
    '''returns boolean\n\n
    isContributingToViewBBox(final int n)\n
    '''
def setContributingToViewBBox():
    '''returns None\n\n
    setContributingToViewBBox(final int n, final boolean b)\n
    '''
def computeBBox():
    '''returns IlvRect\n\n
    computeBBox()\n
    computeBBox(final IlvTransformer ilvTransformer)\n
    '''
def setViewMargins():
    '''returns None\n\n
    setViewMargins(final Insets a9)\n
    '''
def getViewMargins():
    '''returns Insets\n\n
    getViewMargins()\n
    '''
def fitTransformerToContent():
    '''returns None\n\n
    fitTransformerToContent()\n
    fitTransformerToContent(final boolean b)\n
    fitTransformerToContent(final Insets insets)\n
    fitTransformerToContent(final Insets insets, final int n)\n
    fitTransformerToContent(final Insets insets, final int n, final boolean b)\n
    '''
def fitTransformerToArea():
    '''returns None\n\n
    fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)\n
    fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n, final boolean b)\n
    '''
def componentResized():
    '''returns None\n\n
    componentResized(final ComponentEvent componentEvent)\n
    '''
def componentShown():
    '''returns None\n\n
    componentShown(final ComponentEvent componentEvent)\n
    '''
def componentHidden():
    '''returns None\n\n
    componentHidden(final ComponentEvent componentEvent)\n
    '''
def componentMoved():
    '''returns None\n\n
    componentMoved(final ComponentEvent componentEvent)\n
    '''
def computeTransformerFitToArea():
    '''returns IlvTransformer\n\n
    computeTransformerFitToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)\n
    '''
def ensureVisible():
    '''returns None\n\n
    ensureVisible(final IlvRect ilvRect)\n
    ensureVisible(final IlvPoint ilvPoint)\n
    '''
def visibleRect():
    '''returns Rectangle\n\n
    visibleRect()\n
    '''
def verifyTransformer():
    '''returns None\n\n
    verifyTransformer()\n
    '''
def isOptimizedTranslation():
    '''returns boolean\n\n
    isOptimizedTranslation()\n
    '''
def setOptimizedTranslation():
    '''returns None\n\n
    setOptimizedTranslation(final boolean ag)\n
    '''
def translate():
    '''returns None\n\n
    translate(final float n, final float n2, final boolean b)\n
    '''
def setRepaintSkipThreshold():
    '''returns None\n\n
    setRepaintSkipThreshold(final long b)\n
    '''
def getRepaintSkipThreshold():
    '''returns long\n\n
    getRepaintSkipThreshold()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def setPreferredSize():
    '''returns None\n\n
    setPreferredSize(final Dimension d)\n
    '''
def getPreferredSize():
    '''returns Dimension\n\n
    getPreferredSize()\n
    '''
def setMaximumSize():
    '''returns None\n\n
    setMaximumSize(final Dimension d)\n
    '''
def getMaximumSize():
    '''returns Dimension\n\n
    getMaximumSize()\n
    '''
def setMinimumSize():
    '''returns None\n\n
    setMinimumSize(final Dimension d)\n
    '''
def getMinimumSize():
    '''returns Dimension\n\n
    getMinimumSize()\n
    '''
def setCursor():
    '''returns None\n\n
    setCursor(final Cursor cursor)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color color)\n
    '''
def addViewDecoration():
    '''returns None\n\n
    addViewDecoration(final IlvManagerViewDecoration e)\n
    '''
def removeViewDecoration():
    '''returns None\n\n
    removeViewDecoration(final IlvManagerViewDecoration o)\n
    '''
def getViewDecorationCount():
    '''returns int\n\n
    getViewDecorationCount()\n
    '''
def getViewDecoration():
    '''returns IlvManagerViewDecoration\n\n
    getViewDecoration(final int index)\n
    '''
def setGrid():
    '''returns None\n\n
    setGrid(final IlvGrid aa)\n
    '''
def getGrid():
    '''returns IlvGrid\n\n
    getGrid()\n
    '''
def removeNotify():
    '''returns None\n\n
    removeNotify()\n
    '''
def addNotify():
    '''returns None\n\n
    addNotify()\n
    '''
def setEventDispatching():
    '''returns None\n\n
    setEventDispatching(final boolean ac)\n
    '''
def isEventDispatching():
    '''returns boolean\n\n
    isEventDispatching()\n
    '''
def isCollapseExpandIconsEnabled():
    '''returns boolean\n\n
    isCollapseExpandIconsEnabled()\n
    '''
def setCollapseExpandIconsEnabled():
    '''returns None\n\n
    setCollapseExpandIconsEnabled(final boolean b)\n
    '''
def mousePressed():
    '''returns None\n\n
    mousePressed(final MouseEvent mouseEvent)\n
    '''
def apply():
    '''returns None\n\n
    apply(final IlvGraphic ilvGraphic, final Object o)\n
    '''
def isWheelZoomingEnabled():
    '''returns boolean\n\n
    isWheelZoomingEnabled()\n
    '''
def setWheelZoomingEnabled():
    '''returns None\n\n
    setWheelZoomingEnabled(final boolean b)\n
    '''
def mouseWheelMoved():
    '''returns None\n\n
    mouseWheelMoved(final MouseWheelEvent e)\n
    '''
def setWheelZoomingInverted():
    '''returns None\n\n
    setWheelZoomingInverted(final boolean bd)\n
    '''
def isWheelZoomingInverted():
    '''returns boolean\n\n
    isWheelZoomingInverted()\n
    '''
def getTripleBufferedLayerCount():
    '''returns int\n\n
    getTripleBufferedLayerCount()\n
    '''
def invalidateTripleBuffer():
    '''returns None\n\n
    invalidateTripleBuffer(final boolean b)\n
    invalidateTripleBuffer(final IlvRect ilvRect, final boolean b)\n
    '''
def setTripleBufferedLayerCount():
    '''returns None\n\n
    setTripleBufferedLayerCount(final int n)\n
    '''
def setLayerCached():
    '''returns None\n\n
    setLayerCached(final int n, final boolean b)\n
    '''
def isLayerCached():
    '''returns boolean\n\n
    isLayerCached(final int n)\n
    '''
def getPopupMenu():
    '''returns JPopupMenu\n\n
    getPopupMenu(final IlvPoint ilvPoint, final IlvPopupMenuManager ilvPopupMenuManager)\n
    '''
def setSelectedWhenPopupPreferred():
    '''returns None\n\n
    setSelectedWhenPopupPreferred(final boolean ak)\n
    '''
def isSelectedWhenPopupPreferred():
    '''returns boolean\n\n
    isSelectedWhenPopupPreferred()\n
    '''
def isInSwingParent():
    '''returns boolean\n\n
    isInSwingParent()\n
    '''
def setComponentOrientation():
    '''returns None\n\n
    setComponentOrientation(final ComponentOrientation componentOrientation)\n
    '''
def getULocale():
    '''returns ULocale\n\n
    getULocale()\n
    '''
def setULocale():
    '''returns None\n\n
    setULocale(final ULocale uLocale)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def invalidateCache():
    '''returns None\n\n
    invalidateCache(final int n, final IlvRect ilvRect)\n
    invalidateCache()\n
    '''
def cleanCache():
    '''returns None\n\n
    cleanCache()\n
    '''
def cacheLayer():
    '''returns None\n\n
    cacheLayer(final int n, final boolean b)\n
    '''
def getCache():
    '''returns BufferedImage\n\n
    getCache(final int n)\n
    getCache()\n
    getCache(final IlvManagerView ilvManagerView)\n
    '''
def getInvalidRegion():
    '''returns IlvRegion\n\n
    getInvalidRegion()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def validateCache():
    '''returns None\n\n
    validateCache(final boolean a)\n
    '''
def invalidateRect():
    '''returns None\n\n
    invalidateRect(final IlvRect ilvRect)\n
    '''
def setCache():
    '''returns None\n\n
    setCache(final BufferedImage b)\n
    '''
def validateHints():
    '''returns None\n\n
    validateHints(final RenderingHints d)\n
    '''
