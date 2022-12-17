def ():
    '''returns SeqImpl\n\n
    (final ModelCom model)\n
    (final String uri, final ModelCom model)\n
    (final Resource r, final ModelCom m)\n
    (final Node n, final EnhGraph g)\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource(final int index)\n
    getResource(final int index, final ResourceF f)\n
    '''
def getLiteral():
    '''returns Literal\n\n
    getLiteral(final int index)\n
    '''
def getObject():
    '''returns RDFNode\n\n
    getObject(final int index)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final int index)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final int index)\n
    '''
def getShort():
    '''returns short\n\n
    getShort(final int index)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final int index)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final int index)\n
    '''
def getChar():
    '''returns char\n\n
    getChar(final int index)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final int index)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final int index)\n
    '''
def getString():
    '''returns String\n\n
    getString(final int index)\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage(final int index)\n
    '''
def getBag():
    '''returns Bag\n\n
    getBag(final int index)\n
    '''
def getAlt():
    '''returns Alt\n\n
    getAlt(final int index)\n
    '''
def getSeq():
    '''returns Seq\n\n
    getSeq(final int index)\n
    '''
def set():
    '''returns Seq\n\n
    set(final int index, final RDFNode o)\n
    set(final int index, final boolean o)\n
    set(final int index, final long o)\n
    set(final int index, final float o)\n
    set(final int index, final double o)\n
    set(final int index, final char o)\n
    set(final int index, final String o)\n
    set(final int index, final String o, final String l)\n
    set(final int index, final Object o)\n
    '''
def add():
    '''returns Seq\n\n
    add(final int index, final boolean o)\n
    add(final int index, final long o)\n
    add(final int index, final char o)\n
    add(final int index, final float o)\n
    add(final int index, final double o)\n
    add(final int index, final Object o)\n
    add(final int index, final String o)\n
    add(final int index, final String o, final String l)\n
    add(final int index, final RDFNode o)\n
    '''
def iterator():
    '''returns NodeIterator\n\n
    iterator()\n
    '''
def remove():
    '''returns Container\n\n
    remove(final Statement s)\n
    remove(final int index)\n
    remove(final int index, final RDFNode o)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final RDFNode o)\n
    indexOf(final boolean o)\n
    indexOf(final long o)\n
    indexOf(final char o)\n
    indexOf(final float o)\n
    indexOf(final double o)\n
    indexOf(final Object o)\n
    indexOf(final String o)\n
    indexOf(final String o, final String l)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node n, final EnhGraph eg)\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
