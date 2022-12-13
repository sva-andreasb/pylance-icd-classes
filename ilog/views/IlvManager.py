HH_NONE = "int  0"
HH_BLUR = "int  1"
HH_BRIGHTEN = "int  2"
HH_GRAYSCALE = "int  3"
HH_SHARPEN = "int  4"
HH_INVERT_COLORS = "int  5"
HH_CUSTOM = "int  6"
def IlvManager():
    '''    public IlvManager()
    public IlvManager(final int n)
    public IlvManager(final int n, final int n2)
    public IlvManager(final IlvManager ilvManager)
    public IlvManager(final IlvInputStream ilvInputStream)
    '''
def setDebugBoundingBoxesGlobal():
    '''    public static void setDebugBoundingBoxesGlobal(final boolean b9)
    '''
def setDebugBoundingBoxes():
    '''    public void setDebugBoundingBoxes(final boolean b)
    '''
def isDebugBoundingBoxes():
    '''    public boolean isDebugBoundingBoxes()
    '''
def setNameImpl():
    '''    public void setNameImpl(final String nameImpl)
    '''
def setUserData():
    '''    public final void setUserData(final Object l)
    '''
def getUserData():
    '''    public final Object getUserData()
    '''
def addObject():
    '''    public void addObject(final IlvGraphic key, int n, boolean b)
    public void addObject(final IlvGraphic ilvGraphic, final boolean b)
    '''
def removeObject():
    '''    public void removeObject(final IlvGraphic key, final boolean b)
    '''
def getInsertionLayer():
    '''    public final int getInsertionLayer()
    '''
def setInsertionLayer():
    '''    public final void setInsertionLayer(final int s)
    '''
def replaceObject():
    '''    public void replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)
    '''
def isManaged():
    '''    public boolean isManaged(final IlvGraphic ilvGraphic)
    '''
def getCardinal():
    '''    public final int getCardinal()
    public final int getCardinal(final boolean b)
    public final int getCardinal(final int n)
    '''
def getObjects():
    '''    public final IlvGraphicEnumeration getObjects()
    public final IlvGraphicEnumeration getObjects(final boolean b)
    public final IlvGraphicEnumeration getObjects(final int n)
    '''
def getObject():
    '''    public IlvGraphic getObject(final String key)
    public IlvGraphic getObject(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)
    public IlvGraphic getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
    public IlvGraphic getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)
    '''
def setObjectName():
    '''    public boolean setObjectName(final IlvGraphic value, final String s)
    '''
def getObjectName():
    '''    public String getObjectName(final IlvGraphic ilvGraphic)
    '''
def applyToObject():
    '''    public void applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
    '''
def applyToObjects():
    '''    public void applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
    public void applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
    public void applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)
    public void applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)
    '''
def moveObject():
    '''    public void moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)
    '''
def reshapeObject():
    '''    public void reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)
    '''
def addLayer():
    '''    public void addLayer(final IlvManagerLayer ilvManagerLayer, int n)
    public void addLayer(final int n)
    '''
def removeLayer():
    '''    public void removeLayer(final int n, final boolean b)
    '''
def setOptimizedLayerThreshold():
    '''    public void setOptimizedLayerThreshold(final long r)
    '''
def getOptimizedLayerThreshold():
    '''    public long getOptimizedLayerThreshold()
    '''
def setNumberOfLayer():
    '''    public void setNumberOfLayer(int n)
    '''
def getLayersCount():
    '''    public int getLayersCount()
    '''
def getLayer():
    '''    public final int getLayer(final IlvGraphic obj)
    public int getLayer(final String anObject)
    '''
def swapLayers():
    '''    public void swapLayers(final int n, final int n2, final boolean b)
    '''
def addManagerLayerListener():
    '''    public void addManagerLayerListener(final ManagerLayerListener l)
    '''
def removeManagerLayerListener():
    '''    public void removeManagerLayerListener(final ManagerLayerListener l)
    '''
def setLayerName():
    '''    public void setLayerName(final int n, final String name)
    '''
def getLayerName():
    '''    public String getLayerName(final int n)
    '''
