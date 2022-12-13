NAME = "String  \"rtpbridge\""
ELEMENT_NAME = "String  \"rtpbridge\""
NAMESPACE = "String  \"http://www.jivesoftware.com/protocol/rtpbridge\""
def RTPBridge():
    '''    public RTPBridge(final String sid)
    public RTPBridge(final BridgeAction action)
    public RTPBridge(final String sid, final BridgeAction bridgeAction)
    public RTPBridge()
    '''
def getAttributes():
    '''    public String getAttributes()
    '''
def getSid():
    '''    public String getSid()
    '''
def setSid():
    '''    public void setSid(final String sid)
    '''
def getHostA():
    '''    public String getHostA()
    '''
def setHostA():
    '''    public void setHostA(final String hostA)
    '''
def getHostB():
    '''    public String getHostB()
    '''
def setHostB():
    '''    public void setHostB(final String hostB)
    '''
def getPortA():
    '''    public int getPortA()
    '''
def setPortA():
    '''    public void setPortA(final int portA)
    '''
def getPortB():
    '''    public int getPortB()
    '''
def setPortB():
    '''    public void setPortB(final int portB)
    '''
def getIp():
    '''    public String getIp()
    '''
def setIp():
    '''    public void setIp(final String ip)
    '''
def getPass():
    '''    public String getPass()
    '''
def setPass():
    '''    public void setPass(final String pass)
    '''
def getName():
    '''    public String getName()
    '''
def setName():
    '''    public void setName(final String name)
    '''
def getRTPBridge():
    '''    public static RTPBridge getRTPBridge(final XMPPConnection connection, final String sessionID)
    '''
def serviceAvailable():
    '''    public static boolean serviceAvailable(final XMPPConnection connection)
    '''
def relaySession():
    '''    public static RTPBridge relaySession(final XMPPConnection connection, final String sessionID, final String pass, final TransportCandidate proxyCandidate, final TransportCandidate localCandidate)
    '''
def getPublicIP():
    '''    public static String getPublicIP(final XMPPConnection xmppConnection)
    '''
def parse():
    '''    public RTPBridge parse(final XmlPullParser parser, final int initialDepth)
    '''
