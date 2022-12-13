def IlvDashboardDiagram():
    '''    public IlvDashboardDiagram(final IlvDashboardContext b)
    public IlvDashboardDiagram(final IlvDashboardContext b, final IlvSDMView ilvSDMView)
    '''
def getContext():
    '''    public IlvDashboardContext getContext()
    '''
def setQuadtreeEnabled():
    '''    public void setQuadtreeEnabled(final boolean b)
    '''
def prepareForEditing():
    '''    public void prepareForEditing()
    '''
def objectRemoved():
    '''    public void objectRemoved(final SDMModelEvent sdmModelEvent)
    '''
def dataChanged():
    '''    public void dataChanged(final SDMModelEvent sdmModelEvent)
    '''
def canEdit():
    '''    public boolean canEdit()
    '''
def delete():
    '''    public void delete()
    '''
def cut():
    '''    public void cut()
    '''
def copy():
    '''    public void copy()
    '''
def paste():
    '''    public void paste()
    '''
def canPaste():
    '''    public boolean canPaste()
    '''
def duplicate():
    '''    public void duplicate()
    '''
def selectAll():
    '''    public void selectAll()
    '''
def canSelect():
    '''    public boolean canSelect()
    '''
def canGroup():
    '''    public boolean canGroup()
    '''
def group():
    '''    public void group()
    '''
def canUngroup():
    '''    public boolean canUngroup()
    '''
def ungroup():
    '''    public void ungroup()
    '''
def canAlign():
    '''    public boolean canAlign()
    '''
def canDistribute():
    '''    public boolean canDistribute()
    '''
def alignBottom():
    '''    public void alignBottom()
    '''
def alignHorizontalCenter():
    '''    public void alignHorizontalCenter()
    '''
def alignLeft():
    '''    public void alignLeft()
    '''
def alignRight():
    '''    public void alignRight()
    '''
def alignTop():
    '''    public void alignTop()
    '''
def alignVerticalCenter():
    '''    public void alignVerticalCenter()
    '''
def distributeHorizontally():
    '''    public void distributeHorizontally()
    '''
def compare():
    '''    public int compare(final Object o, final Object o2)
    public int compare(final Object o, final Object o2)
    '''
def distributeVertically():
    '''    public void distributeVertically()
    '''
def getBackgroundGraphics():
    '''    public IlvDashboardGraphicIterator getBackgroundGraphics()
    '''
def writeDataFile():
    '''    public void writeDataFile(final URL url)
    '''
def writeData():
    '''    public void writeData()
    '''
def writeDashboardFiles():
    '''    public void writeDashboardFiles()
    '''
def writeBackgroundFile():
    '''    public void writeBackgroundFile(final String name)
    '''
def writeBackground():
    '''    public void writeBackground(final OutputStream outputStream)
    '''
def readBackground():
    '''    public void readBackground(final InputStream inputStream)
    '''
def writeProjectFile():
    '''    public void writeProjectFile(final URL url)
    '''
