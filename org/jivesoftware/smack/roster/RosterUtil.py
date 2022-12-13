def waitUntilOtherEntityIsSubscribed():
'''public static void waitUntilOtherEntityIsSubscribed(final Roster roster, final BareJid otherEntity, final long timeoutMillis)
public static void waitUntilOtherEntityIsSubscribed(final Roster roster, final BareJid otherEntity, final Date deadline)
'''
pass
def entriesAdded():
'''public void entriesAdded(final Collection<Jid> addresses)
'''
pass
def entriesUpdated():
'''public void entriesUpdated(final Collection<Jid> addresses)
'''
pass
def preApproveSubscriptionIfRequiredAndPossible():
'''public static void preApproveSubscriptionIfRequiredAndPossible(final Roster roster, final BareJid jid)
'''
pass
def askForSubscriptionIfRequired():
'''public static void askForSubscriptionIfRequired(final Roster roster, final BareJid jid)
'''
pass
def ensureNotSubscribedToEachOther():
'''public static void ensureNotSubscribedToEachOther(final XMPPConnection connectionOne, final XMPPConnection connectionTwo)
'''
pass
def ensureNotSubscribed():
'''public static void ensureNotSubscribed(final Roster roster, final BareJid jid)
'''
pass
def ensureSubscribed():
'''public static void ensureSubscribed(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final long timeout)
'''
pass
def ensureSubscribedTo():
'''public static void ensureSubscribedTo(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final long timeout)
public static void ensureSubscribedTo(final XMPPConnection connectionOne, final XMPPConnection connectionTwo, final Date deadline)
'''
pass
def processSubscribe():
'''public SubscribeAnswer processSubscribe(final Jid from, final Presence subscribeRequest)
'''
pass
