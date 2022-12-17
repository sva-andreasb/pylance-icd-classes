MIN_MEMORY_DISK_CACHED = "int  -1"
MAX_MEMORY_DISK_CACHED = "int  16384"
READ_CHUNK_SZ = "int  32768"
def ():
    '''returns ManagedMemoryDataSource\n\n
    (final InputStream ss, final int maxCached, final String contentType)\n
    (final InputStream ss, final int maxCached, final String contentType, final boolean readall)\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getDiskCacheFile():
    '''returns File\n\n
    getDiskCacheFile()\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, int len)\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def skip():
    '''returns long\n\n
    skip(long skipped)\n
    '''
