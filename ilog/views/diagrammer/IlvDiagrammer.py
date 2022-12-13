def IlvDiagrammer():
'''public IlvDiagrammer()
public IlvDiagrammer(final IlvSDMView ilvSDMView)
'''
pass
def getDefaultStyleSheet():
'''public URL getDefaultStyleSheet()
'''
pass
def keyPressed():
'''public void keyPressed(final KeyEvent keyEvent)
'''
pass
def setScrollable():
'''public void setScrollable(final boolean g)
'''
pass
def isScrollable():
'''public boolean isScrollable()
'''
pass
def setStyleSheet():
'''public void setStyleSheet(final URL url)
'''
pass
def getStyleSheet():
'''public URL getStyleSheet()
'''
pass
def addStyleSheet():
'''public void addStyleSheet(final URL url)
'''
pass
def removeStyleSheet():
'''public void removeStyleSheet(final URL url)
'''
pass
def getStyleSheets():
'''public URL[] getStyleSheets()
'''
pass
def isStyleApplicationComponents():
'''public boolean isStyleApplicationComponents()
'''
pass
def setStyleApplicationComponents():
'''public void setStyleApplicationComponents(final boolean v)
'''
pass
def setDataFile():
'''public synchronized void setDataFile(final URL url)
'''
pass
def getDataFile():
'''public URL getDataFile()
'''
pass
def writeProjectFile():
'''public void writeProjectFile(final URL url)
'''
pass
def writeDataFile():
'''public void writeDataFile(final URL d)
public void writeDataFile(final String s)
'''
pass
def writeData():
'''public void writeData()
'''
pass
def setDataSource():
'''public void setDataSource(final IlvDiagrammerDataSource ilvDiagrammerDataSource)
'''
pass
def getDataSource():
'''public IlvDiagrammerDataSource getDataSource()
'''
pass
def getProject():
'''public IlvDiagrammerProject getProject()
'''
pass
def setProject():
'''public void setProject(final IlvDiagrammerProject ilvDiagrammerProject)
public void setProject(final IlvDiagrammerProject ilvDiagrammerProject, final boolean b)
'''
pass
def assignProject():
'''public void assignProject(final IlvDiagrammerProject f)
'''
pass
def refresh():
'''public void refresh()
'''
pass
def createNode():
'''public Object createNode(final String s)
'''
pass
def createLink():
'''public Object createLink(final String s, final Object o, final Object o2)
'''
pass
def getTag():
'''public String getTag(final Object o)
'''
pass
def getID():
'''public String getID(final Object o)
'''
pass
def setID():
'''public void setID(final Object o, final String s)
'''
pass
def getObject():
'''public Object getObject(final String s)
'''
pass
def addObject():
'''public void addObject(final Object o, final Object o2)
'''
pass
def removeObject():
'''public void removeObject(final Object o)
'''
pass
def setObjectProperty():
'''public void setObjectProperty(final Object o, final String s, final Object o2)
'''
pass
def getObjectProperty():
'''public Object getObjectProperty(final Object o, final String s)
'''
pass
def getObjects():
'''public Iterator getObjects()
'''
pass
def getAllObjects():
'''public Iterator getAllObjects()
'''
pass
def getChildren():
'''public Iterator getChildren(final Object o)
'''
pass
def getParent():
'''public Object getParent(final Object o)
'''
pass
def getEngine():
'''public IlvSDMEngine getEngine()
'''
pass
def getView():
'''public IlvSDMView getView()
'''
pass
def isLink():
'''public boolean isLink(final Object o)
'''
pass
def getSourceNode():
'''public Object getSourceNode(final Object o)
'''
pass
def setSourceNode():
'''public void setSourceNode(final Object o, final Object o2)
'''
pass
def getTargetNode():
'''public Object getTargetNode(final Object o)
'''
pass
def setTargetNode():
'''public void setTargetNode(final Object o, final Object o2)
'''
pass
def setAdjusting():
'''public void setAdjusting(final boolean adjusting)
'''
pass
def clearAdjusting():
'''public void clearAdjusting()
'''
pass
def isAdjusting():
'''public boolean isAdjusting()
'''
pass
def setSelectMode():
'''public void setSelectMode(final boolean b)
'''
pass
def isSelectMode():
'''public boolean isSelectMode()
'''
pass
def getSelectedObjects():
'''public Iterator getSelectedObjects()
'''
pass
def setSelected():
'''public void setSelected(final Object o, final boolean b)
'''
pass
def isSelected():
'''public boolean isSelected(final Object o)
'''
pass
def deselectAll():
'''public void deselectAll()
'''
pass
def setAllSelectedObjects():
'''public void setAllSelectedObjects(final Collection allSelectedObjects)
'''
pass
def selectAll():
'''public void selectAll()
'''
pass
def canSelect():
'''public boolean canSelect()
'''
pass
def scrollToObject():
'''public void scrollToObject(final Object o)
'''
pass
def setEditingAllowed():
'''public void setEditingAllowed(final boolean b)
'''
pass
def isEditingAllowed():
'''public boolean isEditingAllowed()
'''
pass
def isEditable():
'''public boolean isEditable()
'''
pass
def isResizingAllowed():
'''public boolean isResizingAllowed()
'''
pass
def setResizingAllowed():
'''public void setResizingAllowed(final boolean resizingAllowed)
'''
pass
def cut():
'''public void cut()
'''
pass
def canEdit():
'''public boolean canEdit()
'''
pass
def copy():
'''public void copy()
'''
pass
def paste():
'''public void paste()
'''
pass
def canPaste():
'''public boolean canPaste()
'''
pass
def delete():
'''public void delete()
'''
pass
def duplicate():
'''public void duplicate()
'''
pass
def undo():
'''public void undo()
'''
pass
def canUndo():
'''public boolean canUndo()
'''
pass
def redo():
'''public void redo()
'''
pass
def canRedo():
'''public boolean canRedo()
'''
pass
def isModified():
'''public boolean isModified()
'''
pass
def setModified():
'''public void setModified(final boolean b)
'''
pass
def group():
'''public void group()
'''
pass
def createGroupParent():
'''public Object createGroupParent()
'''
pass
def setGroupParent():
'''public void setGroupParent(final IlvDiagrammer ilvDiagrammer, final Object o)
'''
pass
def canGroup():
'''public boolean canGroup()
'''
pass
def ungroup():
'''public void ungroup()
'''
pass
def canUngroup():
'''public boolean canUngroup()
'''
pass
def getZoomFactor():
'''public double getZoomFactor()
'''
pass
def setZoomFactor():
'''public void setZoomFactor(final double q)
'''
pass
def getMinimumZoom():
'''public double getMinimumZoom()
'''
pass
def setMinimumZoom():
'''public void setMinimumZoom(final double r)
'''
pass
def getMaximumZoom():
'''public double getMaximumZoom()
'''
pass
def setMaximumZoom():
'''public void setMaximumZoom(final double s)
'''
pass
def zoomIn():
'''public void zoomIn()
'''
pass
def canZoomIn():
'''public boolean canZoomIn()
'''
pass
def zoomOut():
'''public void zoomOut()
'''
pass
def canZoomOut():
'''public boolean canZoomOut()
'''
pass
def resetZoom():
'''public void resetZoom()
'''
pass
def canResetZoom():
'''public boolean canResetZoom()
'''
pass
def setZoomMode():
'''public void setZoomMode(final boolean b)
'''
pass
def isZoomMode():
'''public boolean isZoomMode()
'''
pass
def setPanMode():
'''public void setPanMode(final boolean b)
'''
pass
def isPanMode():
'''public boolean isPanMode()
'''
pass
def fitToContents():
'''public void fitToContents()
public void fitToContents(final boolean b)
'''
pass
def setEditLabelMode():
'''public void setEditLabelMode(final boolean b)
'''
pass
def isEditLabelMode():
'''public boolean isEditLabelMode()
'''
pass
def isAutoEditLabel():
'''public boolean isAutoEditLabel()
'''
pass
def setAutoEditLabel():
'''public void setAutoEditLabel(final boolean m)
'''
pass
def setAutomaticNodeLayout():
'''public void setAutomaticNodeLayout(final boolean nodeLayoutEnabled)
'''
pass
def isAutomaticNodeLayout():
'''public boolean isAutomaticNodeLayout()
'''
pass
def layoutAllNodes():
'''public void layoutAllNodes()
'''
pass
def layoutSelectedNodes():
'''public void layoutSelectedNodes()
'''
pass
def isNodeLayoutAvailable():
'''public boolean isNodeLayoutAvailable()
'''
pass
def setAutomaticLinkLayout():
'''public void setAutomaticLinkLayout(final boolean linkLayoutEnabled)
'''
pass
def isAutomaticLinkLayout():
'''public boolean isAutomaticLinkLayout()
'''
pass
def layoutLinks():
'''public void layoutLinks()
'''
pass
def isLinkLayoutAvailable():
'''public boolean isLinkLayoutAvailable()
'''
pass
def setAutomaticLabelLayout():
'''public void setAutomaticLabelLayout(final boolean labelLayoutEnabled)
'''
pass
def isAutomaticLabelLayout():
'''public boolean isAutomaticLabelLayout()
'''
pass
def layoutLabels():
'''public void layoutLabels()
'''
pass
def isLabelLayoutAvailable():
'''public boolean isLabelLayoutAvailable()
'''
pass
def getPrintingController():
'''public IlvManagerPrintingController getPrintingController()
'''
pass
def setPrintingController():
'''public void setPrintingController(final IlvManagerPrintingController x)
'''
pass
def pageSetup():
'''public void pageSetup()
'''
pass
def printPreview():
'''public void printPreview()
'''
pass
def setPrintArea():
'''public void setPrintArea()
'''
pass
def clearPrintArea():
'''public void clearPrintArea()
'''
pass
def print():
'''public void print(final boolean b, final boolean b2, final PrinterExceptionHandler printerExceptionHandler)
'''
pass
def printToBitmap():
'''public void printToBitmap(final File file)
'''
pass
def hasFrameOrDialogAncestor():
'''public boolean hasFrameOrDialogAncestor()
'''
pass
def canPrint():
'''public boolean canPrint()
'''
pass
def setPalette():
'''public void setPalette(final IlvDiagrammer t)
'''
pass
def getPalette():
'''public IlvDiagrammer getPalette()
'''
pass
def isStickyModes():
'''public boolean isStickyModes()
'''
pass
def setStickyModes():
'''public void setStickyModes(final boolean b)
'''
pass
def setBaseTextDirection():
'''public void setBaseTextDirection(final int n)
public void setBaseTextDirection(final int n, final boolean b)
'''
pass
def getBaseTextDirection():
'''public int getBaseTextDirection()
'''
pass
def getSelectInteractor():
'''public IlvSelectInteractor getSelectInteractor()
'''
pass
def setSelectInteractor():
'''public void setSelectInteractor(final IlvSelectInteractor i)
'''
pass
def getZoomInteractor():
'''public IlvZoomViewInteractor getZoomInteractor()
'''
pass
def setZoomInteractor():
'''public void setZoomInteractor(final IlvZoomViewInteractor j)
'''
pass
def getPanInteractor():
'''public IlvPanInteractor getPanInteractor()
'''
pass
def setPanInteractor():
'''public void setPanInteractor(final IlvPanInteractor k)
'''
pass
def getEditLabelInteractor():
'''public IlvEditSDMLabelInteractor getEditLabelInteractor()
'''
pass
def setEditLabelInteractor():
'''public void setEditLabelInteractor(final IlvEditSDMLabelInteractor l)
'''
pass
def isGridVisible():
'''public boolean isGridVisible()
'''
pass
def setGridVisible():
'''public void setGridVisible(final boolean b)
'''
pass
def getGrid():
'''public IlvGrid getGrid()
'''
pass
def setGrid():
'''public void setGrid(final IlvGrid y)
'''
pass
def getUndoManager():
'''public IlvSDMUndoManager getUndoManager()
'''
pass
def canAlign():
'''public boolean canAlign()
'''
pass
def canDistribute():
'''public boolean canDistribute()
'''
pass
def alignLeft():
'''public void alignLeft()
'''
pass
def alignRight():
'''public void alignRight()
'''
pass
def alignTop():
'''public void alignTop()
'''
pass
def alignBottom():
'''public void alignBottom()
'''
pass
def alignVerticalCenter():
'''public void alignVerticalCenter()
'''
pass
def alignHorizontalCenter():
'''public void alignHorizontalCenter()
'''
pass
def distributeHorizontally():
'''public void distributeHorizontally()
'''
pass
def distributeVertically():
'''public void distributeVertically()
'''
pass
def getCurrentDiagrammer():
'''public static IlvDiagrammer getCurrentDiagrammer(final Component component)
'''
pass
def setCurrentDiagrammer():
'''public static void setCurrentDiagrammer(final Component component, final IlvDiagrammer ilvDiagrammer)
public static void setCurrentDiagrammer(final Component component, final IlvDiagrammer target, final boolean b)
'''
pass
def setAsRoot():
'''public static void setAsRoot(final Component component)
'''
pass
def setAutomaticCurrentDiagrammer():
'''public static void setAutomaticCurrentDiagrammer(final boolean enabled)
'''
pass
def isAutomaticCurrentDiagrammer():
'''public static boolean isAutomaticCurrentDiagrammer()
'''
pass
def processServerAction():
'''public boolean processServerAction(final int n, final int n2)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
