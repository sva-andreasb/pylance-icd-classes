TYPE_FILE = "byte  1"
TYPE_DIRECTORY = "byte  2"
TYPE_SYMLINK = "byte  3"
TYPE_SOCKET = "byte  6"
TYPE_CHAR_DEVICE = "byte  7"
TYPE_BLOCK_DEVICE = "byte  8"
TYPE_FIFO = "byte  9"
def FileAttributes():
    '''public FileAttributes()
    '''
def compareTo():
    '''public int compareTo(final Object object)
    '''
def getFilename():
    '''public String getFilename()
    '''
def setFilename():
    '''public void setFilename(final String filename)
    '''
def getType():
    '''public byte getType()
    '''
def setType():
    '''public void setType(final byte type)
    '''
def getSize():
    '''public long getSize()
    '''
def setSize():
    '''public void setSize(final long size)
    '''
def getAllocationSize():
    '''public long getAllocationSize()
    '''
def setAllocationSize():
    '''public void setAllocationSize(final long size)
    '''
def getUID():
    '''public int getUID()
    '''
def setUID():
    '''public void setUID(final int uid)
    '''
def getGID():
    '''public int getGID()
    '''
def setGID():
    '''public void setGID(final int gid)
    '''
def getOwner():
    '''public String getOwner()
    '''
def setOwner():
    '''public void setOwner(final String owner)
    '''
def getGroup():
    '''public String getGroup()
    '''
def setGroup():
    '''public void setGroup(final String group)
    '''
def getPermissions():
    '''public int getPermissions()
    '''
def setPermissions():
    '''public void setPermissions(final int permissions)
    '''
def getPermissionsAsString():
    '''public String getPermissionsAsString()
    '''
def setPermissionsFromString():
    '''public void setPermissionsFromString(final String permissionsString)
    '''
def getAccessDate():
    '''public Date getAccessDate()
    '''
def setAccessDate():
    '''public void setAccessDate(final Date accessTime)
    '''
def getCreationDate():
    '''public Date getCreationDate()
    '''
def setCreationDate():
    '''public void setCreationDate(final Date createTime)
    '''
def getModifyDate():
    '''public Date getModifyDate()
    '''
def setModifyDate():
    '''public void setModifyDate(final Date modifyTime)
    '''
def getACL():
    '''public Acl getACL()
    '''
def isFile():
    '''public boolean isFile()
    '''
def isDirectory():
    '''public boolean isDirectory()
    '''
def isSymbolicLink():
    '''public boolean isSymbolicLink()
    '''
def isSocket():
    '''public boolean isSocket()
    '''
def isCharDevice():
    '''public boolean isCharDevice()
    '''
def isBlockDevice():
    '''public boolean isBlockDevice()
    '''
def isFIFO():
    '''public boolean isFIFO()
    '''
def isReadOnly():
    '''public boolean isReadOnly()
    '''
def isSystem():
    '''public boolean isSystem()
    '''
def isHidden():
    '''public boolean isHidden()
    '''
def isCaseInsensitive():
    '''public boolean isCaseInsensitive()
    '''
def isArchived():
    '''public boolean isArchived()
    '''
def isEncrypted():
    '''public boolean isEncrypted()
    '''
def isCompressed():
    '''public boolean isCompressed()
    '''
def isSparse():
    '''public boolean isSparse()
    '''
def isAppendOnly():
    '''public boolean isAppendOnly()
    '''
def isImmutable():
    '''public boolean isImmutable()
    '''
def isSync():
    '''public boolean isSync()
    '''
def isTranslationError():
    '''public boolean isTranslationError()
    '''
def getTextHint():
    '''public byte getTextHint()
    '''
def setTextHint():
    '''public void setTextHint(final byte textHint)
    '''
def getMimeType():
    '''public String getMimeType()
    '''
def setMimetype():
    '''public void setMimetype(final String mimeType)
    '''
def getLinkCount():
    '''public int getLinkCount()
    '''
def getUntranslatedName():
    '''public String getUntranslatedName()
    '''
def setUntranslatedName():
    '''public void setUntranslatedName(final String untranslatedName)
    '''
def getAttributesAsString():
    '''public String getAttributesAsString(final int version)
    '''
