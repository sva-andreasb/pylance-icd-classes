sid = "short  7"
length = "short  2"
METAFILE_BIT = "short  2"
BITMAP_BIT = "short  9"
UNSPECIFIED_BIT = "short  -1"
def ():
    '''returns FtCfSubRecord\n\n
    ()\n
    (final LittleEndianInput in, final int size)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def clone():
    '''returns FtCfSubRecord\n\n
    clone()\n
    '''
def getFlags():
    '''returns short\n\n
    getFlags()\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final short flags)\n
    '''
