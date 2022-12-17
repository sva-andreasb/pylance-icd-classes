BATCH_BEGIN = "int  -2"
BATCH_END = "int  -1"
BEFORE_DATA_CHANGED = "int  1"
AFTER_DATA_CHANGED = "int  2"
DATA_CHANGED = "int  3"
DATA_ADDED = "int  4"
DATA_LABEL_CHANGED = "int  5"
FULL_UPDATE = "int  6"
def ():
    '''returns DataSetContentsEvent\n\n
    (final IlvDataSet source, final int c, final int a, final int b)\n
    (final IlvDataSet set, final DataSetContentsEvent dataSetContentsEvent)\n
    (final IlvDataSet set)\n
    (final IlvDataSet set, final int n, final int n2)\n
    '''
def getFirstIdx():
    '''returns int\n\n
    getFirstIdx()\n
    '''
def getLastIdx():
    '''returns int\n\n
    getLastIdx()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getDataSet():
    '''returns IlvDataSet\n\n
    getDataSet()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
