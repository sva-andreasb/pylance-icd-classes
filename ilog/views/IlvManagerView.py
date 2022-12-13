THREADED_REDRAW = "int  0"
DIRECT_REDRAW = "int  1"
BLINKING_AUTOMATIC = "int  0"
BLINKING_ENABLED = "int  1"
BLINKING_DISABLED = "int  2"
def IlvManagerView():
    '''    public IlvManagerView(final IlvManager o, final IlvTransformer ilvTransformer, final ULocale uLocale)
    public IlvManagerView(final IlvManager ilvManager, final IlvTransformer ilvTransformer)
    public IlvManagerView(final IlvManager ilvManager)
    public IlvManagerView()
    '''
def hierarchyChanged():
    '''    public void hierarchyChanged(final HierarchyEvent hierarchyEvent)
    public void hierarchyChanged(final HierarchyEvent hierarchyEvent)
    '''
def getManager():
    '''    public final IlvManager getManager()
    '''
def setManager():
    '''    public final void setManager(IlvManager o)
    '''
def addManagerChangedListener():
    '''    public void addManagerChangedListener(final ManagerChangedListener l)
    '''
def removeManagerChangedListener():
    '''    public void removeManagerChangedListener(final ManagerChangedListener l)
    '''
def setTransformer():
    '''    public final void setTransformer(final IlvTransformer ilvTransformer)
    '''
def getTransformer():
    '''    public final IlvTransformer getTransformer()
    '''
def addTransformer():
    '''    public final void addTransformer(final IlvTransformer ilvTransformer)
    '''
def addTransformerListener():
    '''    public final void addTransformerListener(final TransformerListener l)
    '''
def removeTransformerListener():
    '''    public final void removeTransformerListener(final TransformerListener l)
    '''
def isKeepingAspectRatio():
    '''    public final boolean isKeepingAspectRatio()
    '''
def setKeepingAspectRatio():
    '''    public final void setKeepingAspectRatio(final boolean aj)
    '''
def setZoomFactorRange():
    '''    public final void setZoomFactorRange(final double n, final double n2)
    '''
def setMinZoomXFactor():
    '''    public final void setMinZoomXFactor(final double r)
    '''
def getMinZoomXFactor():
    '''    public final double getMinZoomXFactor()
    '''
def setMaxZoomXFactor():
    '''    public final void setMaxZoomXFactor(final double t)
    '''
def getMaxZoomXFactor():
    '''    public final double getMaxZoomXFactor()
    '''
def setMinZoomYFactor():
    '''    public final void setMinZoomYFactor(final double s)
    '''
def getMinZoomYFactor():
    '''    public final double getMinZoomYFactor()
    '''
def setMaxZoomYFactor():
    '''    public final void setMaxZoomYFactor(final double u)
    '''
def getMaxZoomYFactor():
    '''    public final double getMaxZoomYFactor()
    '''
def isAtZoomXFactorLimit():
    '''    public final boolean isAtZoomXFactorLimit()
    '''
def isAtZoomYFactorLimit():
    '''    public final boolean isAtZoomYFactorLimit()
    '''
def setInteractor():
    '''    public void setInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)
    '''
def getInteractor():
    '''    public synchronized IlvManagerViewInteractor getInteractor()
    '''
def pushInteractor():
    '''    public void pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor, final AWTEvent awtEvent)
    public void pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)
    '''
def popInteractor():
    '''    public IlvManagerViewInteractor popInteractor()
    '''
def removeAllInteractors():
    '''    public void removeAllInteractors()
    '''
def addInteractorListener():
    '''    public final void addInteractorListener(final InteractorListener l)
    '''
def removeInteractorListener():
    '''    public final void removeInteractorListener(final InteractorListener l)
    '''
def isTransparent():
    '''    public final boolean isTransparent()
    '''
def setTransparent():
    '''    public final void setTransparent(final boolean ah)
    '''
def isAntialiasing():
    '''    public final boolean isAntialiasing()
    '''
def setAntialiasing():
    '''    public final void setAntialiasing(final boolean ai)
    '''
def isAutoFitToContents():
    '''    public final boolean isAutoFitToContents()
    '''
def setAutoFitToContents():
    '''    public final void setAutoFitToContents(final boolean n)
    '''
def contentsChanged():
    '''    public void contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)
    '''
def setDoubleBuffering():
    '''    public final void setDoubleBuffering(final boolean f)
    '''
def isDoubleBuffering():
    '''    public final boolean isDoubleBuffering()
    '''
def setDoubleBufferFrozen():
    '''    public void setDoubleBufferFrozen(final boolean g)
    '''
def isDoubleBufferFrozen():
    '''    public boolean isDoubleBufferFrozen()
    '''
def createImage():
    '''    public Image createImage(final int n, final int n2)
    '''
def setRegisteredAtToolTipManager():
    '''    public void setRegisteredAtToolTipManager(final boolean bv)
    '''
def isRegisteredAtToolTipManager():
    '''    public boolean isRegisteredAtToolTipManager()
    '''
