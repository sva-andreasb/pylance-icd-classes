def ():
    '''returns EStructuralFeatureExtendedMetaDataImpl\n\n
    ()\n
    (final EPackage.Registry registry)\n
    (final String annotationURI, final EPackage.Registry registry)\n
    (final String annotationURI, final EPackage.Registry registry, final Map annotationMap)\n
    (final EPackage ePackage)\n
    (final EClass eClass)\n
    (final EDataType eDataType)\n
    (final EStructuralFeature eStructuralFeature)\n
    '''
def getType():
    '''returns EClassifier\n\n
    getType(final EPackage ePackage, final String name)\n
    getType(final String namespace, final String name)\n
    '''
def getPackage():
    '''returns EPackage\n\n
    getPackage(final String namespace)\n
    '''
def putPackage():
    '''returns None\n\n
    putPackage(final String namespace, final EPackage ePackage)\n
    '''
def getDocumentRoot():
    '''returns EClass\n\n
    getDocumentRoot(final EPackage ePackage)\n
    '''
def setDocumentRoot():
    '''returns None\n\n
    setDocumentRoot(final EClass eClass)\n
    '''
def getXMLNSPrefixMapFeature():
    '''returns EReference\n\n
    getXMLNSPrefixMapFeature(final EClass eClass)\n
    '''
def getXSISchemaLocationMapFeature():
    '''returns EReference\n\n
    getXSISchemaLocationMapFeature(final EClass eClass)\n
    '''
def isQualified():
    '''returns boolean\n\n
    isQualified(final EPackage ePackage)\n
    isQualified()\n
    '''
def setQualified():
    '''returns None\n\n
    setQualified(final EPackage ePackage, final boolean isQualified)\n
    setQualified(final boolean isQualified)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace(final EPackage ePackage)\n
    getNamespace(final EClassifier eClassifier)\n
    getNamespace(final EStructuralFeature eStructuralFeature)\n
    getNamespace()\n
    '''
def basicGetNamespace():
    '''returns String\n\n
    basicGetNamespace(final EStructuralFeature eStructuralFeature)\n
    '''
def setNamespace():
    '''returns None\n\n
    setNamespace(final EStructuralFeature eStructuralFeature, final String namespace)\n
    setNamespace(final String namespace)\n
    '''
def getName():
    '''returns String\n\n
    getName(final EClassifier eClassifier)\n
    getName(final EStructuralFeature eStructuralFeature)\n
    getName()\n
    getName()\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final EClassifier eClassifier, final String name)\n
    setName(final EStructuralFeature eStructuralFeature, final String name)\n
    setName(final String name)\n
    setName(final String name)\n
    setName(final String name)\n
    '''
def isAnonymous():
    '''returns boolean\n\n
    isAnonymous(final EClassifier eClassifier)\n
    '''
def getAttribute():
    '''returns EStructuralFeature\n\n
    getAttribute(final String namespace, final String name)\n
    getAttribute(final EClass eClass, final String namespace, final String name)\n
    '''
def getElement():
    '''returns EStructuralFeature\n\n
    getElement(final String namespace, final String name)\n
    getElement(final EClass eClass, final String namespace, final String name)\n
    '''
def getFeatureKind():
    '''returns int\n\n
    getFeatureKind(final EStructuralFeature eStructuralFeature)\n
    getFeatureKind()\n
    '''
def setFeatureKind():
    '''returns None\n\n
    setFeatureKind(final EStructuralFeature eStructuralFeature, final int kind)\n
    setFeatureKind(final int kind)\n
    '''
def getContentKind():
    '''returns int\n\n
    getContentKind(final EClass eClass)\n
    getContentKind()\n
    getContentKind()\n
    '''
def setContentKind():
    '''returns None\n\n
    setContentKind(final EClass eClass, final int kind)\n
    setContentKind(final int kind)\n
    setContentKind(final int kind)\n
    '''
def getDerivationKind():
    '''returns int\n\n
    getDerivationKind(final EDataType eDataType)\n
    getDerivationKind()\n
    getDerivationKind()\n
    '''
def getBaseType():
    '''returns EDataType\n\n
    getBaseType(final EDataType eDataType)\n
    getBaseType()\n
    getBaseType()\n
    '''
def basicGetBaseType():
    '''returns EDataType\n\n
    basicGetBaseType(final EDataType eDataType)\n
    '''
def setBaseType():
    '''returns None\n\n
    setBaseType(final EDataType eDataType, final EDataType baseType)\n
    setBaseType(final EDataType baseType)\n
    setBaseType(final EDataType baseType)\n
    '''
def getItemType():
    '''returns EDataType\n\n
    getItemType(final EDataType eDataType)\n
    getItemType()\n
    getItemType()\n
    '''
