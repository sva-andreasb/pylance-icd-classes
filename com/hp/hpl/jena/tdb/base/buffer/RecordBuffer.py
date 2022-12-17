def ():
    '''returns RecordBuffer\n\n
    (final RecordFactory recFactory, final int maxRec)\n
    (final ByteBuffer bb, final RecordFactory recFactory, final int num)\n
    '''
def get():
    '''returns Record\n\n
    get(final int idx)\n
    '''
def getLow():
    '''returns Record\n\n
    getLow()\n
    '''
def getHigh():
    '''returns Record\n\n
    getHigh()\n
    '''
def add():
    '''returns None\n\n
    add(final Record record)\n
    add(final int idx, final Record record)\n
    '''
def set():
    '''returns None\n\n
    set(final int idx, final Record record)\n
    '''
def _get():
    '''returns Record\n\n
    _get(final int idx)\n
    '''
def find():
    '''returns int\n\n
    find(final Record k)\n
    find(final Record rec, final int fromIndex, final int toIndex)\n
    '''
def iterator():
    '''returns Iterator<Record>\n\n
    iterator()\n
    iterator(final Record min, final Record max)\n
    '''
def findGet():
    '''returns Record\n\n
    findGet(final Record k)\n
    '''
def removeByKey():
    '''returns boolean\n\n
    removeByKey(final Record k)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def duplicate():
    '''returns RecordBuffer\n\n
    duplicate()\n
    '''
