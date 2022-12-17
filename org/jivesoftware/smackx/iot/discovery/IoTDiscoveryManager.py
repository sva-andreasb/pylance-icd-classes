def handleIQRequest():
    '''returns IQ\n\n
    handleIQRequest(final IQ iqRequest)\n
    handleIQRequest(final IQ iqRequest)\n
    handleIQRequest(final IQ iqRequest)\n
    '''
def findRegistry():
    '''returns Jid\n\n
    findRegistry()\n
    '''
def registerThing():
    '''returns ThingState\n\n
    registerThing(final Thing thing)\n
    registerThing(final Jid registry, final Thing thing)\n
    '''
def claimThing():
    '''returns IoTClaimed\n\n
    claimThing(final Collection<Tag> metaTags)\n
    claimThing(final Collection<Tag> metaTags, final boolean publicThing)\n
    claimThing(final Jid registry, final Collection<Tag> metaTags, final boolean publicThing)\n
    '''
def removeThing():
    '''returns None\n\n
    removeThing(final BareJid thing)\n
    removeThing(final BareJid thing, final NodeInfo nodeInfo)\n
    removeThing(final Jid registry, final BareJid thing, final NodeInfo nodeInfo)\n
    '''
def unregister():
    '''returns None\n\n
    unregister()\n
    unregister(final NodeInfo nodeInfo)\n
    unregister(final Jid registry, final NodeInfo nodeInfo)\n
    '''
def disownThing():
    '''returns None\n\n
    disownThing(final Jid thing)\n
    disownThing(final Jid thing, final NodeInfo nodeInfo)\n
    disownThing(final Jid registry, final Jid thing, final NodeInfo nodeInfo)\n
    '''
def isRegistry():
    '''returns boolean\n\n
    isRegistry(final BareJid jid)\n
    isRegistry(final Jid jid)\n
    '''
def getStateFor():
    '''returns ThingState\n\n
    getStateFor(final Thing thing)\n
    '''
def connectionCreated():
    '''returns None\n\n
    connectionCreated(final XMPPConnection connection)\n
    '''
