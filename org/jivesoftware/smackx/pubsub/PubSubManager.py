AUTO_CREATE_FEATURE = "String  http://jabber.org/protocol/pubsub#auto-create""
def getInstance():
'''public static PubSubManager getInstance(final XMPPConnection connection)
public static synchronized PubSubManager getInstance(final XMPPConnection connection, final BareJid pubSubService)
'''
pass
def createNode():
'''public LeafNode createNode()
public LeafNode createNode(final String nodeId)
public Node createNode(final String nodeId, final Form config)
'''
pass
def getNode():
'''public <T extends Node> T getNode(final String id)
'''
pass
def getOrCreateLeafNode():
'''public LeafNode getOrCreateLeafNode(final String id)
'''
pass
def getLeafNode():
'''public LeafNode getLeafNode(final String id)
'''
pass
def tryToPublishAndPossibleAutoCreate():
'''public <I extends Item> LeafNode tryToPublishAndPossibleAutoCreate(final String id, final I item)
'''
pass
def discoverNodes():
'''public DiscoverItems discoverNodes(final String nodeId)
'''
pass
def getSubscriptions():
'''public List<Subscription> getSubscriptions()
'''
pass
def getAffiliations():
'''public List<Affiliation> getAffiliations()
'''
pass
def deleteNode():
'''public void deleteNode(final String nodeId)
'''
pass
def getDefaultConfiguration():
'''public ConfigureForm getDefaultConfiguration()
'''
pass
def getServiceJid():
'''public BareJid getServiceJid()
'''
pass
def getSupportedFeatures():
'''public DiscoverInfo getSupportedFeatures()
'''
pass
def supportsAutomaticNodeCreation():
'''public boolean supportsAutomaticNodeCreation()
'''
pass
def canCreateNodesAndPublishItems():
'''public boolean canCreateNodesAndPublishItems()
'''
pass
def getPubSubService():
'''public static DomainBareJid getPubSubService(final XMPPConnection connection)
'''
pass
