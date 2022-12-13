def SmackException():
    '''    public SmackException(final Throwable wrappedThrowable)
    public SmackException(final String message)
    public SmackException(final String message, final Throwable wrappedThrowable)
    '''
def getFilter():
    '''    public StanzaFilter getFilter()
    '''
def newWith():
    '''    public static NoResponseException newWith(final XMPPConnection connection, final String waitingFor)
    public static NoResponseException newWith(final XMPPConnection connection, final StanzaCollector collector)
    public static NoResponseException newWith(final long timeout, final StanzaCollector collector)
    public static NoResponseException newWith(final XMPPConnection connection, final StanzaFilter filter)
    public static NoResponseException newWith(final long timeout, final StanzaFilter filter)
    '''
def NotLoggedInException():
    '''    public NotLoggedInException()
    '''
def AlreadyLoggedInException():
    '''    public AlreadyLoggedInException()
    '''
def AlreadyConnectedException():
    '''    public AlreadyConnectedException()
    '''
def NotConnectedException():
    '''    public NotConnectedException()
    public NotConnectedException(final String optionalHint)
    public NotConnectedException(final XMPPConnection connection, final String details)
    public NotConnectedException(final XMPPConnection connection, final StanzaFilter stanzaFilter)
    '''
def SecurityRequiredException():
    '''    public SecurityRequiredException(final String message)
    '''
def SecurityRequiredByClientException():
    '''    public SecurityRequiredByClientException()
    '''
def SecurityRequiredByServerException():
    '''    public SecurityRequiredByServerException()
    '''
def SecurityNotPossibleException():
    '''    public SecurityNotPossibleException(final String message)
    '''
def ConnectionException():
    '''    public ConnectionException(final Throwable wrappedThrowable)
    '''
def from():
    '''    public static ConnectionException from(final List<HostAddress> failedAddresses)
    '''
def getFailedAddresses():
    '''    public List<HostAddress> getFailedAddresses()
    '''
def FeatureNotSupportedException():
    '''    public FeatureNotSupportedException(final String feature)
    public FeatureNotSupportedException(final String feature, final Jid jid)
    '''
def getFeature():
    '''    public String getFeature()
    '''
def getJid():
    '''    public Jid getJid()
    '''
def ResourceBindingNotOfferedException():
    '''    public ResourceBindingNotOfferedException()
    '''
def SmackWrappedException():
    '''    public SmackWrappedException(final Exception exception)
    '''
