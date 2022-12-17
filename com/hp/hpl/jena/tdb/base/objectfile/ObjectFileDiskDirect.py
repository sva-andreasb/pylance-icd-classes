compression = "boolean  false"
def ():
    '''returns ObjectIterator\n\n
    (final String filename)\n
    (final long start, final long finish)\n
    '''
def write():
    '''returns long\n\n
    write(final ByteBuffer bb)\n
    '''
def read():
    '''returns ByteBuffer\n\n
    read(final long loc)\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    sync(final boolean force)\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    dump(final DumpHandler handler)\n
    '''
def handle():
    '''returns None\n\n
    handle(final long fileIdx, final String str)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
