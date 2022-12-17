YEARMONTHDURATION_DT = "short  46"
DAYTIMEDURATION_DT = "short  47"
PRECISIONDECIMAL_DT = "short  48"
ANYATOMICTYPE_DT = "short  49"
def ():
    '''returns XSFacetImpl\n\n
    ()\n
    (final short kind, final StringList svalues, final ObjectList avalues, final XSObjectList list)\n
    (final short kind, final String svalue, final int ivalue, final Object avalue, final boolean fixed, final XSAnnotation xsAnnotation)\n
    '''
def getType():
    '''returns short\n\n
    getType()\n
    getType()\n
    getType()\n
    '''
def getTypeCategory():
    '''returns short\n\n
    getTypeCategory()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    getName()\n
    '''
def getTypeName():
    '''returns String\n\n
    getTypeName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    getNamespace()\n
    getNamespace()\n
    '''
def getFinal():
    '''returns short\n\n
    getFinal()\n
    '''
def isFinal():
    '''returns boolean\n\n
    isFinal(final short n)\n
    '''
def getBaseType():
    '''returns XSTypeDefinition\n\n
    getBaseType()\n
    '''
def getAnonymous():
    '''returns boolean\n\n
    getAnonymous()\n
    '''
def getVariety():
    '''returns short\n\n
    getVariety()\n
    '''
def isIDType():
    '''returns boolean\n\n
    isIDType()\n
    '''
def getWhitespace():
    '''returns short\n\n
    getWhitespace()\n
    '''
def getPrimitiveKind():
    '''returns short\n\n
    getPrimitiveKind()\n
    '''
def getBuiltInKind():
    '''returns short\n\n
    getBuiltInKind()\n
    '''
def getPrimitiveType():
    '''returns XSSimpleTypeDefinition\n\n
    getPrimitiveType()\n
    '''
def getItemType():
    '''returns XSSimpleTypeDefinition\n\n
    getItemType()\n
    '''
def getMemberTypes():
    '''returns XSObjectList\n\n
    getMemberTypes()\n
    '''
def applyFacets():
    '''returns None\n\n
    applyFacets(final XSFacets xsFacets, final short n, final short n2, ValidationContext fEmptyContext)\n
    '''
def validate():
    '''returns None\n\n
    validate(final String s, ValidationContext fEmptyContext, ValidatedInfo validatedInfo)\n
    validate(final Object o, ValidationContext fEmptyContext, ValidatedInfo validatedInfo)\n
    validate(ValidationContext fEmptyContext, final ValidatedInfo validatedInfo)\n
    '''
def validateWithInfo():
    '''returns ValidatedInfo\n\n
    validateWithInfo(final String s, ValidationContext fEmptyContext, ValidatedInfo validatedInfo)\n
    '''
def isEqual():
    '''returns boolean\n\n
    isEqual(final Object o, final Object obj)\n
    '''
def isIdentical():
    '''returns boolean\n\n
    isIdentical(final Object o, final Object o2)\n
    '''
def getOrdered():
    '''returns short\n\n
    getOrdered()\n
    '''
def getBounded():
    '''returns boolean\n\n
    getBounded()\n
    '''
def getFinite():
    '''returns boolean\n\n
    getFinite()\n
    '''
def getNumeric():
    '''returns boolean\n\n
    getNumeric()\n
    '''
def isDefinedFacet():
    '''returns boolean\n\n
    isDefinedFacet(final short n)\n
    '''
def getDefinedFacets():
    '''returns short\n\n
    getDefinedFacets()\n
    '''
def isFixedFacet():
    '''returns boolean\n\n
    isFixedFacet(final short n)\n
    '''
def getFixedFacets():
    '''returns short\n\n
    getFixedFacets()\n
    '''
def getLexicalFacetValue():
    '''returns String\n\n
    getLexicalFacetValue(final short n)\n
    getLexicalFacetValue()\n
    '''
def getLexicalEnumeration():
    '''returns StringList\n\n
    getLexicalEnumeration()\n
    '''
def getActualEnumeration():
    '''returns ObjectList\n\n
    getActualEnumeration()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    getLength()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Object obj)\n
    contains(final Object o)\n
    '''
def item():
    '''returns Object\n\n
    item(final int n)\n
    item(final int n)\n
    '''
def getEnumerationItemTypeList():
    '''returns ObjectList\n\n
    getEnumerationItemTypeList()\n
    '''
def getEnumerationTypeList():
    '''returns ShortList\n\n
    getEnumerationTypeList()\n
    '''
def getLexicalPattern():
    '''returns StringList\n\n
    getLexicalPattern()\n
    '''
