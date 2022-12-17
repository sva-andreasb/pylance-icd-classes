def ():
    '''returns XMLHelperImpl\n\n
    ()\n
    (final XMLResource resource)\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final Map options)\n
    '''
def setNoNamespacePackage():
    '''returns None\n\n
    setNoNamespacePackage(final EPackage pkg)\n
    '''
def getNoNamespacePackage():
    '''returns EPackage\n\n
    getNoNamespacePackage()\n
    '''
def setXMLMap():
    '''returns None\n\n
    setXMLMap(final XMLResource.XMLMap map)\n
    '''
def setExtendedMetaData():
    '''returns None\n\n
    setExtendedMetaData(final ExtendedMetaData extendedMetaData)\n
    '''
def getExtendedMetaData():
    '''returns ExtendedMetaData\n\n
    getExtendedMetaData()\n
    '''
def getResource():
    '''returns XMLResource\n\n
    getResource()\n
    '''
def setResource():
    '''returns None\n\n
    setResource(final XMLResource resource)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue(final EObject obj, final EStructuralFeature f)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final EClass c)\n
    getQName(final EDataType c)\n
    getQName(final EStructuralFeature feature)\n
    '''
def populateNameInfo():
    '''returns None\n\n
    populateNameInfo(final NameInfo nameInfo, final EClass c)\n
    populateNameInfo(final NameInfo nameInfo, final EDataType eDataType)\n
    populateNameInfo(final NameInfo nameInfo, final EStructuralFeature feature)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final EPackage ePackage)\n
    getPrefix(final String uri)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String prefix)\n
    '''
def getPrefixes():
    '''returns List\n\n
    getPrefixes(final EPackage ePackage)\n
    '''
def getName():
    '''returns String\n\n
    getName(final ENamedElement obj)\n
    '''
def getID():
    '''returns String\n\n
    getID(final EObject obj)\n
    '''
def getIDREF():
    '''returns String\n\n
    getIDREF(final EObject obj)\n
    '''
def getHREF():
    '''returns String\n\n
    getHREF(final EObject obj)\n
    '''
def deresolve():
    '''returns URI\n\n
    deresolve(URI uri)\n
    '''
def getFeatureKind():
    '''returns int\n\n
    getFeatureKind(final EStructuralFeature feature)\n
    '''
def createObject():
    '''returns EObject\n\n
    createObject(final EFactory eFactory, final String classXMIName)\n
    '''
def getFeature():
    '''returns EStructuralFeature\n\n
    getFeature(final EClass eClass, final String namespaceURI, final String name)\n
    getFeature(final EClass eClass, final String namespaceURI, final String name, final boolean isElement)\n
    '''
def getJavaEncoding():
    '''returns String\n\n
    getJavaEncoding(final String xmlEncoding)\n
    '''
def getXMLEncoding():
    '''returns String\n\n
    getXMLEncoding(final String javaEncoding)\n
    '''
def packages():
    '''returns EPackage[]\n\n
    packages()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final EObject object, EStructuralFeature feature, Object value, final int position)\n
    '''
def setManyReference():
    '''returns List\n\n
    setManyReference(final ManyReference reference, final String location)\n
    '''
def setCheckForDuplicates():
    '''returns None\n\n
    setCheckForDuplicates(final boolean checkForDuplicates)\n
    '''
def setProcessDanglingHREF():
    '''returns None\n\n
    setProcessDanglingHREF(final String value)\n
    '''
def getDanglingHREFException():
    '''returns DanglingHREFException\n\n
    getDanglingHREFException()\n
    '''
def resolve():
    '''returns URI\n\n
    resolve(final URI relative, final URI base)\n
    '''
def pushContext():
    '''returns None\n\n
    pushContext()\n
    pushContext()\n
    '''
def popContext():
    '''returns None\n\n
    popContext()\n
    popContext()\n
    '''
def addPrefix():
    '''returns None\n\n
    addPrefix(final String prefix, String uri)\n
    '''
def getAnyContentPrefixToURIMapping():
    '''returns Map\n\n
    getAnyContentPrefixToURIMapping()\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final String prefix)\n
    getURI(final String prefix)\n
    '''
def getPrefixToNamespaceMap():
    '''returns EMap\n\n
    getPrefixToNamespaceMap()\n
    '''
def recordPrefixToURIMapping():
    '''returns None\n\n
    recordPrefixToURIMapping()\n
    '''
def setPrefixToNamespaceMap():
    '''returns None\n\n
    setPrefixToNamespaceMap(final EMap prefixToNamespaceMap)\n
    '''
def setAnySimpleType():
    '''returns None\n\n
    setAnySimpleType(final EClass type)\n
    '''
def convertToString():
    '''returns String\n\n
    convertToString(final EFactory factory, final EDataType dataType, final Object value)\n
    '''
def setMustHavePrefix():
    '''returns None\n\n
    setMustHavePrefix(final boolean mustHavePrefix)\n
    '''
def declarePrefix():
    '''returns boolean\n\n
    declarePrefix(final String prefix, final String uri)\n
    '''
def getDeclaredPrefixCount():
    '''returns int\n\n
    getDeclaredPrefixCount()\n
    '''
def getDeclaredPrefixAt():
    '''returns String\n\n
    getDeclaredPrefixAt(final int index)\n
    '''