def getManagerLayer():
    '''    public IlvManagerLayer getManagerLayer(final String anObject)
    public final IlvManagerLayer getManagerLayer(final int n)
    public final IlvManagerLayer getManagerLayer(final IlvGraphic obj)
    '''
def setLayer():
    '''    public void setLayer(final IlvGraphic obj, final int n, final boolean b)
    '''
def setVisible():
    '''    public void setVisible(final int n, final boolean b, final boolean b2)
    public void setVisible(final IlvManagerView ilvManagerView, final int n, final boolean b, final boolean b2)
    public void setVisible(final IlvGraphic ilvGraphic, final boolean visible, final boolean b)
    '''
def isVisible():
    '''    public boolean isVisible(final int n)
    public boolean isVisible(final IlvManagerView ilvManagerView, final int n)
    public boolean isVisible(final IlvGraphic ilvGraphic)
    public boolean isVisible(final IlvGraphic ilvGraphic, final IlvManagerView ilvManagerView)
    '''
def setInsertionAdjusting():
    '''    public void setInsertionAdjusting(final boolean b)
    '''
def isInsertionAdjusting():
    '''    public boolean isInsertionAdjusting()
    '''
def addManagerContentChangedListener():
    '''    public void addManagerContentChangedListener(final ManagerContentChangedListener l)
    '''
def removeManagerContentChangedListener():
    '''    public void removeManagerContentChangedListener(final ManagerContentChangedListener l)
    '''
def addManagerTreeContentChangedListener():
    '''    public void addManagerTreeContentChangedListener(final ManagerContentChangedListener l)
    '''
def removeManagerTreeContentChangedListener():
    '''    public void removeManagerTreeContentChangedListener(final ManagerContentChangedListener l)
    '''
def setContentsAdjusting():
    '''    public void setContentsAdjusting(final boolean b)
    public void setContentsAdjusting(final boolean contentsAdjusting, final boolean b)
    '''
def isContentsAdjusting():
    '''    public final boolean isContentsAdjusting()
    '''
def getViews():
    '''    public final Enumeration getViews()
    '''
def addManagerViewsListener():
    '''    public void addManagerViewsListener(final ManagerViewsChangedListener l)
    '''
def removeManagerViewsListener():
    '''    public void removeManagerViewsListener(final ManagerViewsChangedListener l)
    '''
def addManagerViewsHierarchyListener():
    '''    public void addManagerViewsHierarchyListener(final ManagerViewsChangedListener l)
    '''
def removeManagerViewsHierarchyListener():
    '''    public void removeManagerViewsHierarchyListener(final ManagerViewsChangedListener l)
    '''
def enableManagerViewsHierarchyEventForwarding():
    '''    public void enableManagerViewsHierarchyEventForwarding()
    '''
def needsManagerViewsHierarchyEvent():
    '''    public boolean needsManagerViewsHierarchyEvent()
    '''
def fireManagerViewsHierarchyEvent():
    '''    public void fireManagerViewsHierarchyEvent(final ManagerViewsChangedEvent managerViewsChangedEvent)
    '''
def reDrawObj():
    '''    public void reDrawObj(final IlvGraphic ilvGraphic)
    '''
def reDrawRegion():
    '''    public void reDrawRegion(final IlvRegion ilvRegion)
    '''
def invalidateRegion():
    '''    public void invalidateRegion(final IlvGraphic ilvGraphic)
    public void invalidateRegion(final IlvRect ilvRect)
    public void invalidateRegion(final IlvManagerView ilvManagerView, final IlvRect ilvRect)
    '''
def initReDraws():
    '''    public void initReDraws()
    '''
def isInvalidating():
    '''    public boolean isInvalidating()
    '''
def abortReDraws():
    '''    public void abortReDraws()
    '''
def reDrawViews():
    '''    public void reDrawViews()
    '''
def blinkingReDraw():
    '''    public void blinkingReDraw()
    '''
def reDraw():
    '''    public void reDraw()
    '''
def computeBBox():
    '''    public IlvRect computeBBox(final IlvTransformer ilvTransformer)
    public IlvRect computeBBox(final IlvTransformer ilvTransformer, final boolean b)
    '''