def getAnnotations():
    '''returns XSObjectList\n\n
    getAnnotations()\n
    getAnnotations()\n
    getAnnotations()\n
    '''
def derivedFromType():
    '''returns boolean\n\n
    derivedFromType(XSTypeDefinition type, final short n)\n
    '''
def derivedFrom():
    '''returns boolean\n\n
    derivedFrom(final String anObject, final String anObject2, final short n)\n
    '''
def isDOMDerivedFrom():
    '''returns boolean\n\n
    isDOMDerivedFrom(final String anObject, final String anObject2, final int n)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getNamespaceItem():
    '''returns XSNamespaceItem\n\n
    getNamespaceItem()\n
    getNamespaceItem()\n
    getNamespaceItem()\n
    '''
def setNamespaceItem():
    '''returns None\n\n
    setNamespaceItem(final XSNamespaceItem fNamespaceItem)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getFacets():
    '''returns XSObjectList\n\n
    getFacets()\n
    '''
def getFacet():
    '''returns XSObject\n\n
    getFacet(final int n)\n
    '''
def getMultiValueFacets():
    '''returns XSObjectList\n\n
    getMultiValueFacets()\n
    '''
def getMinInclusiveValue():
    '''returns Object\n\n
    getMinInclusiveValue()\n
    '''
def getMinExclusiveValue():
    '''returns Object\n\n
    getMinExclusiveValue()\n
    '''
def getMaxInclusiveValue():
    '''returns Object\n\n
    getMaxInclusiveValue()\n
    '''
def getMaxExclusiveValue():
    '''returns Object\n\n
    getMaxExclusiveValue()\n
    '''
def setAnonymous():
    '''returns None\n\n
    setAnonymous(final boolean fAnonymous)\n
    '''
def getTypeNamespace():
    '''returns String\n\n
    getTypeNamespace()\n
    '''
def isDerivedFrom():
    '''returns boolean\n\n
    isDerivedFrom(final String s, final String s2, final int n)\n
    '''
def needFacetChecking():
    '''returns boolean\n\n
    needFacetChecking()\n
    needFacetChecking()\n
    needFacetChecking()\n
    '''
def needExtraChecking():
    '''returns boolean\n\n
    needExtraChecking()\n
    needExtraChecking()\n
    needExtraChecking()\n
    '''
def needToNormalize():
    '''returns boolean\n\n
    needToNormalize()\n
    needToNormalize()\n
    needToNormalize()\n
    '''
def useNamespaces():
    '''returns boolean\n\n
    useNamespaces()\n
    useNamespaces()\n
    useNamespaces()\n
    '''
def isEntityDeclared():
    '''returns boolean\n\n
    isEntityDeclared(final String s)\n
    isEntityDeclared(final String s)\n
    isEntityDeclared(final String s)\n
    '''
def isEntityUnparsed():
    '''returns boolean\n\n
    isEntityUnparsed(final String s)\n
    isEntityUnparsed(final String s)\n
    isEntityUnparsed(final String s)\n
    '''
def isIdDeclared():
    '''returns boolean\n\n
    isIdDeclared(final String s)\n
    isIdDeclared(final String s)\n
    isIdDeclared(final String s)\n
    '''
def addId():
    '''returns None\n\n
    addId(final String s)\n
    addId(final String s)\n
    addId(final String s)\n
    '''
def addIdRef():
    '''returns None\n\n
    addIdRef(final String s)\n
    addIdRef(final String s)\n
    addIdRef(final String s)\n
    '''
def getSymbol():
    '''returns String\n\n
    getSymbol(final String s)\n
    getSymbol(final String s)\n
    getSymbol(final String s)\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final String s)\n
    getURI(final String s)\n
    getURI(final String s)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    getLocale()\n
    getLocale()\n
    '''
def get():
    '''returns Object\n\n
    get(final int i)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getFacetKind():
    '''returns short\n\n
    getFacetKind()\n
    getFacetKind()\n
    '''
def getLexicalFacetValues():
    '''returns StringList\n\n
    getLexicalFacetValues()\n
    '''
def getEnumerationValues():
    '''returns ObjectList\n\n
    getEnumerationValues()\n
    '''
def getAnnotation():
    '''returns XSAnnotation\n\n
    getAnnotation()\n
    '''
def getActualFacetValue():
    '''returns Object\n\n
    getActualFacetValue()\n
    '''
def getIntFacetValue():
    '''returns int\n\n
    getIntFacetValue()\n
    '''
def getFixed():
    '''returns boolean\n\n
    getFixed()\n
    '''
