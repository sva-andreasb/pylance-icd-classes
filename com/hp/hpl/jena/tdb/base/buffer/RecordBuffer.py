def RecordBuffer():
    '''    public RecordBuffer(final RecordFactory recFactory, final int maxRec)
    public RecordBuffer(final ByteBuffer bb, final RecordFactory recFactory, final int num)
    '''
def get():
    '''    public Record get(final int idx)
    '''
def getLow():
    '''    public Record getLow()
    '''
def getHigh():
    '''    public Record getHigh()
    '''
def add():
    '''    public void add(final Record record)
    public void add(final int idx, final Record record)
    '''
def set():
    '''    public void set(final int idx, final Record record)
    '''
def _get():
    '''    public Record _get(final int idx)
    '''
def find():
    '''    public int find(final Record k)
    public int find(final Record rec, final int fromIndex, final int toIndex)
    '''
def iterator():
    '''    public Iterator<Record> iterator()
    public Iterator<Record> iterator(final Record min, final Record max)
    '''
def findGet():
    '''    public Record findGet(final Record k)
    '''
def removeByKey():
    '''    public boolean removeByKey(final Record k)
    '''
def toString():
    '''    public String toString()
    '''
def duplicate():
    '''    public RecordBuffer duplicate()
    '''
