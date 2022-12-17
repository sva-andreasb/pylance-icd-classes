def ():
    '''returns ContainerImpl\n\n
    (final ModelCom model)\n
    (final String uri, final ModelCom model)\n
    (final Resource r, final ModelCom model)\n
    (final Node n, final EnhGraph g)\n
    '''
def isAlt():
    '''returns boolean\n\n
    isAlt()\n
    '''
def isBag():
    '''returns boolean\n\n
    isBag()\n
    '''
def isSeq():
    '''returns boolean\n\n
    isSeq()\n
    '''
def add():
    '''returns Container\n\n
    add(final RDFNode n)\n
    add(final boolean o)\n
    add(final long o)\n
    add(final char o)\n
    add(final float o)\n
    add(final double o)\n
    add(final Object o)\n
    add(final String o)\n
    add(final String o, final String l)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final RDFNode n)\n
    contains(final boolean o)\n
    contains(final long o)\n
    contains(final char o)\n
    contains(final float o)\n
    contains(final double o)\n
    contains(final Object o)\n
    contains(final String o)\n
    contains(final String o, final String l)\n
    '''
def iterator():
    '''returns NodeIterator\n\n
    iterator()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def remove():
    '''returns Container\n\n
    remove(final Statement s)\n
    remove(final int index, final RDFNode object)\n
    '''
def listContainerMembers():
    '''returns NodeIterator\n\n
    listContainerMembers(final NodeIteratorFactory f)\n
    '''
def containerIndexOf():
    '''returns int\n\n
    containerIndexOf(final RDFNode n)\n
    '''
def containerContains():
    '''returns boolean\n\n
    containerContains(final RDFNode n)\n
    '''