def draw():
    '''    public void draw(final Graphics graphics, final IlvManagerView ilvManagerView)
    public void draw(final Graphics graphics, final IlvTransformer ilvTransformer)
    '''
def print():
    '''    public void print(final Graphics graphics, final IlvRect ilvRect, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
    '''
def processEvent():
    '''    public boolean processEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
    '''
def getObjectInteractor():
    '''    public final IlvObjectInteractor getObjectInteractor(final IlvGraphic ilvGraphic)
    '''
def setObjectInteractor():
    '''    public final void setObjectInteractor(final IlvGraphic ilvGraphic, final IlvObjectInteractor objectInteractor)
    '''
def setHoverHighlightingImageOperation():
    '''    public void setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation bq)
    '''
def getHoverHighlightingImageOperation():
    '''    public IlvHoverHighlightingImageOperation getHoverHighlightingImageOperation()
    '''
def setHoverHighlightingMode():
    '''    public void setHoverHighlightingMode(final int n)
    '''
def getHoverHighlightingMode():
    '''    public int getHoverHighlightingMode()
    '''
def shortCut():
    '''    public boolean shortCut(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
    '''
def processHoverHighlightingEvent():
    '''    public boolean processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
    public boolean processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView, final IlvGraphic ilvGraphic)
    '''
def dispatchToObjects():
    '''    public boolean dispatchToObjects(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
    '''
def addAccelerator():
    '''    public void addAccelerator(final IlvAccelerator e)
    '''
def removeAccelerator():
    '''    public void removeAccelerator(final IlvAccelerator o)
    '''
def getAccelerators():
    '''    public IlvAccelerator[] getAccelerators()
    '''
def setAccelerators():
    '''    public void setAccelerators(final IlvAccelerator[] array)
    '''
def deleteAll():
    '''    public void deleteAll(final boolean b)
    public void deleteAll(final int n, final boolean b)
    '''
def allowMoving():
    '''    public boolean allowMoving(final IlvGraphic ilvGraphic)
    '''
def isMovable():
    '''    public boolean isMovable(final IlvGraphic ilvGraphic)
    '''
def setMovable():
    '''    public void setMovable(final IlvGraphic ilvGraphic, final boolean movable)
    '''
def isEditable():
    '''    public boolean isEditable(final IlvGraphic ilvGraphic)
    '''
def setEditable():
    '''    public void setEditable(final IlvGraphic ilvGraphic, final boolean editable)
    '''
def isSelectable():
    '''    public boolean isSelectable(final IlvGraphic ilvGraphic)
    public boolean isSelectable(final int n)
    '''
def objectIsSelectable():
    '''    public boolean objectIsSelectable(final IlvGraphic ilvGraphic)
    '''
def setSelectable():
    '''    public void setSelectable(final IlvGraphic ilvGraphic, final boolean selectable)
    public void setSelectable(final int n, final boolean b)
    '''
def getAllObjects():
    '''    public IlvGraphicVector getAllObjects(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)
    public IlvGraphicVector getAllObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b, final boolean b2)
    '''
def getCollapseExpandObject():
    '''    public IlvObjectWithSelection getCollapseExpandObject(final IlvPoint p4, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
    '''
def getSelectableObject():
    '''    public IlvGraphic getSelectableObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
    '''
def getAllSelectableObjects():
    '''    public IlvGraphicVector getAllSelectableObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)
    '''
def getSelection():
    '''    public IlvSelection getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
    public IlvSelection getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)
    public final IlvSelection getSelection(final IlvGraphic ilvGraphic)
    '''
def isSelected():
    '''    public boolean isSelected(final IlvGraphic ilvGraphic)
    '''
def setSelected():
    '''    public void setSelected(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)
    public void setSelected(final IlvGraphic ilvGraphic, final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
    '''
def addManagerSelectionListener():
    '''    public void addManagerSelectionListener(final ManagerSelectionListener l)
    '''
def removeManagerSelectionListener():
    '''    public void removeManagerSelectionListener(final ManagerSelectionListener l)
    '''
