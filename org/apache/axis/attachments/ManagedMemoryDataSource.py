MIN_MEMORY_DISK_CACHED = "int  -1"
MAX_MEMORY_DISK_CACHED = "int  16384"
READ_CHUNK_SZ = "int  32768"
def ManagedMemoryDataSource():
    '''    public ManagedMemoryDataSource(final InputStream ss, final int maxCached, final String contentType)
    public ManagedMemoryDataSource(final InputStream ss, final int maxCached, final String contentType, final boolean readall)
    '''
def getContentType():
    '''    public String getContentType()
    '''
def getInputStream():
    '''    public synchronized InputStream getInputStream()
    '''
def getName():
    '''    public String getName()
    '''
def getOutputStream():
    '''    public OutputStream getOutputStream()
    '''
def delete():
    '''    public synchronized boolean delete()
    '''
def main():
    '''    public static void main(final String[] arg)
    '''
def getDiskCacheFile():
    '''    public File getDiskCacheFile()
    '''
def available():
    '''    public int available()
    '''
def read():
    '''    public int read()
    public int read(final byte[] b, final int off, int len)
    '''
def markSupported():
    '''    public boolean markSupported()
    '''
def mark():
    '''    public void mark(final int readlimit)
    '''
def reset():
    '''    public void reset()
    '''
def skip():
    '''    public long skip(long skipped)
    '''
def close():
    '''    public synchronized void close()
    '''
