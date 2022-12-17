PLATFORM_UNIX = "int  3"
PLATFORM_FAT = "int  0"
def ():
    '''returns ZipEntry\n\n
    (final String name)\n
    (final java.util.zip.ZipEntry entry)\n
    (final ZipEntry entry)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getInternalAttributes():
    '''returns int\n\n
    getInternalAttributes()\n
    '''
def setInternalAttributes():
    '''returns None\n\n
    setInternalAttributes(final int value)\n
    '''
def getExternalAttributes():
    '''returns long\n\n
    getExternalAttributes()\n
    '''
def setExternalAttributes():
    '''returns None\n\n
    setExternalAttributes(final long value)\n
    '''
def setUnixMode():
    '''returns None\n\n
    setUnixMode(final int mode)\n
    '''
def getUnixMode():
    '''returns int\n\n
    getUnixMode()\n
    '''
def getPlatform():
    '''returns int\n\n
    getPlatform()\n
    '''
def setExtraFields():
    '''returns None\n\n
    setExtraFields(final ZipExtraField[] fields)\n
    '''
def getExtraFields():
    '''returns ZipExtraField[]\n\n
    getExtraFields()\n
    getExtraFields(final boolean includeUnparseable)\n
    '''
def addExtraField():
    '''returns None\n\n
    addExtraField(final ZipExtraField ze)\n
    '''
def addAsFirstExtraField():
    '''returns None\n\n
    addAsFirstExtraField(final ZipExtraField ze)\n
    '''
def removeExtraField():
    '''returns None\n\n
    removeExtraField(final ZipShort type)\n
    '''
def removeUnparseableExtraFieldData():
    '''returns None\n\n
    removeUnparseableExtraFieldData()\n
    '''
def getExtraField():
    '''returns ZipExtraField\n\n
    getExtraField(final ZipShort type)\n
    '''
def getUnparseableExtraFieldData():
    '''returns UnparseableExtraFieldData\n\n
    getUnparseableExtraFieldData()\n
    '''
def setExtra():
    '''returns None\n\n
    setExtra(final byte[] extra)\n
    '''
def setCentralDirectoryExtra():
    '''returns None\n\n
    setCentralDirectoryExtra(final byte[] b)\n
    '''
def getLocalFileDataExtra():
    '''returns byte[]\n\n
    getLocalFileDataExtra()\n
    '''
def getCentralDirectoryExtra():
    '''returns byte[]\n\n
    getCentralDirectoryExtra()\n
    '''
def setComprSize():
    '''returns None\n\n
    setComprSize(final long size)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isDirectory():
    '''returns boolean\n\n
    isDirectory()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
