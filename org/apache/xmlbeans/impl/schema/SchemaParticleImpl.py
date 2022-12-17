def setImmutable():
    '''returns None\n\n
    setImmutable()\n
    '''
def hasTransitionRules():
    '''returns boolean\n\n
    hasTransitionRules()\n
    '''
def hasTransitionNotes():
    '''returns boolean\n\n
    hasTransitionNotes()\n
    '''
def setTransitionRules():
    '''returns None\n\n
    setTransitionRules(final QNameSet start, final boolean isSkippable)\n
    '''
def setTransitionNotes():
    '''returns None\n\n
    setTransitionNotes(final QNameSet excludeNext, final boolean isDeterministic)\n
    '''
def canStartWithElement():
    '''returns boolean\n\n
    canStartWithElement(final QName name)\n
    '''
def acceptedStartNames():
    '''returns QNameSet\n\n
    acceptedStartNames()\n
    '''
def getExcludeNextSet():
    '''returns QNameSet\n\n
    getExcludeNextSet()\n
    '''
def isSkippable():
    '''returns boolean\n\n
    isSkippable()\n
    '''
def isDeterministic():
    '''returns boolean\n\n
    isDeterministic()\n
    '''
def getParticleType():
    '''returns int\n\n
    getParticleType()\n
    '''
def setParticleType():
    '''returns None\n\n
    setParticleType(final int pType)\n
    '''
def isSingleton():
    '''returns boolean\n\n
    isSingleton()\n
    '''
def getMinOccurs():
    '''returns BigInteger\n\n
    getMinOccurs()\n
    '''
def setMinOccurs():
    '''returns None\n\n
    setMinOccurs(final BigInteger min)\n
    '''
def getIntMinOccurs():
    '''returns int\n\n
    getIntMinOccurs()\n
    '''
def getMaxOccurs():
    '''returns BigInteger\n\n
    getMaxOccurs()\n
    '''
def getIntMaxOccurs():
    '''returns int\n\n
    getIntMaxOccurs()\n
    '''
def setMaxOccurs():
    '''returns None\n\n
    setMaxOccurs(final BigInteger max)\n
    '''
def getParticleChildren():
    '''returns SchemaParticle[]\n\n
    getParticleChildren()\n
    '''
def setParticleChildren():
    '''returns None\n\n
    setParticleChildren(final SchemaParticle[] children)\n
    '''
def getParticleChild():
    '''returns SchemaParticle\n\n
    getParticleChild(final int i)\n
    '''
def countOfParticleChild():
    '''returns int\n\n
    countOfParticleChild()\n
    '''
def setWildcardSet():
    '''returns None\n\n
    setWildcardSet(final QNameSet set)\n
    '''
def getWildcardSet():
    '''returns QNameSet\n\n
    getWildcardSet()\n
    '''
def setWildcardProcess():
    '''returns None\n\n
    setWildcardProcess(final int process)\n
    '''
def getWildcardProcess():
    '''returns int\n\n
    getWildcardProcess()\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def setNameAndTypeRef():
    '''returns None\n\n
    setNameAndTypeRef(final QName formname, final SchemaType.Ref typeref)\n
    '''
def isTypeResolved():
    '''returns boolean\n\n
    isTypeResolved()\n
    '''
def resolveTypeRef():
    '''returns None\n\n
    resolveTypeRef(final SchemaType.Ref typeref)\n
    '''
def isAttribute():
    '''returns boolean\n\n
    isAttribute()\n
    '''
def getType():
    '''returns SchemaType\n\n
    getType()\n
    '''
def getDefaultText():
    '''returns String\n\n
    getDefaultText()\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault()\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed()\n
    '''
def setDefault():
    '''returns None\n\n
    setDefault(final String deftext, final boolean isFixed, final XmlObject parseObject)\n
    '''
def isNillable():
    '''returns boolean\n\n
    isNillable()\n
    '''
def setNillable():
    '''returns None\n\n
    setNillable(final boolean nillable)\n
    '''
def getDefaultValue():
    '''returns XmlAnySimpleType\n\n
    getDefaultValue()\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue(final XmlValueRef defaultRef)\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData()\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final Object data)\n
    '''
