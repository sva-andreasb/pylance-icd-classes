MAX_NAMELEN = "int  31"
DEFAULT_DIR_MODE = "int  16877"
DEFAULT_FILE_MODE = "int  33188"
MILLIS_PER_SECOND = "int  1000"
def ():
    '''returns TarEntry\n\n
    (final String name)\n
    (String name, final boolean preserveLeadingSlashes)\n
    (final String name, final byte linkFlag)\n
    (final File file)\n
    (final byte[] headerBuf)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final TarEntry it)\n
    equals(final Object it)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def isDescendent():
    '''returns boolean\n\n
    isDescendent(final TarEntry desc)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int mode)\n
    '''
def getLinkName():
    '''returns String\n\n
    getLinkName()\n
    '''
def getUserId():
    '''returns int\n\n
    getUserId()\n
    '''
def setUserId():
    '''returns None\n\n
    setUserId(final int userId)\n
    '''
def getGroupId():
    '''returns int\n\n
    getGroupId()\n
    '''
def setGroupId():
    '''returns None\n\n
    setGroupId(final int groupId)\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final String userName)\n
    '''
def getGroupName():
    '''returns String\n\n
    getGroupName()\n
    '''
def setGroupName():
    '''returns None\n\n
    setGroupName(final String groupName)\n
    '''
def setIds():
    '''returns None\n\n
    setIds(final int userId, final int groupId)\n
    '''
def setNames():
    '''returns None\n\n
    setNames(final String userName, final String groupName)\n
    '''
def setModTime():
    '''returns None\n\n
    setModTime(final long time)\n
    setModTime(final Date time)\n
    '''
def getModTime():
    '''returns Date\n\n
    getModTime()\n
    '''
def getFile():
    '''returns File\n\n
    getFile()\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def getSize():
    '''returns long\n\n
    getSize()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final long size)\n
    '''
def isGNULongNameEntry():
    '''returns boolean\n\n
    isGNULongNameEntry()\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def getDirectoryEntries():
    '''returns TarEntry[]\n\n
    getDirectoryEntries()\n
    '''
def writeEntryHeader():
    '''returns None\n\n
    writeEntryHeader(final byte[] outbuf)\n
    '''
def parseTarHeader():
    '''returns None\n\n
    parseTarHeader(final byte[] header)\n
    '''
