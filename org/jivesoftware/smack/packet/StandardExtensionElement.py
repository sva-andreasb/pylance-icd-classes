def StandardExtensionElement():
    '''public StandardExtensionElement(final String name, final String namespace)
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def getAttributeValue():
    '''public String getAttributeValue(final String attribute)
    '''
def getAttributes():
    '''public Map<String, String> getAttributes()
    '''
def getFirstElement():
    '''public StandardExtensionElement getFirstElement(final String element, final String namespace)
    public StandardExtensionElement getFirstElement(final String element)
    '''
def getElements():
    '''public List<StandardExtensionElement> getElements(final String element, final String namespace)
    public List<StandardExtensionElement> getElements(final String element)
    public List<StandardExtensionElement> getElements()
    '''
def getText():
    '''public String getText()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def builder():
    '''public static Builder builder(final String name, final String namespace)
    '''
def addAttribute():
    '''public Builder addAttribute(final String name, final String value)
    '''
def addAttributes():
    '''public Builder addAttributes(final Map<String, String> attributes)
    '''
def setText():
    '''public Builder setText(final String text)
    '''
def addElement():
    '''public Builder addElement(final StandardExtensionElement element)
    public Builder addElement(final String name, final String textValue)
    '''
def build():
    '''public StandardExtensionElement build()
    '''
