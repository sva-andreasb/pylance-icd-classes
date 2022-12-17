def ():
    '''returns StatementImpl\n\n
    (final Resource subject, final Property predicate, final RDFNode object, final ModelCom model)\n
    (final Resource subject, final Property predicate, final RDFNode object)\n
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
def getStatementProperty():
    '''returns Statement\n\n
    getStatementProperty(final Property p)\n
    '''
def getResource():
    '''returns Resource\n\n
    getResource()\n
    getResource(final ResourceF f)\n
    '''
def getProperty():
    '''returns Statement\n\n
    getProperty(final Property p)\n
    '''
def getLiteral():
    '''returns Literal\n\n
    getLiteral()\n
    '''
def getBag():
    '''returns Bag\n\n
    getBag()\n
    '''
def getAlt():
    '''returns Alt\n\n
    getAlt()\n
    '''
def getSeq():
    '''returns Seq\n\n
    getSeq()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def asResource():
    '''returns Resource\n\n
    asResource()\n
    '''
def remove():
    '''returns Statement\n\n
    remove()\n
    '''
def removeReification():
    '''returns None\n\n
    removeReification()\n
    '''
def asTriple():
    '''returns Triple\n\n
    asTriple()\n
    '''
def isReified():
    '''returns boolean\n\n
    isReified()\n
    '''
def createReifiedStatement():
    '''returns ReifiedStatement\n\n
    createReifiedStatement()\n
    createReifiedStatement(final String uri)\n
    '''
def listReifiedStatements():
    '''returns RSIterator\n\n
    listReifiedStatements()\n
    '''