def setProject():
    '''    public void setProject(final IlvDiagrammerProject project)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def setModified():
    '''    public void setModified(final boolean b)
    '''
def isModified():
    '''    public boolean isModified()
    '''
def isBackgroundObject():
    '''    public boolean isBackgroundObject(final IlvGraphic ilvGraphic)
    '''
def addSymbol():
    '''    public void addSymbol(final IlvDashboardSymbol e)
    '''
def removeSymbol():
    '''    public void removeSymbol(final IlvDashboardSymbol ilvDashboardSymbol)
    '''
def getObjectSymbol():
    '''    public IlvDashboardSymbol getObjectSymbol(final Object o)
    '''
def getGraphicSymbol():
    '''    public IlvDashboardSymbol getGraphicSymbol(final IlvGraphic ilvGraphic)
    '''
def hasSelectedSymbols():
    '''    public boolean hasSelectedSymbols()
    '''
def getSelectedSymbols():
    '''    public IlvDashboardSymbolIterator getSelectedSymbols()
    '''
def getSymbol():
    '''    public IlvDashboardSymbol getSymbol(final String s)
    '''
def getURL():
    '''    public URL getURL()
    '''
def setURL():
    '''    public void setURL(final URL d)
    '''
def writeDashboard():
    '''    public void writeDashboard(final URL url)
    '''
def readDashboard():
    '''    public void readDashboard(final URL url)
    public void readDashboard(final Document document, final boolean b, final float n, final float n2)
    '''
def readBinary():
    '''    public void readBinary(final URL url)
    public void readBinary(final InputStream inputStream)
    '''
def writeBinary():
    '''    public void writeBinary(final URL url)
    public void writeBinary(final OutputStream outputStream)
    '''
def isUndoingEnabled():
    '''    public boolean isUndoingEnabled()
    '''
def setUndoingEnabled():
    '''    public void setUndoingEnabled(final boolean f)
    '''
def addUndoableEdit():
    '''    public void addUndoableEdit(final UndoableEdit undoableEdit)
    '''
def setCompoundEditMode():
    '''    public void setCompoundEditMode(final boolean compoundMode)
    '''
def canUndo():
    '''    public boolean canUndo()
    '''
def undo():
    '''    public void undo()
    public void undo()
    '''
def canRedo():
    '''    public boolean canRedo()
    '''
def redo():
    '''    public void redo()
    public void redo()
    '''
def setSelectManager():
    '''    public void setSelectManager(final IlvDashboardKeySelectManager h)
    '''
def getSelectManager():
    '''    public IlvDashboardKeySelectManager getSelectManager()
    '''
def clear():
    '''    public void clear()
    '''
def setEditingAllowed():
    '''    public void setEditingAllowed(final boolean editingAllowed)
    '''
def isContained():
    '''    public boolean isContained(final IlvDashboardSymbol o)
    '''
def getSymbolIndex():
    '''    public int getSymbolIndex(final IlvDashboardSymbol o)
    '''
def setSymbolIndex():
    '''    public void setSymbolIndex(final IlvDashboardSymbol element, final int index)
    '''
def addSymbolParameterListener():
    '''    public void addSymbolParameterListener(final IlvDashboardSymbolParameterListener e)
    '''
def removeSymbolParameterListener():
    '''    public void removeSymbolParameterListener(final IlvDashboardSymbolParameterListener o)
    '''
def fireSymbolParameterChanged():
    '''    public void fireSymbolParameterChanged(final IlvDashboardSymbol ilvDashboardSymbol, final IlvDashboardSymbol.Parameter parameter, final Object o, final Object o2, final String s, final String s2)
    '''
def getPrintingController():
    '''    public IlvManagerPrintingController getPrintingController()
    '''
def setBaseTextDirection():
    '''    public void setBaseTextDirection(final int n)
    '''
def getBaseTextDirection():
    '''    public int getBaseTextDirection()
    '''
def isLinkLayoutEnabled():
    '''    public boolean isLinkLayoutEnabled()
    '''
def setLinkLayoutEnabled():
    '''    public void setLinkLayoutEnabled(final boolean b)
    '''
def getSerializableProperties():
    '''    public ArrayList<Object> getSerializableProperties()
    '''
def setSerializableProperties():
    '''    public void setSerializableProperties(final ArrayList<Object> p)
    '''
def getSymbols():
    '''    public IlvDashboardSymbolIterator getSymbols()
    '''
def iterator():
    '''    public Iterator<IlvDashboardSymbol> iterator()
    '''
def addStyleSheet():
    '''    public void addStyleSheet(final URL url)
    '''
def contentsChanged():
    '''    public void contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)
    '''
def layerChanged():
    '''    public void layerChanged(final ManagerLayerEvent managerLayerEvent)
    '''
def layerInserted():
    '''    public void layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)
    '''
def layerMoved():
    '''    public void layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)
    '''
def layerRemoved():
    '''    public void layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)
    '''
def getDocumentBase():
    '''    public URL getDocumentBase()
    '''
def createInputStream():
    '''    public IlvInputStream createInputStream(final InputStream inputStream)
    '''
def createOutputStream():
    '''    public IlvOutputStream createOutputStream(final OutputStream outputStream)
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public IlvDashboardSymbol next()
    '''
def remove():
    '''    public void remove()
    '''
