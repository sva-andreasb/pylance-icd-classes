def IlvDiagrammer():
    '''public IlvDiagrammer()
    public IlvDiagrammer(final IlvSDMView ilvSDMView)
    '''
def getDefaultStyleSheet():
    '''public URL getDefaultStyleSheet()
    '''
def keyPressed():
    '''public void keyPressed(final KeyEvent keyEvent)
    '''
def setScrollable():
    '''public void setScrollable(final boolean g)
    '''
def isScrollable():
    '''public boolean isScrollable()
    '''
def setStyleSheet():
    '''public void setStyleSheet(final URL url)
    '''
def getStyleSheet():
    '''public URL getStyleSheet()
    '''
def addStyleSheet():
    '''public void addStyleSheet(final URL url)
    '''
def removeStyleSheet():
    '''public void removeStyleSheet(final URL url)
    '''
def getStyleSheets():
    '''public URL[] getStyleSheets()
    '''
def isStyleApplicationComponents():
    '''public boolean isStyleApplicationComponents()
    '''
def setStyleApplicationComponents():
    '''public void setStyleApplicationComponents(final boolean v)
    '''
def setDataFile():
    '''public synchronized void setDataFile(final URL url)
    '''
def getDataFile():
    '''public URL getDataFile()
    '''
def writeProjectFile():
    '''public void writeProjectFile(final URL url)
    '''
def writeDataFile():
    '''public void writeDataFile(final URL d)
    public void writeDataFile(final String s)
    '''
def writeData():
    '''public void writeData()
    '''
def setDataSource():
    '''public void setDataSource(final IlvDiagrammerDataSource ilvDiagrammerDataSource)
    '''
def getDataSource():
    '''public IlvDiagrammerDataSource getDataSource()
    '''
def getProject():
    '''public IlvDiagrammerProject getProject()
    '''
def setProject():
    '''public void setProject(final IlvDiagrammerProject ilvDiagrammerProject)
    public void setProject(final IlvDiagrammerProject ilvDiagrammerProject, final boolean b)
    '''
def assignProject():
    '''public void assignProject(final IlvDiagrammerProject f)
    '''
def refresh():
    '''public void refresh()
    '''
def createNode():
    '''public Object createNode(final String s)
    '''
def createLink():
    '''public Object createLink(final String s, final Object o, final Object o2)
    '''
def getTag():
    '''public String getTag(final Object o)
    '''
def getID():
    '''public String getID(final Object o)
    '''
def setID():
    '''public void setID(final Object o, final String s)
    '''
def getObject():
    '''public Object getObject(final String s)
    '''
def addObject():
    '''public void addObject(final Object o, final Object o2)
    '''
def removeObject():
    '''public void removeObject(final Object o)
    '''
def setObjectProperty():
    '''public void setObjectProperty(final Object o, final String s, final Object o2)
    '''
def getObjectProperty():
    '''public Object getObjectProperty(final Object o, final String s)
    '''
def getObjects():
    '''public Iterator getObjects()
    '''
def getAllObjects():
    '''public Iterator getAllObjects()
    '''
def getChildren():
    '''public Iterator getChildren(final Object o)
    '''
def getParent():
    '''public Object getParent(final Object o)
    '''
def getEngine():
    '''public IlvSDMEngine getEngine()
    '''
def getView():
    '''public IlvSDMView getView()
    '''
def isLink():
    '''public boolean isLink(final Object o)
    '''
def getSourceNode():
    '''public Object getSourceNode(final Object o)
    '''
def setSourceNode():
    '''public void setSourceNode(final Object o, final Object o2)
    '''
def getTargetNode():
    '''public Object getTargetNode(final Object o)
    '''
def setTargetNode():
    '''public void setTargetNode(final Object o, final Object o2)
    '''
def setAdjusting():
    '''public void setAdjusting(final boolean adjusting)
    '''
def clearAdjusting():
    '''public void clearAdjusting()
    '''
def isAdjusting():
    '''public boolean isAdjusting()
    '''
def setSelectMode():
    '''public void setSelectMode(final boolean b)
    '''
def isSelectMode():
    '''public boolean isSelectMode()
    '''
def getSelectedObjects():
    '''public Iterator getSelectedObjects()
    '''
def setSelected():
    '''public void setSelected(final Object o, final boolean b)
    '''
def isSelected():
    '''public boolean isSelected(final Object o)
    '''
def deselectAll():
    '''public void deselectAll()
    '''
