def ():
    '''returns SubscriptionCallback\n\n
    (final ClientSession clientSession)\n
    (final ClientSession clientSession, final Object... injectables)\n
    (final ClientSession clientSession, final Object target, final Method method, final String channel)\n
    '''
def process():
    '''returns boolean\n\n
    process(final Object bean)\n
    '''
def processPostConstruct():
    '''returns boolean\n\n
    processPostConstruct(final Object bean)\n
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
    onMessage(final ClientSessionChannel channel, final Message message)\n
    onMessage(final ClientSessionChannel channel, final Message message)\n
    '''
