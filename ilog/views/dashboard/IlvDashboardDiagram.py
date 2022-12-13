def IlvDashboardDiagram():
'''public IlvDashboardDiagram(final IlvDashboardContext b)
public IlvDashboardDiagram(final IlvDashboardContext b, final IlvSDMView ilvSDMView)
'''
pass
def getContext():
'''public IlvDashboardContext getContext()
'''
pass
def setQuadtreeEnabled():
'''public void setQuadtreeEnabled(final boolean b)
'''
pass
def prepareForEditing():
'''public void prepareForEditing()
'''
pass
def objectRemoved():
'''public void objectRemoved(final SDMModelEvent sdmModelEvent)
'''
pass
def dataChanged():
'''public void dataChanged(final SDMModelEvent sdmModelEvent)
'''
pass
def canEdit():
'''public boolean canEdit()
'''
pass
def delete():
'''public void delete()
'''
pass
def cut():
'''public void cut()
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
def duplicate():
'''public void duplicate()
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
def canGroup():
'''public boolean canGroup()
'''
pass
def group():
'''public void group()
'''
pass
def canUngroup():
'''public boolean canUngroup()
'''
pass
def ungroup():
'''public void ungroup()
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
def alignBottom():
'''public void alignBottom()
'''
pass
def alignHorizontalCenter():
'''public void alignHorizontalCenter()
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
def alignVerticalCenter():
'''public void alignVerticalCenter()
'''
pass
def distributeHorizontally():
'''public void distributeHorizontally()
'''
pass
def compare():
'''public int compare(final Object o, final Object o2)
public int compare(final Object o, final Object o2)
'''
pass
def distributeVertically():
'''public void distributeVertically()
'''
pass
def getBackgroundGraphics():
'''public IlvDashboardGraphicIterator getBackgroundGraphics()
'''
pass
def writeDataFile():
'''public void writeDataFile(final URL url)
'''
pass
def writeData():
'''public void writeData()
'''
pass
def writeDashboardFiles():
'''public void writeDashboardFiles()
'''
pass
def writeBackgroundFile():
'''public void writeBackgroundFile(final String name)
'''
pass
def writeBackground():
'''public void writeBackground(final OutputStream outputStream)
'''
pass
def readBackground():
'''public void readBackground(final InputStream inputStream)
'''
pass
def writeProjectFile():
'''public void writeProjectFile(final URL url)
'''
pass
def setProject():
'''public void setProject(final IlvDiagrammerProject project)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def setModified():
'''public void setModified(final boolean b)
'''
pass
def isModified():
'''public boolean isModified()
'''
pass
def isBackgroundObject():
'''public boolean isBackgroundObject(final IlvGraphic ilvGraphic)
'''
pass
def addSymbol():
'''public void addSymbol(final IlvDashboardSymbol e)
'''
pass
def removeSymbol():
'''public void removeSymbol(final IlvDashboardSymbol ilvDashboardSymbol)
'''
pass
def getObjectSymbol():
'''public IlvDashboardSymbol getObjectSymbol(final Object o)
'''
pass
def getGraphicSymbol():
'''public IlvDashboardSymbol getGraphicSymbol(final IlvGraphic ilvGraphic)
'''
pass
def hasSelectedSymbols():
'''public boolean hasSelectedSymbols()
'''
pass
def getSelectedSymbols():
'''public IlvDashboardSymbolIterator getSelectedSymbols()
'''
pass
def getSymbol():
'''public IlvDashboardSymbol getSymbol(final String s)
'''
pass
def getURL():
'''public URL getURL()
'''
pass
def setURL():
'''public void setURL(final URL d)
'''
pass
def writeDashboard():
'''public void writeDashboard(final URL url)
'''
pass
def readDashboard():
'''public void readDashboard(final URL url)
public void readDashboard(final Document document, final boolean b, final float n, final float n2)
'''
pass
def readBinary():
'''public void readBinary(final URL url)
public void readBinary(final InputStream inputStream)
'''
pass
def writeBinary():
'''public void writeBinary(final URL url)
public void writeBinary(final OutputStream outputStream)
'''
pass
def isUndoingEnabled():
'''public boolean isUndoingEnabled()
'''
pass
def setUndoingEnabled():
'''public void setUndoingEnabled(final boolean f)
'''
pass
def addUndoableEdit():
'''public void addUndoableEdit(final UndoableEdit undoableEdit)
'''
pass
def setCompoundEditMode():
'''public void setCompoundEditMode(final boolean compoundMode)
'''
pass
def canUndo():
'''public boolean canUndo()
'''
pass
def undo():
'''public void undo()
public void undo()
'''
pass
def canRedo():
'''public boolean canRedo()
'''
pass
def redo():
'''public void redo()
public void redo()
'''
pass
def setSelectManager():
'''public void setSelectManager(final IlvDashboardKeySelectManager h)
'''
pass
def getSelectManager():
'''public IlvDashboardKeySelectManager getSelectManager()
'''
pass
def clear():
'''public void clear()
'''
pass
def setEditingAllowed():
'''public void setEditingAllowed(final boolean editingAllowed)
'''
pass
def isContained():
'''public boolean isContained(final IlvDashboardSymbol o)
'''
pass
def getSymbolIndex():
'''public int getSymbolIndex(final IlvDashboardSymbol o)
'''
pass
def setSymbolIndex():
'''public void setSymbolIndex(final IlvDashboardSymbol element, final int index)
'''
pass
def addSymbolParameterListener():
'''public void addSymbolParameterListener(final IlvDashboardSymbolParameterListener e)
'''
pass
def removeSymbolParameterListener():
'''public void removeSymbolParameterListener(final IlvDashboardSymbolParameterListener o)
'''
pass
def fireSymbolParameterChanged():
'''public void fireSymbolParameterChanged(final IlvDashboardSymbol ilvDashboardSymbol, final IlvDashboardSymbol.Parameter parameter, final Object o, final Object o2, final String s, final String s2)
'''
pass
def getPrintingController():
'''public IlvManagerPrintingController getPrintingController()
'''
pass
def setBaseTextDirection():
'''public void setBaseTextDirection(final int n)
'''
pass
def getBaseTextDirection():
'''public int getBaseTextDirection()
'''
pass
def isLinkLayoutEnabled():
'''public boolean isLinkLayoutEnabled()
'''
pass
def setLinkLayoutEnabled():
'''public void setLinkLayoutEnabled(final boolean b)
'''
pass
def getSerializableProperties():
'''public ArrayList<Object> getSerializableProperties()
'''
pass
def setSerializableProperties():
'''public void setSerializableProperties(final ArrayList<Object> p)
'''
pass
def getSymbols():
'''public IlvDashboardSymbolIterator getSymbols()
'''
pass
def iterator():
'''public Iterator<IlvDashboardSymbol> iterator()
'''
pass
def addStyleSheet():
'''public void addStyleSheet(final URL url)
'''
pass
def contentsChanged():
'''public void contentsChanged(final ManagerContentChangedEvent managerContentChangedEvent)
'''
pass
def layerChanged():
'''public void layerChanged(final ManagerLayerEvent managerLayerEvent)
'''
pass
def layerInserted():
'''public void layerInserted(final ManagerLayerInsertedEvent managerLayerInsertedEvent)
'''
pass
def layerMoved():
'''public void layerMoved(final ManagerLayerMovedEvent managerLayerMovedEvent)
'''
pass
def layerRemoved():
'''public void layerRemoved(final ManagerLayerRemovedEvent managerLayerRemovedEvent)
'''
pass
def getDocumentBase():
'''public URL getDocumentBase()
'''
pass
def createInputStream():
'''public IlvInputStream createInputStream(final InputStream inputStream)
'''
pass
def createOutputStream():
'''public IlvOutputStream createOutputStream(final OutputStream outputStream)
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public IlvDashboardSymbol next()
'''
pass
def remove():
'''public void remove()
'''
pass
