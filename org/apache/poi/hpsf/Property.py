DEFAULT_CODEPAGE = "int  1252"
def Property():
    '''public Property()
    public Property(final Property p)
    public Property(final long id, final long type, final Object value)
    public Property(final long id, final byte[] src, final long offset, final int length, final int codepage)
    public Property(final long id, final LittleEndianByteArrayInputStream leis, final int length, final int codepage)
    '''
def getID():
    '''public long getID()
    '''
def setID():
    '''public void setID(final long id)
    '''
def getType():
    '''public long getType()
    '''
def setType():
    '''public void setType(final long type)
    '''
def getValue():
    '''public Object getValue()
    '''
def setValue():
    '''public void setValue(final Object value)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    public String toString(final int codepage, final PropertyIDMap idMap)
    '''
def write():
    '''public int write(final OutputStream out, final int codepage)
    '''