def addManagerTreeSelectionListener():
    '''    public void addManagerTreeSelectionListener(final ManagerSelectionListener l)
    '''
def removeManagerTreeSelectionListener():
    '''    public void removeManagerTreeSelectionListener(final ManagerSelectionListener l)
    '''
def setSelectionEventSource():
    '''    public void setSelectionEventSource(final Object ac)
    '''
def setSelectionAdjusting():
    '''    public void setSelectionAdjusting(final boolean b)
    '''
def isSelectionAdjusting():
    '''    public boolean isSelectionAdjusting()
    '''
def selectAll():
    '''    public void selectAll(final IlvManagerView ilvManagerView, final boolean b)
    public void selectAll(final boolean b)
    public void selectAll(final boolean b, final boolean b2)
    '''
def deSelectAll():
    '''    public void deSelectAll(final boolean b)
    public void deSelectAll(final boolean b, final boolean b2)
    public void deSelectAll(final int n, final boolean b)
    '''
def getSelections():
    '''    public final IlvGraphicEnumeration getSelections()
    '''
def getSelectedObjects():
    '''    public final IlvGraphicEnumeration getSelectedObjects()
    public final IlvGraphicEnumeration getSelectedObjects(final boolean b)
    public final IlvGraphicEnumeration getSelectedObjects(final boolean b, final boolean b2)
    '''
def getSelectedObjectsCount():
    '''    public final int getSelectedObjectsCount()
    public final int getSelectedObjectsCount(final boolean b)
    public final int getSelectedObjectsCount(final boolean b, final boolean b2)
    '''
def setSelectionFactory():
    '''    public void setSelectionFactory(final IlvSelectionFactory ay)
    '''
def getSelectionFactory():
    '''    public IlvSelectionFactory getSelectionFactory()
    '''
def write():
    '''    public void write(final IlvOutputStream ilvOutputStream)
    public void write(final OutputStream outputStream, final boolean b)
    public void write(final OutputStream outputStream)
    public void write(final String name, final boolean b)
    public void write(final String s)
    '''
def writeIt():
    '''    public void writeIt(final IlvOutputStream ilvOutputStream)
    '''
def writePrefix():
    '''    public void writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)
    '''
def writeSuffix():
    '''    public void writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)
    '''
def readPrefix():
    '''    public void readPrefix(final IlvInputStream ilvInputStream, final boolean b)
    '''
def readSuffix():
    '''    public void readSuffix(final IlvInputStream ilvInputStream, final boolean b)
    '''
def setFileName():
    '''    public void setFileName(final URL a9)
    '''
def getFileName():
    '''    public URL getFileName()
    '''
def read():
    '''    public boolean read(final InputStream inputStream)
    public boolean read(final String name)
    public boolean read(final URL az)
    '''
def setStreamFactory():
    '''    public void setStreamFactory(final IlvManagerStreamFactory a7)
    '''
def getStreamFactory():
    '''    public IlvManagerStreamFactory getStreamFactory()
    '''
def beforeTransform():
    '''    public final void beforeTransform(final IlvGraphic ilvGraphic, final boolean b, final boolean b2, final boolean b3)
    '''
def afterTransform():
    '''    public final void afterTransform(final IlvGraphic ilvGraphic, final boolean b, final boolean b2, final boolean b3, final boolean b4)
    '''
def check():
    '''    public void check(final boolean b)
    '''
def getSelectedMovingObjects():
    '''    public IlvGraphicEnumeration getSelectedMovingObjects(final boolean[] array)
    '''
def translateSelections():
    '''    public void translateSelections(final float n, final float n2, final IlvManagerView ilvManagerView)
    '''
def translateObjects():
    '''    public void translateObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final float n, final float n2, final IlvTransformer ilvTransformer)
    '''
def deleteSelections():
    '''    public void deleteSelections(final boolean b)
    public void deleteSelections(final boolean b, final boolean b2)
    '''
def duplicateSelections():
    '''    public void duplicateSelections(final int n, final int n2)
    public void duplicateSelections(final float n, final float n2, final IlvTransformer ilvTransformer, final boolean b)
    '''
