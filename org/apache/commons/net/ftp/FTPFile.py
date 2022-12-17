FILE_TYPE = "int  0"
DIRECTORY_TYPE = "int  1"
SYMBOLIC_LINK_TYPE = "int  2"
UNKNOWN_TYPE = "int  3"
USER_ACCESS = "int  0"
GROUP_ACCESS = "int  1"
WORLD_ACCESS = "int  2"
READ_PERMISSION = "int  0"
WRITE_PERMISSION = "int  1"
EXECUTE_PERMISSION = "int  2"
def ():
    '''returns FTPFile\n\n
    ()\n
    '''
def setRawListing():
    '''returns None\n\n
    setRawListing(final String rawListing)\n
    '''
def getRawListing():
    '''returns String\n\n
    getRawListing()\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def isFile():
    '''returns boolean\n\n
    isFile()\n
    '''
def isSymbolicLink():
    '''returns boolean\n\n
    isSymbolicLink()\n
    '''
def isUnknown():
    '''returns boolean\n\n
    isUnknown()\n
    '''
def setType():
    '''returns None\n\n
    setType(final int type)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final long size)\n
    '''
def getSize():
    '''returns long\n\n
    getSize()\n
    '''
def setHardLinkCount():
    '''returns None\n\n
    setHardLinkCount(final int links)\n
    '''
def getHardLinkCount():
    '''returns int\n\n
    getHardLinkCount()\n
    '''
def setGroup():
    '''returns None\n\n
    setGroup(final String group)\n
    '''
def getGroup():
    '''returns String\n\n
    getGroup()\n
    '''
def setUser():
    '''returns None\n\n
    setUser(final String user)\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def setLink():
    '''returns None\n\n
    setLink(final String link)\n
    '''
def getLink():
    '''returns String\n\n
    getLink()\n
    '''
def setTimestamp():
    '''returns None\n\n
    setTimestamp(final Calendar date)\n
    '''
def getTimestamp():
    '''returns Calendar\n\n
    getTimestamp()\n
    '''
def setPermission():
    '''returns None\n\n
    setPermission(final int access, final int permission, final boolean value)\n
    '''
def hasPermission():
    '''returns boolean\n\n
    hasPermission(final int access, final int permission)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
