def MultiFileOutputStream():
'''public MultiFileOutputStream()
public MultiFileOutputStream(final File root, final String namePrefix)
'''
pass
def init():
'''public MultiFileOutputStream init(final UploadObjectObserver observer, final long partSize, final long diskLimit)
'''
pass
def write():
'''public void write(final int b)
public void write(final byte[] b)
public void write(final byte[] b, final int off, final int len)
'''
pass
def onFileDelete():
'''public void onFileDelete(final FileDeletionEvent event)
'''
pass
def flush():
'''public void flush()
'''
pass
def close():
'''public void close()
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def getNumFilesWritten():
'''public int getNumFilesWritten()
'''
pass
def getFile():
'''public File getFile(final int partNumber)
'''
pass
def getPartSize():
'''public long getPartSize()
'''
pass
def getRoot():
'''public File getRoot()
'''
pass
def getNamePrefix():
'''public String getNamePrefix()
'''
pass
def getTotalBytesWritten():
'''public long getTotalBytesWritten()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def getDiskLimit():
'''public long getDiskLimit()
'''
pass
