def ():
    '''returns IlvDiagrammer\n\n
    ()\n
    (final IlvSDMView ilvSDMView)\n
    '''
def getDefaultStyleSheet():
    '''returns URL\n\n
    getDefaultStyleSheet()\n
    '''
def keyPressed():
    '''returns None\n\n
    keyPressed(final KeyEvent keyEvent)\n
    '''
def setScrollable():
    '''returns None\n\n
    setScrollable(final boolean g)\n
    '''
def isScrollable():
    '''returns boolean\n\n
    isScrollable()\n
    '''
def setStyleSheet():
    '''returns None\n\n
    setStyleSheet(final URL url)\n
    '''
def getStyleSheet():
    '''returns URL\n\n
    getStyleSheet()\n
    '''
def addStyleSheet():
    '''returns None\n\n
    addStyleSheet(final URL url)\n
    '''
def removeStyleSheet():
    '''returns None\n\n
    removeStyleSheet(final URL url)\n
    '''
def getStyleSheets():
    '''returns URL[]\n\n
    getStyleSheets()\n
    '''
def isStyleApplicationComponents():
    '''returns boolean\n\n
    isStyleApplicationComponents()\n
    '''
def setStyleApplicationComponents():
    '''returns None\n\n
    setStyleApplicationComponents(final boolean v)\n
    '''
def getDataFile():
    '''returns URL\n\n
    getDataFile()\n
    '''
def writeProjectFile():
    '''returns None\n\n
    writeProjectFile(final URL url)\n
    '''
def writeDataFile():
    '''returns None\n\n
    writeDataFile(final URL d)\n
    writeDataFile(final String s)\n
    '''
def writeData():
    '''returns None\n\n
    writeData()\n
    '''
def setDataSource():
    '''returns None\n\n
    setDataSource(final IlvDiagrammerDataSource ilvDiagrammerDataSource)\n
    '''
def getDataSource():
    '''returns IlvDiagrammerDataSource\n\n
    getDataSource()\n
    '''
def getProject():
    '''returns IlvDiagrammerProject\n\n
    getProject()\n
    '''
def setProject():
    '''returns None\n\n
    setProject(final IlvDiagrammerProject ilvDiagrammerProject)\n
    setProject(final IlvDiagrammerProject ilvDiagrammerProject, final boolean b)\n
    '''
def assignProject():
    '''returns None\n\n
    assignProject(final IlvDiagrammerProject f)\n
    '''
def refresh():
    '''returns None\n\n
    refresh()\n
    '''
def createNode():
    '''returns Object\n\n
    createNode(final String s)\n
    '''
def createLink():
    '''returns Object\n\n
    createLink(final String s, final Object o, final Object o2)\n
    '''
def getTag():
    '''returns String\n\n
    getTag(final Object o)\n
    '''
def getID():
    '''returns String\n\n
    getID(final Object o)\n
    '''
def setID():
    '''returns None\n\n
    setID(final Object o, final String s)\n
    '''
def getObject():
    '''returns Object\n\n
    getObject(final String s)\n
    '''
def addObject():
    '''returns None\n\n
    addObject(final Object o, final Object o2)\n
    '''
def removeObject():
    '''returns None\n\n
    removeObject(final Object o)\n
    '''
def setObjectProperty():
    '''returns None\n\n
    setObjectProperty(final Object o, final String s, final Object o2)\n
    '''
def getObjectProperty():
    '''returns Object\n\n
    getObjectProperty(final Object o, final String s)\n
    '''
def getObjects():
    '''returns Iterator\n\n
    getObjects()\n
    '''
def getAllObjects():
    '''returns Iterator\n\n
    getAllObjects()\n
    '''
def getChildren():
    '''returns Iterator\n\n
    getChildren(final Object o)\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
    '''
def getEngine():
    '''returns IlvSDMEngine\n\n
    getEngine()\n
    '''
def getView():
    '''returns IlvSDMView\n\n
    getView()\n
    '''
def isLink():
    '''returns boolean\n\n
    isLink(final Object o)\n
    '''
def getSourceNode():
    '''returns Object\n\n
    getSourceNode(final Object o)\n
    '''
def setSourceNode():
    '''returns None\n\n
    setSourceNode(final Object o, final Object o2)\n
    '''
def getTargetNode():
    '''returns Object\n\n
    getTargetNode(final Object o)\n
    '''
def setTargetNode():
    '''returns None\n\n
    setTargetNode(final Object o, final Object o2)\n
    '''
def setAdjusting():
    '''returns None\n\n
    setAdjusting(final boolean adjusting)\n
    '''
def clearAdjusting():
    '''returns None\n\n
    clearAdjusting()\n
    '''
def isAdjusting():
    '''returns boolean\n\n
    isAdjusting()\n
    '''
def setSelectMode():
    '''returns None\n\n
    setSelectMode(final boolean b)\n
    '''
def isSelectMode():
    '''returns boolean\n\n
    isSelectMode()\n
    '''
