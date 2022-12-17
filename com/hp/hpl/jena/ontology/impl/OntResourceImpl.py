def ():
    '''returns SingleEqualityFilter\n\n
    (final Node n, final EnhGraph g)\n
    (final Class<T> as)\n
    (final Class<T> as)\n
    (final Class<T> as)\n
    (final Class<T> as)\n
    (final String lang)\n
    (final T x)\n
    '''
def getOntModel():
    '''returns OntModel\n\n
    getOntModel()\n
    '''
def getProfile():
    '''returns Profile\n\n
    getProfile()\n
    '''
def isOntLanguageTerm():
    '''returns boolean\n\n
    isOntLanguageTerm()\n
    '''
def setSameAs():
    '''returns None\n\n
    setSameAs(final Resource res)\n
    '''
def addSameAs():
    '''returns None\n\n
    addSameAs(final Resource res)\n
    '''
def getSameAs():
    '''returns OntResource\n\n
    getSameAs()\n
    '''
def listSameAs():
    '''returns ExtendedIterator<OntResource>\n\n
    listSameAs()\n
    '''
def isSameAs():
    '''returns boolean\n\n
    isSameAs(final Resource res)\n
    '''
def removeSameAs():
    '''returns None\n\n
    removeSameAs(final Resource res)\n
    '''
def setDifferentFrom():
    '''returns None\n\n
    setDifferentFrom(final Resource res)\n
    '''
def addDifferentFrom():
    '''returns None\n\n
    addDifferentFrom(final Resource res)\n
    '''
def getDifferentFrom():
    '''returns OntResource\n\n
    getDifferentFrom()\n
    '''
def listDifferentFrom():
    '''returns ExtendedIterator<OntResource>\n\n
    listDifferentFrom()\n
    '''
def isDifferentFrom():
    '''returns boolean\n\n
    isDifferentFrom(final Resource res)\n
    '''
def removeDifferentFrom():
    '''returns None\n\n
    removeDifferentFrom(final Resource res)\n
    '''
def setSeeAlso():
    '''returns None\n\n
    setSeeAlso(final Resource res)\n
    '''
def addSeeAlso():
    '''returns None\n\n
    addSeeAlso(final Resource res)\n
    '''
def getSeeAlso():
    '''returns Resource\n\n
    getSeeAlso()\n
    '''
def listSeeAlso():
    '''returns ExtendedIterator<RDFNode>\n\n
    listSeeAlso()\n
    '''
def hasSeeAlso():
    '''returns boolean\n\n
    hasSeeAlso(final Resource res)\n
    '''
def removeSeeAlso():
    '''returns None\n\n
    removeSeeAlso(final Resource res)\n
    '''
def setIsDefinedBy():
    '''returns None\n\n
    setIsDefinedBy(final Resource res)\n
    '''
def addIsDefinedBy():
    '''returns None\n\n
    addIsDefinedBy(final Resource res)\n
    '''
def getIsDefinedBy():
    '''returns Resource\n\n
    getIsDefinedBy()\n
    '''
def listIsDefinedBy():
    '''returns ExtendedIterator<RDFNode>\n\n
    listIsDefinedBy()\n
    '''
def isDefinedBy():
    '''returns boolean\n\n
    isDefinedBy(final Resource res)\n
    '''
def removeDefinedBy():
    '''returns None\n\n
    removeDefinedBy(final Resource res)\n
    '''
def setVersionInfo():
    '''returns None\n\n
    setVersionInfo(final String info)\n
    '''
def addVersionInfo():
    '''returns None\n\n
    addVersionInfo(final String info)\n
    '''
def getVersionInfo():
    '''returns String\n\n
    getVersionInfo()\n
    '''
def listVersionInfo():
    '''returns ExtendedIterator<String>\n\n
    listVersionInfo()\n
    '''
def hasVersionInfo():
    '''returns boolean\n\n
    hasVersionInfo(final String info)\n
    '''
def removeVersionInfo():
    '''returns None\n\n
    removeVersionInfo(final String info)\n
    '''
def setLabel():
    '''returns None\n\n
    setLabel(final String label, final String lang)\n
    '''
def addLabel():
    '''returns None\n\n
    addLabel(final String label, final String lang)\n
    addLabel(final Literal label)\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel(final String lang)\n
    '''
def listLabels():
    '''returns ExtendedIterator<RDFNode>\n\n
    listLabels(final String lang)\n
    '''