def imageUpdate():
    '''    public boolean imageUpdate(final Image image, final int n, final int n2, final int n3, final int n4, final int n5)
    '''
def update():
    '''    public void update(final Graphics graphics)
    '''
def repaint():
    '''    public void repaint(final IlvRect ilvRect)
    public void repaint(final long n, final int x, final int y, final int width, final int height)
    '''
def paint():
    '''    public void paint(final Graphics graphics)
    public void paint(final Graphics graphics, final IlvManagerView ilvManagerView)
    '''
def print():
    '''    public void print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)
    '''
def isOpaque():
    '''    public boolean isOpaque()
    '''
def setBounds():
    '''    public void setBounds(final int x, final int y, final int width, final int height)
    '''
def isVisible():
    '''    public boolean isVisible(final int n)
    '''
def setVisible():
    '''    public void setVisible(final int n, final boolean b)
    '''
def isContributingToViewBBox():
    '''    public boolean isContributingToViewBBox(final int n)
    '''
def setContributingToViewBBox():
    '''    public void setContributingToViewBBox(final int n, final boolean b)
    '''
def computeBBox():
    '''    public IlvRect computeBBox()
    public IlvRect computeBBox(final IlvTransformer ilvTransformer)
    '''
def setViewMargins():
    '''    public void setViewMargins(final Insets a9)
    '''
def getViewMargins():
    '''    public Insets getViewMargins()
    '''
def fitTransformerToContent():
    '''    public void fitTransformerToContent()
    public void fitTransformerToContent(final boolean b)
    public void fitTransformerToContent(final Insets insets)
    public void fitTransformerToContent(final Insets insets, final int n)
    public void fitTransformerToContent(final Insets insets, final int n, final boolean b)
    '''
def fitTransformerToArea():
    '''    public void fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)
    public void fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n, final boolean b)
    '''
def componentResized():
    '''    public void componentResized(final ComponentEvent componentEvent)
    '''
def componentShown():
    '''    public void componentShown(final ComponentEvent componentEvent)
    '''
def componentHidden():
    '''    public void componentHidden(final ComponentEvent componentEvent)
    '''
def componentMoved():
    '''    public void componentMoved(final ComponentEvent componentEvent)
    '''
def computeTransformerFitToArea():
    '''    public IlvTransformer computeTransformerFitToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)
    '''
def ensureVisible():
    '''    public void ensureVisible(final IlvRect ilvRect)
    public void ensureVisible(final IlvPoint ilvPoint)
    '''
def visibleRect():
    '''    public Rectangle visibleRect()
    '''
def verifyTransformer():
    '''    public void verifyTransformer()
    '''
def zoom():
    '''    public final void zoom(final IlvPoint ilvPoint, final double n, final double n2, final boolean b)
    '''
def isOptimizedTranslation():
    '''    public boolean isOptimizedTranslation()
    '''
def setOptimizedTranslation():
    '''    public void setOptimizedTranslation(final boolean ag)
    '''
def translate():
    '''    public void translate(final float n, final float n2, final boolean b)
    '''
def setRepaintSkipThreshold():
    '''    public void setRepaintSkipThreshold(final long b)
    '''
def getRepaintSkipThreshold():
    '''    public long getRepaintSkipThreshold()
    '''
def run():
    '''    public void run()
    public void run()
    public void run()
    public void run()
    public void run()
    public void run()
    public void run()
    '''
def setRedrawMode():
    '''    public final void setRedrawMode(final int av)
    '''
def getRedrawMode():
    '''    public final int getRedrawMode()
    '''
def setBlinkingMode():
    '''    public final void setBlinkingMode(final int aw)
    '''
def getBlinkingMode():
    '''    public final int getBlinkingMode()
    '''
def getRegion():
    '''    public final IlvRegion getRegion()
    '''
def invalidateRect():
    '''    public final void invalidateRect(final IlvRect ilvRect)
    public void invalidateRect(final IlvRect ilvRect)
    '''
def invalidateView():
    '''    public final void invalidateView()
    '''
def reDrawViews():
    '''    public final void reDrawViews()
    '''
def reDrawViewsForBlinking():
    '''    public final void reDrawViewsForBlinking()
    '''
def getDefaultXORColor():
    '''    public final Color getDefaultXORColor()
    '''
def setDefaultXORColor():
    '''    public final void setDefaultXORColor(final Color ar)
    '''
def getDefaultGhostColor():
    '''    public final Color getDefaultGhostColor()
    '''
def setDefaultGhostColor():
    '''    public final void setDefaultGhostColor(final Color as)
    '''
def getBackgroundPatternLocation():
    '''    public final URL getBackgroundPatternLocation()
    '''
def setBackgroundPatternLocation():
    '''    public final void setBackgroundPatternLocation(URL prepare)
    '''
def getBackgroundPattern():
    '''    public final Image getBackgroundPattern()
    '''
def setBackgroundPattern():
    '''    public final void setBackgroundPattern(final Image image)
    '''
def setPreferredSize():
    '''    public void setPreferredSize(final Dimension d)
    '''
def getPreferredSize():
    '''    public Dimension getPreferredSize()
    '''
