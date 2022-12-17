def addExtension():
    '''returns None\n\n
    addExtension(final ClientSession.Extension extension)\n
    '''
def removeExtension():
    '''returns None\n\n
    removeExtension(final ClientSession.Extension extension)\n
    '''
def getChannel():
    '''returns ClientSessionChannel\n\n
    getChannel(final String channelId)\n
    '''
def startBatch():
    '''returns None\n\n
    startBatch()\n
    '''
def endBatch():
    '''returns boolean\n\n
    endBatch()\n
    '''
def batch():
    '''returns None\n\n
    batch(final Runnable batch)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    getAttribute(final String name)\n
    '''
def getAttributeNames():
    '''returns Set<String>\n\n
    getAttributeNames()\n
    getAttributeNames()\n
    '''
def removeAttribute():
    '''returns Object\n\n
    removeAttribute(final String name)\n
    removeAttribute(final String name)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final Object value)\n
    setAttribute(final String name, final Object value)\n
    '''
def receive():
    '''returns None\n\n
    receive(final Message.Mutable message)\n
    '''
def dump():
    '''returns None\n\n
    dump(final StringBuilder b, final String indent)\n
    '''
def getChannelId():
    '''returns ChannelId\n\n
    getChannelId()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final ClientSessionChannel.ClientSessionChannelListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ClientSessionChannel.ClientSessionChannelListener listener)\n
    '''
def subscribe():
    '''returns None\n\n
    subscribe(final ClientSessionChannel.MessageListener listener)\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe(final ClientSessionChannel.MessageListener listener)\n
    unsubscribe()\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    '''
def isReleased():
    '''returns boolean\n\n
    isReleased()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def isDeepWild():
    '''returns boolean\n\n
    isDeepWild()\n
    '''
def isMeta():
    '''returns boolean\n\n
    isMeta()\n
    '''
def isService():
    '''returns boolean\n\n
    isService()\n
    '''
def isBroadcast():
    '''returns boolean\n\n
    isBroadcast()\n
    '''
def isWild():
    '''returns boolean\n\n
    isWild()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getReference():
    '''returns T\n\n
    getReference()\n
    '''
def isMarked():
    '''returns boolean\n\n
    isMarked()\n
    '''