def getSelectedObjects():
    '''returns Iterator\n\n
    getSelectedObjects()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final Object o, final boolean b)\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final Object o)\n
    '''
def deselectAll():
    '''returns None\n\n
    deselectAll()\n
    '''
def setAllSelectedObjects():
    '''returns None\n\n
    setAllSelectedObjects(final Collection allSelectedObjects)\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll()\n
    '''
def canSelect():
    '''returns boolean\n\n
    canSelect()\n
    '''
def scrollToObject():
    '''returns None\n\n
    scrollToObject(final Object o)\n
    '''
def setEditingAllowed():
    '''returns None\n\n
    setEditingAllowed(final boolean b)\n
    '''
def isEditingAllowed():
    '''returns boolean\n\n
    isEditingAllowed()\n
    '''
def isEditable():
    '''returns boolean\n\n
    isEditable()\n
    '''
def isResizingAllowed():
    '''returns boolean\n\n
    isResizingAllowed()\n
    '''
def setResizingAllowed():
    '''returns None\n\n
    setResizingAllowed(final boolean resizingAllowed)\n
    '''
def cut():
    '''returns None\n\n
    cut()\n
    '''
def canEdit():
    '''returns boolean\n\n
    canEdit()\n
    '''
def copy():
    '''returns None\n\n
    copy()\n
    '''
def paste():
    '''returns None\n\n
    paste()\n
    '''
def canPaste():
    '''returns boolean\n\n
    canPaste()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def duplicate():
    '''returns None\n\n
    duplicate()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    '''
def canRedo():
    '''returns boolean\n\n
    canRedo()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean b)\n
    '''
def group():
    '''returns None\n\n
    group()\n
    '''
def createGroupParent():
    '''returns Object\n\n
    createGroupParent()\n
    '''
def setGroupParent():
    '''returns None\n\n
    setGroupParent(final IlvDiagrammer ilvDiagrammer, final Object o)\n
    '''
def canGroup():
    '''returns boolean\n\n
    canGroup()\n
    '''
def ungroup():
    '''returns None\n\n
    ungroup()\n
    '''
def canUngroup():
    '''returns boolean\n\n
    canUngroup()\n
    '''
def getZoomFactor():
    '''returns double\n\n
    getZoomFactor()\n
    '''
def setZoomFactor():
    '''returns None\n\n
    setZoomFactor(final double q)\n
    '''
def getMinimumZoom():
    '''returns double\n\n
    getMinimumZoom()\n
    '''
def setMinimumZoom():
    '''returns None\n\n
    setMinimumZoom(final double r)\n
    '''
def getMaximumZoom():
    '''returns double\n\n
    getMaximumZoom()\n
    '''
def setMaximumZoom():
    '''returns None\n\n
    setMaximumZoom(final double s)\n
    '''
def zoomIn():
    '''returns None\n\n
    zoomIn()\n
    '''
def canZoomIn():
    '''returns boolean\n\n
    canZoomIn()\n
    '''
def zoomOut():
    '''returns None\n\n
    zoomOut()\n
    '''
def canZoomOut():
    '''returns boolean\n\n
    canZoomOut()\n
    '''
def resetZoom():
    '''returns None\n\n
    resetZoom()\n
    '''
def canResetZoom():
    '''returns boolean\n\n
    canResetZoom()\n
    '''
def setZoomMode():
    '''returns None\n\n
    setZoomMode(final boolean b)\n
    '''
def isZoomMode():
    '''returns boolean\n\n
    isZoomMode()\n
    '''
def setPanMode():
    '''returns None\n\n
    setPanMode(final boolean b)\n
    '''
def isPanMode():
    '''returns boolean\n\n
    isPanMode()\n
    '''
def fitToContents():
    '''returns None\n\n
    fitToContents()\n
    fitToContents(final boolean b)\n
    '''
def setEditLabelMode():
    '''returns None\n\n
    setEditLabelMode(final boolean b)\n
    '''
def isEditLabelMode():
    '''returns boolean\n\n
    isEditLabelMode()\n
    '''
def isAutoEditLabel():
    '''returns boolean\n\n
    isAutoEditLabel()\n
    '''
def setAutoEditLabel():
    '''returns None\n\n
    setAutoEditLabel(final boolean m)\n
    '''
def setAutomaticNodeLayout():
    '''returns None\n\n
    setAutomaticNodeLayout(final boolean nodeLayoutEnabled)\n
    '''
def isAutomaticNodeLayout():
    '''returns boolean\n\n
    isAutomaticNodeLayout()\n
    '''
def layoutAllNodes():
    '''returns None\n\n
    layoutAllNodes()\n
    '''
def layoutSelectedNodes():
    '''returns None\n\n
    layoutSelectedNodes()\n
    '''
def isNodeLayoutAvailable():
    '''returns boolean\n\n
    isNodeLayoutAvailable()\n
    '''
def setAutomaticLinkLayout():
    '''returns None\n\n
    setAutomaticLinkLayout(final boolean linkLayoutEnabled)\n
    '''
def isAutomaticLinkLayout():
    '''returns boolean\n\n
    isAutomaticLinkLayout()\n
    '''
def layoutLinks():
    '''returns None\n\n
    layoutLinks()\n
    '''
def isLinkLayoutAvailable():
    '''returns boolean\n\n
    isLinkLayoutAvailable()\n
    '''
def setAutomaticLabelLayout():
    '''returns None\n\n
    setAutomaticLabelLayout(final boolean labelLayoutEnabled)\n
    '''
def isAutomaticLabelLayout():
    '''returns boolean\n\n
    isAutomaticLabelLayout()\n
    '''
def layoutLabels():
    '''returns None\n\n
    layoutLabels()\n
    '''
def isLabelLayoutAvailable():
    '''returns boolean\n\n
    isLabelLayoutAvailable()\n
    '''
def getPrintingController():
    '''returns IlvManagerPrintingController\n\n
    getPrintingController()\n
    '''
def setPrintingController():
    '''returns None\n\n
    setPrintingController(final IlvManagerPrintingController x)\n
    '''
def pageSetup():
    '''returns None\n\n
    pageSetup()\n
    '''
def printPreview():
    '''returns None\n\n
    printPreview()\n
    '''
def setPrintArea():
    '''returns None\n\n
    setPrintArea()\n
    '''
def clearPrintArea():
    '''returns None\n\n
    clearPrintArea()\n
    '''
def print():
    '''returns None\n\n
    print(final boolean b, final boolean b2, final PrinterExceptionHandler printerExceptionHandler)\n
    '''
def printToBitmap():
    '''returns None\n\n
    printToBitmap(final File file)\n
    '''
def hasFrameOrDialogAncestor():
    '''returns boolean\n\n
    hasFrameOrDialogAncestor()\n
    '''
def canPrint():
    '''returns boolean\n\n
    canPrint()\n
    '''
def setPalette():
    '''returns None\n\n
    setPalette(final IlvDiagrammer t)\n
    '''
def getPalette():
    '''returns IlvDiagrammer\n\n
    getPalette()\n
    '''
def isStickyModes():
    '''returns boolean\n\n
    isStickyModes()\n
    '''
def setStickyModes():
    '''returns None\n\n
    setStickyModes(final boolean b)\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n)\n
    setBaseTextDirection(final int n, final boolean b)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def getSelectInteractor():
    '''returns IlvSelectInteractor\n\n
    getSelectInteractor()\n
    '''
