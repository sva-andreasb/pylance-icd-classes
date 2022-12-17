ELEMENT = "String  \"query\""
NAMESPACE = "String  \"http://jabber.org/protocol/disco#items\""
UPDATE_ACTION = "String  \"update\""
REMOVE_ACTION = "String  \"remove\""
def ():
    '''returns Item\n\n
    ()\n
    (final Jid entityID)\n
    '''
def addItem():
    '''returns None\n\n
    addItem(final Item item)\n
    '''
def addItems():
    '''returns None\n\n
    addItems(final Collection<Item> itemsToAdd)\n
    '''
def getItems():
    '''returns List<Item>\n\n
    getItems()\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    getNode()\n
    '''
def setNode():
    '''returns None\n\n
    setNode(final String node)\n
    setNode(final String node)\n
    '''
def getEntityID():
    '''returns Jid\n\n
    getEntityID()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getAction():
    '''returns String\n\n
    getAction()\n
    '''
def setAction():
    '''returns None\n\n
    setAction(final String action)\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML()\n
    '''