def setAllSelectedObjects():
    '''public void setAllSelectedObjects(final Collection allSelectedObjects)
    '''
def selectAll():
    '''public void selectAll()
    '''
def canSelect():
    '''public boolean canSelect()
    '''
def scrollToObject():
    '''public void scrollToObject(final Object o)
    '''
def setEditingAllowed():
    '''public void setEditingAllowed(final boolean b)
    '''
def isEditingAllowed():
    '''public boolean isEditingAllowed()
    '''
def isEditable():
    '''public boolean isEditable()
    '''
def isResizingAllowed():
    '''public boolean isResizingAllowed()
    '''
def setResizingAllowed():
    '''public void setResizingAllowed(final boolean resizingAllowed)
    '''
def cut():
    '''public void cut()
    '''
def canEdit():
    '''public boolean canEdit()
    '''
def copy():
    '''public void copy()
    '''
def paste():
    '''public void paste()
    '''
def canPaste():
    '''public boolean canPaste()
    '''
def delete():
    '''public void delete()
    '''
def duplicate():
    '''public void duplicate()
    '''
def undo():
    '''public void undo()
    '''
def canUndo():
    '''public boolean canUndo()
    '''
def redo():
    '''public void redo()
    '''
def canRedo():
    '''public boolean canRedo()
    '''
def isModified():
    '''public boolean isModified()
    '''
def setModified():
    '''public void setModified(final boolean b)
    '''
def group():
    '''public void group()
    '''
def createGroupParent():
    '''public Object createGroupParent()
    '''
def setGroupParent():
    '''public void setGroupParent(final IlvDiagrammer ilvDiagrammer, final Object o)
    '''
def canGroup():
    '''public boolean canGroup()
    '''
def ungroup():
    '''public void ungroup()
    '''
def canUngroup():
    '''public boolean canUngroup()
    '''
def getZoomFactor():
    '''public double getZoomFactor()
    '''
def setZoomFactor():
    '''public void setZoomFactor(final double q)
    '''
def getMinimumZoom():
    '''public double getMinimumZoom()
    '''
def setMinimumZoom():
    '''public void setMinimumZoom(final double r)
    '''
def getMaximumZoom():
    '''public double getMaximumZoom()
    '''
def setMaximumZoom():
    '''public void setMaximumZoom(final double s)
    '''
def zoomIn():
    '''public void zoomIn()
    '''
def canZoomIn():
    '''public boolean canZoomIn()
    '''
def zoomOut():
    '''public void zoomOut()
    '''
def canZoomOut():
    '''public boolean canZoomOut()
    '''
def resetZoom():
    '''public void resetZoom()
    '''
def canResetZoom():
    '''public boolean canResetZoom()
    '''
def setZoomMode():
    '''public void setZoomMode(final boolean b)
    '''
def isZoomMode():
    '''public boolean isZoomMode()
    '''
def setPanMode():
    '''public void setPanMode(final boolean b)
    '''
def isPanMode():
    '''public boolean isPanMode()
    '''
def fitToContents():
    '''public void fitToContents()
    public void fitToContents(final boolean b)
    '''
def setEditLabelMode():
    '''public void setEditLabelMode(final boolean b)
    '''
def isEditLabelMode():
    '''public boolean isEditLabelMode()
    '''
def isAutoEditLabel():
    '''public boolean isAutoEditLabel()
    '''
def setAutoEditLabel():
    '''public void setAutoEditLabel(final boolean m)
    '''
def setAutomaticNodeLayout():
    '''public void setAutomaticNodeLayout(final boolean nodeLayoutEnabled)
    '''
def isAutomaticNodeLayout():
    '''public boolean isAutomaticNodeLayout()
    '''
def layoutAllNodes():
    '''public void layoutAllNodes()
    '''
def layoutSelectedNodes():
    '''public void layoutSelectedNodes()
    '''
def isNodeLayoutAvailable():
    '''public boolean isNodeLayoutAvailable()
    '''
def setAutomaticLinkLayout():
    '''public void setAutomaticLinkLayout(final boolean linkLayoutEnabled)
    '''
def isAutomaticLinkLayout():
    '''public boolean isAutomaticLinkLayout()
    '''
def layoutLinks():
    '''public void layoutLinks()
    '''
def isLinkLayoutAvailable():
    '''public boolean isLinkLayoutAvailable()
    '''