def hasLabel():
    '''returns boolean\n\n
    hasLabel(final String label, final String lang)\n
    hasLabel(final Literal label)\n
    '''
def removeLabel():
    '''returns None\n\n
    removeLabel(final String label, final String lang)\n
    removeLabel(final Literal label)\n
    '''
def setComment():
    '''returns None\n\n
    setComment(final String comment, final String lang)\n
    '''
def addComment():
    '''returns None\n\n
    addComment(final String comment, final String lang)\n
    addComment(final Literal comment)\n
    '''
def getComment():
    '''returns String\n\n
    getComment(final String lang)\n
    '''
def listComments():
    '''returns ExtendedIterator<RDFNode>\n\n
    listComments(final String lang)\n
    '''
def hasComment():
    '''returns boolean\n\n
    hasComment(final String comment, final String lang)\n
    hasComment(final Literal comment)\n
    '''
def removeComment():
    '''returns None\n\n
    removeComment(final String comment, final String lang)\n
    removeComment(final Literal comment)\n
    '''
def setRDFType():
    '''returns None\n\n
    setRDFType(final Resource cls)\n
    '''
def addRDFType():
    '''returns None\n\n
    addRDFType(final Resource cls)\n
    '''
def getRDFType():
    '''returns Resource\n\n
    getRDFType()\n
    getRDFType(final boolean direct)\n
    '''
def listRDFTypes():
    '''returns ExtendedIterator<Resource>\n\n
    listRDFTypes(final boolean direct)\n
    '''
def hasRDFType():
    '''returns boolean\n\n
    hasRDFType(final String uri)\n
    hasRDFType(final Resource ontClass)\n
    hasRDFType(final Resource ontClass, final boolean direct)\n
    '''
def removeRDFType():
    '''returns None\n\n
    removeRDFType(final Resource cls)\n
    '''
def getCardinality():
    '''returns int\n\n
    getCardinality(final Property p)\n
    '''
def setPropertyValue():
    '''returns None\n\n
    setPropertyValue(final Property property, final RDFNode value)\n
    '''
def getPropertyValue():
    '''returns RDFNode\n\n
    getPropertyValue(final Property property)\n
    '''
def listPropertyValues():
    '''returns NodeIterator\n\n
    listPropertyValues(final Property property)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final Property property, final RDFNode value)\n
    '''
def asAnnotationProperty():
    '''returns AnnotationProperty\n\n
    asAnnotationProperty()\n
    '''
def asProperty():
    '''returns OntProperty\n\n
    asProperty()\n
    '''
def asObjectProperty():
    '''returns ObjectProperty\n\n
    asObjectProperty()\n
    '''
def asDatatypeProperty():
    '''returns DatatypeProperty\n\n
    asDatatypeProperty()\n
    '''
def asIndividual():
    '''returns Individual\n\n
    asIndividual()\n
    '''
def asClass():
    '''returns OntClass\n\n
    asClass()\n
    '''
def asOntology():
    '''returns Ontology\n\n
    asOntology()\n
    '''
def asAllDifferent():
    '''returns AllDifferent\n\n
    asAllDifferent()\n
    '''
def asDataRange():
    '''returns DataRange\n\n
    asDataRange()\n
    '''
def isAnnotationProperty():
    '''returns boolean\n\n
    isAnnotationProperty()\n
    '''
def isProperty():
    '''returns boolean\n\n
    isProperty()\n
    '''
def isObjectProperty():
    '''returns boolean\n\n
    isObjectProperty()\n
    '''
def isDatatypeProperty():
    '''returns boolean\n\n
    isDatatypeProperty()\n
    '''
def isIndividual():
    '''returns boolean\n\n
    isIndividual()\n
    '''
def isClass():
    '''returns boolean\n\n
    isClass()\n
    '''
def isOntology():
    '''returns boolean\n\n
    isOntology()\n
    '''
def isDataRange():
    '''returns boolean\n\n
    isDataRange()\n
    '''
def isAllDifferent():
    '''returns boolean\n\n
    isAllDifferent()\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node node, final EnhGraph eg)\n
    '''
def map1():
    '''returns RDFNode\n\n
    map1(final RDFNode x)\n
    map1(final Resource x)\n
    map1(final Statement x)\n
    map1(final Statement x)\n
    map1(final Statement x)\n
    map1(final Statement x)\n
    map1(final Statement x)\n
    map1(final Statement x)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Statement x)\n
    accept(final T x)\n
    '''
