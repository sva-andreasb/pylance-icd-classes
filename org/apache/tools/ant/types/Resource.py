UNKNOWN_SIZE = "long  -1L"
UNKNOWN_DATETIME = "long  0L"
def ():
    '''returns Resource\n\n
    ()\n
    (final String name)\n
    (final String name, final boolean exists, final long lastmodified)\n
    (final String name, final boolean exists, final long lastmodified, final boolean directory)\n
    (final String name, final boolean exists, final long lastmodified, final boolean directory, final long size)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def isExists():
    '''returns boolean\n\n
    isExists()\n
    '''
def setExists():
    '''returns None\n\n
    setExists(final boolean exists)\n
    '''
def getLastModified():
    '''returns long\n\n
    getLastModified()\n
    '''
def setLastModified():
    '''returns None\n\n
    setLastModified(final long lastmodified)\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def setDirectory():
    '''returns None\n\n
    setDirectory(final boolean directory)\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final long size)\n
    '''
def getSize():
    '''returns long\n\n
    getSize()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object other)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isFilesystemOnly():
    '''returns boolean\n\n
    isFilesystemOnly()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setRefid():
    '''returns None\n\n
    setRefid(final Reference r)\n
    '''
def as():
    '''returns Object\n\n
    as(final Class clazz)\n
    '''
