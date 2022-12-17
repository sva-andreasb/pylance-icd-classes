def ():
    '''returns Schema\n\n
    (final Field... fs)\n
    '''
def write():
    '''returns None\n\n
    write(final ByteBuffer buffer, final Object o)\n
    '''
def read():
    '''returns Struct\n\n
    read(final ByteBuffer buffer)\n
    '''
def sizeOf():
    '''returns int\n\n
    sizeOf(final Object o)\n
    '''
def numFields():
    '''returns int\n\n
    numFields()\n
    '''
def get():
    '''returns BoundField\n\n
    get(final int slot)\n
    get(final String name)\n
    '''
def fields():
    '''returns BoundField[]\n\n
    fields()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def validate():
    '''returns Struct\n\n
    validate(final Object item)\n
    '''
def walk():
    '''returns None\n\n
    walk(final Visitor visitor)\n
    '''
def visit():
    '''returns None\n\n
    visit(final Schema schema)\n
    visit(final ArrayOf array)\n
    visit(final Type field)\n
    '''
