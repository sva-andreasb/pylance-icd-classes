def isUnloaded():
    '''returns boolean\n\n
    isUnloaded()\n
    '''
def finishLoading():
    '''returns None\n\n
    finishLoading()\n
    '''
def isSGResolved():
    '''returns boolean\n\n
    isSGResolved()\n
    '''
def isSGResolving():
    '''returns boolean\n\n
    isSGResolving()\n
    '''
def isResolved():
    '''returns boolean\n\n
    isResolved()\n
    '''
def isResolving():
    '''returns boolean\n\n
    isResolving()\n
    '''
def isUnjavaized():
    '''returns boolean\n\n
    isUnjavaized()\n
    '''
def isJavaized():
    '''returns boolean\n\n
    isJavaized()\n
    '''
def startResolvingSGs():
    '''returns None\n\n
    startResolvingSGs()\n
    '''
def finishResolvingSGs():
    '''returns None\n\n
    finishResolvingSGs()\n
    '''
def startResolving():
    '''returns None\n\n
    startResolving()\n
    '''
def finishResolving():
    '''returns None\n\n
    finishResolving()\n
    '''
def startJavaizing():
    '''returns None\n\n
    startJavaizing()\n
    '''
def finishJavaizing():
    '''returns None\n\n
    finishJavaizing()\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final QName name)\n
    '''
def getSourceName():
    '''returns String\n\n
    getSourceName()\n
    '''
def setFilename():
    '''returns None\n\n
    setFilename(final String filename)\n
    '''
def getComponentType():
    '''returns int\n\n
    getComponentType()\n
    '''
def isAnonymousType():
    '''returns boolean\n\n
    isAnonymousType()\n
    '''
def isDocumentType():
    '''returns boolean\n\n
    isDocumentType()\n
    '''
def isAttributeType():
    '''returns boolean\n\n
    isAttributeType()\n
    '''
def getDocumentElementName():
    '''returns QName\n\n
    getDocumentElementName()\n
    '''
def getAttributeTypeAttributeName():
    '''returns QName\n\n
    getAttributeTypeAttributeName()\n
    '''
def setAnnotation():
    '''returns None\n\n
    setAnnotation(final SchemaAnnotation ann)\n
    '''
def getAnnotation():
    '''returns SchemaAnnotation\n\n
    getAnnotation()\n
    '''
def setDocumentType():
    '''returns None\n\n
    setDocumentType(final boolean isDocument)\n
    '''
def setAttributeType():
    '''returns None\n\n
    setAttributeType(final boolean isAttribute)\n
    '''
def getContentType():
    '''returns int\n\n
    getContentType()\n
    '''
def setComplexTypeVariety():
    '''returns None\n\n
    setComplexTypeVariety(final int complexTypeVariety)\n
    '''
def getElementSequencer():
    '''returns SchemaTypeElementSequencer\n\n
    getElementSequencer()\n
    '''
def blockRestriction():
    '''returns boolean\n\n
    blockRestriction()\n
    '''
def blockExtension():
    '''returns boolean\n\n
    blockExtension()\n
    '''
def isAbstract():
    '''returns boolean\n\n
    isAbstract()\n
    '''
def finalExtension():
    '''returns boolean\n\n
    finalExtension()\n
    '''
def finalRestriction():
    '''returns boolean\n\n
    finalRestriction()\n
    '''
def finalList():
    '''returns boolean\n\n
    finalList()\n
    '''
def finalUnion():
    '''returns boolean\n\n
    finalUnion()\n
    '''
def setContainerField():
    '''returns None\n\n
    setContainerField(final SchemaField field)\n
    '''
def setContainerFieldRef():
    '''returns None\n\n
    setContainerFieldRef(final SchemaComponent.Ref ref)\n
    '''
def setContainerFieldIndex():
    '''returns None\n\n
    setContainerFieldIndex(final short code, final int index)\n
    '''
def getOuterType():
    '''returns SchemaType\n\n
    getOuterType()\n
    '''
def setOuterSchemaTypeRef():
    '''returns None\n\n
    setOuterSchemaTypeRef(final Ref typeref)\n
    '''
