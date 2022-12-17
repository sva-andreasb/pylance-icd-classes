def ():
    '''returns Struct\n\n
    (final Schema schema)\n
    '''
def schema():
    '''returns Schema\n\n
    schema()\n
    '''
def get():
    '''returns Object\n\n
    get(final BoundField field)\n
    get(final Field.Int8 field)\n
    get(final Field.Int32 field)\n
    get(final Field.Int64 field)\n
    get(final Field.Int16 field)\n
    get(final Field.Str field)\n
    get(final Field.NullableStr field)\n
    get(final String name)\n
    '''
def getOrElse():
    '''returns String\n\n
    getOrElse(final Field.Int64 field, final long alternative)\n
    getOrElse(final Field.Int16 field, final short alternative)\n
    getOrElse(final Field.Int32 field, final int alternative)\n
    getOrElse(final Field.NullableStr field, final String alternative)\n
    getOrElse(final Field.Str field, final String alternative)\n
    '''
def hasField():
    '''returns boolean\n\n
    hasField(final String name)\n
    hasField(final Field def)\n
    '''
def getStruct():
    '''returns Struct\n\n
    getStruct(final BoundField field)\n
    getStruct(final String name)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final BoundField field)\n
    getByte(final String name)\n
    '''
def getRecords():
    '''returns Records\n\n
    getRecords(final String name)\n
    '''
def getShort():
    '''returns Short\n\n
    getShort(final BoundField field)\n
    getShort(final String name)\n
    '''
def getInt():
    '''returns Integer\n\n
    getInt(final BoundField field)\n
    getInt(final String name)\n
    '''
def getUnsignedInt():
    '''returns Long\n\n
    getUnsignedInt(final String name)\n
    '''
def getLong():
    '''returns Long\n\n
    getLong(final BoundField field)\n
    getLong(final String name)\n
    '''
def getArray():
    '''returns Object[]\n\n
    getArray(final BoundField field)\n
    getArray(final String name)\n
    '''
def getString():
    '''returns String\n\n
    getString(final BoundField field)\n
    getString(final String name)\n
    '''
def getBoolean():
    '''returns Boolean\n\n
    getBoolean(final BoundField field)\n
    getBoolean(final String name)\n
    '''
def getBytes():
    '''returns ByteBuffer\n\n
    getBytes(final BoundField field)\n
    getBytes(final String name)\n
    '''
def set():
    '''returns Struct\n\n
    set(final BoundField field, final Object value)\n
    set(final String name, final Object value)\n
    set(final Field.Str def, final String value)\n
    set(final Field.NullableStr def, final String value)\n
    set(final Field.Int8 def, final byte value)\n
    set(final Field.Int32 def, final int value)\n
    set(final Field.Int64 def, final long value)\n
    set(final Field.Int16 def, final short value)\n
    '''
def setIfExists():
    '''returns Struct\n\n
    setIfExists(final Field def, final Object value)\n
    setIfExists(final String fieldName, final Object value)\n
    '''
def instance():
    '''returns Struct\n\n
    instance(final BoundField field)\n
    instance(final String field)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def sizeOf():
    '''returns int\n\n
    sizeOf()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final ByteBuffer buffer)\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