def setMaximumSize():
    '''    public void setMaximumSize(final Dimension d)
    '''
def getMaximumSize():
    '''    public Dimension getMaximumSize()
    '''
def setMinimumSize():
    '''    public void setMinimumSize(final Dimension d)
    '''
def getMinimumSize():
    '''    public Dimension getMinimumSize()
    '''
def setCursor():
    '''    public void setCursor(final Cursor cursor)
    '''
def setBackground():
    '''    public void setBackground(final Color color)
    '''
def addViewDecoration():
    '''    public void addViewDecoration(final IlvManagerViewDecoration e)
    '''
def removeViewDecoration():
    '''    public void removeViewDecoration(final IlvManagerViewDecoration o)
    '''
def getViewDecorationCount():
    '''    public int getViewDecorationCount()
    '''
def getViewDecoration():
    '''    public IlvManagerViewDecoration getViewDecoration(final int index)
    '''
def setGrid():
    '''    public void setGrid(final IlvGrid aa)
    '''
def getGrid():
    '''    public IlvGrid getGrid()
    '''
def snapToGrid():
    '''    public final void snapToGrid(final IlvPoint ilvPoint)
    '''
def removeNotify():
    '''    public void removeNotify()
    '''
def addNotify():
    '''    public void addNotify()
    '''
def setEventDispatching():
    '''    public void setEventDispatching(final boolean ac)
    '''
def isEventDispatching():
    '''    public boolean isEventDispatching()
    '''
def isCollapseExpandIconsEnabled():
    '''    public boolean isCollapseExpandIconsEnabled()
    '''
def setCollapseExpandIconsEnabled():
    '''    public void setCollapseExpandIconsEnabled(final boolean b)
    '''
def mousePressed():
    '''    public void mousePressed(final MouseEvent mouseEvent)
    '''
def apply():
    '''    public void apply(final IlvGraphic ilvGraphic, final Object o)
    '''
def isWheelZoomingEnabled():
    '''    public boolean isWheelZoomingEnabled()
    '''
def setWheelZoomingEnabled():
    '''    public void setWheelZoomingEnabled(final boolean b)
    '''
def mouseWheelMoved():
    '''    public void mouseWheelMoved(final MouseWheelEvent e)
    '''
def setWheelZoomingInverted():
    '''    public void setWheelZoomingInverted(final boolean bd)
    '''
def isWheelZoomingInverted():
    '''    public boolean isWheelZoomingInverted()
    '''
def getTripleBufferedLayerCount():
    '''    public int getTripleBufferedLayerCount()
    '''
def invalidateTripleBuffer():
    '''    public void invalidateTripleBuffer(final boolean b)
    public void invalidateTripleBuffer(final IlvRect ilvRect, final boolean b)
    '''
def setTripleBufferedLayerCount():
    '''    public void setTripleBufferedLayerCount(final int n)
    '''
def setLayerCached():
    '''    public void setLayerCached(final int n, final boolean b)
    '''
def isLayerCached():
    '''    public boolean isLayerCached(final int n)
    '''
def getPopupMenu():
    '''    public JPopupMenu getPopupMenu(final IlvPoint ilvPoint, final IlvPopupMenuManager ilvPopupMenuManager)
    '''
def setSelectedWhenPopupPreferred():
    '''    public void setSelectedWhenPopupPreferred(final boolean ak)
    '''
def isSelectedWhenPopupPreferred():
    '''    public boolean isSelectedWhenPopupPreferred()
    '''
def isInSwingParent():
    '''    public boolean isInSwingParent()
    '''
def setComponentOrientation():
    '''    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    '''
def getStoredULocale():
    '''    public final ULocale getStoredULocale()
    '''
def getULocale():
    '''    public ULocale getULocale()
    '''
def setULocale():
    '''    public void setULocale(final ULocale uLocale)
    '''
def setLocale():
    '''    public void setLocale(final Locale locale)
    '''
def initDisplayInfo():
    '''    public static void initDisplayInfo()
    '''
def getCurrentView():
    '''    public static IlvManagerView getCurrentView(final Graphics graphics)
    '''
def LayerCacheManager():
    '''    public LayerCacheManager()
    '''
def invalidateCache():
    '''    public void invalidateCache(final int n, final IlvRect ilvRect)
    public void invalidateCache()
    '''
def cleanCache():
    '''    public void cleanCache()
    '''
def cacheLayer():
    '''    public void cacheLayer(final int n, final boolean b)
    '''
def getCache():
    '''    public LayerCache getCache(final int n)
    public BufferedImage getCache()
    public BufferedImage getCache(final IlvManagerView ilvManagerView)
    '''
def LayerCache():
    '''    public LayerCache()
    '''
def getInvalidRegion():
    '''    public IlvRegion getInvalidRegion()
    '''
def isValid():
    '''    public boolean isValid()
    '''
def validateCache():
    '''    public void validateCache(final boolean a)
    '''
def setCache():
    '''    public void setCache(final BufferedImage b)
    '''
def validateHints():
    '''    public void validateHints(final RenderingHints d)
    '''
