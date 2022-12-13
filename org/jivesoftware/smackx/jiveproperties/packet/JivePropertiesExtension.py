NAMESPACE = "String  \"http://www.jivesoftware.com/xmlns/xmpp/properties\""
ELEMENT = "String  \"properties\""
def JivePropertiesExtension():
    '''    public JivePropertiesExtension()
    public JivePropertiesExtension(final Map<String, Object> properties)
    '''
def getProperty():
    '''    public synchronized Object getProperty(final String name)
    '''
def setProperty():
    '''    public synchronized void setProperty(final String name, final Object value)
    '''
def deleteProperty():
    '''    public synchronized void deleteProperty(final String name)
    '''
def getPropertyNames():
    '''    public synchronized Collection<String> getPropertyNames()
    '''
def getProperties():
    '''    public synchronized Map<String, Object> getProperties()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public CharSequence toXML(final String enclosingNamespace)
    '''
def from():
    '''    public static JivePropertiesExtension from(final Message message)
    '''
