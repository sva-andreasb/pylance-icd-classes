def subscribe():
    '''returns boolean\n\n
    subscribe(final ServerSession session)\n
    '''
def unsubscribe():
    '''returns boolean\n\n
    unsubscribe(final ServerSession session)\n
    '''
def getSubscribers():
    '''returns Set<ServerSession>\n\n
    getSubscribers()\n
    '''
def isBroadcast():
    '''returns boolean\n\n
    isBroadcast()\n
    '''
def isDeepWild():
    '''returns boolean\n\n
    isDeepWild()\n
    '''
def isLazy():
    '''returns boolean\n\n
    isLazy()\n
    '''
def isPersistent():
    '''returns boolean\n\n
    isPersistent()\n
    '''
def isWild():
    '''returns boolean\n\n
    isWild()\n
    '''
def setLazy():
    '''returns None\n\n
    setLazy(final boolean lazy)\n
    '''
def setPersistent():
    '''returns None\n\n
    setPersistent(final boolean persistent)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final ServerChannel.ServerChannelListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ServerChannel.ServerChannelListener listener)\n
    '''
def getChannelId():
    '''returns ChannelId\n\n
    getChannelId()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def isMeta():
    '''returns boolean\n\n
    isMeta()\n
    '''
def isService():
    '''returns boolean\n\n
    isService()\n
    '''
def publish():
    '''returns None\n\n
    publish(final Session from, final ServerMessage.Mutable mutable)\n
    publish(final Session from, final Object data, final String id)\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final Object value)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    '''
def getAttributeNames():
    '''returns Set<String>\n\n
    getAttributeNames()\n
    '''
def removeAttribute():
    '''returns Object\n\n
    removeAttribute(final String name)\n
    '''
def addAuthorizer():
    '''returns None\n\n
    addAuthorizer(final Authorizer authorizer)\n
    '''
def removeAuthorizer():
    '''returns None\n\n
    removeAuthorizer(final Authorizer authorizer)\n
    '''
def getAuthorizers():
    '''returns List<Authorizer>\n\n
    getAuthorizers()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
