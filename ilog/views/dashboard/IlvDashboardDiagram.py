def ():
    '''returns IlvDashboardDiagram\n\n
    (final IlvDashboardContext b)\n
    (final IlvDashboardContext b, final IlvSDMView ilvSDMView)\n
    '''
def getContext():
    '''returns IlvDashboardContext\n\n
    getContext()\n
    '''
def setQuadtreeEnabled():
    '''returns None\n\n
    setQuadtreeEnabled(final boolean b)\n
    '''
def prepareForEditing():
    '''returns None\n\n
    prepareForEditing()\n
    '''
def objectRemoved():
    '''returns None\n\n
    objectRemoved(final SDMModelEvent sdmModelEvent)\n
    '''
def dataChanged():
    '''returns None\n\n
    dataChanged(final SDMModelEvent sdmModelEvent)\n
    '''
def canEdit():
    '''returns boolean\n\n
    canEdit()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def cut():
    '''returns None\n\n
    cut()\n
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
def duplicate():
    '''returns None\n\n
    duplicate()\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll()\n
    '''
def canSelect():
    '''returns boolean\n\n
    canSelect()\n
    '''
def canGroup():
    '''returns boolean\n\n
    canGroup()\n
    '''
def group():
    '''returns None\n\n
    group()\n
    '''
def canUngroup():
    '''returns boolean\n\n
    canUngroup()\n
    '''
def ungroup():
    '''returns None\n\n
    ungroup()\n
    '''
def canAlign():
    '''returns boolean\n\n
    canAlign()\n
    '''
def canDistribute():
    '''returns boolean\n\n
    canDistribute()\n
    '''
def alignBottom():
    '''returns None\n\n
    alignBottom()\n
    '''
def alignHorizontalCenter():
    '''returns None\n\n
    alignHorizontalCenter()\n
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
def alignVerticalCenter():
    '''returns None\n\n
    alignVerticalCenter()\n
    '''
def distributeHorizontally():
    '''returns None\n\n
    distributeHorizontally()\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o, final Object o2)\n
    compare(final Object o, final Object o2)\n
    '''
def distributeVertically():
    '''returns None\n\n
    distributeVertically()\n
    '''
def getBackgroundGraphics():
    '''returns IlvDashboardGraphicIterator\n\n
    getBackgroundGraphics()\n
    '''
def writeDataFile():
    '''returns None\n\n
    writeDataFile(final URL url)\n
    '''
def writeData():
    '''returns None\n\n
    writeData()\n
    '''
def writeDashboardFiles():
    '''returns None\n\n
    writeDashboardFiles()\n
    '''
def writeBackgroundFile():
    '''returns None\n\n
    writeBackgroundFile(final String name)\n
    '''
def writeBackground():
    '''returns None\n\n
    writeBackground(final OutputStream outputStream)\n
    '''
def readBackground():
    '''returns None\n\n
    readBackground(final InputStream inputStream)\n
    '''
def writeProjectFile():
    '''returns None\n\n
    writeProjectFile(final URL url)\n
    '''
def setProject():
    '''returns None\n\n
    setProject(final IlvDiagrammerProject project)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean b)\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def isBackgroundObject():
    '''returns boolean\n\n
    isBackgroundObject(final IlvGraphic ilvGraphic)\n
    '''
def addSymbol():
    '''returns None\n\n
    addSymbol(final IlvDashboardSymbol e)\n
    '''
def removeSymbol():
    '''returns None\n\n
    removeSymbol(final IlvDashboardSymbol ilvDashboardSymbol)\n
    '''
def getObjectSymbol():
    '''returns IlvDashboardSymbol\n\n
    getObjectSymbol(final Object o)\n
    '''
def getGraphicSymbol():
    '''returns IlvDashboardSymbol\n\n
    getGraphicSymbol(final IlvGraphic ilvGraphic)\n
    '''
def hasSelectedSymbols():
    '''returns boolean\n\n
    hasSelectedSymbols()\n
    '''
def getSelectedSymbols():
    '''returns IlvDashboardSymbolIterator\n\n
    getSelectedSymbols()\n
    '''
def getSymbol():
    '''returns IlvDashboardSymbol\n\n
    getSymbol(final String s)\n
    '''
def getURL():
    '''returns URL\n\n
    getURL()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final URL d)\n
    '''
def writeDashboard():
    '''returns None\n\n
    writeDashboard(final URL url)\n
    '''
