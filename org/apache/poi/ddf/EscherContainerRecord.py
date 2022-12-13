DGG_CONTAINER = "short  -4096"
BSTORE_CONTAINER = "short  -4095"
DG_CONTAINER = "short  -4094"
SPGR_CONTAINER = "short  -4093"
SP_CONTAINER = "short  -4092"
SOLVER_CONTAINER = "short  -4091"
def EscherContainerRecord():
    '''public EscherContainerRecord()
    '''
def fillFields():
    '''public int fillFields(final byte[] data, final int pOffset, final EscherRecordFactory recordFactory)
    '''
def serialize():
    '''public int serialize(final int offset, final byte[] data, final EscherSerializationListener listener)
    '''
def getRecordSize():
    '''public int getRecordSize()
    '''
def hasChildOfType():
    '''public boolean hasChildOfType(final short recordId)
    '''
def getChild():
    '''public EscherRecord getChild(final int index)
    '''
def getChildRecords():
    '''public List<EscherRecord> getChildRecords()
    '''
def getChildIterator():
    '''public Iterator<EscherRecord> getChildIterator()
    '''
def iterator():
    '''public Iterator<EscherRecord> iterator()
    '''
def setChildRecords():
    '''public void setChildRecords(final List<EscherRecord> childRecords)
    '''
def removeChildRecord():
    '''public boolean removeChildRecord(final EscherRecord toBeRemoved)
    '''
def getChildContainers():
    '''public List<EscherContainerRecord> getChildContainers()
    '''
def getRecordName():
    '''public String getRecordName()
    '''
def display():
    '''public void display(final PrintWriter w, final int indent)
    '''
def addChildRecord():
    '''public void addChildRecord(final EscherRecord record)
    '''
def addChildBefore():
    '''public void addChildBefore(final EscherRecord record, final int insertBeforeRecordId)
    '''
def getChildById():
    '''public <T extends EscherRecord> T getChildById(final short recordId)
    '''
def getRecordsById():
    '''public void getRecordsById(final short recordId, final List<EscherRecord> out)
    '''
