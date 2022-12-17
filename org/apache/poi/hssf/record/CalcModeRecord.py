sid = "short  13"
MANUAL = "short  0"
AUTOMATIC = "short  1"
AUTOMATIC_EXCEPT_TABLES = "short  -1"
def ():
    '''returns CalcModeRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def setCalcMode():
    '''returns None\n\n
    setCalcMode(final short calcmode)\n
    '''
def getCalcMode():
    '''returns short\n\n
    getCalcMode()\n
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
    '''returns CalcModeRecord\n\n
    clone()\n
    '''
