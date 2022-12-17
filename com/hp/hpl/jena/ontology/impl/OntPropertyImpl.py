def ():
    '''returns OntPropertyImpl\n\n
    (final Node n, final EnhGraph g)\n
    '''
def isProperty():
    '''returns boolean\n\n
    isProperty()\n
    '''
def getOrdinal():
    '''returns int\n\n
    getOrdinal()\n
    '''
def setSuperProperty():
    '''returns None\n\n
    setSuperProperty(final Property prop)\n
    '''
def addSuperProperty():
    '''returns None\n\n
    addSuperProperty(final Property prop)\n
    '''
def getSuperProperty():
    '''returns OntProperty\n\n
    getSuperProperty()\n
    '''
def listSuperProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listSuperProperties()\n
    listSuperProperties(final boolean direct)\n
    '''
def hasSuperProperty():
    '''returns boolean\n\n
    hasSuperProperty(final Property prop, final boolean direct)\n
    '''
def removeSuperProperty():
    '''returns None\n\n
    removeSuperProperty(final Property prop)\n
    '''
def setSubProperty():
    '''returns None\n\n
    setSubProperty(final Property prop)\n
    '''
def addSubProperty():
    '''returns None\n\n
    addSubProperty(final Property prop)\n
    '''
def getSubProperty():
    '''returns OntProperty\n\n
    getSubProperty()\n
    '''
def listSubProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listSubProperties()\n
    listSubProperties(final boolean direct)\n
    '''
def hasSubProperty():
    '''returns boolean\n\n
    hasSubProperty(final Property prop, final boolean direct)\n
    '''
def removeSubProperty():
    '''returns None\n\n
    removeSubProperty(final Property prop)\n
    '''
def setDomain():
    '''returns None\n\n
    setDomain(final Resource res)\n
    '''
def addDomain():
    '''returns None\n\n
    addDomain(final Resource res)\n
    '''
def getDomain():
    '''returns OntResource\n\n
    getDomain()\n
    '''
def listDomain():
    '''returns ExtendedIterator<OntClass>\n\n
    listDomain()\n
    '''
def hasDomain():
    '''returns boolean\n\n
    hasDomain(final Resource res)\n
    '''
def removeDomain():
    '''returns None\n\n
    removeDomain(final Resource cls)\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final Resource res)\n
    '''
def addRange():
    '''returns None\n\n
    addRange(final Resource res)\n
    '''
def getRange():
    '''returns OntResource\n\n
    getRange()\n
    '''
def listRange():
    '''returns ExtendedIterator<OntClass>\n\n
    listRange()\n
    '''
def hasRange():
    '''returns boolean\n\n
    hasRange(final Resource res)\n
    '''
def removeRange():
    '''returns None\n\n
    removeRange(final Resource cls)\n
    '''
def setEquivalentProperty():
    '''returns None\n\n
    setEquivalentProperty(final Property prop)\n
    '''
def addEquivalentProperty():
    '''returns None\n\n
    addEquivalentProperty(final Property prop)\n
    '''
def getEquivalentProperty():
    '''returns OntProperty\n\n
    getEquivalentProperty()\n
    '''
def listEquivalentProperties():
    '''returns ExtendedIterator<OntProperty>\n\n
    listEquivalentProperties()\n
    '''
def hasEquivalentProperty():
    '''returns boolean\n\n
    hasEquivalentProperty(final Property prop)\n
    '''
def removeEquivalentProperty():
    '''returns None\n\n
    removeEquivalentProperty(final Property prop)\n
    '''
def setInverseOf():
    '''returns None\n\n
    setInverseOf(final Property prop)\n
    '''
def addInverseOf():
    '''returns None\n\n
    addInverseOf(final Property prop)\n
    '''
def getInverseOf():
    '''returns OntProperty\n\n
    getInverseOf()\n
    '''
def isInverseOf():
    '''returns boolean\n\n
    isInverseOf(final Property prop)\n
    '''
def removeInverseProperty():
    '''returns None\n\n
    removeInverseProperty(final Property prop)\n
    '''
def asFunctionalProperty():
    '''returns FunctionalProperty\n\n
    asFunctionalProperty()\n
    '''
def asDatatypeProperty():
    '''returns DatatypeProperty\n\n
    asDatatypeProperty()\n
    '''
def asObjectProperty():
    '''returns ObjectProperty\n\n
    asObjectProperty()\n
    '''
def asTransitiveProperty():
    '''returns TransitiveProperty\n\n
    asTransitiveProperty()\n
    '''
def asInverseFunctionalProperty():
    '''returns InverseFunctionalProperty\n\n
    asInverseFunctionalProperty()\n
    '''
def asSymmetricProperty():
    '''returns SymmetricProperty\n\n
    asSymmetricProperty()\n
    '''
def convertToFunctionalProperty():
    '''returns FunctionalProperty\n\n
    convertToFunctionalProperty()\n
    '''
def convertToDatatypeProperty():
    '''returns DatatypeProperty\n\n
    convertToDatatypeProperty()\n
    '''
def convertToObjectProperty():
    '''returns ObjectProperty\n\n
    convertToObjectProperty()\n
    '''
def convertToTransitiveProperty():
    '''returns TransitiveProperty\n\n
    convertToTransitiveProperty()\n
    '''
def convertToInverseFunctionalProperty():
    '''returns InverseFunctionalProperty\n\n
    convertToInverseFunctionalProperty()\n
    '''
def convertToSymmetricProperty():
    '''returns SymmetricProperty\n\n
    convertToSymmetricProperty()\n
    '''
def isFunctionalProperty():
    '''returns boolean\n\n
    isFunctionalProperty()\n
    '''
def isDatatypeProperty():
    '''returns boolean\n\n
    isDatatypeProperty()\n
    '''
def isObjectProperty():
    '''returns boolean\n\n
    isObjectProperty()\n
    '''
def isTransitiveProperty():
    '''returns boolean\n\n
    isTransitiveProperty()\n
    '''
def isInverseFunctionalProperty():
    '''returns boolean\n\n
    isInverseFunctionalProperty()\n
    '''
def isSymmetricProperty():
    '''returns boolean\n\n
    isSymmetricProperty()\n
    '''
def getInverse():
    '''returns OntProperty\n\n
    getInverse()\n
    '''
def listInverse():
    '''returns ExtendedIterator<OntProperty>\n\n
    listInverse()\n
    '''
def hasInverse():
    '''returns boolean\n\n
    hasInverse()\n
    '''
def listDeclaringClasses():
    '''returns ExtendedIterator<OntClass>\n\n
    listDeclaringClasses()\n
    listDeclaringClasses(final boolean direct)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final OntClass c)\n
    accept(final OntClass o)\n
    '''
def listReferringRestrictions():
    '''returns ExtendedIterator<Restriction>\n\n
    listReferringRestrictions()\n
    '''
def inModel():
    '''returns Property\n\n
    inModel(final Model m)\n
    '''
def wrap():
    '''returns EnhNode\n\n
    wrap(final Node n, final EnhGraph eg)\n
    '''
def canWrap():
    '''returns boolean\n\n
    canWrap(final Node node, final EnhGraph eg)\n
    '''
