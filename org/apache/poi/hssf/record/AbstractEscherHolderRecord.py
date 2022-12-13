def AbstractEscherHolderRecord():
'''public AbstractEscherHolderRecord()
public AbstractEscherHolderRecord(final RecordInputStream in)
'''
pass
def toString():
'''public String toString()
'''
pass
def serialize():
'''public int serialize(final int offset, final byte[] data)
'''
pass
def getRecordSize():
'''public int getRecordSize()
'''
pass
def clone():
'''public AbstractEscherHolderRecord clone()
'''
pass
def addEscherRecord():
'''public void addEscherRecord(final int index, final EscherRecord element)
public boolean addEscherRecord(final EscherRecord element)
'''
pass
def getEscherRecords():
'''public List<EscherRecord> getEscherRecords()
'''
pass
def clearEscherRecords():
'''public void clearEscherRecords()
'''
pass
def getEscherContainer():
'''public EscherContainerRecord getEscherContainer()
'''
pass
def findFirstWithId():
'''public EscherRecord findFirstWithId(final short id)
'''
pass
def getEscherRecord():
'''public EscherRecord getEscherRecord(final int index)
'''
pass
def join():
'''public void join(final AbstractEscherHolderRecord record)
'''
pass
def processContinueRecord():
'''public void processContinueRecord(final byte[] record)
'''
pass
def getRawData():
'''public byte[] getRawData()
'''
pass
def setRawData():
'''public void setRawData(final byte[] rawData)
'''
pass
def decode():
'''public void decode()
'''
pass
