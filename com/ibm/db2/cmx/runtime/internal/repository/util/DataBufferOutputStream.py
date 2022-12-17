DefaultCapacity = "int  5242880"
DefaultPrefix = "String  \"PQRY\""
DefaultSuffix = "String  \"Buffer.dat\""
def ():
    '''returns DataBufferOutputStream\n\n
    ()\n
    (final int n, final String dataFilePrefix, final String dataFileSuffix, final File dataFileDirectory)\n
    '''
def write():
    '''returns None\n\n
    write(final int n)\n
    write(final byte[] b)\n
    write(final byte[] b, final int off, final int len)\n
    '''
def isOutputClosed():
    '''returns boolean\n\n
    isOutputClosed()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getLength():
    '''returns long\n\n
    getLength()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getDataFileName():
    '''returns String\n\n
    getDataFileName()\n
    '''
def isCachingInMemory():
    '''returns boolean\n\n
    isCachingInMemory()\n
    '''
