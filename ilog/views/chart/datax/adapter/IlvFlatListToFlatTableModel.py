def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int n, final int n2)\n
    '''
def getDoubleAt():
    '''returns double\n\n
    getDoubleAt(final int n, final int n2)\n
    '''
def getSupportedEventsMask():
    '''returns int\n\n
    getSupportedEventsMask()\n
    '''
def eventSeriesBegin():
    '''returns None\n\n
    eventSeriesBegin()\n
    '''
def eventSeriesEnd():
    '''returns None\n\n
    eventSeriesEnd()\n
    '''
def dataChanged():
    '''returns None\n\n
    dataChanged(final FlatListModelEvent flatListModelEvent)\n
    '''
def beforeDataChange():
    '''returns None\n\n
    beforeDataChange(final FlatListModelEvent flatListModelEvent)\n
    '''
def objectsAdded():
    '''returns None\n\n
    objectsAdded(final FlatListModelEvent flatListModelEvent)\n
    '''
def objectsRemoved():
    '''returns None\n\n
    objectsRemoved(final FlatListModelEvent flatListModelEvent)\n
    '''
def beforeObjectsRemoved():
    '''returns None\n\n
    beforeObjectsRemoved(final FlatListModelEvent flatListModelEvent)\n
    '''
def columnAdded():
    '''returns None\n\n
    columnAdded(final FlatListModelEvent flatListModelEvent)\n
    '''
def columnRemoved():
    '''returns None\n\n
    columnRemoved(final FlatListModelEvent flatListModelEvent)\n
    '''
def beforeColumnRemoved():
    '''returns None\n\n
    beforeColumnRemoved(final FlatListModelEvent flatListModelEvent)\n
    '''
def columnPropertyChanged():
    '''returns None\n\n
    columnPropertyChanged(final FlatListModelEvent flatListModelEvent)\n
    '''
def setRowCount():
    '''returns None\n\n
    setRowCount(final int n)\n
    '''
def insertRows():
    '''returns None\n\n
    insertRows(final int n, final int n2)\n
    '''
def insertRow():
    '''returns None\n\n
    insertRow(final int n, final Object[] array)\n
    '''
def removeRows():
    '''returns None\n\n
    removeRows(final int n, final int n2)\n
    '''
def setColumnCount():
    '''returns None\n\n
    setColumnCount(final int n)\n
    '''
def insertColumn():
    '''returns None\n\n
    insertColumn(final int n, final IlvDataColumnInfo ilvDataColumnInfo)\n
    insertColumn(final int n, final IlvDataColumnInfo ilvDataColumnInfo, final Object[] array)\n
    insertColumn(final int n, final IlvDataColumnInfo ilvDataColumnInfo, final double[] array)\n
    '''
def removeColumn():
    '''returns None\n\n
    removeColumn(final int n)\n
    '''
def setColumns():
    '''returns None\n\n
    setColumns(final List<IlvDataColumnInfo> list)\n
    '''
def setColumn():
    '''returns None\n\n
    setColumn(final int n, final IlvDataColumnInfo ilvDataColumnInfo)\n
    '''
def getUnderlyingModel():
    '''returns IlvFlatListModel\n\n
    getUnderlyingModel()\n
    '''
def getObjectAt():
    '''returns Object\n\n
    getObjectAt(final int n)\n
    '''
def getIndexOf():
    '''returns int\n\n
    getIndexOf(final Object obj)\n
    '''
def ():
    '''returns IlvFlatListToFlatTableModel\n\n
    (final IlvFlatListModel ilvFlatListModel)\n
    (final IlvFlatListModel b, final int n)\n
    (final IlvDefaultFlatListModel ilvDefaultFlatListModel, final IlvObjectFactory ilvObjectFactory)\n
    (final IlvDefaultFlatListModel b, final IlvObjectFactory f, final int n)\n
    (final IlvFlatListModel ilvFlatListModel, final IlvDataColumnInfo[] array)\n
    (final IlvFlatListModel b, final IlvDataColumnInfo[] array, final int n)\n
    (final IlvDefaultFlatListModel ilvDefaultFlatListModel, final IlvObjectFactory ilvObjectFactory, final IlvDataColumnInfo[] array)\n
    (final IlvDefaultFlatListModel b, final IlvObjectFactory f, final IlvDataColumnInfo[] array, final int n)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
