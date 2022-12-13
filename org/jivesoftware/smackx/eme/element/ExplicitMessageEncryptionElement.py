ELEMENT = "String  \"encryption\""
NAMESPACE = "String  \"urn:xmpp:eme:0\""
def ExplicitMessageEncryptionElement():
    '''public ExplicitMessageEncryptionElement(final ExplicitMessageEncryptionProtocol protocol)
    public ExplicitMessageEncryptionElement(final String encryptionNamespace)
    public ExplicitMessageEncryptionElement(final String encryptionNamespace, final String name)
    '''
def getProtocol():
    '''public ExplicitMessageEncryptionProtocol getProtocol()
    '''
def getEncryptionNamespace():
    '''public String getEncryptionNamespace()
    '''
def getName():
    '''public String getName()
    public String getName()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    public String getNamespace()
    '''
def toXML():
    '''public XmlStringBuilder toXML(final String enclosingNamespace)
    '''
def from():
    '''public static ExplicitMessageEncryptionElement from(final Message message)
    public static ExplicitMessageEncryptionProtocol from(final String namespace)
    '''