def readDashboard():
    '''returns None\n\n
    readDashboard(final URL url)\n
    readDashboard(final Document document, final boolean b, final float n, final float n2)\n
    '''
def readBinary():
    '''returns None\n\n
    readBinary(final URL url)\n
    readBinary(final InputStream inputStream)\n
    '''
def writeBinary():
    '''returns None\n\n
    writeBinary(final URL url)\n
    writeBinary(final OutputStream outputStream)\n
    '''
def isUndoingEnabled():
    '''returns boolean\n\n
    isUndoingEnabled()\n
    '''
def setUndoingEnabled():
    '''returns None\n\n
    setUndoingEnabled(final boolean f)\n
    '''
def addUndoableEdit():
    '''returns None\n\n
    addUndoableEdit(final UndoableEdit undoableEdit)\n
    '''
def setCompoundEditMode():
    '''returns None\n\n
    setCompoundEditMode(final boolean compoundMode)\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    undo()\n
    '''
def canRedo():
    '''returns boolean\n\n
    canRedo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    redo()\n
    '''
def setSelectManager():
    '''returns None\n\n
    setSelectManager(final IlvDashboardKeySelectManager h)\n
    '''
def getSelectManager():
    '''returns IlvDashboardKeySelectManager\n\n
    getSelectManager()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def setEditingAllowed():
    '''returns None\n\n
    setEditingAllowed(final boolean editingAllowed)\n
    '''
def isContained():
    '''returns boolean\n\n
    isContained(final IlvDashboardSymbol o)\n
    '''
def getSymbolIndex():
    '''returns int\n\n
    getSymbolIndex(final IlvDashboardSymbol o)\n
    '''
def setSymbolIndex():
    '''returns None\n\n
    setSymbolIndex(final IlvDashboardSymbol element, final int index)\n
    '''
def addSymbolParameterListener():
    '''returns None\n\n
    addSymbolParameterListener(final IlvDashboardSymbolParameterListener e)\n
    '''
def removeSymbolParameterListener():
    '''returns None\n\n
    removeSymbolParameterListener(final IlvDashboardSymbolParameterListener o)\n
    '''
def fireSymbolParameterChanged():
    '''returns None\n\n
    fireSymbolParameterChanged(final IlvDashboardSymbol ilvDashboardSymbol, final IlvDashboardSymbol.Parameter parameter, final Object o, final Object o2, final String s, final String s2)\n
    '''
def getPrintingController():
    '''returns IlvManagerPrintingController\n\n
    getPrintingController()\n
    '''
def setBaseTextDirection():
    '''returns None\n\n
    setBaseTextDirection(final int n)\n
    '''
def getBaseTextDirection():
    '''returns int\n\n
    getBaseTextDirection()\n
    '''
def isLinkLayoutEnabled():
    '''returns boolean\n\n
    isLinkLayoutEnabled()\n
    '''
def setLinkLayoutEnabled():
    '''returns None\n\n
    setLinkLayoutEnabled(final boolean b)\n
    '''
def getSerializableProperties():
    '''returns ArrayList<Object>\n\n
    getSerializableProperties()\n
    '''
def setSerializableProperties():
    '''returns None\n\n
    setSerializableProperties(final ArrayList<Object> p)\n
    '''
def getSymbols():
    '''returns IlvDashboardSymbolIterator\n\n
    getSymbols()\n
    '''
def iterator():
    '''returns Iterator<IlvDashboardSymbol>\n\n
    iterator()\n
    '''
def addStyleSheet():
    '''returns None\n\n
    addStyleSheet(final URL url)\n
    '''
def contentsChanged():
    '''returns None\n\n
    contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)\n
    '''
def layerChanged():
    '''returns None\n\n
    layerChanged(final ManagerLayerEvent managerLayerEvent)\n
    '''
def layerInserted():
    '''returns None\n\n
    layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)\n
    '''
def layerMoved():
    '''returns None\n\n
    layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)\n
    '''
def layerRemoved():
    '''returns None\n\n
    layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)\n
    '''
def getDocumentBase():
    '''returns URL\n\n
    getDocumentBase()\n
    '''
def createInputStream():
    '''returns IlvInputStream\n\n
    createInputStream(final InputStream inputStream)\n
    '''
def createOutputStream():
    '''returns IlvOutputStream\n\n
    createOutputStream(final OutputStream outputStream)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns IlvDashboardSymbol\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
