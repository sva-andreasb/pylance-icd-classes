def ():
    '''returns StandardExtensionElement\n\n
    (final String name, final String namespace)\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final String attribute)\n
    '''
def getFirstElement():
    '''returns StandardExtensionElement\n\n
    getFirstElement(final String element, final String namespace)\n
    getFirstElement(final String element)\n
    '''
def getElements():
    '''returns List<StandardExtensionElement>\n\n
    getElements(final String element, final String namespace)\n
    getElements(final String element)\n
    getElements()\n
    '''
def getText():
    '''returns String\n\n
    getText()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    '''
def addAttribute():
    '''returns Builder\n\n
    addAttribute(final String name, final String value)\n
    '''
def addAttributes():
    '''returns Builder\n\n
    addAttributes(final Map<String, String> attributes)\n
    '''
def setText():
    '''returns Builder\n\n
    setText(final String text)\n
    '''
def addElement():
    '''returns Builder\n\n
    addElement(final StandardExtensionElement element)\n
    addElement(final String name, final String textValue)\n
    '''
def build():
    '''returns StandardExtensionElement\n\n
    build()\n
    '''
