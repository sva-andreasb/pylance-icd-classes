def SmackException():
'''public SmackException(final Throwable wrappedThrowable)
public SmackException(final String message)
public SmackException(final String message, final Throwable wrappedThrowable)
'''
pass
def getFilter():
'''public StanzaFilter getFilter()
'''
pass
def newWith():
'''public static NoResponseException newWith(final XMPPConnection connection, final String waitingFor)
public static NoResponseException newWith(final XMPPConnection connection, final StanzaCollector collector)
public static NoResponseException newWith(final long timeout, final StanzaCollector collector)
public static NoResponseException newWith(final XMPPConnection connection, final StanzaFilter filter)
public static NoResponseException newWith(final long timeout, final StanzaFilter filter)
'''
pass
def NotLoggedInException():
'''public NotLoggedInException()
'''
pass
def AlreadyLoggedInException():
'''public AlreadyLoggedInException()
'''
pass
def AlreadyConnectedException():
'''public AlreadyConnectedException()
'''
pass
def NotConnectedException():
'''public NotConnectedException()
public NotConnectedException(final String optionalHint)
public NotConnectedException(final XMPPConnection connection, final String details)
public NotConnectedException(final XMPPConnection connection, final StanzaFilter stanzaFilter)
'''
pass
def SecurityRequiredException():
'''public SecurityRequiredException(final String message)
'''
pass
def SecurityRequiredByClientException():
'''public SecurityRequiredByClientException()
'''
pass
def SecurityRequiredByServerException():
'''public SecurityRequiredByServerException()
'''
pass
def SecurityNotPossibleException():
'''public SecurityNotPossibleException(final String message)
'''
pass
def ConnectionException():
'''public ConnectionException(final Throwable wrappedThrowable)
'''
pass
def from():
'''public static ConnectionException from(final List<HostAddress> failedAddresses)
'''
pass
def getFailedAddresses():
'''public List<HostAddress> getFailedAddresses()
'''
pass
def FeatureNotSupportedException():
'''public FeatureNotSupportedException(final String feature)
public FeatureNotSupportedException(final String feature, final Jid jid)
'''
pass
def getFeature():
'''public String getFeature()
'''
pass
def getJid():
'''public Jid getJid()
'''
pass
def ResourceBindingNotOfferedException():
'''public ResourceBindingNotOfferedException()
'''
pass
def SmackWrappedException():
'''public SmackWrappedException(final Exception exception)
'''
pass
