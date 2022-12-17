sid = "short  215"
BLOCK_SIZE = "int  32"
def ():
    '''returns Builder\n\n
    (final RecordInputStream in)\n
    ()\n
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
    '''returns DBCellRecord\n\n
    clone()\n
    '''
def addCellOffset():
    '''returns None\n\n
    addCellOffset(final int cellRefOffset)\n
    '''
def build():
    '''returns DBCellRecord\n\n
    build(final int rowOffset)\n
    '''
