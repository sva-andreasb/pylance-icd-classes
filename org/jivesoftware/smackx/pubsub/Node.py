def getId():
    '''returns String\n\n
    getId()\n
    '''
def getNodeConfiguration():
    '''returns ConfigureForm\n\n
    getNodeConfiguration()\n
    '''
def sendConfigurationForm():
    '''returns None\n\n
    sendConfigurationForm(final Form submitForm)\n
    '''
def discoverInfo():
    '''returns DiscoverInfo\n\n
    discoverInfo()\n
    '''
def getSubscriptions():
    '''returns List<Subscription>\n\n
    getSubscriptions()\n
    getSubscriptions(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)\n
    '''
def getSubscriptionsAsOwner():
    '''returns List<Subscription>\n\n
    getSubscriptionsAsOwner()\n
    getSubscriptionsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)\n
    '''
def modifySubscriptionsAsOwner():
    '''returns PubSub\n\n
    modifySubscriptionsAsOwner(final List<Subscription> changedSubs)\n
    '''
def getAffiliations():
    '''returns List<Affiliation>\n\n
    getAffiliations()\n
    getAffiliations(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)\n
    '''
def getAffiliationsAsOwner():
    '''returns List<Affiliation>\n\n
    getAffiliationsAsOwner()\n
    getAffiliationsAsOwner(final List<ExtensionElement> additionalExtensions, final Collection<ExtensionElement> returnedExtensions)\n
    '''
def modifyAffiliationAsOwner():
    '''returns PubSub\n\n
    modifyAffiliationAsOwner(final List<Affiliation> affiliations)\n
    '''
def subscribe():
    '''returns Subscription\n\n
    subscribe(final String jid)\n
    subscribe(final String jid, final SubscribeForm subForm)\n
    '''
def unsubscribe():
    '''returns None\n\n
    unsubscribe(final String jid)\n
    unsubscribe(final String jid, final String subscriptionId)\n
    '''
def getSubscriptionOptions():
    '''returns SubscribeForm\n\n
    getSubscriptionOptions(final String jid)\n
    getSubscriptionOptions(final String jid, final String subscriptionId)\n
    '''
def addItemEventListener():
    '''returns None\n\n
    addItemEventListener(final ItemEventListener listener)\n
    '''
def removeItemEventListener():
    '''returns None\n\n
    removeItemEventListener(final ItemEventListener listener)\n
    '''
def addConfigurationListener():
    '''returns None\n\n
    addConfigurationListener(final NodeConfigListener listener)\n
    '''
def removeConfigurationListener():
    '''returns None\n\n
    removeConfigurationListener(final NodeConfigListener listener)\n
    '''
def addItemDeleteListener():
    '''returns None\n\n
    addItemDeleteListener(final ItemDeleteListener listener)\n
    '''
def removeItemDeleteListener():
    '''returns None\n\n
    removeItemDeleteListener(final ItemDeleteListener listener)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def ():
    '''returns NodeConfigTranslator\n\n
    (final ItemEventListener eventListener)\n
    (final ItemDeleteListener eventListener)\n
    (final NodeConfigListener eventListener)\n
    '''
def processStanza():
    '''returns None\n\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    processStanza(final Stanza packet)\n
    '''
def acceptSpecific():
    '''returns boolean\n\n
    acceptSpecific(final Message message)\n
    '''
