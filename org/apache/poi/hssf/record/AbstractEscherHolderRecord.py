def ():
    '''returns AbstractEscherHolderRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def clone():
    '''returns AbstractEscherHolderRecord\n\n
    clone()\n
    '''
def addEscherRecord():
    '''returns boolean\n\n
    addEscherRecord(final int index, final EscherRecord element)\n
    addEscherRecord(final EscherRecord element)\n
    '''
def getEscherRecords():
    '''returns List<EscherRecord>\n\n
    getEscherRecords()\n
    '''
def clearEscherRecords():
    '''returns None\n\n
    clearEscherRecords()\n
    '''
def getEscherContainer():
    '''returns EscherContainerRecord\n\n
    getEscherContainer()\n
    '''
def findFirstWithId():
    '''returns EscherRecord\n\n
    findFirstWithId(final short id)\n
    '''
def getEscherRecord():
    '''returns EscherRecord\n\n
    getEscherRecord(final int index)\n
    '''
def join():
    '''returns None\n\n
    join(final AbstractEscherHolderRecord record)\n
    '''
def processContinueRecord():
    '''returns None\n\n
    processContinueRecord(final byte[] record)\n
    '''
def getRawData():
    '''returns byte[]\n\n
    getRawData()\n
    '''
def setRawData():
    '''returns None\n\n
    setRawData(final byte[] rawData)\n
    '''
def decode():
    '''returns None\n\n
    decode()\n
    '''
