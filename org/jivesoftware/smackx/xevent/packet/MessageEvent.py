NAMESPACE = "String  \"jabber:x:event\""
ELEMENT = "String  \"x\""
OFFLINE = "String  \"offline\""
COMPOSING = "String  \"composing\""
DISPLAYED = "String  \"displayed\""
DELIVERED = "String  \"delivered\""
CANCELLED = "String  \"cancelled\""
def MessageEvent():
    '''public MessageEvent()
    '''
def getElementName():
    '''public String getElementName()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def isComposing():
    '''public boolean isComposing()
    '''
def isDelivered():
    '''public boolean isDelivered()
    '''
def isDisplayed():
    '''public boolean isDisplayed()
    '''
def isOffline():
    '''public boolean isOffline()
    '''
def isCancelled():
    '''public boolean isCancelled()
    '''
def getStanzaId():
    '''public String getStanzaId()
    '''
def getEventTypes():
    '''public List<String> getEventTypes()
    '''
def setComposing():
    '''public void setComposing(final boolean composing)
    '''
def setDelivered():
    '''public void setDelivered(final boolean delivered)
    '''
def setDisplayed():
    '''public void setDisplayed(final boolean displayed)
    '''
def setOffline():
    '''public void setOffline(final boolean offline)
    '''
def setCancelled():
    '''public void setCancelled(final boolean cancelled)
    '''
def setStanzaId():
    '''public void setStanzaId(final String packetID)
    '''
def isMessageEventRequest():
    '''public boolean isMessageEventRequest()
    '''
def toXML():
    '''public String toXML(final String enclosingNamespace)
    '''