def isCompiled():
    '''returns boolean\n\n
    isCompiled()\n
    '''
def setCompiled():
    '''returns None\n\n
    setCompiled(final boolean f)\n
    '''
def isSkippedAnonymousType():
    '''returns boolean\n\n
    isSkippedAnonymousType()\n
    '''
def getShortJavaName():
    '''returns String\n\n
    getShortJavaName()\n
    '''
def setShortJavaName():
    '''returns None\n\n
    setShortJavaName(final String name)\n
    '''
def getFullJavaName():
    '''returns String\n\n
    getFullJavaName()\n
    '''
def setFullJavaName():
    '''returns None\n\n
    setFullJavaName(final String name)\n
    '''
def setShortJavaImplName():
    '''returns None\n\n
    setShortJavaImplName(final String name)\n
    '''
def setFullJavaImplName():
    '''returns None\n\n
    setFullJavaImplName(final String name)\n
    '''
def getFullJavaImplName():
    '''returns String\n\n
    getFullJavaImplName()\n
    '''
def getShortJavaImplName():
    '''returns String\n\n
    getShortJavaImplName()\n
    '''
def getUserTypeName():
    '''returns String\n\n
    getUserTypeName()\n
    '''
def setUserTypeName():
    '''returns None\n\n
    setUserTypeName(final String userTypeName)\n
    '''
def getUserTypeHandlerName():
    '''returns String\n\n
    getUserTypeHandlerName()\n
    '''
def setUserTypeHandlerName():
    '''returns None\n\n
    setUserTypeHandlerName(final String typeHandler)\n
    '''
def setInterfaceExtensions():
    '''returns None\n\n
    setInterfaceExtensions(final InterfaceExtension[] interfaces)\n
    '''
def getInterfaceExtensions():
    '''returns InterfaceExtension[]\n\n
    getInterfaceExtensions()\n
    '''
def setPrePostExtension():
    '''returns None\n\n
    setPrePostExtension(final PrePostExtension prepost)\n
    '''
def getPrePostExtension():
    '''returns PrePostExtension\n\n
    getPrePostExtension()\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData()\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final Object data)\n
    '''
def getTypeSystem():
    '''returns SchemaTypeSystem\n\n
    getTypeSystem()\n
    '''
def getContentModel():
    '''returns SchemaParticle\n\n
    getContentModel()\n
    '''
def getLocalElementByIndex():
    '''returns SchemaLocalElement\n\n
    getLocalElementByIndex(final int i)\n
    '''
def getIndexForLocalElement():
    '''returns int\n\n
    getIndexForLocalElement(final SchemaLocalElement elt)\n
    '''
def getIndexForLocalAttribute():
    '''returns int\n\n
    getIndexForLocalAttribute(final SchemaLocalAttribute attr)\n
    '''
def getAttributeModel():
    '''returns SchemaAttributeModel\n\n
    getAttributeModel()\n
    '''
def getProperties():
    '''returns SchemaProperty[]\n\n
    getProperties()\n
    '''
def getDerivedProperties():
    '''returns SchemaProperty[]\n\n
    getDerivedProperties()\n
    '''
def getElementProperties():
    '''returns SchemaProperty[]\n\n
    getElementProperties()\n
    '''
def getAttributeProperties():
    '''returns SchemaProperty[]\n\n
    getAttributeProperties()\n
    '''
def getElementProperty():
    '''returns SchemaProperty\n\n
    getElementProperty(final QName eltName)\n
    '''
def getAttributeProperty():
    '''returns SchemaProperty\n\n
    getAttributeProperty(final QName attrName)\n
    '''
def hasAllContent():
    '''returns boolean\n\n
    hasAllContent()\n
    '''
def isOrderSensitive():
    '''returns boolean\n\n
    isOrderSensitive()\n
    '''
def setOrderSensitive():
    '''returns None\n\n
    setOrderSensitive(final boolean sensitive)\n
    '''
