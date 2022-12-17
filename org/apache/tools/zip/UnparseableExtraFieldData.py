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
def parseFromLocalFileData():
    '''returns None\n\n
    parseFromLocalFileData(final byte[] buffer, final int offset, final int length)\n
    '''
def parseFromCentralDirectoryData():
    '''returns None\n\n
    parseFromCentralDirectoryData(final byte[] buffer, final int offset, final int length)\n
    '''