def map():
    '''    public void map(final IlvApplyObject ilvApplyObject, final Object o)
    public void map(final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
    '''
def mapIntersects():
    '''    public void mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
    public void mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)
    '''
def mapInside():
    '''    public void mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
    public void mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)
    '''
def pasteSelection():
    '''    public IlvGraphicEnumeration pasteSelection(final IlvPoint ilvPoint, final boolean b)
    '''
def copySelection():
    '''    public void copySelection()
    '''
def lostOwnership():
    '''    public void lostOwnership(final Clipboard clipboard, final Transferable transferable)
    '''
def removeProperty():
    '''    public boolean removeProperty(final String key)
    '''
def setProperty():
    '''    public void setProperty(final String key, final Object value)
    '''
def replaceProperty():
    '''    public boolean replaceProperty(final String key, final Object value)
    '''
def getProperty():
    '''    public Object getProperty(final String key)
    '''
def hasProperty():
    '''    public boolean hasProperty(final String key, final Object o)
    '''
def getManagers():
    '''    public final IlvGraphicEnumeration getManagers()
    public final IlvGraphicEnumeration getManagers(final int n)
    '''
def getManagersCount():
    '''    public final int getManagersCount()
    public final int getManagersCount(final int n)
    '''
def zoomable():
    '''    public boolean zoomable()
    '''
def applyTransform():
    '''    public void applyTransform(final IlvTransformer ilvTransformer)
    '''
def moveResize():
    '''    public void moveResize(IlvRect obj)
    '''
def setGraphicBag():
    '''    public void setGraphicBag(final IlvGraphicBag graphicBag)
    '''
def setCollapsed():
    '''    public final void setCollapsed(final boolean bh)
    '''
def isCollapsed():
    '''    public final boolean isCollapsed()
    '''
def isCollapsible():
    '''    public final boolean isCollapsible()
    '''
def setCollapsedGraphic():
    '''    public final void setCollapsedGraphic(final IlvGraphic bi)
    '''
def getCollapsedGraphic():
    '''    public final IlvGraphic getCollapsedGraphic()
    '''
def isAutoLabelForCollapsedGraphic():
    '''    public final boolean isAutoLabelForCollapsedGraphic()
    '''
def setAutoLabelForCollapsedGraphic():
    '''    public final void setAutoLabelForCollapsedGraphic(final boolean bj)
    '''
def addManagerExpansionListener():
    '''    public void addManagerExpansionListener(final ManagerExpansionListener l)
    '''
def removeManagerExpansionListener():
    '''    public void removeManagerExpansionListener(final ManagerExpansionListener l)
    '''
def addGraphicBagHierarchyListener():
    '''    public void addGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)
    '''
def removeGraphicBagHierarchyListener():
    '''    public void removeGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)
    '''
def enableGraphicBagHierarchyEventForwarding():
    '''    public void enableGraphicBagHierarchyEventForwarding()
    '''
def needsGraphicBagHierarchyEvent():
    '''    public boolean needsGraphicBagHierarchyEvent()
    '''
def fireGraphicBagHierarchyEvent():
    '''    public void fireGraphicBagHierarchyEvent(final GraphicBagHierarchyEvent graphicBagHierarchyEvent)
    '''
def setSelectionInvariantSubManagerBounds():
    '''    public void setSelectionInvariantSubManagerBounds(final boolean b)
    '''
def isSelectionInvariantSubManagerBounds():
    '''    public boolean isSelectionInvariantSubManagerBounds()
    '''
def boundingBox():
    '''    public IlvRect boundingBox(final IlvTransformer ilvTransformer)
    '''
def copy():
    '''    public IlvGraphic copy()
    '''
def getFrame():
    '''    public IlvManagerFrame getFrame()
    '''
def setFrame():
    '''    public void setFrame(final IlvManagerFrame bg)
    '''
def getParent():
    '''    public final IlvManager getParent()
    '''
def getTransformer():
    '''    public IlvTransformer getTransformer()
    public IlvTransformer getTransformer()
    '''
def setTransformer():
    '''    public final void setTransformer(final IlvTransformer ilvTransformer)
    '''
def isKeepingAspectRatio():
    '''    public final boolean isKeepingAspectRatio()
    '''
