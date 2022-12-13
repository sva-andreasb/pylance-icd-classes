def ClientAnnotationProcessor():
    '''public ClientAnnotationProcessor(final ClientSession clientSession)
    public ClientAnnotationProcessor(final ClientSession clientSession, final Object... injectables)
    '''
def process():
    '''public boolean process(final Object bean)
    '''
def processPostConstruct():
    '''public boolean processPostConstruct(final Object bean)
    '''
def deprocess():
    '''public boolean deprocess(final Object bean)
    '''
def deprocessCallbacks():
    '''public boolean deprocessCallbacks(final Object bean)
    '''
def processPreDestroy():
    '''public boolean processPreDestroy(final Object bean)
    '''
def onMessage():
    '''public void onMessage(final ClientSessionChannel channel, final Message message)
    public void onMessage(final ClientSessionChannel channel, final Message message)
    '''
def SubscriptionCallback():
    '''public SubscriptionCallback(final ClientSession clientSession, final Object target, final Method method, final String channel)
    '''
