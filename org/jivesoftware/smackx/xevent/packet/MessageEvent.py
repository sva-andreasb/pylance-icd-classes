NAMESPACE = "String  \"jabber:x:event\""
ELEMENT = "String  \"x\""
OFFLINE = "String  \"offline\""
COMPOSING = "String  \"composing\""
DISPLAYED = "String  \"displayed\""
DELIVERED = "String  \"delivered\""
CANCELLED = "String  \"cancelled\""
def ():
    '''returns MessageEvent\n\n
    ()\n
    '''
def getElementName():
    '''returns String\n\n
    getElementName()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def isComposing():
    '''returns boolean\n\n
    isComposing()\n
    '''
def isDelivered():
    '''returns boolean\n\n
    isDelivered()\n
    '''
def isDisplayed():
    '''returns boolean\n\n
    isDisplayed()\n
    '''
def isOffline():
    '''returns boolean\n\n
    isOffline()\n
    '''
def isCancelled():
    '''returns boolean\n\n
    isCancelled()\n
    '''
def getStanzaId():
    '''returns String\n\n
    getStanzaId()\n
    '''
def getEventTypes():
    '''returns List<String>\n\n
    getEventTypes()\n
    '''
def setComposing():
    '''returns None\n\n
    setComposing(final boolean composing)\n
    '''
def setDelivered():
    '''returns None\n\n
    setDelivered(final boolean delivered)\n
    '''
def setDisplayed():
    '''returns None\n\n
    setDisplayed(final boolean displayed)\n
    '''
def setOffline():
    '''returns None\n\n
    setOffline(final boolean offline)\n
    '''
def setCancelled():
    '''returns None\n\n
    setCancelled(final boolean cancelled)\n
    '''
def setStanzaId():
    '''returns None\n\n
    setStanzaId(final String packetID)\n
    '''
def isMessageEventRequest():
    '''returns boolean\n\n
    isMessageEventRequest()\n
    '''
def toXML():
    '''returns String\n\n
    toXML(final String enclosingNamespace)\n
    '''
