DGG_CONTAINER = "short  -4096"
BSTORE_CONTAINER = "short  -4095"
DG_CONTAINER = "short  -4094"
SPGR_CONTAINER = "short  -4093"
SP_CONTAINER = "short  -4092"
SOLVER_CONTAINER = "short  -4091"
def ():
    '''returns EscherContainerRecord\n\n
    ()\n
    '''
def fillFields():
    '''returns int\n\n
    fillFields(final byte[] data, final int pOffset, final EscherRecordFactory recordFactory)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data, final EscherSerializationListener listener)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def hasChildOfType():
    '''returns boolean\n\n
    hasChildOfType(final short recordId)\n
    '''
def getChild():
    '''returns EscherRecord\n\n
    getChild(final int index)\n
    '''
def getChildRecords():
    '''returns List<EscherRecord>\n\n
    getChildRecords()\n
    '''
def getChildIterator():
    '''returns Iterator<EscherRecord>\n\n
    getChildIterator()\n
    '''
def iterator():
    '''returns Iterator<EscherRecord>\n\n
    iterator()\n
    '''
def setChildRecords():
    '''returns None\n\n
    setChildRecords(final List<EscherRecord> childRecords)\n
    '''
def removeChildRecord():
    '''returns boolean\n\n
    removeChildRecord(final EscherRecord toBeRemoved)\n
    '''
def getChildContainers():
    '''returns List<EscherContainerRecord>\n\n
    getChildContainers()\n
    '''
def getRecordName():
    '''returns String\n\n
    getRecordName()\n
    '''
def display():
    '''returns None\n\n
    display(final PrintWriter w, final int indent)\n
    '''
def addChildRecord():
    '''returns None\n\n
    addChildRecord(final EscherRecord record)\n
    '''
def addChildBefore():
    '''returns None\n\n
    addChildBefore(final EscherRecord record, final int insertBeforeRecordId)\n
    '''
def getRecordsById():
    '''returns None\n\n
    getRecordsById(final short recordId, final List<EscherRecord> out)\n
    '''
