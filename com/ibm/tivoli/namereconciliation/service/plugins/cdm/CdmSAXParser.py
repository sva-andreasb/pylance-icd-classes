def ():
    '''returns FoundVersionException\n\n
    (final String namingRulesLocation)\n
    (final String message)\n
    '''
def getNamingRulesVersion():
    '''returns String\n\n
    getNamingRulesVersion(final String namingRulesLocation)\n
    getNamingRulesVersion(final MetadataService metaService)\n
    '''
def getNextNamingPolicy():
    '''returns NamingPolicy\n\n
    getNextNamingPolicy(final String duplicateClassName)\n
    '''
def containsMultipleSuperiors():
    '''returns boolean\n\n
    containsMultipleSuperiors(final String classType)\n
    '''
def getNamingPolicyForClass():
    '''returns NamingPolicy\n\n
    getNamingPolicyForClass(final String className)\n
    '''
def isSuperiorClass():
    '''returns boolean\n\n
    isSuperiorClass(final String className)\n
    '''
def isParent():
    '''returns boolean\n\n
    isParent(final String parentClass, final String childClass)\n
    '''
def isIdentifyingAttribute():
    '''returns boolean\n\n
    isIdentifyingAttribute(final String classType, final String attribute)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    startElement(final String uri, final String localName, final String qName, final Attributes attributes)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String uri, final String localName, final String qName)\n
    endElement(final String uri, final String localName, final String qName)\n
    '''
