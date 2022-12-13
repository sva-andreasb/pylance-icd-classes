def waitUntilOtherEntityIsSubscribed():
    '''public static void waitUntilOtherEntityIsSubscribed(final Roster roster, final BareJid otherEntity, final long timeoutMillis)
    public static void waitUntilOtherEntityIsSubscribed(final Roster roster, final BareJid otherEntity, final Date deadline)
    '''
def entriesAdded():
    '''public void entriesAdded(final Collection<Jid> addresses)
    '''
def entriesUpdated():
    '''public void entriesUpdated(final Collection<Jid> addresses)
    '''
def preApproveSubscriptionIfRequiredAndPossible():
    '''public static void preApproveSubscriptionIfRequiredAndPossible(final Roster roster, final BareJid jid)
    '''
def askForSubscriptionIfRequired():
    '''public static void askForSubscriptionIfRequired(final Roster roster, final BareJid jid)
    '''
def ensureNotSubscribedToEachOther():
    '''public static void ensureNotSubscribedToEachOther(final XMPPConnection connectionOne, final XMPPConnection connectionTwo)
    '''
def ensureNotSubscribed():
    '''public static void ensureNotSubscribed(final Roster roster, final BareJid jid)
    '''
def ensureSubscribed():
    '''public static void ensureSubscribed(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final long timeout)
    '''
def ensureSubscribedTo():
    '''public static void ensureSubscribedTo(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final long timeout)
    public static void ensureSubscribedTo(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final Date deadline)
    '''
def processSubscribe():
    '''public SubscribeAnswer processSubscribe(final Jid from, final Presence subscribeRequest)
    '''
