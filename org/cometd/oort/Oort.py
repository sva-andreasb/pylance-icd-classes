EXT_OORT_FIELD = "String  \"org.cometd.oort\""
EXT_OORT_URL_FIELD = "String  \"oortURL\""
EXT_OORT_ID_FIELD = "String  \"oortId\""
EXT_OORT_SECRET_FIELD = "String  \"oortSecret\""
EXT_COMET_URL_FIELD = "String  \"cometURL\""
EXT_OORT_ALIAS_URL_FIELD = "String  \"oortAliasURL\""
OORT_CLOUD_CHANNEL = "String  \"/oort/cloud\""
def ():
    '''returns Event\n\n
    (final BayeuxServer bayeux, final String url)\n
    (final String cometURL, final String remoteOortId)\n
    (final Oort source, final String cometURL)\n
    '''
def configureChannel():
    '''returns None\n\n
    configureChannel(final ConfigurableServerChannel channel)\n
    '''
def getBayeuxServer():
    '''returns BayeuxServer\n\n
    getBayeuxServer()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    getURL()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    getId()\n
    '''
def getSecret():
    '''returns String\n\n
    getSecret()\n
    '''
def setSecret():
    '''returns None\n\n
    setSecret(final String secret)\n
    '''
def isDebugEnabled():
    '''returns boolean\n\n
    isDebugEnabled()\n
    '''
def setDebugEnabled():
    '''returns None\n\n
    setDebugEnabled(final boolean debug)\n
    '''
def isClientDebugEnabled():
    '''returns boolean\n\n
    isClientDebugEnabled()\n
    '''
def setClientDebugEnabled():
    '''returns None\n\n
    setClientDebugEnabled(final boolean clientDebugEnabled)\n
    '''
def observeComet():
    '''returns OortComet\n\n
    observeComet(final String cometURL)\n
    '''
def deobserveComet():
    '''returns OortComet\n\n
    deobserveComet(final String cometURL)\n
    '''
def getKnownComets():
    '''returns Set<String>\n\n
    getKnownComets()\n
    '''
def getComet():
    '''returns OortComet\n\n
    getComet(final String cometURL)\n
    '''
def observeChannel():
    '''returns None\n\n
    observeChannel(final String channelName)\n
    '''
def deobserveChannel():
    '''returns None\n\n
    deobserveChannel(final String channelId)\n
    '''
def isOort():
    '''returns boolean\n\n
    isOort(final ServerSession session)\n
    '''
def isOortHandshake():
    '''returns boolean\n\n
    isOortHandshake(final Message handshake)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addCometListener():
    '''returns None\n\n
    addCometListener(final CometListener listener)\n
    '''
def removeCometListener():
    '''returns None\n\n
    removeCometListener(final CometListener listener)\n
    '''
def setThreadPool():
    '''returns None\n\n
    setThreadPool(final ThreadPool threadPool)\n
    '''
def getThreadPool():
    '''returns ThreadPool\n\n
    getThreadPool()\n
    '''
def getWebSocketClientFactory():
    '''returns WebSocketClientFactory\n\n
    getWebSocketClientFactory()\n
    '''
def setWebSocketClientFactory():
    '''returns None\n\n
    setWebSocketClientFactory(final WebSocketClientFactory wsFactory)\n
    '''
def getHttpClient():
    '''returns HttpClient\n\n
    getHttpClient()\n
    '''
def setHttpClient():
    '''returns None\n\n
    setHttpClient(final HttpClient httpClient)\n
    '''
def getObservedChannels():
    '''returns Set<String>\n\n
    getObservedChannels()\n
    '''
def getOortSession():
    '''returns LocalSession\n\n
    getOortSession()\n
    '''
def rcv():
    '''returns boolean\n\n
    rcv(final ServerSession from, final ServerMessage.Mutable message)\n
    '''
def rcvMeta():
    '''returns boolean\n\n
    rcvMeta(final ServerSession from, final ServerMessage.Mutable message)\n
    '''
def send():
    '''returns boolean\n\n
    send(final ServerSession from, final ServerSession to, final ServerMessage.Mutable message)\n
    '''
def sendMeta():
    '''returns boolean\n\n
    sendMeta(final ServerSession to, final ServerMessage.Mutable message)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)\n
    onMessage(final ServerSession to, final ServerSession from, final ServerMessage message)\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    '''
def removed():
    '''returns None\n\n
    removed(final ServerSession session, final boolean timeout)\n
    '''
def getServerSession():
    '''returns ServerSession\n\n
    getServerSession()\n
    '''
def getOortComet():
    '''returns OortComet\n\n
    getOortComet()\n
    '''
def addAliasURL():
    '''returns None\n\n
    addAliasURL(final String url)\n
    '''
def matchesURL():
    '''returns boolean\n\n
    matchesURL(final String url)\n
    '''
def getCometURL():
    '''returns String\n\n
    getCometURL()\n
    '''
