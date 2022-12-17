def ():
    '''returns SubscriptionCallback\n\n
    (final BayeuxServer bayeuxServer)\n
    (final BayeuxServer bayeuxServer, final Object... injectables)\n
    (final LocalSession localSession, final Object target, final Method method, final String channel)\n
    '''
def process():
    '''returns boolean\n\n
    process(final Object bean)\n
    '''
def processConfigurations():
    '''returns boolean\n\n
    processConfigurations(final Object bean)\n
    '''
def configureChannel():
    '''returns None\n\n
    configureChannel(final ConfigurableServerChannel channel)\n
    '''
def processDependencies():
    '''returns boolean\n\n
    processDependencies(final Object bean)\n
    '''
def processPostConstruct():
    '''returns boolean\n\n
    processPostConstruct(final Object bean)\n
    '''
def processCallbacks():
    '''returns boolean\n\n
    processCallbacks(final Object bean)\n
    '''
def deprocess():
    '''returns boolean\n\n
    deprocess(final Object bean)\n
    '''
def deprocessCallbacks():
    '''returns boolean\n\n
    deprocessCallbacks(final Object bean)\n
    '''
def processPreDestroy():
    '''returns boolean\n\n
    processPreDestroy(final Object bean)\n
    '''
def onMessage():
    '''returns None\n\n
    onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    '''
