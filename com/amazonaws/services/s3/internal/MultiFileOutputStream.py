def ():
    '''returns MultiFileOutputStream\n\n
    ()\n
    (final File root, final String namePrefix)\n
    '''
def init():
    '''returns MultiFileOutputStream\n\n
    init(final UploadObjectObserver observer, final long partSize, final long diskLimit)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] b)\n
    write(final byte[] b, final int off, final int len)\n
    '''
def onFileDelete():
    '''returns None\n\n
    onFileDelete(final FileDeletionEvent event)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def getNumFilesWritten():
    '''returns int\n\n
    getNumFilesWritten()\n
    '''
def getFile():
    '''returns File\n\n
    getFile(final int partNumber)\n
    '''
def getPartSize():
    '''returns long\n\n
    getPartSize()\n
    '''
def getRoot():
    '''returns File\n\n
    getRoot()\n
    '''
def getNamePrefix():
    '''returns String\n\n
    getNamePrefix()\n
    '''
def getTotalBytesWritten():
    '''returns long\n\n
    getTotalBytesWritten()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getDiskLimit():
    '''returns long\n\n
    getDiskLimit()\n
    '''