def setContentModel():
    '''returns None\n\n
    setContentModel(final SchemaParticle contentModel, final SchemaAttributeModel attrModel, final Map propertyModelByElementName, final Map propertyModelByAttributeName, final boolean isAll)\n
    '''
def hasAttributeWildcards():
    '''returns boolean\n\n
    hasAttributeWildcards()\n
    '''
def hasElementWildcards():
    '''returns boolean\n\n
    hasElementWildcards()\n
    '''
def isValidSubstitution():
    '''returns boolean\n\n
    isValidSubstitution(final QName name)\n
    '''
def getElementType():
    '''returns SchemaType\n\n
    getElementType(final QName eltName, final QName xsiType, final SchemaTypeLoader wildcardTypeLoader)\n
    '''
def getAttributeType():
    '''returns SchemaType\n\n
    getAttributeType(final QName attrName, final SchemaTypeLoader wildcardTypeLoader)\n
    '''
def createElementType():
    '''returns XmlObject\n\n
    createElementType(final QName eltName, final QName xsiType, final SchemaTypeLoader wildcardTypeLoader)\n
    '''
def createAttributeType():
    '''returns XmlObject\n\n
    createAttributeType(final QName attrName, final SchemaTypeLoader wildcardTypeLoader)\n
    '''
def setWildcardSummary():
    '''returns None\n\n
    setWildcardSummary(final QNameSet elementSet, final boolean haswcElt, final QNameSet attributeSet, final boolean haswcAtt)\n
    '''
def getAnonymousTypes():
    '''returns SchemaType[]\n\n
    getAnonymousTypes()\n
    '''
def setAnonymousTypeRefs():
    '''returns None\n\n
    setAnonymousTypeRefs(final Ref[] anonymousTyperefs)\n
    '''
def setSimpleTypeVariety():
    '''returns None\n\n
    setSimpleTypeVariety(final int variety)\n
    '''
def getSimpleVariety():
    '''returns int\n\n
    getSimpleVariety()\n
    '''
def isURType():
    '''returns boolean\n\n
    isURType()\n
    '''
def isNoType():
    '''returns boolean\n\n
    isNoType()\n
    '''
def isSimpleType():
    '''returns boolean\n\n
    isSimpleType()\n
    '''
def setSimpleType():
    '''returns None\n\n
    setSimpleType(final boolean f)\n
    '''
def isUnionOfLists():
    '''returns boolean\n\n
    isUnionOfLists()\n
    '''
def setUnionOfLists():
    '''returns None\n\n
    setUnionOfLists(final boolean f)\n
    '''
def getPrimitiveType():
    '''returns SchemaType\n\n
    getPrimitiveType()\n
    '''
def setPrimitiveTypeRef():
    '''returns None\n\n
    setPrimitiveTypeRef(final Ref typeref)\n
    '''
def getDecimalSize():
    '''returns int\n\n
    getDecimalSize()\n
    '''
def setDecimalSize():
    '''returns None\n\n
    setDecimalSize(final int bits)\n
    '''
def getBaseType():
    '''returns SchemaType\n\n
    getBaseType()\n
    '''
def setBaseTypeRef():
    '''returns None\n\n
    setBaseTypeRef(final Ref typeref)\n
    '''
def getBaseDepth():
    '''returns int\n\n
    getBaseDepth()\n
    '''
def setBaseDepth():
    '''returns None\n\n
    setBaseDepth(final int depth)\n
    '''
def getContentBasedOnType():
    '''returns SchemaType\n\n
    getContentBasedOnType()\n
    '''
def setContentBasedOnTypeRef():
    '''returns None\n\n
    setContentBasedOnTypeRef(final Ref typeref)\n
    '''
def getDerivationType():
    '''returns int\n\n
    getDerivationType()\n
    '''
def setDerivationType():
    '''returns None\n\n
    setDerivationType(final int type)\n
    '''
def getListItemType():
    '''returns SchemaType\n\n
    getListItemType()\n
    '''
def setListItemTypeRef():
    '''returns None\n\n
    setListItemTypeRef(final Ref typeref)\n
    '''
def getUnionMemberTypes():
    '''returns SchemaType[]\n\n
    getUnionMemberTypes()\n
    '''
