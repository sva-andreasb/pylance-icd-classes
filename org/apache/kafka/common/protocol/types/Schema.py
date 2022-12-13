def Schema():
'''public Schema(final Field... fs)
'''
pass
def write():
'''public void write(final ByteBuffer buffer, final Object o)
'''
pass
def read():
'''public Struct read(final ByteBuffer buffer)
'''
pass
def sizeOf():
'''public int sizeOf(final Object o)
'''
pass
def numFields():
'''public int numFields()
'''
pass
def get():
'''public BoundField get(final int slot)
public BoundField get(final String name)
'''
pass
def fields():
'''public BoundField[] fields()
'''
pass
def toString():
'''public String toString()
'''
pass
def validate():
'''public Struct validate(final Object item)
'''
pass
def walk():
'''public void walk(final Visitor visitor)
'''
pass
def visit():
'''public void visit(final Schema schema)
public void visit(final ArrayOf array)
public void visit(final Type field)
'''
pass
