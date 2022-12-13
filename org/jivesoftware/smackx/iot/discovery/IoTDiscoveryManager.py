def getInstanceFor():
    '''    public static synchronized IoTDiscoveryManager getInstanceFor(final XMPPConnection connection)
    '''
def handleIQRequest():
    '''    public IQ handleIQRequest(final IQ iqRequest)
    public IQ handleIQRequest(final IQ iqRequest)
    public IQ handleIQRequest(final IQ iqRequest)
    '''
def findRegistry():
    '''    public Jid findRegistry()
    '''
def registerThing():
    '''    public ThingState registerThing(final Thing thing)
    public ThingState registerThing(final Jid registry, final Thing thing)
    '''
def claimThing():
    '''    public IoTClaimed claimThing(final Collection<Tag> metaTags)
    public IoTClaimed claimThing(final Collection<Tag> metaTags, final boolean publicThing)
    public IoTClaimed claimThing(final Jid registry, final Collection<Tag> metaTags, final boolean publicThing)
    '''
def removeThing():
    '''    public void removeThing(final BareJid thing)
    public void removeThing(final BareJid thing, final NodeInfo nodeInfo)
    public void removeThing(final Jid registry, final BareJid thing, final NodeInfo nodeInfo)
    '''
def unregister():
    '''    public void unregister()
    public void unregister(final NodeInfo nodeInfo)
    public void unregister(final Jid registry, final NodeInfo nodeInfo)
    '''
def disownThing():
    '''    public void disownThing(final Jid thing)
    public void disownThing(final Jid thing, final NodeInfo nodeInfo)
    public void disownThing(final Jid registry, final Jid thing, final NodeInfo nodeInfo)
    '''
def isRegistry():
    '''    public boolean isRegistry(final BareJid jid)
    public boolean isRegistry(final Jid jid)
    '''
def getStateFor():
    '''    public ThingState getStateFor(final Thing thing)
    '''
def connectionCreated():
    '''    public void connectionCreated(final XMPPConnection connection)
    '''