def setUnionMemberTypeRefs():
    '''returns None\n\n
    setUnionMemberTypeRefs(final Ref[] typerefs)\n
    '''
def getAnonymousUnionMemberOrdinal():
    '''returns int\n\n
    getAnonymousUnionMemberOrdinal()\n
    '''
def setAnonymousUnionMemberOrdinal():
    '''returns None\n\n
    setAnonymousUnionMemberOrdinal(final int i)\n
    '''
def getSubstitutionGroup():
    '''returns QName\n\n
    getSubstitutionGroup()\n
    '''
def setSubstitutionGroup():
    '''returns None\n\n
    setSubstitutionGroup(final QName sg)\n
    '''
def addSubstitutionGroupMember():
    '''returns None\n\n
    addSubstitutionGroupMember(final QName member)\n
    '''
def getSubstitutionGroupMembers():
    '''returns QName[]\n\n
    getSubstitutionGroupMembers()\n
    '''
def getWhiteSpaceRule():
    '''returns int\n\n
    getWhiteSpaceRule()\n
    '''
def setWhiteSpaceRule():
    '''returns None\n\n
    setWhiteSpaceRule(final int ws)\n
    '''
def getFacet():
    '''returns XmlAnySimpleType\n\n
    getFacet(final int facetCode)\n
    '''
def isFacetFixed():
    '''returns boolean\n\n
    isFacetFixed(final int facetCode)\n
    '''
def getBasicFacets():
    '''returns XmlAnySimpleType[]\n\n
    getBasicFacets()\n
    '''
def getFixedFacets():
    '''returns boolean[]\n\n
    getFixedFacets()\n
    '''
def setBasicFacets():
    '''returns None\n\n
    setBasicFacets(final XmlValueRef[] values, final boolean[] fixed)\n
    '''
def ordered():
    '''returns int\n\n
    ordered()\n
    '''
def setOrdered():
    '''returns None\n\n
    setOrdered(final int ordering)\n
    '''
def isBounded():
    '''returns boolean\n\n
    isBounded()\n
    '''
def setBounded():
    '''returns None\n\n
    setBounded(final boolean f)\n
    '''
def isFinite():
    '''returns boolean\n\n
    isFinite()\n
    '''
def setFinite():
    '''returns None\n\n
    setFinite(final boolean f)\n
    '''
def isNumeric():
    '''returns boolean\n\n
    isNumeric()\n
    '''
def setNumeric():
    '''returns None\n\n
    setNumeric(final boolean f)\n
    '''
def hasPatternFacet():
    '''returns boolean\n\n
    hasPatternFacet()\n
    '''
def setPatternFacet():
    '''returns None\n\n
    setPatternFacet(final boolean hasPatterns)\n
    '''
def matchPatternFacet():
    '''returns boolean\n\n
    matchPatternFacet(final String s)\n
    '''
def getPatterns():
    '''returns String[]\n\n
    getPatterns()\n
    '''
def getPatternExpressions():
    '''returns RegularExpression[]\n\n
    getPatternExpressions()\n
    '''
def setPatterns():
    '''returns None\n\n
    setPatterns(final RegularExpression[] list)\n
    '''
def getEnumerationValues():
    '''returns XmlAnySimpleType[]\n\n
    getEnumerationValues()\n
    '''
def setEnumerationValues():
    '''returns None\n\n
    setEnumerationValues(final XmlValueRef[] a)\n
    '''
def enumForString():
    '''returns StringEnumAbstractBase\n\n
    enumForString(final String s)\n
    '''
def enumForInt():
    '''returns StringEnumAbstractBase\n\n
    enumForInt(final int i)\n
    '''
def enumEntryForString():
    '''returns SchemaStringEnumEntry\n\n
    enumEntryForString(final String s)\n
    '''
def getBaseEnumType():
    '''returns SchemaType\n\n
    getBaseEnumType()\n
    '''
def setBaseEnumTypeRef():
    '''returns None\n\n
    setBaseEnumTypeRef(final Ref baseEnumTyperef)\n
    '''