def setKeepingAspectRatio():
    '''    public final void setKeepingAspectRatio(final boolean b)
    '''
def getDrawingTransformer():
    '''    public IlvTransformer getDrawingTransformer(final IlvManagerView ilvManagerView)
    '''
def getTopLevelTransformer():
    '''    public IlvTransformer getTopLevelTransformer()
    '''
def getTreeLock():
    '''    public final Object getTreeLock()
    '''
def getULocale():
    '''    public ULocale getULocale()
    '''
def getStoredULocale():
    '''    public final ULocale getStoredULocale()
    '''
def setULocale():
    '''    public void setULocale(final ULocale uLocale)
    public void setULocale(final ULocale bs, final boolean b)
    '''
def isLocaleSensitive():
    '''    public boolean isLocaleSensitive()
    '''
def getComponentOrientation():
    '''    public ComponentOrientation getComponentOrientation()
    '''
def getStoredComponentOrientation():
    '''    public final ComponentOrientation getStoredComponentOrientation()
    '''
def setComponentOrientation():
    '''    public void setComponentOrientation(final ComponentOrientation componentOrientation)
    public void setComponentOrientation(final ComponentOrientation bt, final boolean b)
    '''
def isComponentOrientationSensitive():
    '''    public boolean isComponentOrientationSensitive()
    '''
def isBaseTextDirectionSensitive():
    '''    public boolean isBaseTextDirectionSensitive()
    '''
def containsFrame():
    '''    public boolean containsFrame(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
    '''
def contains():
    '''    public boolean contains(final IlvPoint ilvPoint, final IlvPoint p3, final IlvTransformer ilvTransformer)
    '''
def getIntersectionWithOutline():
    '''    public IlvPoint getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)
    '''
def setSizeLimitToDrawSubmanagerContents():
    '''    public void setSizeLimitToDrawSubmanagerContents(final float bm)
    '''
def getSizeLimitToDrawSubmanagerContents():
    '''    public float getSizeLimitToDrawSubmanagerContents()
    '''
def componentOrientationChanged():
    '''    public void componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)
    '''
def localeChanged():
    '''    public void localeChanged(final ULocale uLocale, final ULocale uLocale2)
    '''
def baseTextDirectionChanged():
    '''    public void baseTextDirectionChanged(final int d, final int baseTextDirection)
    '''
def setBaseTextDirection():
    '''    public void setBaseTextDirection(final int n, final boolean b)
    '''
def run():
    '''    public void run()
    '''
def repaint():
    '''    public void repaint(final IlvRect ilvRect)
    '''
def getGraphics():
    '''    public Graphics getGraphics()
    '''
def getGrid():
    '''    public IlvGrid getGrid()
    '''
def setCursor():
    '''    public void setCursor(final Cursor cursor)
    '''
def getCursor():
    '''    public Cursor getCursor()
    '''
def isCursorSet():
    '''    public boolean isCursorSet()
    '''
def ensureVisible():
    '''    public void ensureVisible(final IlvPoint ilvPoint)
    '''
def snapToGrid():
    '''    public void snapToGrid(final IlvPoint ilvPoint)
    '''
def getDefaultXORColor():
    '''    public Color getDefaultXORColor()
    '''
def getDefaultGhostColor():
    '''    public Color getDefaultGhostColor()
    '''
def hasMoreElements():
    '''    public final boolean hasMoreElements()
    public final boolean hasMoreElements()
    public final boolean hasMoreElements()
    public final boolean hasMoreElements()
    public boolean hasMoreElements()
    '''
def nextElement():
    '''    public final IlvGraphic nextElement()
    public final IlvGraphic nextElement()
    public final IlvGraphic nextElement()
    public final IlvGraphic nextElement()
    public IlvGraphic nextElement()
    '''
def init():
    '''    public final void init(final float b, final float c, final IlvTransformer d)
    '''
def apply():
    '''    public final void apply(final IlvGraphic ilvGraphic, final Object o)
    '''
def translateObj():
    '''    public final void translateObj(final IlvGraphic ilvGraphic, final boolean b)
    '''
