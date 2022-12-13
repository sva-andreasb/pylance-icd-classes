def Struct():
'''public Struct(final Schema schema)
'''
pass
def schema():
'''public Schema schema()
'''
pass
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
pass
def getOrElse():
'''public Long getOrElse(final Field.Int64 field, final long alternative)
public Short getOrElse(final Field.Int16 field, final short alternative)
public Integer getOrElse(final Field.Int32 field, final int alternative)
public String getOrElse(final Field.NullableStr field, final String alternative)
public String getOrElse(final Field.Str field, final String alternative)
'''
pass
def hasField():
'''public boolean hasField(final String name)
public boolean hasField(final Field def)
'''
pass
def getStruct():
'''public Struct getStruct(final BoundField field)
public Struct getStruct(final String name)
'''
pass
def getByte():
'''public Byte getByte(final BoundField field)
public byte getByte(final String name)
'''
pass
def getRecords():
'''public Records getRecords(final String name)
'''
pass
def getShort():
'''public Short getShort(final BoundField field)
public Short getShort(final String name)
'''
pass
def getInt():
'''public Integer getInt(final BoundField field)
public Integer getInt(final String name)
'''
pass
def getUnsignedInt():
'''public Long getUnsignedInt(final String name)
'''
pass
def getLong():
'''public Long getLong(final BoundField field)
public Long getLong(final String name)
'''
pass
def getArray():
'''public Object[] getArray(final BoundField field)
public Object[] getArray(final String name)
'''
pass
def getString():
'''public String getString(final BoundField field)
public String getString(final String name)
'''
pass
def getBoolean():
'''public Boolean getBoolean(final BoundField field)
public Boolean getBoolean(final String name)
'''
pass
def getBytes():
'''public ByteBuffer getBytes(final BoundField field)
public ByteBuffer getBytes(final String name)
'''
pass
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
pass
def setIfExists():
'''public Struct setIfExists(final Field def, final Object value)
public Struct setIfExists(final String fieldName, final Object value)
'''
pass
def instance():
'''public Struct instance(final BoundField field)
public Struct instance(final String field)
'''
pass
def clear():
'''public void clear()
'''
pass
def sizeOf():
'''public int sizeOf()
'''
pass
def writeTo():
'''public void writeTo(final ByteBuffer buffer)
'''
pass
def validate():
'''public void validate()
'''
pass
def toString():
'''public String toString()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
