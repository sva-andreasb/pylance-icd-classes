def ():
    '''returns SimpleSelector\n\n
    ()\n
    (final Resource subject, final Property predicate, final RDFNode object)\n
    (final Resource subject, final Property predicate, final boolean object)\n
    (final Resource subject, final Property predicate, final long object)\n
    (final Resource subject, final Property predicate, final char object)\n
    (final Resource subject, final Property predicate, final float object)\n
    (final Resource subject, final Property predicate, final double object)\n
    (final Resource subject, final Property predicate, final String object)\n
    (final Resource subject, final Property predicate, final String object, final String language)\n
    (final Resource subject, final Property predicate, final Object object)\n
    '''
def getSubject():
    '''returns Resource\n\n
    getSubject()\n
    '''
def getPredicate():
    '''returns Property\n\n
    getPredicate()\n
    '''
def getObject():
    '''returns RDFNode\n\n
    getObject()\n
    '''
def isSimple():
    '''returns boolean\n\n
    isSimple()\n
    '''
def test():
    '''returns boolean\n\n
    test(final Statement s)\n
    '''
def selects():
    '''returns boolean\n\n
    selects(final Statement s)\n
    '''
