EXT_OORT_FIELD = "String  \"org.cometd.oort\""
EXT_OORT_URL_FIELD = "String  \"oortURL\""
EXT_OORT_ID_FIELD = "String  \"oortId\""
EXT_OORT_SECRET_FIELD = "String  \"oortSecret\""
EXT_COMET_URL_FIELD = "String  \"cometURL\""
EXT_OORT_ALIAS_URL_FIELD = "String  \"oortAliasURL\""
OORT_CLOUD_CHANNEL = "String  \"/oort/cloud\""
def Oort():
    '''public Oort(final BayeuxServer bayeux, final String url)
    '''
def configureChannel():
    '''public void configureChannel(final ConfigurableServerChannel channel)
    '''
def getBayeuxServer():
    '''public BayeuxServer getBayeuxServer()
    '''
def getURL():
    '''public String getURL()
    public String getURL()
    '''
def getId():
    '''public String getId()
    public String getId()
    '''
def getSecret():
    '''public String getSecret()
    '''
def setSecret():
    '''public void setSecret(final String secret)
    '''
def isDebugEnabled():
    '''public boolean isDebugEnabled()
    '''
def setDebugEnabled():
    '''public void setDebugEnabled(final boolean debug)
    '''
def isClientDebugEnabled():
    '''public boolean isClientDebugEnabled()
    '''
def setClientDebugEnabled():
    '''public void setClientDebugEnabled(final boolean clientDebugEnabled)
    '''
def observeComet():
    '''public OortComet observeComet(final String cometURL)
    '''
def deobserveComet():
    '''public OortComet deobserveComet(final String cometURL)
    '''
def getKnownComets():
    '''public Set<String> getKnownComets()
    '''
def getComet():
    '''public OortComet getComet(final String cometURL)
    '''
def observeChannel():
    '''public void observeChannel(final String channelName)
    '''
def deobserveChannel():
    '''public void deobserveChannel(final String channelId)
    '''
def isOort():
    '''public boolean isOort(final ServerSession session)
    '''
def isOortHandshake():
    '''public boolean isOortHandshake(final Message handshake)
    '''
def toString():
    '''public String toString()
    '''
def addCometListener():
    '''public void addCometListener(final CometListener listener)
    '''
def removeCometListener():
    '''public void removeCometListener(final CometListener listener)
    '''
def setThreadPool():
    '''public void setThreadPool(final ThreadPool threadPool)
    '''
def getThreadPool():
    '''public ThreadPool getThreadPool()
    '''
def getWebSocketClientFactory():
    '''public WebSocketClientFactory getWebSocketClientFactory()
    '''
def setWebSocketClientFactory():
    '''public void setWebSocketClientFactory(final WebSocketClientFactory wsFactory)
    '''
def getHttpClient():
    '''public HttpClient getHttpClient()
    '''
def setHttpClient():
    '''public void setHttpClient(final HttpClient httpClient)
    '''
def getObservedChannels():
    '''public Set<String> getObservedChannels()
    '''
def getOortSession():
    '''public LocalSession getOortSession()
    '''
def rcv():
    '''public boolean rcv(final ServerSession from, final ServerMessage.Mutable message)
    '''
def rcvMeta():
    '''public boolean rcvMeta(final ServerSession from, final ServerMessage.Mutable message)
    '''
def send():
    '''public boolean send(final ServerSession from, final ServerSession to, final ServerMessage.Mutable message)
    '''
def sendMeta():
    '''public boolean sendMeta(final ServerSession to, final ServerMessage.Mutable message)
    '''
def onMessage():
    '''public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
    public boolean onMessage(final ServerSession to, final ServerSession from, final ServerMessage message)
    public void onMessage(final ClientSessionChannel channel, final Message message)
    '''
def OortCometDisconnectListener():
    '''public OortCometDisconnectListener(final String cometURL, final String remoteOortId)
    '''
def removed():
    '''public void removed(final ServerSession session, final boolean timeout)
    '''
def getServerSession():
    '''public ServerSession getServerSession()
    '''
def getOortComet():
    '''public OortComet getOortComet()
    '''
def addAliasURL():
    '''public void addAliasURL(final String url)
    '''
def matchesURL():
    '''public boolean matchesURL(final String url)
    '''
def Event():
    '''public Event(final Oort source, final String cometURL)
    '''
def getCometURL():
    '''public String getCometURL()
    '''
