OS_WIN16 = "int  0"
OS_MACINTOSH = "int  1"
OS_WIN32 = "int  2"
def ():
    '''returns PropertySet\n\n
    ()\n
    (final InputStream stream)\n
    (final byte[] stream, final int offset, final int length)\n
    (final byte[] stream)\n
    (final PropertySet ps)\n
    '''
def getByteOrder():
    '''returns int\n\n
    getByteOrder()\n
    '''
def setByteOrder():
    '''returns None\n\n
    setByteOrder(final int byteOrder)\n
    '''
def getFormat():
    '''returns int\n\n
    getFormat()\n
    '''
def setFormat():
    '''returns None\n\n
    setFormat(final int format)\n
    '''
def getOSVersion():
    '''returns int\n\n
    getOSVersion()\n
    '''
def setOSVersion():
    '''returns None\n\n
    setOSVersion(final int osVersion)\n
    '''
def getClassID():
    '''returns ClassID\n\n
    getClassID()\n
    '''
def setClassID():
    '''returns None\n\n
    setClassID(final ClassID classID)\n
    '''
def getSectionCount():
    '''returns int\n\n
    getSectionCount()\n
    '''
def getSections():
    '''returns List<Section>\n\n
    getSections()\n
    '''
def addSection():
    '''returns None\n\n
    addSection(final Section section)\n
    '''
def clearSections():
    '''returns None\n\n
    clearSections()\n
    '''
def getPropertySetIDMap():
    '''returns PropertyIDMap\n\n
    getPropertySetIDMap()\n
    '''
def write():
    '''returns None\n\n
    write(final OutputStream out)\n
    write(final DirectoryEntry dir, final String name)\n
    '''
def toInputStream():
    '''returns InputStream\n\n
    toInputStream()\n
    '''
def isSummaryInformation():
    '''returns boolean\n\n
    isSummaryInformation()\n
    '''
def isDocumentSummaryInformation():
    '''returns boolean\n\n
    isDocumentSummaryInformation()\n
    '''
def getProperties():
    '''returns Property[]\n\n
    getProperties()\n
    '''
def wasNull():
    '''returns boolean\n\n
    wasNull()\n
    '''
def getFirstSection():
    '''returns Section\n\n
    getFirstSection()\n
    '''
def getSingleSection():
    '''returns Section\n\n
    getSingleSection()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
