THREADED_REDRAW = "int  0"
DIRECT_REDRAW = "int  1"
BLINKING_AUTOMATIC = "int  0"
BLINKING_ENABLED = "int  1"
BLINKING_DISABLED = "int  2"
def IlvManagerView():
'''public IlvManagerView(final IlvManager o, final IlvTransformer ilvTransformer, final ULocale uLocale)
public IlvManagerView(final IlvManager ilvManager, final IlvTransformer ilvTransformer)
public IlvManagerView(final IlvManager ilvManager)
public IlvManagerView()
'''
pass
def hierarchyChanged():
'''public void hierarchyChanged(final HierarchyEvent hierarchyEvent)
public void hierarchyChanged(final HierarchyEvent hierarchyEvent)
'''
pass
def getManager():
'''public final IlvManager getManager()
'''
pass
def setManager():
'''public final void setManager(IlvManager o)
'''
pass
def addManagerChangedListener():
'''public void addManagerChangedListener(final ManagerChangedListener l)
'''
pass
def removeManagerChangedListener():
'''public void removeManagerChangedListener(final ManagerChangedListener l)
'''
pass
def setTransformer():
'''public final void setTransformer(final IlvTransformer ilvTransformer)
'''
pass
def getTransformer():
'''public final IlvTransformer getTransformer()
'''
pass
def addTransformer():
'''public final void addTransformer(final IlvTransformer ilvTransformer)
'''
pass
def addTransformerListener():
'''public final void addTransformerListener(final TransformerListener l)
'''
pass
def removeTransformerListener():
'''public final void removeTransformerListener(final TransformerListener l)
'''
pass
def isKeepingAspectRatio():
'''public final boolean isKeepingAspectRatio()
'''
pass
def setKeepingAspectRatio():
'''public final void setKeepingAspectRatio(final boolean aj)
'''
pass
def setZoomFactorRange():
'''public final void setZoomFactorRange(final double n, final double n2)
'''
pass
def setMinZoomXFactor():
'''public final void setMinZoomXFactor(final double r)
'''
pass
def getMinZoomXFactor():
'''public final double getMinZoomXFactor()
'''
pass
def setMaxZoomXFactor():
'''public final void setMaxZoomXFactor(final double t)
'''
pass
def getMaxZoomXFactor():
'''public final double getMaxZoomXFactor()
'''
pass
def setMinZoomYFactor():
'''public final void setMinZoomYFactor(final double s)
'''
pass
def getMinZoomYFactor():
'''public final double getMinZoomYFactor()
'''
pass
def setMaxZoomYFactor():
'''public final void setMaxZoomYFactor(final double u)
'''
pass
def getMaxZoomYFactor():
'''public final double getMaxZoomYFactor()
'''
pass
def isAtZoomXFactorLimit():
'''public final boolean isAtZoomXFactorLimit()
'''
pass
def isAtZoomYFactorLimit():
'''public final boolean isAtZoomYFactorLimit()
'''
pass
def setInteractor():
'''public void setInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)
'''
pass
def getInteractor():
'''public synchronized IlvManagerViewInteractor getInteractor()
'''
pass
def pushInteractor():
'''public void pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor, final AWTEvent awtEvent)
public void pushInteractor(final IlvManagerViewInteractor ilvManagerViewInteractor)
'''
pass
def popInteractor():
'''public IlvManagerViewInteractor popInteractor()
'''
pass
def removeAllInteractors():
'''public void removeAllInteractors()
'''
pass
def addInteractorListener():
'''public final void addInteractorListener(final InteractorListener l)
'''
pass
def removeInteractorListener():
'''public final void removeInteractorListener(final InteractorListener l)
'''
pass
def isTransparent():
'''public final boolean isTransparent()
'''
pass
def setTransparent():
'''public final void setTransparent(final boolean ah)
'''
pass
def isAntialiasing():
'''public final boolean isAntialiasing()
'''
pass
def setAntialiasing():
'''public final void setAntialiasing(final boolean ai)
'''
pass
def isAutoFitToContents():
'''public final boolean isAutoFitToContents()
'''
pass
def setAutoFitToContents():
'''public final void setAutoFitToContents(final boolean n)
'''
pass
def contentsChanged():
'''public void contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)
'''
pass
def setDoubleBuffering():
'''public final void setDoubleBuffering(final boolean f)
'''
pass
def isDoubleBuffering():
'''public final boolean isDoubleBuffering()
'''
pass
def setDoubleBufferFrozen():
'''public void setDoubleBufferFrozen(final boolean g)
'''
pass
def isDoubleBufferFrozen():
'''public boolean isDoubleBufferFrozen()
'''
pass
def createImage():
'''public Image createImage(final int n, final int n2)
'''
pass
def setRegisteredAtToolTipManager():
'''public void setRegisteredAtToolTipManager(final boolean bv)
'''
pass
def isRegisteredAtToolTipManager():
'''public boolean isRegisteredAtToolTipManager()
'''
pass
def imageUpdate():
'''public boolean imageUpdate(final Image image, final int n, final int n2, final int n3, final int n4, final int n5)
'''
pass
def update():
'''public void update(final Graphics graphics)
'''
pass
def repaint():
'''public void repaint(final IlvRect ilvRect)
public void repaint(final long n, final int x, final int y, final int width, final int height)
'''
pass
def paint():
'''public void paint(final Graphics graphics)
public void paint(final Graphics graphics, final IlvManagerView ilvManagerView)
'''
pass
def print():
'''public void print(final Graphics graphics, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)
'''
pass
def isOpaque():
'''public boolean isOpaque()
'''
pass
def setBounds():
'''public void setBounds(final int x, final int y, final int width, final int height)
'''
pass
def isVisible():
'''public boolean isVisible(final int n)
'''
pass
def setVisible():
'''public void setVisible(final int n, final boolean b)
'''
pass
def isContributingToViewBBox():
'''public boolean isContributingToViewBBox(final int n)
'''
pass
def setContributingToViewBBox():
'''public void setContributingToViewBBox(final int n, final boolean b)
'''
pass
def computeBBox():
'''public IlvRect computeBBox()
public IlvRect computeBBox(final IlvTransformer ilvTransformer)
'''
pass
def setViewMargins():
'''public void setViewMargins(final Insets a9)
'''
pass
def getViewMargins():
'''public Insets getViewMargins()
'''
pass
def fitTransformerToContent():
'''public void fitTransformerToContent()
public void fitTransformerToContent(final boolean b)
public void fitTransformerToContent(final Insets insets)
public void fitTransformerToContent(final Insets insets, final int n)
public void fitTransformerToContent(final Insets insets, final int n, final boolean b)
'''
pass
def fitTransformerToArea():
'''public void fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)
public void fitTransformerToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n, final boolean b)
'''
pass
def componentResized():
'''public void componentResized(final ComponentEvent componentEvent)
'''
pass
def componentShown():
'''public void componentShown(final ComponentEvent componentEvent)
'''
pass
def componentHidden():
'''public void componentHidden(final ComponentEvent componentEvent)
'''
pass
def componentMoved():
'''public void componentMoved(final ComponentEvent componentEvent)
'''
pass
def computeTransformerFitToArea():
'''public IlvTransformer computeTransformerFitToArea(final Insets insets, final FitAreaCalculator fitAreaCalculator, final int n)
'''
pass
def ensureVisible():
'''public void ensureVisible(final IlvRect ilvRect)
public void ensureVisible(final IlvPoint ilvPoint)
'''
pass
def visibleRect():
'''public Rectangle visibleRect()
'''
pass
def verifyTransformer():
'''public void verifyTransformer()
'''
pass
def zoom():
'''public final void zoom(final IlvPoint ilvPoint, final double n, final double n2, final boolean b)
'''
pass
def isOptimizedTranslation():
'''public boolean isOptimizedTranslation()
'''
pass
def setOptimizedTranslation():
'''public void setOptimizedTranslation(final boolean ag)
'''
pass
def translate():
'''public void translate(final float n, final float n2, final boolean b)
'''
pass
def setRepaintSkipThreshold():
'''public void setRepaintSkipThreshold(final long b)
'''
pass
def getRepaintSkipThreshold():
'''public long getRepaintSkipThreshold()
'''
pass
def run():
'''public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
public void run()
'''
pass
def setRedrawMode():
'''public final void setRedrawMode(final int av)
'''
pass
def getRedrawMode():
'''public final int getRedrawMode()
'''
pass
def setBlinkingMode():
'''public final void setBlinkingMode(final int aw)
'''
pass
def getBlinkingMode():
'''public final int getBlinkingMode()
'''
pass
def getRegion():
'''public final IlvRegion getRegion()
'''
pass
def invalidateRect():
'''public final void invalidateRect(final IlvRect ilvRect)
public void invalidateRect(final IlvRect ilvRect)
'''
pass
def invalidateView():
'''public final void invalidateView()
'''
pass
def reDrawViews():
'''public final void reDrawViews()
'''
pass
def reDrawViewsForBlinking():
'''public final void reDrawViewsForBlinking()
'''
pass
def getDefaultXORColor():
'''public final Color getDefaultXORColor()
'''
pass
def setDefaultXORColor():
'''public final void setDefaultXORColor(final Color ar)
'''
pass
def getDefaultGhostColor():
'''public final Color getDefaultGhostColor()
'''
pass
def setDefaultGhostColor():
'''public final void setDefaultGhostColor(final Color as)
'''
pass
def getBackgroundPatternLocation():
'''public final URL getBackgroundPatternLocation()
'''
pass
def setBackgroundPatternLocation():
'''public final void setBackgroundPatternLocation(URL prepare)
'''
pass
def getBackgroundPattern():
'''public final Image getBackgroundPattern()
'''
pass
def setBackgroundPattern():
'''public final void setBackgroundPattern(final Image image)
'''
pass
def setPreferredSize():
'''public void setPreferredSize(final Dimension d)
'''
pass
def getPreferredSize():
'''public Dimension getPreferredSize()
'''
pass
def setMaximumSize():
'''public void setMaximumSize(final Dimension d)
'''
pass
def getMaximumSize():
'''public Dimension getMaximumSize()
'''
pass
def setMinimumSize():
'''public void setMinimumSize(final Dimension d)
'''
pass
def getMinimumSize():
'''public Dimension getMinimumSize()
'''
pass
def setCursor():
'''public void setCursor(final Cursor cursor)
'''
pass
def setBackground():
'''public void setBackground(final Color color)
'''
pass
def addViewDecoration():
'''public void addViewDecoration(final IlvManagerViewDecoration e)
'''
pass
def removeViewDecoration():
'''public void removeViewDecoration(final IlvManagerViewDecoration o)
'''
pass
def getViewDecorationCount():
'''public int getViewDecorationCount()
'''
pass
def getViewDecoration():
'''public IlvManagerViewDecoration getViewDecoration(final int index)
'''
pass
def setGrid():
'''public void setGrid(final IlvGrid aa)
'''
pass
def getGrid():
'''public IlvGrid getGrid()
'''
pass
def snapToGrid():
'''public final void snapToGrid(final IlvPoint ilvPoint)
'''
pass
def removeNotify():
'''public void removeNotify()
'''
pass
def addNotify():
'''public void addNotify()
'''
pass
def setEventDispatching():
'''public void setEventDispatching(final boolean ac)
'''
pass
def isEventDispatching():
'''public boolean isEventDispatching()
'''
pass
def isCollapseExpandIconsEnabled():
'''public boolean isCollapseExpandIconsEnabled()
'''
pass
def setCollapseExpandIconsEnabled():
'''public void setCollapseExpandIconsEnabled(final boolean b)
'''
pass
def mousePressed():
'''public void mousePressed(final MouseEvent mouseEvent)
'''
pass
def apply():
'''public void apply(final IlvGraphic ilvGraphic, final Object o)
'''
pass
def isWheelZoomingEnabled():
'''public boolean isWheelZoomingEnabled()
'''
pass
def setWheelZoomingEnabled():
'''public void setWheelZoomingEnabled(final boolean b)
'''
pass
def mouseWheelMoved():
'''public void mouseWheelMoved(final MouseWheelEvent e)
'''
pass
def setWheelZoomingInverted():
'''public void setWheelZoomingInverted(final boolean bd)
'''
pass
def isWheelZoomingInverted():
'''public boolean isWheelZoomingInverted()
'''
pass
def getTripleBufferedLayerCount():
'''public int getTripleBufferedLayerCount()
'''
pass
def invalidateTripleBuffer():
'''public void invalidateTripleBuffer(final boolean b)
public void invalidateTripleBuffer(final IlvRect ilvRect, final boolean b)
'''
pass
def setTripleBufferedLayerCount():
'''public void setTripleBufferedLayerCount(final int n)
'''
pass
def setLayerCached():
'''public void setLayerCached(final int n, final boolean b)
'''
pass
def isLayerCached():
'''public boolean isLayerCached(final int n)
'''
pass
def getPopupMenu():
'''public JPopupMenu getPopupMenu(final IlvPoint ilvPoint, final IlvPopupMenuManager ilvPopupMenuManager)
'''
pass
def setSelectedWhenPopupPreferred():
'''public void setSelectedWhenPopupPreferred(final boolean ak)
'''
pass
def isSelectedWhenPopupPreferred():
'''public boolean isSelectedWhenPopupPreferred()
'''
pass
def isInSwingParent():
'''public boolean isInSwingParent()
'''
pass
def setComponentOrientation():
'''public void setComponentOrientation(final ComponentOrientation componentOrientation)
'''
pass
def getStoredULocale():
'''public final ULocale getStoredULocale()
'''
pass
def getULocale():
'''public ULocale getULocale()
'''
pass
def setULocale():
'''public void setULocale(final ULocale uLocale)
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def initDisplayInfo():
'''public static void initDisplayInfo()
'''
pass
def getCurrentView():
'''public static IlvManagerView getCurrentView(final Graphics graphics)
'''
pass
def LayerCacheManager():
'''public LayerCacheManager()
'''
pass
def invalidateCache():
'''public void invalidateCache(final int n, final IlvRect ilvRect)
public void invalidateCache()
'''
pass
def cleanCache():
'''public void cleanCache()
'''
pass
def cacheLayer():
'''public void cacheLayer(final int n, final boolean b)
'''
pass
def getCache():
'''public LayerCache getCache(final int n)
public BufferedImage getCache()
public BufferedImage getCache(final IlvManagerView ilvManagerView)
'''
pass
def LayerCache():
'''public LayerCache()
'''
pass
def getInvalidRegion():
'''public IlvRegion getInvalidRegion()
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def validateCache():
'''public void validateCache(final boolean a)
'''
pass
def setCache():
'''public void setCache(final BufferedImage b)
'''
pass
def validateHints():
'''public void validateHints(final RenderingHints d)
'''
pass
