def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final int index, final int n)\n
    '''
def getDoubleAt():
    '''returns double\n\n
    getDoubleAt(final int index, final int n)\n
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
    dataChanged(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def beforeDataChange():
    '''returns None\n\n
    beforeDataChange(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def objectsAdded():
    '''returns None\n\n
    objectsAdded(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def objectsRemoved():
    '''returns None\n\n
    objectsRemoved(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def beforeObjectsRemoved():
    '''returns None\n\n
    beforeObjectsRemoved(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def columnAdded():
    '''returns None\n\n
    columnAdded(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def columnRemoved():
    '''returns None\n\n
    columnRemoved(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def beforeColumnRemoved():
    '''returns None\n\n
    beforeColumnRemoved(final FlatSetModelEvent flatSetModelEvent)\n
    '''
def columnPropertyChanged():
    '''returns None\n\n
    columnPropertyChanged(final FlatSetModelEvent flatSetModelEvent)\n
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
    '''returns IlvFlatSetModel\n\n
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
    '''returns IlvFlatSetToFlatTableModel\n\n
    (final IlvFlatSetModel ilvFlatSetModel)\n
    (final IlvFlatSetModel b, final int n)\n
    (final IlvDefaultFlatSetModel ilvDefaultFlatSetModel, final IlvObjectFactory ilvObjectFactory)\n
    (final IlvDefaultFlatSetModel b, final IlvObjectFactory g, final int n)\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvDataColumnInfo[] array)\n
    (final IlvFlatSetModel b, final IlvDataColumnInfo[] array, final int n)\n
    (final IlvDefaultFlatSetModel ilvDefaultFlatSetModel, final IlvObjectFactory ilvObjectFactory, final IlvDataColumnInfo[] array)\n
    (final IlvDefaultFlatSetModel b, final IlvObjectFactory g, final IlvDataColumnInfo[] array, final int n)\n
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