def getStringEnumEntries():
    '''returns SchemaStringEnumEntry[]\n\n
    getStringEnumEntries()\n
    '''
def setStringEnumEntries():
    '''returns None\n\n
    setStringEnumEntries(final SchemaStringEnumEntry[] sEnums)\n
    '''
def hasStringEnumValues():
    '''returns boolean\n\n
    hasStringEnumValues()\n
    '''
def copyEnumerationValues():
    '''returns None\n\n
    copyEnumerationValues(final SchemaTypeImpl baseImpl)\n
    '''
def getBuiltinTypeCode():
    '''returns int\n\n
    getBuiltinTypeCode()\n
    '''
def setBuiltinTypeCode():
    '''returns None\n\n
    setBuiltinTypeCode(final int builtinTypeCode)\n
    '''
def getJavaClass():
    '''returns Class\n\n
    getJavaClass()\n
    '''
def getJavaImplClass():
    '''returns Class\n\n
    getJavaImplClass()\n
    '''
def getUserTypeClass():
    '''returns Class\n\n
    getUserTypeClass()\n
    '''
def getUserTypeHandlerClass():
    '''returns Class\n\n
    getUserTypeHandlerClass()\n
    '''
def getJavaImplConstructor():
    '''returns Constructor\n\n
    getJavaImplConstructor()\n
    '''
def getJavaImplConstructor2():
    '''returns Constructor\n\n
    getJavaImplConstructor2()\n
    '''
def getEnumJavaClass():
    '''returns Class\n\n
    getEnumJavaClass()\n
    '''
def setJavaClass():
    '''returns None\n\n
    setJavaClass(final Class javaClass)\n
    '''
def isPrimitiveType():
    '''returns boolean\n\n
    isPrimitiveType()\n
    '''
def isBuiltinType():
    '''returns boolean\n\n
    isBuiltinType()\n
    '''
def createUnwrappedNode():
    '''returns XmlObject\n\n
    createUnwrappedNode()\n
    '''
def createTypeStoreUser():
    '''returns TypeStoreUser\n\n
    createTypeStoreUser()\n
    '''
def newValidatingValue():
    '''returns XmlAnySimpleType\n\n
    newValidatingValue(final Object obj)\n
    '''
def newValue():
    '''returns XmlAnySimpleType\n\n
    newValue(final Object obj)\n
    newValue(final Object obj, final boolean validateOnSet)\n
    '''
def getCommonBaseType():
    '''returns SchemaType\n\n
    getCommonBaseType(final SchemaType type)\n
    '''
def isAssignableFrom():
    '''returns boolean\n\n
    isAssignableFrom(SchemaType type)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setParseContext():
    '''returns None\n\n
    setParseContext(final XmlObject parseObject, final String targetNamespace, final boolean chameleon, final String elemFormDefault, final String attFormDefault, final boolean redefinition)\n
    '''
def getParseObject():
    '''returns XmlObject\n\n
    getParseObject()\n
    '''
def getTargetNamespace():
    '''returns String\n\n
    getTargetNamespace()\n
    '''
def isChameleon():
    '''returns boolean\n\n
    isChameleon()\n
    '''
def getElemFormDefault():
    '''returns String\n\n
    getElemFormDefault()\n
    '''
def getAttFormDefault():
    '''returns String\n\n
    getAttFormDefault()\n
    '''
def getChameleonNamespace():
    '''returns String\n\n
    getChameleonNamespace()\n
    '''
def isRedefinition():
    '''returns boolean\n\n
    isRedefinition()\n
    '''
def getRef():
    '''returns Ref\n\n
    getRef()\n
    '''
def qnameSetForWildcardElements():
    '''returns QNameSet\n\n
    qnameSetForWildcardElements()\n
    '''
def qnameSetForWildcardAttributes():
    '''returns QNameSet\n\n
    qnameSetForWildcardAttributes()\n
    '''
def next():
    '''returns boolean\n\n
    next(final QName elementName)\n
    '''
def peek():
    '''returns boolean\n\n
    peek(final QName elementName)\n
    '''
