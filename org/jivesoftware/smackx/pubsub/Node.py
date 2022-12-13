def getId():
'''public String getId()
'''
pass
def getNodeConfiguration():
'''public ConfigureForm getNodeConfiguration()
'''
pass
def sendConfigurationForm():
'''public void sendConfigurationForm(final Form submitForm)
'''
pass
def discoverInfo():
'''public DiscoverInfo discoverInfo()
'''
pass
def getSubscriptions():
'''public List<Subscription> getSubscriptions()
public List<Subscription> getSubscriptions(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
'''
pass
def getSubscriptionsAsOwner():
'''public List<Subscription> getSubscriptionsAsOwner()
public List<Subscription> getSubscriptionsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
'''
pass
def modifySubscriptionsAsOwner():
'''public PubSub modifySubscriptionsAsOwner(final List<Subscription> changedSubs)
'''
pass
def getAffiliations():
'''public List<Affiliation> getAffiliations()
public List<Affiliation> getAffiliations(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
'''
pass
def getAffiliationsAsOwner():
'''public List<Affiliation> getAffiliationsAsOwner()
public List<Affiliation> getAffiliationsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
'''
pass
def modifyAffiliationAsOwner():
'''public PubSub modifyAffiliationAsOwner(final List<Affiliation> affiliations)
'''
pass
def subscribe():
'''public Subscription subscribe(final String jid)
public Subscription subscribe(final String jid, final SubscribeForm subForm)
'''
pass
def unsubscribe():
'''public void unsubscribe(final String jid)
public void unsubscribe(final String jid, final String subscriptionId)
'''
pass
def getSubscriptionOptions():
'''public SubscribeForm getSubscriptionOptions(final String jid)
public SubscribeForm getSubscriptionOptions(final String jid, final String subscriptionId)
'''
pass
def addItemEventListener():
'''public void addItemEventListener(final ItemEventListener listener)
'''
pass
def removeItemEventListener():
'''public void removeItemEventListener(final ItemEventListener listener)
'''
pass
def addConfigurationListener():
'''public void addConfigurationListener(final NodeConfigListener listener)
'''
pass
def removeConfigurationListener():
'''public void removeConfigurationListener(final NodeConfigListener listener)
'''
pass
def addItemDeleteListener():
'''public void addItemDeleteListener(final ItemDeleteListener listener)
'''
pass
def removeItemDeleteListener():
'''public void removeItemDeleteListener(final ItemDeleteListener listener)
'''
pass
def toString():
'''public String toString()
'''
pass
def ItemEventTranslator():
'''public ItemEventTranslator(final ItemEventListener eventListener)
'''
pass
def processStanza():
'''public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
public void processStanza(final Stanza packet)
'''
pass
def ItemDeleteTranslator():
'''public ItemDeleteTranslator(final ItemDeleteListener eventListener)
'''
pass
def NodeConfigTranslator():
'''public NodeConfigTranslator(final NodeConfigListener eventListener)
'''
pass
def acceptSpecific():
'''public boolean acceptSpecific(final Message message)
'''
pass
