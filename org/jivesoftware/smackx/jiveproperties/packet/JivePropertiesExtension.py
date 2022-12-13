NAMESPACE = "String  http://www.jivesoftware.com/xmlns/xmpp/properties""
ELEMENT = "String  properties""
def JivePropertiesExtension():
'''public JivePropertiesExtension()
public JivePropertiesExtension(final Map<String, Object> properties)
'''
pass
def getProperty():
'''public synchronized Object getProperty(final String name)
'''
pass
def setProperty():
'''public synchronized void setProperty(final String name, final Object value)
'''
pass
def deleteProperty():
'''public synchronized void deleteProperty(final String name)
'''
pass
def getPropertyNames():
'''public synchronized Collection<String> getPropertyNames()
'''
pass
def getProperties():
'''public synchronized Map<String, Object> getProperties()
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
def toXML():
'''public CharSequence toXML(final String enclosingNamespace)
'''
pass
def from():
'''public static JivePropertiesExtension from(final Message message)
'''
pass