def setAutomaticLabelLayout():
    '''public void setAutomaticLabelLayout(final boolean labelLayoutEnabled)
    '''
def isAutomaticLabelLayout():
    '''public boolean isAutomaticLabelLayout()
    '''
def layoutLabels():
    '''public void layoutLabels()
    '''
def isLabelLayoutAvailable():
    '''public boolean isLabelLayoutAvailable()
    '''
def getPrintingController():
    '''public IlvManagerPrintingController getPrintingController()
    '''
def setPrintingController():
    '''public void setPrintingController(final IlvManagerPrintingController x)
    '''
def pageSetup():
    '''public void pageSetup()
    '''
def printPreview():
    '''public void printPreview()
    '''
def setPrintArea():
    '''public void setPrintArea()
    '''
def clearPrintArea():
    '''public void clearPrintArea()
    '''
def print():
    '''public void print(final boolean b, final boolean b2, final PrinterExceptionHandler printerExceptionHandler)
    '''
def printToBitmap():
    '''public void printToBitmap(final File file)
    '''
def hasFrameOrDialogAncestor():
    '''public boolean hasFrameOrDialogAncestor()
    '''
def canPrint():
    '''public boolean canPrint()
    '''
def setPalette():
    '''public void setPalette(final IlvDiagrammer t)
    '''
def getPalette():
    '''public IlvDiagrammer getPalette()
    '''
def isStickyModes():
    '''public boolean isStickyModes()
    '''
def setStickyModes():
    '''public void setStickyModes(final boolean b)
    '''
def setBaseTextDirection():
    '''public void setBaseTextDirection(final int n)
    public void setBaseTextDirection(final int n, final boolean b)
    '''
def getBaseTextDirection():
    '''public int getBaseTextDirection()
    '''
def getSelectInteractor():
    '''public IlvSelectInteractor getSelectInteractor()
    '''
def setSelectInteractor():
    '''public void setSelectInteractor(final IlvSelectInteractor i)
    '''
def getZoomInteractor():
    '''public IlvZoomViewInteractor getZoomInteractor()
    '''
def setZoomInteractor():
    '''public void setZoomInteractor(final IlvZoomViewInteractor j)
    '''
def getPanInteractor():
    '''public IlvPanInteractor getPanInteractor()
    '''
def setPanInteractor():
    '''public void setPanInteractor(final IlvPanInteractor k)
    '''
def getEditLabelInteractor():
    '''public IlvEditSDMLabelInteractor getEditLabelInteractor()
    '''
def setEditLabelInteractor():
    '''public void setEditLabelInteractor(final IlvEditSDMLabelInteractor l)
    '''
def isGridVisible():
    '''public boolean isGridVisible()
    '''
def setGridVisible():
    '''public void setGridVisible(final boolean b)
    '''
def getGrid():
    '''public IlvGrid getGrid()
    '''
def setGrid():
    '''public void setGrid(final IlvGrid y)
    '''
def getUndoManager():
    '''public IlvSDMUndoManager getUndoManager()
    '''
def canAlign():
    '''public boolean canAlign()
    '''
def canDistribute():
    '''public boolean canDistribute()
    '''
def alignLeft():
    '''public void alignLeft()
    '''
def alignRight():
    '''public void alignRight()
    '''
def alignTop():
    '''public void alignTop()
    '''
def alignBottom():
    '''public void alignBottom()
    '''
def alignVerticalCenter():
    '''public void alignVerticalCenter()
    '''
def alignHorizontalCenter():
    '''public void alignHorizontalCenter()
    '''
def distributeHorizontally():
    '''public void distributeHorizontally()
    '''
def distributeVertically():
    '''public void distributeVertically()
    '''
def getCurrentDiagrammer():
    '''public static IlvDiagrammer getCurrentDiagrammer(final Component component)
    '''
def setCurrentDiagrammer():
    '''public static void setCurrentDiagrammer(final Component component, final IlvDiagrammer ilvDiagrammer)
    public static void setCurrentDiagrammer(final Component component, final IlvDiagrammer target, final boolean b)
    '''
def setAsRoot():
    '''public static void setAsRoot(final Component component)
    '''
def setAutomaticCurrentDiagrammer():
    '''public static void setAutomaticCurrentDiagrammer(final boolean enabled)
    '''
def isAutomaticCurrentDiagrammer():
    '''public static boolean isAutomaticCurrentDiagrammer()
    '''
def processServerAction():
    '''public boolean processServerAction(final int n, final int n2)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
