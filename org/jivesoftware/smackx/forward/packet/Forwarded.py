NAMESPACE = "String  urn:xmpp:forward:0""
ELEMENT = "String  forwarded""
def Forwarded():
'''public Forwarded(final DelayInformation delay, final Stanza fwdPacket)
public Forwarded(final Stanza fwdPacket)
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
'''public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def getForwardedPacket():
'''public Stanza getForwardedPacket()
'''
pass
def getForwardedStanza():
'''public Stanza getForwardedStanza()
'''
pass
def getDelayInformation():
'''public DelayInformation getDelayInformation()
'''
pass
def from():
'''public static Forwarded from(final Stanza packet)
'''
pass
def extractMessagesFrom():
'''public static List<Message> extractMessagesFrom(final Collection<Forwarded> forwardedCollection)
'''
pass
