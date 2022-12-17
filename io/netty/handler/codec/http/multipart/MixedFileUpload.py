def ():
    '''returns MixedFileUpload\n\n
    (final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize)\n
    (final String name, final String filename, final String contentType, final String contentTransferEncoding, final Charset charset, final long size, final long limitSize, final String baseDir, final boolean deleteOnExit)\n
    '''
def getMaxSize():
    '''returns long\n\n
    getMaxSize()\n
    '''
def setMaxSize():
    '''returns None\n\n
    setMaxSize(final long maxSize)\n
    '''
def checkSize():
    '''returns None\n\n
    checkSize(final long newSize)\n
    '''
def addContent():
    '''returns None\n\n
    addContent(final ByteBuf buffer, final boolean last)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns byte[]\n\n
    get()\n
    '''
def getByteBuf():
    '''returns ByteBuf\n\n
    getByteBuf()\n
    '''
def getCharset():
    '''returns Charset\n\n
    getCharset()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def getContentTransferEncoding():
    '''returns String\n\n
    getContentTransferEncoding()\n
    '''
def getFilename():
    '''returns String\n\n
    getFilename()\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    getString(final Charset encoding)\n
    '''
def isCompleted():
    '''returns boolean\n\n
    isCompleted()\n
    '''
def isInMemory():
    '''returns boolean\n\n
    isInMemory()\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def definedLength():
    '''returns long\n\n
    definedLength()\n
    '''
def renameTo():
    '''returns boolean\n\n
    renameTo(final File dest)\n
    '''
def setCharset():
    '''returns None\n\n
    setCharset(final Charset charset)\n
    '''
def setContent():
    '''returns None\n\n
    setContent(final ByteBuf buffer)\n
    setContent(final File file)\n
    setContent(final InputStream inputStream)\n
    '''
def setContentType():
    '''returns None\n\n
    setContentType(final String contentType)\n
    '''
def setContentTransferEncoding():
    '''returns None\n\n
    setContentTransferEncoding(final String contentTransferEncoding)\n
    '''
def setFilename():
    '''returns None\n\n
    setFilename(final String filename)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final InterfaceHttpData o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getChunk():
    '''returns ByteBuf\n\n
    getChunk(final int length)\n
    '''
def getFile():
    '''returns File\n\n
    getFile()\n
    '''
def copy():
    '''returns FileUpload\n\n
    copy()\n
    '''
def duplicate():
    '''returns FileUpload\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns FileUpload\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns FileUpload\n\n
    replace(final ByteBuf content)\n
    '''
def content():
    '''returns ByteBuf\n\n
    content()\n
    '''
def refCnt():
    '''returns int\n\n
    refCnt()\n
    '''
def retain():
    '''returns FileUpload\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns FileUpload\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    release(final int decrement)\n
    '''
