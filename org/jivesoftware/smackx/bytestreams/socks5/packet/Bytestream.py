ELEMENT = "String  query""
NAMESPACE = "String  http://jabber.org/protocol/bytestreams""
def Bytestream():
'''public Bytestream()
public Bytestream(final String SID)
'''
pass
def setSessionID():
'''public void setSessionID(final String sessionID)
'''
pass
def getSessionID():
'''public String getSessionID()
'''
pass
def setMode():
'''public void setMode(final Mode mode)
'''
pass
def getMode():
'''public Mode getMode()
'''
pass
def addStreamHost():
'''public StreamHost addStreamHost(final Jid JID, final String address)
public StreamHost addStreamHost(final Jid JID, final String address, final int port)
public void addStreamHost(final StreamHost host)
'''
pass
def getStreamHosts():
'''public List<StreamHost> getStreamHosts()
'''
pass
def getStreamHost():
'''public StreamHost getStreamHost(final Jid JID)
'''
pass
def countStreamHosts():
'''public int countStreamHosts()
'''
pass
def setUsedHost():
'''public void setUsedHost(final Jid JID)
'''
pass
def getUsedHost():
'''public StreamHostUsed getUsedHost()
'''
pass
def getToActivate():
'''public Activate getToActivate()
'''
pass
def setToActivate():
'''public void setToActivate(final Jid targetID)
'''
pass
def StreamHost():
'''public StreamHost(final Jid jid, final String address)
public StreamHost(final Jid JID, final String address, final int port)
'''
pass
def getJID():
'''public Jid getJID()
public Jid getJID()
'''
pass
def getAddress():
'''public String getAddress()
'''
pass
def getPort():
'''public int getPort()
'''
pass
def getElementName():
'''public String getElementName()
public String getElementName()
public String getElementName()
'''
pass
def toXML():
'''public XmlStringBuilder toXML(final String enclosingNamespace)
public XmlStringBuilder toXML(final String enclosingNamespace)
public XmlStringBuilder toXML(final String enclosingNamespace)
'''
pass
def StreamHostUsed():
'''public StreamHostUsed(final Jid JID)
'''
pass
def Activate():
'''public Activate(final Jid target)
'''
pass
def getTarget():
'''public Jid getTarget()
'''
pass
def fromName():
'''public static Mode fromName(final String name)
'''
pass
