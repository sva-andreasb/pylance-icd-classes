def getId():
    '''public String getId()
    '''
def getNodeConfiguration():
    '''public ConfigureForm getNodeConfiguration()
    '''
def sendConfigurationForm():
    '''public void sendConfigurationForm(final Form submitForm)
    '''
def discoverInfo():
    '''public DiscoverInfo discoverInfo()
    '''
def getSubscriptions():
    '''public List<Subscription> getSubscriptions()
    public List<Subscription> getSubscriptions(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
    '''
def getSubscriptionsAsOwner():
    '''public List<Subscription> getSubscriptionsAsOwner()
    public List<Subscription> getSubscriptionsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
    '''
def modifySubscriptionsAsOwner():
    '''public PubSub modifySubscriptionsAsOwner(final List<Subscription> changedSubs)
    '''
def getAffiliations():
    '''public List<Affiliation> getAffiliations()
    public List<Affiliation> getAffiliations(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
    '''
def getAffiliationsAsOwner():
    '''public List<Affiliation> getAffiliationsAsOwner()
    public List<Affiliation> getAffiliationsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)
    '''
def modifyAffiliationAsOwner():
    '''public PubSub modifyAffiliationAsOwner(final List<Affiliation> affiliations)
    '''
def subscribe():
    '''public Subscription subscribe(final String jid)
    public Subscription subscribe(final String jid, final SubscribeForm subForm)
    '''
def unsubscribe():
    '''public void unsubscribe(final String jid)
    public void unsubscribe(final String jid, final String subscriptionId)
    '''
def getSubscriptionOptions():
    '''public SubscribeForm getSubscriptionOptions(final String jid)
    public SubscribeForm getSubscriptionOptions(final String jid, final String subscriptionId)
    '''
def addItemEventListener():
    '''public void addItemEventListener(final ItemEventListener listener)
    '''
def removeItemEventListener():
    '''public void removeItemEventListener(final ItemEventListener listener)
    '''
def addConfigurationListener():
    '''public void addConfigurationListener(final NodeConfigListener listener)
    '''
def removeConfigurationListener():
    '''public void removeConfigurationListener(final NodeConfigListener listener)
    '''
def addItemDeleteListener():
    '''public void addItemDeleteListener(final ItemDeleteListener listener)
    '''
def removeItemDeleteListener():
    '''public void removeItemDeleteListener(final ItemDeleteListener listener)
    '''
def toString():
    '''public String toString()
    '''
def ItemEventTranslator():
    '''public ItemEventTranslator(final ItemEventListener eventListener)
    '''
def processStanza():
    '''public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    public void processStanza(final Stanza packet)
    '''
def ItemDeleteTranslator():
    '''public ItemDeleteTranslator(final ItemDeleteListener eventListener)
    '''
def NodeConfigTranslator():
    '''public NodeConfigTranslator(final NodeConfigListener eventListener)
    '''
def acceptSpecific():
    '''public boolean acceptSpecific(final Message message)
    '''
