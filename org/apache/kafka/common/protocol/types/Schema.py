def Schema():
    '''    public Schema(final Field... fs)
    '''
def write():
    '''    public void write(final ByteBuffer buffer, final Object o)
    '''
def read():
    '''    public Struct read(final ByteBuffer buffer)
    '''
def sizeOf():
    '''    public int sizeOf(final Object o)
    '''
def numFields():
    '''    public int numFields()
    '''
def get():
    '''    public BoundField get(final int slot)
    public BoundField get(final String name)
    '''
def fields():
    '''    public BoundField[] fields()
    '''
def toString():
    '''    public String toString()
    '''
def validate():
    '''    public Struct validate(final Object item)
    '''
def walk():
    '''    public void walk(final Visitor visitor)
    '''
def visit():
    '''    public void visit(final Schema schema)
    public void visit(final ArrayOf array)
    public void visit(final Type field)
    '''
