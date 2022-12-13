def cancel():
'''public void cancel()
'''
pass
def getPacketFilter():
'''public StanzaFilter getPacketFilter()
'''
pass
def getStanzaFilter():
'''public StanzaFilter getStanzaFilter()
'''
pass
def pollResult():
'''public <P extends Stanza> P pollResult()
'''
pass
def pollResultOrThrow():
'''public <P extends Stanza> P pollResultOrThrow()
'''
pass
def nextResultBlockForever():
'''public <P extends Stanza> P nextResultBlockForever()
'''
pass
def nextResult():
'''public <P extends Stanza> P nextResult()
public <P extends Stanza> P nextResult(final long timeout)
'''
pass
def nextResultOrThrow():
'''public <P extends Stanza> P nextResultOrThrow()
public <P extends Stanza> P nextResultOrThrow(final long timeout)
'''
pass
def getCollectedStanzasAfterCancelled():
'''public List<Stanza> getCollectedStanzasAfterCancelled()
'''
pass
def getCollectedCount():
'''public int getCollectedCount()
'''
pass
def newConfiguration():
'''public static Configuration newConfiguration()
'''
pass
def setPacketFilter():
'''public Configuration setPacketFilter(final StanzaFilter packetFilter)
'''
pass
def setStanzaFilter():
'''public Configuration setStanzaFilter(final StanzaFilter stanzaFilter)
'''
pass
def setSize():
'''public Configuration setSize(final int size)
'''
pass
def setCollectorToReset():
'''public Configuration setCollectorToReset(final StanzaCollector collector)
'''
pass
def setRequest():
'''public Configuration setRequest(final Stanza request)
'''
pass
