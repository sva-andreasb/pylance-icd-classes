TEXT = "String  text""
ITEM = "String  item""
def getStanzaId():
'''public String getStanzaId()
'''
pass
def getPacketID():
'''public String getPacketID()
'''
pass
def setStanzaId():
'''public void setStanzaId(final String id)
public String setStanzaId()
'''
pass
def setPacketID():
'''public void setPacketID(final String packetID)
'''
pass
def hasStanzaIdSet():
'''public boolean hasStanzaIdSet()
'''
pass
def getTo():
'''public Jid getTo()
'''
pass
def setTo():
'''public void setTo(final String to)
public void setTo(final Jid to)
'''
pass
def getFrom():
'''public Jid getFrom()
'''
pass
def setFrom():
'''public void setFrom(final String from)
public void setFrom(final Jid from)
'''
pass
def getError():
'''public StanzaError getError()
'''
pass
def setError():
'''public void setError(final StanzaError error)
public void setError(final StanzaError.Builder xmppErrorBuilder)
'''
pass
def getLanguage():
'''public String getLanguage()
'''
pass
def setLanguage():
'''public void setLanguage(final String language)
'''
pass
def getExtensions():
'''public List<ExtensionElement> getExtensions()
public List<ExtensionElement> getExtensions(final String elementName, final String namespace)
'''
pass
def getExtension():
'''public ExtensionElement getExtension(final String namespace)
public <PE extends ExtensionElement> PE getExtension(final String elementName, final String namespace)
'''
pass
def addExtension():
'''public void addExtension(final ExtensionElement extension)
'''
pass
def overrideExtension():
'''public ExtensionElement overrideExtension(final ExtensionElement extension)
'''
pass
def addExtensions():
'''public void addExtensions(final Collection<ExtensionElement> extensions)
'''
pass
def hasExtension():
'''public boolean hasExtension(final String elementName, final String namespace)
public boolean hasExtension(final String namespace)
'''
pass
def removeExtension():
'''public ExtensionElement removeExtension(final String elementName, final String namespace)
public ExtensionElement removeExtension(final ExtensionElement extension)
'''
pass
def getDefaultLanguage():
'''public static String getDefaultLanguage()
'''
pass
