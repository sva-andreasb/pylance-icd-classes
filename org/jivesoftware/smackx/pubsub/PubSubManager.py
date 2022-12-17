AUTO_CREATE_FEATURE = "String  \"http://jabber.org/protocol/pubsub#auto-create\""
def createNode():
    '''returns Node\n\n
    createNode()\n
    createNode(final String nodeId)\n
    createNode(final String nodeId, final Form config)\n
    '''
def getOrCreateLeafNode():
    '''returns LeafNode\n\n
    getOrCreateLeafNode(final String id)\n
    '''
def getLeafNode():
    '''returns LeafNode\n\n
    getLeafNode(final String id)\n
    '''
def discoverNodes():
    '''returns DiscoverItems\n\n
    discoverNodes(final String nodeId)\n
    '''
def getSubscriptions():
    '''returns List<Subscription>\n\n
    getSubscriptions()\n
    '''
def getAffiliations():
    '''returns List<Affiliation>\n\n
    getAffiliations()\n
    '''
def deleteNode():
    '''returns None\n\n
    deleteNode(final String nodeId)\n
    '''
def getDefaultConfiguration():
    '''returns ConfigureForm\n\n
    getDefaultConfiguration()\n
    '''
def getServiceJid():
    '''returns BareJid\n\n
    getServiceJid()\n
    '''
def getSupportedFeatures():
    '''returns DiscoverInfo\n\n
    getSupportedFeatures()\n
    '''
def supportsAutomaticNodeCreation():
    '''returns boolean\n\n
    supportsAutomaticNodeCreation()\n
    '''
def canCreateNodesAndPublishItems():
    '''returns boolean\n\n
    canCreateNodesAndPublishItems()\n
    '''
