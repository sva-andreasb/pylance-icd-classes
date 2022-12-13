def MixedFileUpload():
    '''    public MixedFileUpload(final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize)
    public MixedFileUpload(final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize, final String baseDir, final boolean deleteOnExit)
    '''
def getMaxSize():
    '''    public long getMaxSize()
    '''
def setMaxSize():
    '''    public void setMaxSize(final long maxSize)
    '''
def checkSize():
    '''    public void checkSize(final long newSize)
    '''
def addContent():
    '''    public void addContent(final ByteBuf buffer, final boolean last)
    '''
def delete():
    '''    public void delete()
    '''
def get():
    '''    public byte[] get()
    '''
def getByteBuf():
    '''    public ByteBuf getByteBuf()
    '''
def getCharset():
    '''    public Charset getCharset()
    '''
def getContentType():
    '''    public String getContentType()
    '''
def getContentTransferEncoding():
    '''    public String getContentTransferEncoding()
    '''
def getFilename():
    '''    public String getFilename()
    '''
def getString():
    '''    public String getString()
    public String getString(final Charset encoding)
    '''
def isCompleted():
    '''    public boolean isCompleted()
    '''
def isInMemory():
    '''    public boolean isInMemory()
    '''
def length():
    '''    public long length()
    '''
def definedLength():
    '''    public long definedLength()
    '''
def renameTo():
    '''    public boolean renameTo(final File dest)
    '''
def setCharset():
    '''    public void setCharset(final Charset charset)
    '''
def setContent():
    '''    public void setContent(final ByteBuf buffer)
    public void setContent(final File file)
    public void setContent(final InputStream inputStream)
    '''
def setContentType():
    '''    public void setContentType(final String contentType)
    '''
def setContentTransferEncoding():
    '''    public void setContentTransferEncoding(final String contentTransferEncoding)
    '''
def setFilename():
    '''    public void setFilename(final String filename)
    '''
def getName():
    '''    public String getName()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
def compareTo():
    '''    public int compareTo(final InterfaceHttpData o)
    '''
def toString():
    '''    public String toString()
    '''
def getChunk():
    '''    public ByteBuf getChunk(final int length)
    '''
def getFile():
    '''    public File getFile()
    '''
def copy():
    '''    public FileUpload copy()
    '''
def duplicate():
    '''    public FileUpload duplicate()
    '''
def retainedDuplicate():
    '''    public FileUpload retainedDuplicate()
    '''
def replace():
    '''    public FileUpload replace(final ByteBuf content)
    '''
def content():
    '''    public ByteBuf content()
    '''
def refCnt():
    '''    public int refCnt()
    '''
def retain():
    '''    public FileUpload retain()
    public FileUpload retain(final int increment)
    '''
def touch():
    '''    public FileUpload touch()
    public FileUpload touch(final Object hint)
    '''
def release():
    '''    public boolean release()
    public boolean release(final int decrement)
    '''
