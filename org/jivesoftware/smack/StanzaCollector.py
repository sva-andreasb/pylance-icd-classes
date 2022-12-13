def cancel():
    '''public void cancel()
    '''
def getPacketFilter():
    '''public StanzaFilter getPacketFilter()
    '''
def getStanzaFilter():
    '''public StanzaFilter getStanzaFilter()
    '''
def pollResult():
    '''public <P extends Stanza> P pollResult()
    '''
def pollResultOrThrow():
    '''public <P extends Stanza> P pollResultOrThrow()
    '''
def nextResultBlockForever():
    '''public <P extends Stanza> P nextResultBlockForever()
    '''
def nextResult():
    '''public <P extends Stanza> P nextResult()
    public <P extends Stanza> P nextResult(final long timeout)
    '''
def nextResultOrThrow():
    '''public <P extends Stanza> P nextResultOrThrow()
    public <P extends Stanza> P nextResultOrThrow(final long timeout)
    '''
def getCollectedStanzasAfterCancelled():
    '''public List<Stanza> getCollectedStanzasAfterCancelled()
    '''
def getCollectedCount():
    '''public int getCollectedCount()
    '''
def newConfiguration():
    '''public static Configuration newConfiguration()
    '''
def setPacketFilter():
    '''public Configuration setPacketFilter(final StanzaFilter packetFilter)
    '''
def setStanzaFilter():
    '''public Configuration setStanzaFilter(final StanzaFilter stanzaFilter)
    '''
def setSize():
    '''public Configuration setSize(final int size)
    '''
def setCollectorToReset():
    '''public Configuration setCollectorToReset(final StanzaCollector collector)
    '''
def setRequest():
    '''public Configuration setRequest(final Stanza request)
    '''
