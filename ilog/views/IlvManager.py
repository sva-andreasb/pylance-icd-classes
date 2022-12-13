HH_NONE = "int  0"
HH_BLUR = "int  1"
HH_BRIGHTEN = "int  2"
HH_GRAYSCALE = "int  3"
HH_SHARPEN = "int  4"
HH_INVERT_COLORS = "int  5"
HH_CUSTOM = "int  6"
def IlvManager():
'''public IlvManager()
public IlvManager(final int n)
public IlvManager(final int n, final int n2)
public IlvManager(final IlvManager ilvManager)
public IlvManager(final IlvInputStream ilvInputStream)
'''
pass
def setDebugBoundingBoxesGlobal():
'''public static void setDebugBoundingBoxesGlobal(final boolean b9)
'''
pass
def setDebugBoundingBoxes():
'''public void setDebugBoundingBoxes(final boolean b)
'''
pass
def isDebugBoundingBoxes():
'''public boolean isDebugBoundingBoxes()
'''
pass
def setNameImpl():
'''public void setNameImpl(final String nameImpl)
'''
pass
def setUserData():
'''public final void setUserData(final Object l)
'''
pass
def getUserData():
'''public final Object getUserData()
'''
pass
def addObject():
'''public void addObject(final IlvGraphic key, int n, boolean b)
public void addObject(final IlvGraphic ilvGraphic, final boolean b)
'''
pass
def removeObject():
'''public void removeObject(final IlvGraphic key, final boolean b)
'''
pass
def getInsertionLayer():
'''public final int getInsertionLayer()
'''
pass
def setInsertionLayer():
'''public final void setInsertionLayer(final int s)
'''
pass
def replaceObject():
'''public void replaceObject(final IlvGraphic obj, final IlvGraphic ilvGraphic, final boolean b)
'''
pass
def isManaged():
'''public boolean isManaged(final IlvGraphic ilvGraphic)
'''
pass
def getCardinal():
'''public final int getCardinal()
public final int getCardinal(final boolean b)
public final int getCardinal(final int n)
'''
pass
def getObjects():
'''public final IlvGraphicEnumeration getObjects()
public final IlvGraphicEnumeration getObjects(final boolean b)
public final IlvGraphicEnumeration getObjects(final int n)
'''
pass
def getObject():
'''public IlvGraphic getObject(final String key)
public IlvGraphic getObject(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)
public IlvGraphic getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
public IlvGraphic getObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)
'''
pass
def setObjectName():
'''public boolean setObjectName(final IlvGraphic value, final String s)
'''
pass
def getObjectName():
'''public String getObjectName(final IlvGraphic ilvGraphic)
'''
pass
def applyToObject():
'''public void applyToObject(final IlvGraphic ilvGraphic, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
'''
pass
def applyToObjects():
'''public void applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
public void applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
public void applyToObjects(final IlvGraphicVector ilvGraphicVector, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)
public void applyToObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final IlvApplyObjects ilvApplyObjects, final Object o, final boolean b)
'''
pass
def moveObject():
'''public void moveObject(final IlvGraphic ilvGraphic, final float n, final float n2, final boolean b)
'''
pass
def reshapeObject():
'''public void reshapeObject(final IlvGraphic ilvGraphic, final IlvRect ilvRect, final boolean b)
'''
pass
def addLayer():
'''public void addLayer(final IlvManagerLayer ilvManagerLayer, int n)
public void addLayer(final int n)
'''
pass
def removeLayer():
'''public void removeLayer(final int n, final boolean b)
'''
pass
def setOptimizedLayerThreshold():
'''public void setOptimizedLayerThreshold(final long r)
'''
pass
def getOptimizedLayerThreshold():
'''public long getOptimizedLayerThreshold()
'''
pass
def setNumberOfLayer():
'''public void setNumberOfLayer(int n)
'''
pass
def getLayersCount():
'''public int getLayersCount()
'''
pass
def getLayer():
'''public final int getLayer(final IlvGraphic obj)
public int getLayer(final String anObject)
'''
pass
def swapLayers():
'''public void swapLayers(final int n, final int n2, final boolean b)
'''
pass
def addManagerLayerListener():
'''public void addManagerLayerListener(final ManagerLayerListener l)
'''
pass
def removeManagerLayerListener():
'''public void removeManagerLayerListener(final ManagerLayerListener l)
'''
pass
def setLayerName():
'''public void setLayerName(final int n, final String name)
'''
pass
def getLayerName():
'''public String getLayerName(final int n)
'''
pass
def getManagerLayer():
'''public IlvManagerLayer getManagerLayer(final String anObject)
public final IlvManagerLayer getManagerLayer(final int n)
public final IlvManagerLayer getManagerLayer(final IlvGraphic obj)
'''
pass
def setLayer():
'''public void setLayer(final IlvGraphic obj, final int n, final boolean b)
'''
pass
def setVisible():
'''public void setVisible(final int n, final boolean b, final boolean b2)
public void setVisible(final IlvManagerView ilvManagerView, final int n, final boolean b, final boolean b2)
public void setVisible(final IlvGraphic ilvGraphic, final boolean visible, final boolean b)
'''
pass
def isVisible():
'''public boolean isVisible(final int n)
public boolean isVisible(final IlvManagerView ilvManagerView, final int n)
public boolean isVisible(final IlvGraphic ilvGraphic)
public boolean isVisible(final IlvGraphic ilvGraphic, final IlvManagerView ilvManagerView)
'''
pass
def setInsertionAdjusting():
'''public void setInsertionAdjusting(final boolean b)
'''
pass
def isInsertionAdjusting():
'''public boolean isInsertionAdjusting()
'''
pass
def addManagerContentChangedListener():
'''public void addManagerContentChangedListener(final ManagerContentChangedListener l)
'''
pass
def removeManagerContentChangedListener():
'''public void removeManagerContentChangedListener(final ManagerContentChangedListener l)
'''
pass
def addManagerTreeContentChangedListener():
'''public void addManagerTreeContentChangedListener(final ManagerContentChangedListener l)
'''
pass
def removeManagerTreeContentChangedListener():
'''public void removeManagerTreeContentChangedListener(final ManagerContentChangedListener l)
'''
pass
def setContentsAdjusting():
'''public void setContentsAdjusting(final boolean b)
public void setContentsAdjusting(final boolean contentsAdjusting, final boolean b)
'''
pass
def isContentsAdjusting():
'''public final boolean isContentsAdjusting()
'''
pass
def getViews():
'''public final Enumeration getViews()
'''
pass
def addManagerViewsListener():
'''public void addManagerViewsListener(final ManagerViewsChangedListener l)
'''
pass
def removeManagerViewsListener():
'''public void removeManagerViewsListener(final ManagerViewsChangedListener l)
'''
pass
def addManagerViewsHierarchyListener():
'''public void addManagerViewsHierarchyListener(final ManagerViewsChangedListener l)
'''
pass
def removeManagerViewsHierarchyListener():
'''public void removeManagerViewsHierarchyListener(final ManagerViewsChangedListener l)
'''
pass
def enableManagerViewsHierarchyEventForwarding():
'''public void enableManagerViewsHierarchyEventForwarding()
'''
pass
def needsManagerViewsHierarchyEvent():
'''public boolean needsManagerViewsHierarchyEvent()
'''
pass
def fireManagerViewsHierarchyEvent():
'''public void fireManagerViewsHierarchyEvent(final ManagerViewsChangedEvent managerViewsChangedEvent)
'''
pass
def reDrawObj():
'''public void reDrawObj(final IlvGraphic ilvGraphic)
'''
pass
def reDrawRegion():
'''public void reDrawRegion(final IlvRegion ilvRegion)
'''
pass
def invalidateRegion():
'''public void invalidateRegion(final IlvGraphic ilvGraphic)
public void invalidateRegion(final IlvRect ilvRect)
public void invalidateRegion(final IlvManagerView ilvManagerView, final IlvRect ilvRect)
'''
pass
def initReDraws():
'''public void initReDraws()
'''
pass
def isInvalidating():
'''public boolean isInvalidating()
'''
pass
def abortReDraws():
'''public void abortReDraws()
'''
pass
def reDrawViews():
'''public void reDrawViews()
'''
pass
def blinkingReDraw():
'''public void blinkingReDraw()
'''
pass
def reDraw():
'''public void reDraw()
'''
pass
def computeBBox():
'''public IlvRect computeBBox(final IlvTransformer ilvTransformer)
public IlvRect computeBBox(final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def draw():
'''public void draw(final Graphics graphics, final IlvManagerView ilvManagerView)
public void draw(final Graphics graphics, final IlvTransformer ilvTransformer)
'''
pass
def print():
'''public void print(final Graphics graphics, final IlvRect ilvRect, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def processEvent():
'''public boolean processEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
'''
pass
def getObjectInteractor():
'''public final IlvObjectInteractor getObjectInteractor(final IlvGraphic ilvGraphic)
'''
pass
def setObjectInteractor():
'''public final void setObjectInteractor(final IlvGraphic ilvGraphic, final IlvObjectInteractor objectInteractor)
'''
pass
def setHoverHighlightingImageOperation():
'''public void setHoverHighlightingImageOperation(final IlvHoverHighlightingImageOperation bq)
'''
pass
def getHoverHighlightingImageOperation():
'''public IlvHoverHighlightingImageOperation getHoverHighlightingImageOperation()
'''
pass
def setHoverHighlightingMode():
'''public void setHoverHighlightingMode(final int n)
'''
pass
def getHoverHighlightingMode():
'''public int getHoverHighlightingMode()
'''
pass
def shortCut():
'''public boolean shortCut(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
'''
pass
def processHoverHighlightingEvent():
'''public boolean processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
public boolean processHoverHighlightingEvent(final AWTEvent awtEvent, final IlvManagerView ilvManagerView, final IlvGraphic ilvGraphic)
'''
pass
def dispatchToObjects():
'''public boolean dispatchToObjects(final AWTEvent awtEvent, final IlvManagerView ilvManagerView)
'''
pass
def addAccelerator():
'''public void addAccelerator(final IlvAccelerator e)
'''
pass
def removeAccelerator():
'''public void removeAccelerator(final IlvAccelerator o)
'''
pass
def getAccelerators():
'''public IlvAccelerator[] getAccelerators()
'''
pass
def setAccelerators():
'''public void setAccelerators(final IlvAccelerator[] array)
'''
pass
def deleteAll():
'''public void deleteAll(final boolean b)
public void deleteAll(final int n, final boolean b)
'''
pass
def allowMoving():
'''public boolean allowMoving(final IlvGraphic ilvGraphic)
'''
pass
def isMovable():
'''public boolean isMovable(final IlvGraphic ilvGraphic)
'''
pass
def setMovable():
'''public void setMovable(final IlvGraphic ilvGraphic, final boolean movable)
'''
pass
def isEditable():
'''public boolean isEditable(final IlvGraphic ilvGraphic)
'''
pass
def setEditable():
'''public void setEditable(final IlvGraphic ilvGraphic, final boolean editable)
'''
pass
def isSelectable():
'''public boolean isSelectable(final IlvGraphic ilvGraphic)
public boolean isSelectable(final int n)
'''
pass
def objectIsSelectable():
'''public boolean objectIsSelectable(final IlvGraphic ilvGraphic)
'''
pass
def setSelectable():
'''public void setSelectable(final IlvGraphic ilvGraphic, final boolean selectable)
public void setSelectable(final int n, final boolean b)
'''
pass
def getAllObjects():
'''public IlvGraphicVector getAllObjects(final IlvPoint ilvPoint, final int n, final IlvManagerView ilvManagerView)
public IlvGraphicVector getAllObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b, final boolean b2)
'''
pass
def getCollapseExpandObject():
'''public IlvObjectWithSelection getCollapseExpandObject(final IlvPoint p4, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def getSelectableObject():
'''public IlvGraphic getSelectableObject(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def getAllSelectableObjects():
'''public IlvGraphicVector getAllSelectableObjects(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final IlvTransformer ilvTransformer, final boolean b, final boolean b2)
'''
pass
def getSelection():
'''public IlvSelection getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
public IlvSelection getSelection(final IlvPoint ilvPoint, final IlvManagerView ilvManagerView, final boolean b)
public final IlvSelection getSelection(final IlvGraphic ilvGraphic)
'''
pass
def isSelected():
'''public boolean isSelected(final IlvGraphic ilvGraphic)
'''
pass
def setSelected():
'''public void setSelected(final IlvGraphic ilvGraphic, final boolean b, final boolean b2)
public void setSelected(final IlvGraphic ilvGraphic, final IlvPoint ilvPoint, final IlvManagerView ilvManagerView)
'''
pass
def addManagerSelectionListener():
'''public void addManagerSelectionListener(final ManagerSelectionListener l)
'''
pass
def removeManagerSelectionListener():
'''public void removeManagerSelectionListener(final ManagerSelectionListener l)
'''
pass
def addManagerTreeSelectionListener():
'''public void addManagerTreeSelectionListener(final ManagerSelectionListener l)
'''
pass
def removeManagerTreeSelectionListener():
'''public void removeManagerTreeSelectionListener(final ManagerSelectionListener l)
'''
pass
def setSelectionEventSource():
'''public void setSelectionEventSource(final Object ac)
'''
pass
def setSelectionAdjusting():
'''public void setSelectionAdjusting(final boolean b)
'''
pass
def isSelectionAdjusting():
'''public boolean isSelectionAdjusting()
'''
pass
def selectAll():
'''public void selectAll(final IlvManagerView ilvManagerView, final boolean b)
public void selectAll(final boolean b)
public void selectAll(final boolean b, final boolean b2)
'''
pass
def deSelectAll():
'''public void deSelectAll(final boolean b)
public void deSelectAll(final boolean b, final boolean b2)
public void deSelectAll(final int n, final boolean b)
'''
pass
def getSelections():
'''public final IlvGraphicEnumeration getSelections()
'''
pass
def getSelectedObjects():
'''public final IlvGraphicEnumeration getSelectedObjects()
public final IlvGraphicEnumeration getSelectedObjects(final boolean b)
public final IlvGraphicEnumeration getSelectedObjects(final boolean b, final boolean b2)
'''
pass
def getSelectedObjectsCount():
'''public final int getSelectedObjectsCount()
public final int getSelectedObjectsCount(final boolean b)
public final int getSelectedObjectsCount(final boolean b, final boolean b2)
'''
pass
def setSelectionFactory():
'''public void setSelectionFactory(final IlvSelectionFactory ay)
'''
pass
def getSelectionFactory():
'''public IlvSelectionFactory getSelectionFactory()
'''
pass
def write():
'''public void write(final IlvOutputStream ilvOutputStream)
public void write(final OutputStream outputStream, final boolean b)
public void write(final OutputStream outputStream)
public void write(final String name, final boolean b)
public void write(final String s)
'''
pass
def writeIt():
'''public void writeIt(final IlvOutputStream ilvOutputStream)
'''
pass
def writePrefix():
'''public void writePrefix(final IlvOutputStream ilvOutputStream, final boolean b)
'''
pass
def writeSuffix():
'''public void writeSuffix(final IlvOutputStream ilvOutputStream, final boolean b)
'''
pass
def readPrefix():
'''public void readPrefix(final IlvInputStream ilvInputStream, final boolean b)
'''
pass
def readSuffix():
'''public void readSuffix(final IlvInputStream ilvInputStream, final boolean b)
'''
pass
def setFileName():
'''public void setFileName(final URL a9)
'''
pass
def getFileName():
'''public URL getFileName()
'''
pass
def read():
'''public boolean read(final InputStream inputStream)
public boolean read(final String name)
public boolean read(final URL az)
'''
pass
def setStreamFactory():
'''public void setStreamFactory(final IlvManagerStreamFactory a7)
'''
pass
def getStreamFactory():
'''public IlvManagerStreamFactory getStreamFactory()
'''
pass
def beforeTransform():
'''public final void beforeTransform(final IlvGraphic ilvGraphic, final boolean b, final boolean b2, final boolean b3)
'''
pass
def afterTransform():
'''public final void afterTransform(final IlvGraphic ilvGraphic, final boolean b, final boolean b2, final boolean b3, final boolean b4)
'''
pass
def check():
'''public void check(final boolean b)
'''
pass
def getSelectedMovingObjects():
'''public IlvGraphicEnumeration getSelectedMovingObjects(final boolean[] array)
'''
pass
def translateSelections():
'''public void translateSelections(final float n, final float n2, final IlvManagerView ilvManagerView)
'''
pass
def translateObjects():
'''public void translateObjects(final IlvGraphicEnumeration ilvGraphicEnumeration, final float n, final float n2, final IlvTransformer ilvTransformer)
'''
pass
def deleteSelections():
'''public void deleteSelections(final boolean b)
public void deleteSelections(final boolean b, final boolean b2)
'''
pass
def duplicateSelections():
'''public void duplicateSelections(final int n, final int n2)
public void duplicateSelections(final float n, final float n2, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def map():
'''public void map(final IlvApplyObject ilvApplyObject, final Object o)
public void map(final IlvApplyObject ilvApplyObject, final Object o, final boolean b)
'''
pass
def mapIntersects():
'''public void mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
public void mapIntersects(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def mapInside():
'''public void mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer)
public void mapInside(final IlvApplyObject ilvApplyObject, final Object o, final IlvRect ilvRect, final IlvTransformer ilvTransformer, final boolean b)
'''
pass
def pasteSelection():
'''public IlvGraphicEnumeration pasteSelection(final IlvPoint ilvPoint, final boolean b)
'''
pass
def copySelection():
'''public void copySelection()
'''
pass
def lostOwnership():
'''public void lostOwnership(final Clipboard clipboard, final Transferable transferable)
'''
pass
def removeProperty():
'''public boolean removeProperty(final String key)
'''
pass
def setProperty():
'''public void setProperty(final String key, final Object value)
'''
pass
def replaceProperty():
'''public boolean replaceProperty(final String key, final Object value)
'''
pass
def getProperty():
'''public Object getProperty(final String key)
'''
pass
def hasProperty():
'''public boolean hasProperty(final String key, final Object o)
'''
pass
def getManagers():
'''public final IlvGraphicEnumeration getManagers()
public final IlvGraphicEnumeration getManagers(final int n)
'''
pass
def getManagersCount():
'''public final int getManagersCount()
public final int getManagersCount(final int n)
'''
pass
def zoomable():
'''public boolean zoomable()
'''
pass
def applyTransform():
'''public void applyTransform(final IlvTransformer ilvTransformer)
'''
pass
def moveResize():
'''public void moveResize(IlvRect obj)
'''
pass
def setGraphicBag():
'''public void setGraphicBag(final IlvGraphicBag graphicBag)
'''
pass
def setCollapsed():
'''public final void setCollapsed(final boolean bh)
'''
pass
def isCollapsed():
'''public final boolean isCollapsed()
'''
pass
def isCollapsible():
'''public final boolean isCollapsible()
'''
pass
def setCollapsedGraphic():
'''public final void setCollapsedGraphic(final IlvGraphic bi)
'''
pass
def getCollapsedGraphic():
'''public final IlvGraphic getCollapsedGraphic()
'''
pass
def isAutoLabelForCollapsedGraphic():
'''public final boolean isAutoLabelForCollapsedGraphic()
'''
pass
def setAutoLabelForCollapsedGraphic():
'''public final void setAutoLabelForCollapsedGraphic(final boolean bj)
'''
pass
def addManagerExpansionListener():
'''public void addManagerExpansionListener(final ManagerExpansionListener l)
'''
pass
def removeManagerExpansionListener():
'''public void removeManagerExpansionListener(final ManagerExpansionListener l)
'''
pass
def addGraphicBagHierarchyListener():
'''public void addGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)
'''
pass
def removeGraphicBagHierarchyListener():
'''public void removeGraphicBagHierarchyListener(final GraphicBagHierarchyListener l)
'''
pass
def enableGraphicBagHierarchyEventForwarding():
'''public void enableGraphicBagHierarchyEventForwarding()
'''
pass
def needsGraphicBagHierarchyEvent():
'''public boolean needsGraphicBagHierarchyEvent()
'''
pass
def fireGraphicBagHierarchyEvent():
'''public void fireGraphicBagHierarchyEvent(final GraphicBagHierarchyEvent graphicBagHierarchyEvent)
'''
pass
def setSelectionInvariantSubManagerBounds():
'''public void setSelectionInvariantSubManagerBounds(final boolean b)
'''
pass
def isSelectionInvariantSubManagerBounds():
'''public boolean isSelectionInvariantSubManagerBounds()
'''
pass
def boundingBox():
'''public IlvRect boundingBox(final IlvTransformer ilvTransformer)
'''
pass
def copy():
'''public IlvGraphic copy()
'''
pass
def getFrame():
'''public IlvManagerFrame getFrame()
'''
pass
def setFrame():
'''public void setFrame(final IlvManagerFrame bg)
'''
pass
def getParent():
'''public final IlvManager getParent()
'''
pass
def getTransformer():
'''public IlvTransformer getTransformer()
public IlvTransformer getTransformer()
'''
pass
def setTransformer():
'''public final void setTransformer(final IlvTransformer ilvTransformer)
'''
pass
def isKeepingAspectRatio():
'''public final boolean isKeepingAspectRatio()
'''
pass
def setKeepingAspectRatio():
'''public final void setKeepingAspectRatio(final boolean b)
'''
pass
def getDrawingTransformer():
'''public IlvTransformer getDrawingTransformer(final IlvManagerView ilvManagerView)
'''
pass
def getTopLevelTransformer():
'''public IlvTransformer getTopLevelTransformer()
'''
pass
def getTreeLock():
'''public final Object getTreeLock()
'''
pass
def getULocale():
'''public ULocale getULocale()
'''
pass
def getStoredULocale():
'''public final ULocale getStoredULocale()
'''
pass
def setULocale():
'''public void setULocale(final ULocale uLocale)
public void setULocale(final ULocale bs, final boolean b)
'''
pass
def isLocaleSensitive():
'''public boolean isLocaleSensitive()
'''
pass
def getComponentOrientation():
'''public ComponentOrientation getComponentOrientation()
'''
pass
def getStoredComponentOrientation():
'''public final ComponentOrientation getStoredComponentOrientation()
'''
pass
def setComponentOrientation():
'''public void setComponentOrientation(final ComponentOrientation componentOrientation)
public void setComponentOrientation(final ComponentOrientation bt, final boolean b)
'''
pass
def isComponentOrientationSensitive():
'''public boolean isComponentOrientationSensitive()
'''
pass
def isBaseTextDirectionSensitive():
'''public boolean isBaseTextDirectionSensitive()
'''
pass
def containsFrame():
'''public boolean containsFrame(final IlvPoint ilvPoint, final IlvPoint ilvPoint2, final IlvTransformer ilvTransformer)
'''
pass
def contains():
'''public boolean contains(final IlvPoint ilvPoint, final IlvPoint p3, final IlvTransformer ilvTransformer)
'''
pass
def getIntersectionWithOutline():
'''public IlvPoint getIntersectionWithOutline(final IlvPoint ilvPoint, final IlvPoint obj, final IlvTransformer ilvTransformer)
'''
pass
def setSizeLimitToDrawSubmanagerContents():
'''public void setSizeLimitToDrawSubmanagerContents(final float bm)
'''
pass
def getSizeLimitToDrawSubmanagerContents():
'''public float getSizeLimitToDrawSubmanagerContents()
'''
pass
def componentOrientationChanged():
'''public void componentOrientationChanged(final ComponentOrientation componentOrientation, final ComponentOrientation componentOrientation2)
'''
pass
def localeChanged():
'''public void localeChanged(final ULocale uLocale, final ULocale uLocale2)
'''
pass
def baseTextDirectionChanged():
'''public void baseTextDirectionChanged(final int d, final int baseTextDirection)
'''
pass
def setBaseTextDirection():
'''public void setBaseTextDirection(final int n, final boolean b)
'''
pass
def run():
'''public void run()
'''
pass
def repaint():
'''public void repaint(final IlvRect ilvRect)
'''
pass
def getGraphics():
'''public Graphics getGraphics()
'''
pass
def getGrid():
'''public IlvGrid getGrid()
'''
pass
def setCursor():
'''public void setCursor(final Cursor cursor)
'''
pass
def getCursor():
'''public Cursor getCursor()
'''
pass
def isCursorSet():
'''public boolean isCursorSet()
'''
pass
def ensureVisible():
'''public void ensureVisible(final IlvPoint ilvPoint)
'''
pass
def snapToGrid():
'''public void snapToGrid(final IlvPoint ilvPoint)
'''
pass
def getDefaultXORColor():
'''public Color getDefaultXORColor()
'''
pass
def getDefaultGhostColor():
'''public Color getDefaultGhostColor()
'''
pass
def hasMoreElements():
'''public final boolean hasMoreElements()
public final boolean hasMoreElements()
public final boolean hasMoreElements()
public final boolean hasMoreElements()
public boolean hasMoreElements()
'''
pass
def nextElement():
'''public final IlvGraphic nextElement()
public final IlvGraphic nextElement()
public final IlvGraphic nextElement()
public final IlvGraphic nextElement()
public IlvGraphic nextElement()
'''
pass
def init():
'''public final void init(final float b, final float c, final IlvTransformer d)
'''
pass
def apply():
'''public final void apply(final IlvGraphic ilvGraphic, final Object o)
'''
pass
def translateObj():
'''public final void translateObj(final IlvGraphic ilvGraphic, final boolean b)
'''
pass
