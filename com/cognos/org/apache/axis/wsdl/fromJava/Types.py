def ():
    '''returns Types\n\n
    (final Definition def, final TypeMapping tm, final TypeMapping defaultTM, final Namespaces namespaces, final String targetNamespace, final List stopClasses, final ServiceDesc serviceDesc)\n
    (final Definition def, final TypeMapping tm, final TypeMapping defaultTM, final Namespaces namespaces, final String targetNamespace, final List stopClasses, final ServiceDesc serviceDesc, final Emitter emitter)\n
    '''
def getNamespaces():
    '''returns Namespaces\n\n
    getNamespaces()\n
    '''
def loadInputSchema():
    '''returns None\n\n
    loadInputSchema(final String inputSchema)\n
    '''
def getBaseName():
    '''returns String\n\n
    getBaseName(final QName qNameIn)\n
    getBaseName(final QName qNameIn)\n
    '''
def loadInputTypes():
    '''returns None\n\n
    loadInputTypes(final String inputWSDL)\n
    '''
def writeTypeForPart():
    '''returns QName\n\n
    writeTypeForPart(Class type, QName qname)\n
    '''
def writeTypeAndSubTypeForPart():
    '''returns QName\n\n
    writeTypeAndSubTypeForPart(final Class type, final QName qname)\n
    '''
def writeElementForPart():
    '''returns QName\n\n
    writeElementForPart(Class type, QName qname)\n
    '''
def writeWrapperElement():
    '''returns Element\n\n
    writeWrapperElement(final QName qname, final boolean request, final boolean hasParams)\n
    '''
def writeWrappedParameter():
    '''returns None\n\n
    writeWrappedParameter(final Element sequence, final String name, QName type, final Class javaType)\n
    '''
def getTypeQName():
    '''returns QName\n\n
    getTypeQName(final Class javaType)\n
    '''
def getQNameString():
    '''returns String\n\n
    getQNameString(final QName qname)\n
    '''
def writeSchemaTypeDecl():
    '''returns None\n\n
    writeSchemaTypeDecl(final QName qname, final Element element)\n
    '''
def writeSchemaElementDecl():
    '''returns None\n\n
    writeSchemaElementDecl(final QName qname, final Element element)\n
    '''
def writeSchemaElement():
    '''returns None\n\n
    writeSchemaElement(final QName qName, final Element element)\n
    writeSchemaElement(final String namespaceURI, final Element element)\n
    '''
def writeType():
    '''returns String\n\n
    writeType(final Class type)\n
    writeType(final Class type, QName qName)\n
    '''
def createArrayElement():
    '''returns Element\n\n
    createArrayElement(final String componentTypeName)\n
    '''
def createLiteralArrayElement():
    '''returns Element\n\n
    createLiteralArrayElement(final String componentType, final QName itemName)\n
    '''
def writeEnumType():
    '''returns Element\n\n
    writeEnumType(final QName qName, final Class cls)\n
    '''
def writeElementDecl():
    '''returns None\n\n
    writeElementDecl(final QName qname, final Class javaType, final QName typeQName, final boolean nillable, final QName itemQName)\n
    '''
def createElement():
    '''returns Element\n\n
    createElement(final String elementName, final String elementType, final boolean nullable, final boolean omittable, final Document docHolder)\n
    createElement(final String elementName)\n
    '''
def createAttributeElement():
    '''returns Element\n\n
    createAttributeElement(final String elementName, final Class javaType, final QName xmlType, final boolean nullable, final Document docHolder)\n
    '''
def isAcceptableAsAttribute():
    '''returns boolean\n\n
    isAcceptableAsAttribute(final Class type)\n
    '''
def updateNamespaces():
    '''returns None\n\n
    updateNamespaces()\n
    '''
def insertTypesFragment():
    '''returns None\n\n
    insertTypesFragment(final Document doc)\n
    '''
def getStopClasses():
    '''returns List\n\n
    getStopClasses()\n
    '''
def createElementWithAnonymousType():
    '''returns Element\n\n
    createElementWithAnonymousType(final String elementName, final Class fieldType, final boolean omittable, final Document ownerDocument)\n
    '''
def getServiceDesc():
    '''returns ServiceDesc\n\n
    getServiceDesc()\n
    '''
