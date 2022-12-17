def createResource():
    '''returns Resource\n\n
    createResource()\n
    createResource(final String uriref)\n
    '''
def createPlainLiteral():
    '''returns Literal\n\n
    createPlainLiteral(final String string)\n
    '''
def createTypedLiteral():
    '''returns Literal\n\n
    createTypedLiteral(final String string, final RDFDatatype dType)\n
    createTypedLiteral(final Object value)\n
    '''
def createProperty():
    '''returns Property\n\n
    createProperty(final String uriref)\n
    createProperty(final String namespace, final String localName)\n
    '''
def createStatement():
    '''returns Statement\n\n
    createStatement(final Resource subject, final Property predicate, final RDFNode object)\n
    '''
