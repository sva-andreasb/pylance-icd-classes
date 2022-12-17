TYPE_FILE = "byte  1"
TYPE_DIRECTORY = "byte  2"
TYPE_SYMLINK = "byte  3"
TYPE_SOCKET = "byte  6"
TYPE_CHAR_DEVICE = "byte  7"
TYPE_BLOCK_DEVICE = "byte  8"
TYPE_FIFO = "byte  9"
def ():
    '''returns FileAttributes\n\n
    ()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object object)\n
    '''
def getFilename():
    '''returns String\n\n
    getFilename()\n
    '''
def setFilename():
    '''returns None\n\n
    setFilename(final String filename)\n
    '''
def getType():
    '''returns byte\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final byte type)\n
    '''
def getSize():
    '''returns long\n\n
    getSize()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final long size)\n
    '''
def getAllocationSize():
    '''returns long\n\n
    getAllocationSize()\n
    '''
def setAllocationSize():
    '''returns None\n\n
    setAllocationSize(final long size)\n
    '''
def getUID():
    '''returns int\n\n
    getUID()\n
    '''
def setUID():
    '''returns None\n\n
    setUID(final int uid)\n
    '''
def getGID():
    '''returns int\n\n
    getGID()\n
    '''
def setGID():
    '''returns None\n\n
    setGID(final int gid)\n
    '''
def getOwner():
    '''returns String\n\n
    getOwner()\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final String owner)\n
    '''
def getGroup():
    '''returns String\n\n
    getGroup()\n
    '''
def setGroup():
    '''returns None\n\n
    setGroup(final String group)\n
    '''
def getPermissions():
    '''returns int\n\n
    getPermissions()\n
    '''
def setPermissions():
    '''returns None\n\n
    setPermissions(final int permissions)\n
    '''
def getPermissionsAsString():
    '''returns String\n\n
    getPermissionsAsString()\n
    '''
def setPermissionsFromString():
    '''returns None\n\n
    setPermissionsFromString(final String permissionsString)\n
    '''
def getAccessDate():
    '''returns Date\n\n
    getAccessDate()\n
    '''
def setAccessDate():
    '''returns None\n\n
    setAccessDate(final Date accessTime)\n
    '''
def getCreationDate():
    '''returns Date\n\n
    getCreationDate()\n
    '''
def setCreationDate():
    '''returns None\n\n
    setCreationDate(final Date createTime)\n
    '''
def getModifyDate():
    '''returns Date\n\n
    getModifyDate()\n
    '''
def setModifyDate():
    '''returns None\n\n
    setModifyDate(final Date modifyTime)\n
    '''
def getACL():
    '''returns Acl\n\n
    getACL()\n
    '''
def isFile():
    '''returns boolean\n\n
    isFile()\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def isSymbolicLink():
    '''returns boolean\n\n
    isSymbolicLink()\n
    '''
def isSocket():
    '''returns boolean\n\n
    isSocket()\n
    '''
def isCharDevice():
    '''returns boolean\n\n
    isCharDevice()\n
    '''
def isBlockDevice():
    '''returns boolean\n\n
    isBlockDevice()\n
    '''
def isFIFO():
    '''returns boolean\n\n
    isFIFO()\n
    '''
def isReadOnly():
    '''returns boolean\n\n
    isReadOnly()\n
    '''
def isSystem():
    '''returns boolean\n\n
    isSystem()\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def isCaseInsensitive():
    '''returns boolean\n\n
    isCaseInsensitive()\n
    '''
def isArchived():
    '''returns boolean\n\n
    isArchived()\n
    '''
def isEncrypted():
    '''returns boolean\n\n
    isEncrypted()\n
    '''
def isCompressed():
    '''returns boolean\n\n
    isCompressed()\n
    '''
def isSparse():
    '''returns boolean\n\n
    isSparse()\n
    '''
def isAppendOnly():
    '''returns boolean\n\n
    isAppendOnly()\n
    '''
def isImmutable():
    '''returns boolean\n\n
    isImmutable()\n
    '''
def isSync():
    '''returns boolean\n\n
    isSync()\n
    '''
def isTranslationError():
    '''returns boolean\n\n
    isTranslationError()\n
    '''
def getTextHint():
    '''returns byte\n\n
    getTextHint()\n
    '''
def setTextHint():
    '''returns None\n\n
    setTextHint(final byte textHint)\n
    '''
def getMimeType():
    '''returns String\n\n
    getMimeType()\n
    '''
def setMimetype():
    '''returns None\n\n
    setMimetype(final String mimeType)\n
    '''
def getLinkCount():
    '''returns int\n\n
    getLinkCount()\n
    '''
def getUntranslatedName():
    '''returns String\n\n
    getUntranslatedName()\n
    '''
def setUntranslatedName():
    '''returns None\n\n
    setUntranslatedName(final String untranslatedName)\n
    '''
def getAttributesAsString():
    '''returns String\n\n
    getAttributesAsString(final int version)\n
    '''
