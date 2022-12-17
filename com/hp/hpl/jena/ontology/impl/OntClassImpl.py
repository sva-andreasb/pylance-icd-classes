def ():
    '''returns OntClassImpl\n\n
    (final Node n, final EnhGraph g)\n
    '''
def setSuperClass():
    '''returns None\n\n
    setSuperClass(final Resource cls)\n
    '''
def addSuperClass():
    '''returns None\n\n
    addSuperClass(final Resource cls)\n
    '''
def getSuperClass():
    '''returns OntClass\n\n
    getSuperClass()\n
    '''
def listSuperClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listSuperClasses()\n
    listSuperClasses(final boolean direct)\n
    '''
def hasSuperClass():
    '''returns boolean\n\n
    hasSuperClass(final Resource cls)\n
    hasSuperClass()\n
    hasSuperClass(final Resource cls, final boolean direct)\n
    '''
def removeSuperClass():
    '''returns None\n\n
    removeSuperClass(final Resource cls)\n
    '''
def setSubClass():
    '''returns None\n\n
    setSubClass(final Resource cls)\n
    '''
def addSubClass():
    '''returns None\n\n
    addSubClass(final Resource cls)\n
    '''
def getSubClass():
    '''returns OntClass\n\n
    getSubClass()\n
    '''
def listSubClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listSubClasses()\n
    listSubClasses(final boolean direct)\n
    '''
def hasSubClass():
    '''returns boolean\n\n
    hasSubClass(final Resource cls)\n
    hasSubClass()\n
    hasSubClass(Resource cls, final boolean direct)\n
    '''
def removeSubClass():
    '''returns None\n\n
    removeSubClass(final Resource cls)\n
    '''
def setEquivalentClass():
    '''returns None\n\n
    setEquivalentClass(final Resource cls)\n
    '''
def addEquivalentClass():
    '''returns None\n\n
    addEquivalentClass(final Resource cls)\n
    '''
def getEquivalentClass():
    '''returns OntClass\n\n
    getEquivalentClass()\n
    '''
def listEquivalentClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listEquivalentClasses()\n
    '''
def hasEquivalentClass():
    '''returns boolean\n\n
    hasEquivalentClass(final Resource cls)\n
    '''
def removeEquivalentClass():
    '''returns None\n\n
    removeEquivalentClass(final Resource cls)\n
    '''
def setDisjointWith():
    '''returns None\n\n
    setDisjointWith(final Resource cls)\n
    '''
def addDisjointWith():
    '''returns None\n\n
    addDisjointWith(final Resource cls)\n
    '''
def getDisjointWith():
    '''returns OntClass\n\n
    getDisjointWith()\n
    '''
def listDisjointWith():
    '''returns ExtendedIterator<OntClass>\n\n
    listDisjointWith()\n
    '''
def isDisjointWith():
    '''returns boolean\n\n
    isDisjointWith(final Resource cls)\n
    '''
def removeDisjointWith():
    '''returns None\n\n
    removeDisjointWith(final Resource cls)\n
    '''
def listDeclaredProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listDeclaredProperties()\n
    listDeclaredProperties(final boolean direct)\n
    '''
def hasDeclaredProperty():
    '''returns boolean\n\n
    hasDeclaredProperty(final Property p, final boolean direct)\n
    '''
def listInstances():
    '''returns ExtendedIterator<Individual>\n\n
    listInstances()\n
    listInstances(final boolean direct)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Individual o)\n
    '''
def createIndividual():
    '''returns Individual\n\n
    createIndividual()\n
    createIndividual(final String uri)\n
    '''
def dropIndividual():
    '''returns None\n\n
    dropIndividual(final Resource individual)\n
    '''
def isHierarchyRoot():
    '''returns boolean\n\n
    isHierarchyRoot()\n
    '''
def asEnumeratedClass():
    '''returns EnumeratedClass\n\n
    asEnumeratedClass()\n
    '''
def asUnionClass():
    '''returns UnionClass\n\n
    asUnionClass()\n
    '''
def asIntersectionClass():
    '''returns IntersectionClass\n\n
    asIntersectionClass()\n
    '''
def asComplementClass():
    '''returns ComplementClass\n\n
    asComplementClass()\n
    '''
def asRestriction():
    '''returns Restriction\n\n
    asRestriction()\n
    '''
def isEnumeratedClass():
    '''returns boolean\n\n
    isEnumeratedClass()\n
    '''
def isUnionClass():
    '''returns boolean\n\n
    isUnionClass()\n
    '''
def isIntersectionClass():
    '''returns boolean\n\n
    isIntersectionClass()\n
    '''
def isComplementClass():
    '''returns boolean\n\n
    isComplementClass()\n
    '''
def isRestriction():
    '''returns boolean\n\n
    isRestriction()\n
    '''
def convertToEnumeratedClass():
    '''returns EnumeratedClass\n\n
    convertToEnumeratedClass(final RDFList individuals)\n
    '''
def convertToIntersectionClass():
    '''returns IntersectionClass\n\n
    convertToIntersectionClass(final RDFList classes)\n
    '''
def convertToUnionClass():
    '''returns UnionClass\n\n
    convertToUnionClass(final RDFList classes)\n
    '''
def convertToComplementClass():
    '''returns ComplementClass\n\n
    convertToComplementClass(final Resource cls)\n
    '''
def convertToRestriction():
    '''returns Restriction\n\n
    convertToRestriction(final Property prop)\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node node, final EnhGraph eg)\n
    '''
