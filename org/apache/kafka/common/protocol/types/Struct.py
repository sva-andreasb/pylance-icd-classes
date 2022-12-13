def Struct():
    '''public Struct(final Schema schema)
    '''
def schema():
    '''public Schema schema()
    '''
def get():
    '''public Object get(final BoundField field)
    public Byte get(final Field.Int8 field)
    public Integer get(final Field.Int32 field)
    public Long get(final Field.Int64 field)
    public Short get(final Field.Int16 field)
    public String get(final Field.Str field)
    public String get(final Field.NullableStr field)
    public Object get(final String name)
    '''
def getOrElse():
    '''public Long getOrElse(final Field.Int64 field, final long alternative)
    public Short getOrElse(final Field.Int16 field, final short alternative)
    public Integer getOrElse(final Field.Int32 field, final int alternative)
    public String getOrElse(final Field.NullableStr field, final String alternative)
    public String getOrElse(final Field.Str field, final String alternative)
    '''
def hasField():
    '''public boolean hasField(final String name)
    public boolean hasField(final Field def)
    '''
def getStruct():
    '''public Struct getStruct(final BoundField field)
    public Struct getStruct(final String name)
    '''
def getByte():
    '''public Byte getByte(final BoundField field)
    public byte getByte(final String name)
    '''
def getRecords():
    '''public Records getRecords(final String name)
    '''
def getShort():
    '''public Short getShort(final BoundField field)
    public Short getShort(final String name)
    '''
def getInt():
    '''public Integer getInt(final BoundField field)
    public Integer getInt(final String name)
    '''
def getUnsignedInt():
    '''public Long getUnsignedInt(final String name)
    '''
def getLong():
    '''public Long getLong(final BoundField field)
    public Long getLong(final String name)
    '''
def getArray():
    '''public Object[] getArray(final BoundField field)
    public Object[] getArray(final String name)
    '''
def getString():
    '''public String getString(final BoundField field)
    public String getString(final String name)
    '''
def getBoolean():
    '''public Boolean getBoolean(final BoundField field)
    public Boolean getBoolean(final String name)
    '''
def getBytes():
    '''public ByteBuffer getBytes(final BoundField field)
    public ByteBuffer getBytes(final String name)
    '''
def set():
    '''public Struct set(final BoundField field, final Object value)
    public Struct set(final String name, final Object value)
    public Struct set(final Field.Str def, final String value)
    public Struct set(final Field.NullableStr def, final String value)
    public Struct set(final Field.Int8 def, final byte value)
    public Struct set(final Field.Int32 def, final int value)
    public Struct set(final Field.Int64 def, final long value)
    public Struct set(final Field.Int16 def, final short value)
    '''
def setIfExists():
    '''public Struct setIfExists(final Field def, final Object value)
    public Struct setIfExists(final String fieldName, final Object value)
    '''
def instance():
    '''public Struct instance(final BoundField field)
    public Struct instance(final String field)
    '''
def clear():
    '''public void clear()
    '''
def sizeOf():
    '''public int sizeOf()
    '''
def writeTo():
    '''public void writeTo(final ByteBuffer buffer)
    '''
def validate():
    '''public void validate()
    '''
def toString():
    '''public String toString()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
