ELEMENT = "String  \"query\""
NAMESPACE = "String  \"http://jabber.org/protocol/bytestreams\""
def ():
    '''returns Activate\n\n
    ()\n
    (final String SID)\n
    (final Jid jid, final String address)\n
    (final Jid JID, final String address, final int port)\n
    (final Jid JID)\n
    (final Jid target)\n
    '''
def setSessionID():
    '''returns None\n\n
    setSessionID(final String sessionID)\n
    '''
def getSessionID():
    '''returns String\n\n
    getSessionID()\n
    '''
def setMode():
    '''returns None\n\n
    setMode(final Mode mode)\n
    '''
def getMode():
    '''returns Mode\n\n
    getMode()\n
    '''
def addStreamHost():
    '''returns None\n\n
    addStreamHost(final Jid JID, final String address)\n
    addStreamHost(final Jid JID, final String address, final int port)\n
    addStreamHost(final StreamHost host)\n
    '''
def getStreamHosts():
    '''returns List<StreamHost>\n\n
    getStreamHosts()\n
    '''
def getStreamHost():
    '''returns StreamHost\n\n
    getStreamHost(final Jid JID)\n
    '''
def countStreamHosts():
    '''returns int\n\n
    countStreamHosts()\n
    '''
def setUsedHost():
    '''returns None\n\n
    setUsedHost(final Jid JID)\n
    '''
def getUsedHost():
    '''returns StreamHostUsed\n\n
    getUsedHost()\n
    '''
def getToActivate():
    '''returns Activate\n\n
    getToActivate()\n
    '''
def setToActivate():
    '''returns None\n\n
    setToActivate(final Jid targetID)\n
    '''
def getJID():
    '''returns Jid\n\n
    getJID()\n
    getJID()\n
    '''
def getAddress():
    '''returns String\n\n
    getAddress()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    getElementName()\n
    getElementName()\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    toXML(final String enclosingNamespace)\n
    '''
def getTarget():
    '''returns Jid\n\n
    getTarget()\n
    '''
