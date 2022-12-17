NO = "int  -1"
YES = "int  1"
def ():
    '''returns SegmentInfo\n\n
    (final Directory dir, final Version version, final Version minVersion, final String name, final int maxDoc, final boolean isCompoundFile, final Codec codec, final Map<String, String> diagnostics, final byte[] id, final Map<String, String> attributes, final Sort indexSort)\n
    '''
def getUseCompoundFile():
    '''returns boolean\n\n
    getUseCompoundFile()\n
    '''
def setCodec():
    '''returns None\n\n
    setCodec(final Codec codec)\n
    '''
def getCodec():
    '''returns Codec\n\n
    getCodec()\n
    '''
def maxDoc():
    '''returns int\n\n
    maxDoc()\n
    '''
def files():
    '''returns Set<String>\n\n
    files()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final int delCount)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getVersion():
    '''returns Version\n\n
    getVersion()\n
    '''
def getMinVersion():
    '''returns Version\n\n
    getMinVersion()\n
    '''
def getId():
    '''returns byte[]\n\n
    getId()\n
    '''
def setFiles():
    '''returns None\n\n
    setFiles(final Collection<String> files)\n
    '''
def addFiles():
    '''returns None\n\n
    addFiles(final Collection<String> files)\n
    '''
def addFile():
    '''returns None\n\n
    addFile(final String file)\n
    '''
def getAttribute():
    '''returns String\n\n
    getAttribute(final String key)\n
    '''
def putAttribute():
    '''returns String\n\n
    putAttribute(final String key, final String value)\n
    '''
def getIndexSort():
    '''returns Sort\n\n
    getIndexSort()\n
    '''
