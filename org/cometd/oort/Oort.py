EXT_OORT_FIELD = "String  org.cometd.oort""
EXT_OORT_URL_FIELD = "String  oortURL""
EXT_OORT_ID_FIELD = "String  oortId""
EXT_OORT_SECRET_FIELD = "String  oortSecret""
EXT_COMET_URL_FIELD = "String  cometURL""
EXT_OORT_ALIAS_URL_FIELD = "String  oortAliasURL""
OORT_CLOUD_CHANNEL = "String  /oort/cloud""
def Oort():
'''public Oort(final BayeuxServer bayeux, final String url)
'''
pass
def configureChannel():
'''public void configureChannel(final ConfigurableServerChannel channel)
'''
pass
def getBayeuxServer():
'''public BayeuxServer getBayeuxServer()
'''
pass
def getURL():
'''public String getURL()
public String getURL()
'''
pass
def getId():
'''public String getId()
public String getId()
'''
pass
def getSecret():
'''public String getSecret()
'''
pass
def setSecret():
'''public void setSecret(final String secret)
'''
pass
def isDebugEnabled():
'''public boolean isDebugEnabled()
'''
pass
def setDebugEnabled():
'''public void setDebugEnabled(final boolean debug)
'''
pass
def isClientDebugEnabled():
'''public boolean isClientDebugEnabled()
'''
pass
def setClientDebugEnabled():
'''public void setClientDebugEnabled(final boolean clientDebugEnabled)
'''
pass
def observeComet():
'''public OortComet observeComet(final String cometURL)
'''
pass
def deobserveComet():
'''public OortComet deobserveComet(final String cometURL)
'''
pass
def getKnownComets():
'''public Set<String> getKnownComets()
'''
pass
def getComet():
'''public OortComet getComet(final String cometURL)
'''
pass
def observeChannel():
'''public void observeChannel(final String channelName)
'''
pass
def deobserveChannel():
'''public void deobserveChannel(final String channelId)
'''
pass
def isOort():
'''public boolean isOort(final ServerSession session)
'''
pass
def isOortHandshake():
'''public boolean isOortHandshake(final Message handshake)
'''
pass
def toString():
'''public String toString()
'''
pass
def addCometListener():
'''public void addCometListener(final CometListener listener)
'''
pass
def removeCometListener():
'''public void removeCometListener(final CometListener listener)
'''
pass
def setThreadPool():
'''public void setThreadPool(final ThreadPool threadPool)
'''
pass
def getThreadPool():
'''public ThreadPool getThreadPool()
'''
pass
def getWebSocketClientFactory():
'''public WebSocketClientFactory getWebSocketClientFactory()
'''
pass
def setWebSocketClientFactory():
'''public void setWebSocketClientFactory(final WebSocketClientFactory wsFactory)
'''
pass
def getHttpClient():
'''public HttpClient getHttpClient()
'''
pass
def setHttpClient():
'''public void setHttpClient(final HttpClient httpClient)
'''
pass
def getObservedChannels():
'''public Set<String> getObservedChannels()
'''
pass
def getOortSession():
'''public LocalSession getOortSession()
'''
pass
def rcv():
'''public boolean rcv(final ServerSession from, final ServerMessage.Mutable message)
'''
pass
def rcvMeta():
'''public boolean rcvMeta(final ServerSession from, final ServerMessage.Mutable message)
'''
pass
def send():
'''public boolean send(final ServerSession from, final ServerSession to, final ServerMessage.Mutable message)
'''
pass
def sendMeta():
'''public boolean sendMeta(final ServerSession to, final ServerMessage.Mutable message)
'''
pass
def onMessage():
'''public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
public boolean onMessage(final ServerSession to, final ServerSession from, final ServerMessage message)
public void onMessage(final ClientSessionChannel channel, final Message message)
'''
pass
def OortCometDisconnectListener():
'''public OortCometDisconnectListener(final String cometURL, final String remoteOortId)
'''
pass
def removed():
'''public void removed(final ServerSession session, final boolean timeout)
'''
pass
def getServerSession():
'''public ServerSession getServerSession()
'''
pass
def getOortComet():
'''public OortComet getOortComet()
'''
pass
def addAliasURL():
'''public void addAliasURL(final String url)
'''
pass
def matchesURL():
'''public boolean matchesURL(final String url)
'''
pass
def Event():
'''public Event(final Oort source, final String cometURL)
'''
pass
def getCometURL():
'''public String getCometURL()
'''
pass
