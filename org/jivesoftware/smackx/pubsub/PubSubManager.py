AUTO_CREATE_FEATURE = "String  \"http://jabber.org/protocol/pubsub#auto-create\""
def getInstance():
    '''    public static PubSubManager getInstance(final XMPPConnection connection)
    public static synchronized PubSubManager getInstance(final XMPPConnection connection, final BareJid pubSubService)
    '''
def createNode():
    '''    public LeafNode createNode()
    public LeafNode createNode(final String nodeId)
    public Node createNode(final String nodeId, final Form config)
    '''
def getNode():
    '''    public <T extends Node> T getNode(final String id)
    '''
def getOrCreateLeafNode():
    '''    public LeafNode getOrCreateLeafNode(final String id)
    '''
def getLeafNode():
    '''    public LeafNode getLeafNode(final String id)
    '''
def tryToPublishAndPossibleAutoCreate():
    '''    public <I extends Item> LeafNode tryToPublishAndPossibleAutoCreate(final String id, final I item)
    '''
def discoverNodes():
    '''    public DiscoverItems discoverNodes(final String nodeId)
    '''
def getSubscriptions():
    '''    public List<Subscription> getSubscriptions()
    '''
def getAffiliations():
    '''    public List<Affiliation> getAffiliations()
    '''
def deleteNode():
    '''    public void deleteNode(final String nodeId)
    '''
def getDefaultConfiguration():
    '''    public ConfigureForm getDefaultConfiguration()
    '''
def getServiceJid():
    '''    public BareJid getServiceJid()
    '''
def getSupportedFeatures():
    '''    public DiscoverInfo getSupportedFeatures()
    '''
def supportsAutomaticNodeCreation():
    '''    public boolean supportsAutomaticNodeCreation()
    '''
def canCreateNodesAndPublishItems():
    '''    public boolean canCreateNodesAndPublishItems()
    '''
def getPubSubService():
    '''    public static DomainBareJid getPubSubService(final XMPPConnection connection)
    '''
