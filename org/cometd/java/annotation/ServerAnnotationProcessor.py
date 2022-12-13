def ServerAnnotationProcessor():
    '''    public ServerAnnotationProcessor(final BayeuxServer bayeuxServer)
    public ServerAnnotationProcessor(final BayeuxServer bayeuxServer, final Object... injectables)
    '''
def process():
    '''    public boolean process(final Object bean)
    '''
def processConfigurations():
    '''    public boolean processConfigurations(final Object bean)
    '''
def configureChannel():
    '''    public void configureChannel(final ConfigurableServerChannel channel)
    '''
def processDependencies():
    '''    public boolean processDependencies(final Object bean)
    '''
def processPostConstruct():
    '''    public boolean processPostConstruct(final Object bean)
    '''
def processCallbacks():
    '''    public boolean processCallbacks(final Object bean)
    '''
def deprocess():
    '''    public boolean deprocess(final Object bean)
    '''
def deprocessCallbacks():
    '''    public boolean deprocessCallbacks(final Object bean)
    '''
def processPreDestroy():
    '''    public boolean processPreDestroy(final Object bean)
    '''
def onMessage():
    '''    public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
    public void onMessage(final ClientSessionChannel channel, final Message message)
    '''
def SubscriptionCallback():
    '''    public SubscriptionCallback(final LocalSession localSession, final Object target, final Method method, final String channel)
    '''
