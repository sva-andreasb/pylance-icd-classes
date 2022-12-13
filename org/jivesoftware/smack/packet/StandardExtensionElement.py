def StandardExtensionElement():
'''public StandardExtensionElement(final String name, final String namespace)
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def getAttributeValue():
'''public String getAttributeValue(final String attribute)
'''
pass
def getAttributes():
'''public Map<String, String> getAttributes()
'''
pass
def getFirstElement():
'''public StandardExtensionElement getFirstElement(final String element, final String namespace)
public StandardExtensionElement getFirstElement(final String element)
'''
pass
def getElements():
'''public List<StandardExtensionElement> getElements(final String element, final String namespace)
public List<StandardExtensionElement> getElements(final String element)
public List<StandardExtensionElement> getElements()
'''
pass
def getText():
'''public String getText()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def builder():
'''public static Builder builder(final String name, final String namespace)
'''
pass
def addAttribute():
'''public Builder addAttribute(final String name, final String value)
'''
pass
def addAttributes():
'''public Builder addAttributes(final Map<String, String> attributes)
'''
pass
def setText():
'''public Builder setText(final String text)
'''
pass
def addElement():
'''public Builder addElement(final StandardExtensionElement element)
public Builder addElement(final String name, final String textValue)
'''
pass
def build():
'''public StandardExtensionElement build()
'''
pass
