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
def FTPFile():
    '''    public FTPFile()
    '''
def setRawListing():
    '''    public void setRawListing(final String rawListing)
    '''
def getRawListing():
    '''    public String getRawListing()
    '''
def isDirectory():
    '''    public boolean isDirectory()
    '''
def isFile():
    '''    public boolean isFile()
    '''
def isSymbolicLink():
    '''    public boolean isSymbolicLink()
    '''
def isUnknown():
    '''    public boolean isUnknown()
    '''
def setType():
    '''    public void setType(final int type)
    '''
def getType():
    '''    public int getType()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getName():
    '''    public String getName()
    '''
def setSize():
    '''    public void setSize(final long size)
    '''
def getSize():
    '''    public long getSize()
    '''
def setHardLinkCount():
    '''    public void setHardLinkCount(final int links)
    '''
def getHardLinkCount():
    '''    public int getHardLinkCount()
    '''
def setGroup():
    '''    public void setGroup(final String group)
    '''
def getGroup():
    '''    public String getGroup()
    '''
def setUser():
    '''    public void setUser(final String user)
    '''
def getUser():
    '''    public String getUser()
    '''
def setLink():
    '''    public void setLink(final String link)
    '''
def getLink():
    '''    public String getLink()
    '''
def setTimestamp():
    '''    public void setTimestamp(final Calendar date)
    '''
def getTimestamp():
    '''    public Calendar getTimestamp()
    '''
def setPermission():
    '''    public void setPermission(final int access, final int permission, final boolean value)
    '''
def hasPermission():
    '''    public boolean hasPermission(final int access, final int permission)
    '''
def toString():
    '''    public String toString()
    '''
