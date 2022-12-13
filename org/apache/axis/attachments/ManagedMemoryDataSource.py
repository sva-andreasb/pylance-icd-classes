MIN_MEMORY_DISK_CACHED = "int  -1"
MAX_MEMORY_DISK_CACHED = "int  16384"
READ_CHUNK_SZ = "int  32768"
def ManagedMemoryDataSource():
'''public ManagedMemoryDataSource(final InputStream ss, final int maxCached, final String contentType)
public ManagedMemoryDataSource(final InputStream ss, final int maxCached, final String contentType, final boolean readall)
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getInputStream():
'''public synchronized InputStream getInputStream()
'''
pass
def getName():
'''public String getName()
'''
pass
def getOutputStream():
'''public OutputStream getOutputStream()
'''
pass
def delete():
'''public synchronized boolean delete()
'''
pass
def main():
'''public static void main(final String[] arg)
'''
pass
def getDiskCacheFile():
'''public File getDiskCacheFile()
'''
pass
def available():
'''public int available()
'''
pass
def read():
'''public int read()
public int read(final byte[] b, final int off, int len)
'''
pass
def markSupported():
'''public boolean markSupported()
'''
pass
def mark():
'''public void mark(final int readlimit)
'''
pass
def reset():
'''public void reset()
'''
pass
def skip():
'''public long skip(long skipped)
'''
pass
def close():
'''public synchronized void close()
'''
pass