def setSelectInteractor():
    '''returns None\n\n
    setSelectInteractor(final IlvSelectInteractor i)\n
    '''
def getZoomInteractor():
    '''returns IlvZoomViewInteractor\n\n
    getZoomInteractor()\n
    '''
def setZoomInteractor():
    '''returns None\n\n
    setZoomInteractor(final IlvZoomViewInteractor j)\n
    '''
def getPanInteractor():
    '''returns IlvPanInteractor\n\n
    getPanInteractor()\n
    '''
def setPanInteractor():
    '''returns None\n\n
    setPanInteractor(final IlvPanInteractor k)\n
    '''
def getEditLabelInteractor():
    '''returns IlvEditSDMLabelInteractor\n\n
    getEditLabelInteractor()\n
    '''
def setEditLabelInteractor():
    '''returns None\n\n
    setEditLabelInteractor(final IlvEditSDMLabelInteractor l)\n
    '''
def isGridVisible():
    '''returns boolean\n\n
    isGridVisible()\n
    '''
def setGridVisible():
    '''returns None\n\n
    setGridVisible(final boolean b)\n
    '''
def getGrid():
    '''returns IlvGrid\n\n
    getGrid()\n
    '''
def setGrid():
    '''returns None\n\n
    setGrid(final IlvGrid y)\n
    '''
def getUndoManager():
    '''returns IlvSDMUndoManager\n\n
    getUndoManager()\n
    '''
def canAlign():
    '''returns boolean\n\n
    canAlign()\n
    '''
def canDistribute():
    '''returns boolean\n\n
    canDistribute()\n
    '''
def alignLeft():
    '''returns None\n\n
    alignLeft()\n
    '''
def alignRight():
    '''returns None\n\n
    alignRight()\n
    '''
def alignTop():
    '''returns None\n\n
    alignTop()\n
    '''
def alignBottom():
    '''returns None\n\n
    alignBottom()\n
    '''
def alignVerticalCenter():
    '''returns None\n\n
    alignVerticalCenter()\n
    '''
def alignHorizontalCenter():
    '''returns None\n\n
    alignHorizontalCenter()\n
    '''
def distributeHorizontally():
    '''returns None\n\n
    distributeHorizontally()\n
    '''
def distributeVertically():
    '''returns None\n\n
    distributeVertically()\n
    '''
def processServerAction():
    '''returns boolean\n\n
    processServerAction(final int n, final int n2)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
