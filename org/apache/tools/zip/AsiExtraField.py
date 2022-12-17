def ():
    '''returns AsiExtraField\n\n
    ()\n
    '''
def getHeaderId():
    '''returns ZipShort\n\n
    getHeaderId()\n
    '''
def getLocalFileDataLength():
    '''returns ZipShort\n\n
    getLocalFileDataLength()\n
    '''
def getCentralDirectoryLength():
    '''returns ZipShort\n\n
    getCentralDirectoryLength()\n
    '''
def getLocalFileDataData():
    '''returns byte[]\n\n
    getLocalFileDataData()\n
    '''
def getCentralDirectoryData():
    '''returns byte[]\n\n
    getCentralDirectoryData()\n
    '''
def setUserId():
    '''returns None\n\n
    setUserId(final int uid)\n
    '''
def getUserId():
    '''returns int\n\n
    getUserId()\n
    '''
def setGroupId():
    '''returns None\n\n
    setGroupId(final int gid)\n
    '''
def getGroupId():
    '''returns int\n\n
    getGroupId()\n
    '''
def setLinkedFile():
    '''returns None\n\n
    setLinkedFile(final String name)\n
    '''
def getLinkedFile():
    '''returns String\n\n
    getLinkedFile()\n
    '''
def isLink():
    '''returns boolean\n\n
    isLink()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final int mode)\n
    '''
def getMode():
    '''returns int\n\n
    getMode()\n
    '''
def setDirectory():
    '''returns None\n\n
    setDirectory(final boolean dirFlag)\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def parseFromLocalFileData():
    '''returns None\n\n
    parseFromLocalFileData(final byte[] data, final int offset, final int length)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
