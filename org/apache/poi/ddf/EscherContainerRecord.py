DGG_CONTAINER = "short  -4096"
BSTORE_CONTAINER = "short  -4095"
DG_CONTAINER = "short  -4094"
SPGR_CONTAINER = "short  -4093"
SP_CONTAINER = "short  -4092"
SOLVER_CONTAINER = "short  -4091"
def EscherContainerRecord():
'''public EscherContainerRecord()
'''
pass
def fillFields():
'''public int fillFields(final byte[] data, final int pOffset, final EscherRecordFactory recordFactory)
'''
pass
def serialize():
'''public int serialize(final int offset, final byte[] data, final EscherSerializationListener listener)
'''
pass
def getRecordSize():
'''public int getRecordSize()
'''
pass
def hasChildOfType():
'''public boolean hasChildOfType(final short recordId)
'''
pass
def getChild():
'''public EscherRecord getChild(final int index)
'''
pass
def getChildRecords():
'''public List<EscherRecord> getChildRecords()
'''
pass
def getChildIterator():
'''public Iterator<EscherRecord> getChildIterator()
'''
pass
def iterator():
'''public Iterator<EscherRecord> iterator()
'''
pass
def setChildRecords():
'''public void setChildRecords(final List<EscherRecord> childRecords)
'''
pass
def removeChildRecord():
'''public boolean removeChildRecord(final EscherRecord toBeRemoved)
'''
pass
def getChildContainers():
'''public List<EscherContainerRecord> getChildContainers()
'''
pass
def getRecordName():
'''public String getRecordName()
'''
pass
def display():
'''public void display(final PrintWriter w, final int indent)
'''
pass
def addChildRecord():
'''public void addChildRecord(final EscherRecord record)
'''
pass
def addChildBefore():
'''public void addChildBefore(final EscherRecord record, final int insertBeforeRecordId)
'''
pass
def getChildById():
'''public <T extends EscherRecord> T getChildById(final short recordId)
'''
pass
def getRecordsById():
'''public void getRecordsById(final short recordId, final List<EscherRecord> out)
'''
pass
