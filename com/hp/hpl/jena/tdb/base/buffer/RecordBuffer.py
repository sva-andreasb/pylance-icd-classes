def RecordBuffer():
'''public RecordBuffer(final RecordFactory recFactory, final int maxRec)
public RecordBuffer(final ByteBuffer bb, final RecordFactory recFactory, final int num)
'''
pass
def get():
'''public Record get(final int idx)
'''
pass
def getLow():
'''public Record getLow()
'''
pass
def getHigh():
'''public Record getHigh()
'''
pass
def add():
'''public void add(final Record record)
public void add(final int idx, final Record record)
'''
pass
def set():
'''public void set(final int idx, final Record record)
'''
pass
def _get():
'''public Record _get(final int idx)
'''
pass
def find():
'''public int find(final Record k)
public int find(final Record rec, final int fromIndex, final int toIndex)
'''
pass
def iterator():
'''public Iterator<Record> iterator()
public Iterator<Record> iterator(final Record min, final Record max)
'''
pass
def findGet():
'''public Record findGet(final Record k)
'''
pass
def removeByKey():
'''public boolean removeByKey(final Record k)
'''
pass
def toString():
'''public String toString()
'''
pass
def duplicate():
'''public RecordBuffer duplicate()
'''
pass
