def setContent():
    '''returns None\n\n
    setContent(final ByteBuf buffer)\n
    setContent(final File file)\n
    setContent(final InputStream inputStream)\n
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
def getChunk():
    '''returns ByteBuf\n\n
    getChunk(final int length)\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    getString(final Charset encoding)\n
    '''
def isInMemory():
    '''returns boolean\n\n
    isInMemory()\n
    '''
def renameTo():
    '''returns boolean\n\n
    renameTo(final File dest)\n
    '''
def getFile():
    '''returns File\n\n
    getFile()\n
    '''
def touch():
    '''returns HttpData\n\n
    touch()\n
    touch(final Object hint)\n
    '''
