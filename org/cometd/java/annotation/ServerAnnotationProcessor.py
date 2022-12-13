def ServerAnnotationProcessor():
'''public ServerAnnotationProcessor(final BayeuxServer bayeuxServer)
public ServerAnnotationProcessor(final BayeuxServer bayeuxServer, final Object... injectables)
'''
pass
def process():
'''public boolean process(final Object bean)
'''
pass
def processConfigurations():
'''public boolean processConfigurations(final Object bean)
'''
pass
def configureChannel():
'''public void configureChannel(final ConfigurableServerChannel channel)
'''
pass
def processDependencies():
'''public boolean processDependencies(final Object bean)
'''
pass
def processPostConstruct():
'''public boolean processPostConstruct(final Object bean)
'''
pass
def processCallbacks():
'''public boolean processCallbacks(final Object bean)
'''
pass
def deprocess():
'''public boolean deprocess(final Object bean)
'''
pass
def deprocessCallbacks():
'''public boolean deprocessCallbacks(final Object bean)
'''
pass
def processPreDestroy():
'''public boolean processPreDestroy(final Object bean)
'''
pass
def onMessage():
'''public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
public void onMessage(final ClientSessionChannel channel, final Message message)
'''
pass
def SubscriptionCallback():
'''public SubscriptionCallback(final LocalSession localSession, final Object target, final Method method, final String channel)
'''
pass
