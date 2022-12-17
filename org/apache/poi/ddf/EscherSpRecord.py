RECORD_ID = "short  -4086"
RECORD_DESCRIPTION = "String  \"MsofbtSp\""
FLAG_GROUP = "int  1"
FLAG_CHILD = "int  2"
FLAG_PATRIARCH = "int  4"
FLAG_DELETED = "int  8"
FLAG_OLESHAPE = "int  16"
FLAG_HAVEMASTER = "int  32"
FLAG_FLIPHORIZ = "int  64"
FLAG_FLIPVERT = "int  128"
FLAG_CONNECTOR = "int  256"
FLAG_HAVEANCHOR = "int  512"
FLAG_BACKGROUND = "int  1024"
FLAG_HASSHAPETYPE = "int  2048"
def fillFields():
    '''returns int\n\n
    fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data, final EscherSerializationListener listener)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def getRecordId():
    '''returns short\n\n
    getRecordId()\n
    '''
def getRecordName():
    '''returns String\n\n
    getRecordName()\n
    '''
def getShapeId():
    '''returns int\n\n
    getShapeId()\n
    '''
def setShapeId():
    '''returns None\n\n
    setShapeId(final int field_1_shapeId)\n
    '''
def getFlags():
    '''returns int\n\n
    getFlags()\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final int field_2_flags)\n
    '''
def getShapeType():
    '''returns short\n\n
    getShapeType()\n
    '''
def setShapeType():
    '''returns None\n\n
    setShapeType(final short value)\n
    '''
