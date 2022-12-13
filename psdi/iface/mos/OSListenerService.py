def getInstance():
    '''    public static OSListenerService getInstance()
    '''
def subscribeOSEvents():
    '''    public void subscribeOSEvents(final String osName, final OSListener osListener, final String subscriptionId)
    public void subscribeOSEvents(final String osName, final OSListener osListener, final String subscriptionId, final boolean enforceOSRelation)
    public void subscribeOSEvents(final String osName, final OSListener osListener, final String subscriptionId, final Set<String> objNames)
    public void subscribeOSEvents(final String osName, final OSListener osListener, final String subscriptionId, final Set<String> objNames, final boolean enforceOSRelation)
    '''
def unsubscribeOSEvents():
    '''    public void unsubscribeOSEvents(final String subscriptionId)
    '''
def reload():
    '''    public void reload()
    '''