def setItemType():
    '''returns None\n\n
    setItemType(final EDataType eDataType, final EDataType itemType)\n
    setItemType(final EDataType itemType)\n
    setItemType(final EDataType itemType)\n
    '''
def getMemberTypes():
    '''returns List\n\n
    getMemberTypes(final EDataType eDataType)\n
    getMemberTypes()\n
    getMemberTypes()\n
    '''
def setMemberTypes():
    '''returns None\n\n
    setMemberTypes(final EDataType eDataType, final List memberTypes)\n
    setMemberTypes(final List memberTypes)\n
    setMemberTypes(final List memberTypes)\n
    '''
def getLocalAttribute():
    '''returns EStructuralFeature\n\n
    getLocalAttribute(final EClass eClass, final String namespace, final String name)\n
    '''
def getAllAttributes():
    '''returns List\n\n
    getAllAttributes(final EClass eClass)\n
    '''
def getAllElements():
    '''returns List\n\n
    getAllElements(final EClass eClass)\n
    '''
def getAttributes():
    '''returns List\n\n
    getAttributes(final EClass eClass)\n
    '''
def getElements():
    '''returns List\n\n
    getElements(final EClass eClass)\n
    '''
def getSimpleFeature():
    '''returns EStructuralFeature\n\n
    getSimpleFeature(final EClass eClass)\n
    '''
def getMixedFeature():
    '''returns EAttribute\n\n
    getMixedFeature(final EClass eClass)\n
    '''
def getWildcards():
    '''returns List\n\n
    getWildcards(final EStructuralFeature eStructuralFeature)\n
    getWildcards()\n
    '''
def setWildcards():
    '''returns None\n\n
    setWildcards(final EStructuralFeature eStructuralFeature, final List wildcards)\n
    setWildcards(final List wildcards)\n
    '''
def getProcessingKind():
    '''returns int\n\n
    getProcessingKind(final EStructuralFeature eStructuralFeature)\n
    getProcessingKind()\n
    '''
def setProcessingKind():
    '''returns None\n\n
    setProcessingKind(final EStructuralFeature eStructuralFeature, final int kind)\n
    setProcessingKind(final int kind)\n
    '''
def getGroup():
    '''returns EStructuralFeature\n\n
    getGroup(final EStructuralFeature eStructuralFeature)\n
    getGroup()\n
    '''
def setGroup():
    '''returns None\n\n
    setGroup(final EStructuralFeature eStructuralFeature, final EStructuralFeature group)\n
    setGroup(final EStructuralFeature group)\n
    '''
def getAffiliation():
    '''returns EStructuralFeature\n\n
    getAffiliation(final EStructuralFeature eStructuralFeature)\n
    getAffiliation(final EClass eClass, final EStructuralFeature eStructuralFeature)\n
    getAffiliation()\n
    '''
def setAffiliation():
    '''returns None\n\n
    setAffiliation(final EStructuralFeature eStructuralFeature, final EStructuralFeature affiliation)\n
    setAffiliation(final EStructuralFeature affiliation)\n
    '''
def getAttributeWildcardAffiliation():
    '''returns EStructuralFeature\n\n
    getAttributeWildcardAffiliation(final EClass eClass, final String namespace, final String name)\n
    '''
def getElementWildcardAffiliation():
    '''returns EStructuralFeature\n\n
    getElementWildcardAffiliation(final EClass eClass, final String namespace, final String name)\n
    '''
def matches():
    '''returns boolean\n\n
    matches(final List wildcards, final String namespace)\n
    matches(final String wildcard, final String namespace)\n
    '''
def getWhiteSpaceFacet():
    '''returns int\n\n
    getWhiteSpaceFacet(final EDataType eDataType)\n
    getWhiteSpaceFacet()\n
    getWhiteSpaceFacet()\n
    '''
def setWhiteSpaceFacet():
    '''returns None\n\n
    setWhiteSpaceFacet(final EDataType eDataType, final int whiteSpace)\n
    setWhiteSpaceFacet(final int whiteSpace)\n
    setWhiteSpaceFacet(final int whiteSpace)\n
    '''
def getEnumerationFacet():
    '''returns List\n\n
    getEnumerationFacet(final EDataType eDataType)\n
    getEnumerationFacet()\n
    getEnumerationFacet()\n
    '''
def setEnumerationFacet():
    '''returns None\n\n
    setEnumerationFacet(final EDataType eDataType, final List literals)\n
    setEnumerationFacet(final List literals)\n
    setEnumerationFacet(final List literals)\n
    '''
def getPatternFacet():
    '''returns List\n\n
    getPatternFacet(final EDataType eDataType)\n
    getPatternFacet()\n
    getPatternFacet()\n
    '''
def setPatternFacet():
    '''returns None\n\n
    setPatternFacet(final EDataType eDataType, final List pattern)\n
    setPatternFacet(final List pattern)\n
    setPatternFacet(final List pattern)\n
    '''
