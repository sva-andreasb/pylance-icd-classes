def ():
    '''returns RecordFactory\n\n
    (final int keyLength, final int valueLength)\n
    '''
def keyFactory():
    '''returns RecordFactory\n\n
    keyFactory()\n
    '''
def createKeyOnly():
    '''returns Record\n\n
    createKeyOnly()\n
    createKeyOnly(final Record record)\n
    '''
def create():
    '''returns Record\n\n
    create(final byte[] key)\n
    create()\n
    create(final byte[] key, final byte[] value)\n
    '''
def insertInto():
    '''returns None\n\n
    insertInto(final Record record, final ByteBuffer bb, final int idx)\n
    '''
def buildFrom():
    '''returns Record\n\n
    buildFrom(final ByteBuffer bb, final int idx)\n
    '''
def hasValue():
    '''returns boolean\n\n
    hasValue()\n
    '''
def recordLength():
    '''returns int\n\n
    recordLength()\n
    '''
def keyLength():
    '''returns int\n\n
    keyLength()\n
    '''
def valueLength():
    '''returns int\n\n
    valueLength()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
