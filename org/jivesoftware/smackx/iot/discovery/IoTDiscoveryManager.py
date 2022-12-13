def getInstanceFor():
'''public static synchronized IoTDiscoveryManager getInstanceFor(final XMPPConnection connection)
'''
pass
def handleIQRequest():
'''public IQ handleIQRequest(final IQ iqRequest)
public IQ handleIQRequest(final IQ iqRequest)
public IQ handleIQRequest(final IQ iqRequest)
'''
pass
def findRegistry():
'''public Jid findRegistry()
'''
pass
def registerThing():
'''public ThingState registerThing(final Thing thing)
public ThingState registerThing(final Jid registry, final Thing thing)
'''
pass
def claimThing():
'''public IoTClaimed claimThing(final Collection<Tag> metaTags)
public IoTClaimed claimThing(final Collection<Tag> metaTags, final boolean publicThing)
public IoTClaimed claimThing(final Jid registry, final Collection<Tag> metaTags, final boolean publicThing)
'''
pass
def removeThing():
'''public void removeThing(final BareJid thing)
public void removeThing(final BareJid thing, final NodeInfo nodeInfo)
public void removeThing(final Jid registry, final BareJid thing, final NodeInfo nodeInfo)
'''
pass
def unregister():
'''public void unregister()
public void unregister(final NodeInfo nodeInfo)
public void unregister(final Jid registry, final NodeInfo nodeInfo)
'''
pass
def disownThing():
'''public void disownThing(final Jid thing)
public void disownThing(final Jid thing, final NodeInfo nodeInfo)
public void disownThing(final Jid registry, final Jid thing, final NodeInfo nodeInfo)
'''
pass
def isRegistry():
'''public boolean isRegistry(final BareJid jid)
public boolean isRegistry(final Jid jid)
'''
pass
def getStateFor():
'''public ThingState getStateFor(final Thing thing)
'''
pass
def connectionCreated():
'''public void connectionCreated(final XMPPConnection connection)
'''
pass