def getTotalDigitsFacet():
    '''returns int\n\n
    getTotalDigitsFacet(final EDataType eDataType)\n
    getTotalDigitsFacet()\n
    getTotalDigitsFacet()\n
    '''
def setTotalDigitsFacet():
    '''returns None\n\n
    setTotalDigitsFacet(final EDataType eDataType, final int digits)\n
    setTotalDigitsFacet(final int digits)\n
    setTotalDigitsFacet(final int digits)\n
    '''
def getFractionDigitsFacet():
    '''returns int\n\n
    getFractionDigitsFacet(final EDataType eDataType)\n
    getFractionDigitsFacet()\n
    getFractionDigitsFacet()\n
    '''
def setFractionDigitsFacet():
    '''returns None\n\n
    setFractionDigitsFacet(final EDataType eDataType, final int digits)\n
    setFractionDigitsFacet(final int digits)\n
    setFractionDigitsFacet(final int digits)\n
    '''
def getLengthFacet():
    '''returns int\n\n
    getLengthFacet(final EDataType eDataType)\n
    getLengthFacet()\n
    getLengthFacet()\n
    '''
def setLengthFacet():
    '''returns None\n\n
    setLengthFacet(final EDataType eDataType, final int length)\n
    setLengthFacet(final int length)\n
    setLengthFacet(final int length)\n
    '''
def getMinLengthFacet():
    '''returns int\n\n
    getMinLengthFacet(final EDataType eDataType)\n
    getMinLengthFacet()\n
    getMinLengthFacet()\n
    '''
def setMinLengthFacet():
    '''returns None\n\n
    setMinLengthFacet(final EDataType eDataType, final int length)\n
    setMinLengthFacet(final int minLength)\n
    setMinLengthFacet(final int minLength)\n
    '''
def getMaxLengthFacet():
    '''returns int\n\n
    getMaxLengthFacet(final EDataType eDataType)\n
    getMaxLengthFacet()\n
    getMaxLengthFacet()\n
    '''
def setMaxLengthFacet():
    '''returns None\n\n
    setMaxLengthFacet(final EDataType eDataType, final int length)\n
    setMaxLengthFacet(final int maxLength)\n
    setMaxLengthFacet(final int maxLength)\n
    '''
def getMinExclusiveFacet():
    '''returns String\n\n
    getMinExclusiveFacet(final EDataType eDataType)\n
    getMinExclusiveFacet()\n
    getMinExclusiveFacet()\n
    '''
def setMinExclusiveFacet():
    '''returns None\n\n
    setMinExclusiveFacet(final EDataType eDataType, final String literal)\n
    setMinExclusiveFacet(final String literal)\n
    setMinExclusiveFacet(final String literal)\n
    '''
def getMaxExclusiveFacet():
    '''returns String\n\n
    getMaxExclusiveFacet(final EDataType eDataType)\n
    getMaxExclusiveFacet()\n
    getMaxExclusiveFacet()\n
    '''
def setMaxExclusiveFacet():
    '''returns None\n\n
    setMaxExclusiveFacet(final EDataType eDataType, final String literal)\n
    setMaxExclusiveFacet(final String literal)\n
    setMaxExclusiveFacet(final String literal)\n
    '''
def getMinInclusiveFacet():
    '''returns String\n\n
    getMinInclusiveFacet(final EDataType eDataType)\n
    getMinInclusiveFacet()\n
    getMinInclusiveFacet()\n
    '''
def setMinInclusiveFacet():
    '''returns None\n\n
    setMinInclusiveFacet(final EDataType eDataType, final String literal)\n
    setMinInclusiveFacet(final String literal)\n
    setMinInclusiveFacet(final String literal)\n
    '''
def getMaxInclusiveFacet():
    '''returns String\n\n
    getMaxInclusiveFacet(final EDataType eDataType)\n
    getMaxInclusiveFacet()\n
    getMaxInclusiveFacet()\n
    '''
def setMaxInclusiveFacet():
    '''returns None\n\n
    setMaxInclusiveFacet(final EDataType eDataType, final String literal)\n
    setMaxInclusiveFacet(final String literal)\n
    setMaxInclusiveFacet(final String literal)\n
    '''
def demandPackage():
    '''returns EPackage\n\n
    demandPackage(final String namespace)\n
    '''
def demandType():
    '''returns EClassifier\n\n
    demandType(final String namespace, final String name)\n
    '''
def demandFeature():
    '''returns EStructuralFeature\n\n
    demandFeature(final String namespace, final String name, final boolean isElement)\n
    demandFeature(final String namespace, final String name, final boolean isElement, final boolean isReference)\n
    '''
def demandedPackages():
    '''returns Collection\n\n
    demandedPackages()\n
    '''
def getValidatorMap():
    '''returns Map\n\n
    getValidatorMap()\n
    '''
