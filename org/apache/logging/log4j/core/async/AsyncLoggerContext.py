def ():
    '''returns AsyncLoggerContext\n\n
    (final String name)\n
    (final String name, final Object externalContext)\n
    (final String name, final Object externalContext, final URI configLocn)\n
    (final String name, final Object externalContext, final String configLocn)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    start(final Configuration config)\n
    '''
def stop():
    '''returns boolean\n\n
    stop(final long timeout, final TimeUnit timeUnit)\n
    '''
def createRingBufferAdmin():
    '''returns RingBufferAdmin\n\n
    createRingBufferAdmin()\n
    '''
def setUseThreadLocals():
    '''returns None\n\n
    setUseThreadLocals(final boolean useThreadLocals)\n
    '''
