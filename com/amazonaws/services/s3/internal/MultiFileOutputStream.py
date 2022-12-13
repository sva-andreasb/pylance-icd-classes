def MultiFileOutputStream():
    '''    public MultiFileOutputStream()
    public MultiFileOutputStream(final File root, final String namePrefix)
    '''
def init():
    '''    public MultiFileOutputStream init(final UploadObjectObserver observer, final long partSize, final long diskLimit)
    '''
def write():
    '''    public void write(final int b)
    public void write(final byte[] b)
    public void write(final byte[] b, final int off, final int len)
    '''
def onFileDelete():
    '''    public void onFileDelete(final FileDeletionEvent event)
    '''
def flush():
    '''    public void flush()
    '''
def close():
    '''    public void close()
    '''
def cleanup():
    '''    public void cleanup()
    '''
def getNumFilesWritten():
    '''    public int getNumFilesWritten()
    '''
def getFile():
    '''    public File getFile(final int partNumber)
    '''
def getPartSize():
    '''    public long getPartSize()
    '''
def getRoot():
    '''    public File getRoot()
    '''
def getNamePrefix():
    '''    public String getNamePrefix()
    '''
def getTotalBytesWritten():
    '''    public long getTotalBytesWritten()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def getDiskLimit():
    '''    public long getDiskLimit()
    '''
