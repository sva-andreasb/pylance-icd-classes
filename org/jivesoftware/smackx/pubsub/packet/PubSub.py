ELEMENT = "String  pubsub""
NAMESPACE = "String  http://jabber.org/protocol/pubsub""
def PubSub():
'''public PubSub()
public PubSub(final PubSubNamespace ns)
public PubSub(final Jid to, final IQ.Type type, final PubSubNamespace ns)
'''
pass
def getExtension():
'''public <PE extends ExtensionElement> PE getExtension(final PubSubElementType elem)
'''
pass
def createPubsubPacket():
'''public static PubSub createPubsubPacket(final Jid to, final IQ.Type type, final NodeExtension extension)
'''
pass