def getRoot():
    '''returns Object\n\n
    getRoot()\n
    '''
def getChildren():
    '''returns Collection\n\n
    getChildren(final Object o)\n
    '''
def getPath():
    '''returns TreePath\n\n
    getPath(final Object o)\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def getColumn():
    '''returns IlvDataColumnInfo\n\n
    getColumn(final int n)\n
    '''
def getValueAt():
    '''returns Object\n\n
    getValueAt(final Object o, final int n)\n
    '''
def getDoubleAt():
    '''returns double\n\n
    getDoubleAt(final Object o, final int n)\n
    '''
def setValueAt():
    '''returns None\n\n
    setValueAt(final Object o, final Object o2, final int n)\n
    '''
def setDoubleAt():
    '''returns None\n\n
    setDoubleAt(final double n, final Object o, final int n2)\n
    '''
def getSupportedEventsMask():
    '''returns int\n\n
    getSupportedEventsMask()\n
    '''
def getParent():
    '''returns Object\n\n
    getParent(final Object o)\n
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
def classificationChanged():
    '''returns None\n\n
    classificationChanged(final PartitionerEvent partitionerEvent)\n
    '''
def ():
    '''returns IlvFlatSetToTreeSetModel\n\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvPartitioner[] array)\n
    (final IlvFlatSetModel b, final IlvPartitioner[] array, final int n)\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvPartitionerFactory[] array)\n
    (final IlvFlatSetModel b, final IlvPartitionerFactory[] array, final int n)\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvPartitioner ilvPartitioner)\n
    (final IlvFlatSetModel b, final IlvPartitioner ilvPartitioner, final int n)\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvPartitionerFactory ilvPartitionerFactory)\n
    (final IlvFlatSetModel ilvFlatSetModel, final IlvPartitionerFactory ilvPartitionerFactory, final int n)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getPartitionedModel():
    '''returns IlvObjectModelWithColumns\n\n
    getPartitionedModel()\n
    '''
def getId():
    '''returns IlvClusterId\n\n
    getId()\n
    '''
