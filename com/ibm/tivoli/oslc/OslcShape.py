def ():
    '''returns OslcShape\n\n
    (final Model oslcModel, final String resType, final String shapeURI)\n
    '''
def setMaxSize():
    '''returns None\n\n
    setMaxSize(final Resource property, final String size)\n
    '''
def setOccurs():
    '''returns None\n\n
    setOccurs(final Resource property, final String occursURI)\n
    '''
def setPropertyName():
    '''returns None\n\n
    setPropertyName(final Resource property, final String propName)\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue(final Resource property, final String defValue)\n
    '''
def setPropertyDefinition():
    '''returns None\n\n
    setPropertyDefinition(final Resource property, final String propNsURI)\n
    '''
def setValueType():
    '''returns None\n\n
    setValueType(final Resource property)\n
    setValueType(final Resource property, final String valueType)\n
    '''
def setRepresentation():
    '''returns None\n\n
    setRepresentation(final Resource property, final String repURI)\n
    '''
def setRange():
    '''returns None\n\n
    setRange(final Resource property, final String rangeURI)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final Resource property, final String title)\n
    '''
def setUsage():
    '''returns None\n\n
    setUsage(final Resource Property, final Set<String> usageURISet)\n
    '''
def createResourceProperty():
    '''returns Resource\n\n
    createResourceProperty(String occursURI, final String propName, final String propNs, final String valueTypeURI, final String rangeURI, final String valueShapeURI, final String title, final Set<String> usageURIs, final String representationURI)\n
    '''
def createLiteralProperty():
    '''returns None\n\n
    createLiteralProperty(String occursURI, final String propName, final String propNs, String valueTypeURI, final String title, String defaultValue, final int maxSize)\n
    '''
