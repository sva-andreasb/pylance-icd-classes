def ():
    '''returns ResourceImpl\n\n
    (final Node n, final ModelCom m)\n
    ()\n
    (final ModelCom m)\n
    (final Node n, final EnhGraph m)\n
    (final String uri)\n
    (final String nameSpace, final String localName)\n
    (final AnonId id)\n
    (final AnonId id, final ModelCom m)\n
    (final String uri, final ModelCom m)\n
    (final Resource r, final ModelCom m)\n
    (final String nameSpace, final String localName, final ModelCom m)\n
    '''
def visitWith():
    '''returns Object\n\n
    visitWith(final RDFVisitor rv)\n
    '''
def asResource():
    '''returns Resource\n\n
    asResource()\n
    '''
def asLiteral():
    '''returns Literal\n\n
    asLiteral()\n
    '''
def inModel():
    '''returns Resource\n\n
    inModel(final Model m)\n
    '''
def getId():
    '''returns AnonId\n\n
    getId()\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getNameSpace():
    '''returns String\n\n
    getNameSpace()\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName()\n
    '''
def hasURI():
    '''returns boolean\n\n
    hasURI(final String uri)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getRequiredProperty():
    '''returns Statement\n\n
    getRequiredProperty(final Property p)\n
    '''
def getProperty():
    '''returns Statement\n\n
    getProperty(final Property p)\n
    '''
def listProperties():
    '''returns StmtIterator\n\n
    listProperties(final Property p)\n
    listProperties()\n
    '''
def addLiteral():
    '''returns Resource\n\n
    addLiteral(final Property p, final boolean o)\n
    addLiteral(final Property p, final long o)\n
    addLiteral(final Property p, final char o)\n
    addLiteral(final Property p, final double o)\n
    addLiteral(final Property p, final float o)\n
    addLiteral(final Property p, final Object o)\n
    addLiteral(final Property p, final Literal o)\n
    '''
def addProperty():
    '''returns Resource\n\n
    addProperty(final Property p, final long o)\n
    addProperty(final Property p, final float o)\n
    addProperty(final Property p, final double o)\n
    addProperty(final Property p, final String o)\n
    addProperty(final Property p, final String o, final String l)\n
    addProperty(final Property p, final String lexicalForm, final RDFDatatype datatype)\n
    addProperty(final Property p, final RDFNode o)\n
    '''
def hasProperty():
    '''returns boolean\n\n
    hasProperty(final Property p)\n
    hasProperty(final Property p, final String o)\n
    hasProperty(final Property p, final String o, final String l)\n
    hasProperty(final Property p, final RDFNode o)\n
    '''
def hasLiteral():
    '''returns boolean\n\n
    hasLiteral(final Property p, final boolean o)\n
    hasLiteral(final Property p, final long o)\n
    hasLiteral(final Property p, final char o)\n
    hasLiteral(final Property p, final double o)\n
    hasLiteral(final Property p, final float o)\n
    hasLiteral(final Property p, final Object o)\n
    '''
def removeProperties():
    '''returns Resource\n\n
    removeProperties()\n
    '''
def removeAll():
    '''returns Resource\n\n
    removeAll(final Property p)\n
    '''
def begin():
    '''returns Resource\n\n
    begin()\n
    '''
def abort():
    '''returns Resource\n\n
    abort()\n
    '''
def commit():
    '''returns Resource\n\n
    commit()\n
    '''
def getModel():
    '''returns Model\n\n
    getModel()\n
    '''
def getPropertyResourceValue():
    '''returns Resource\n\n
    getPropertyResourceValue(final Property p)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node n, final EnhGraph eg)\n
    canWrap(final Node n, final EnhGraph eg)\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
