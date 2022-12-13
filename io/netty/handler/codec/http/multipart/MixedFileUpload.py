def MixedFileUpload():
'''public MixedFileUpload(final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize)
public MixedFileUpload(final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize, final String baseDir, final boolean deleteOnExit)
'''
pass
def getMaxSize():
'''public long getMaxSize()
'''
pass
def setMaxSize():
'''public void setMaxSize(final long maxSize)
'''
pass
def checkSize():
'''public void checkSize(final long newSize)
'''
pass
def addContent():
'''public void addContent(final ByteBuf buffer, final boolean last)
'''
pass
def delete():
'''public void delete()
'''
pass
def get():
'''public byte[] get()
'''
pass
def getByteBuf():
'''public ByteBuf getByteBuf()
'''
pass
def getCharset():
'''public Charset getCharset()
'''
pass
def getContentType():
'''public String getContentType()
'''
pass
def getContentTransferEncoding():
'''public String getContentTransferEncoding()
'''
pass
def getFilename():
'''public String getFilename()
'''
pass
def getString():
'''public String getString()
public String getString(final Charset encoding)
'''
pass
def isCompleted():
'''public boolean isCompleted()
'''
pass
def isInMemory():
'''public boolean isInMemory()
'''
pass
def length():
'''public long length()
'''
pass
def definedLength():
'''public long definedLength()
'''
pass
def renameTo():
'''public boolean renameTo(final File dest)
'''
pass
def setCharset():
'''public void setCharset(final Charset charset)
'''
pass
def setContent():
'''public void setContent(final ByteBuf buffer)
public void setContent(final File file)
public void setContent(final InputStream inputStream)
'''
pass
def setContentType():
'''public void setContentType(final String contentType)
'''
pass
def setContentTransferEncoding():
'''public void setContentTransferEncoding(final String contentTransferEncoding)
'''
pass
def setFilename():
'''public void setFilename(final String filename)
'''
pass
def getName():
'''public String getName()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def compareTo():
'''public int compareTo(final InterfaceHttpData o)
'''
pass
def toString():
'''public String toString()
'''
pass
def getChunk():
'''public ByteBuf getChunk(final int length)
'''
pass
def getFile():
'''public File getFile()
'''
pass
def copy():
'''public FileUpload copy()
'''
pass
def duplicate():
'''public FileUpload duplicate()
'''
pass
def retainedDuplicate():
'''public FileUpload retainedDuplicate()
'''
pass
def replace():
'''public FileUpload replace(final ByteBuf content)
'''
pass
def content():
'''public ByteBuf content()
'''
pass
def refCnt():
'''public int refCnt()
'''
pass
def retain():
'''public FileUpload retain()
public FileUpload retain(final int increment)
'''
pass
def touch():
'''public FileUpload touch()
public FileUpload touch(final Object hint)
'''
pass
def release():
'''public boolean release()
public boolean release(final int decrement)
'''
pass
