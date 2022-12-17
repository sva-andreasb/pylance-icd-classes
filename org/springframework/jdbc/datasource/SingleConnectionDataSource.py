def ():
    '''returns CloseSuppressingInvocationHandler\n\n
    ()\n
    (final String driverClassName, final String url, final String username, final String password, final boolean suppressClose)\n
    (final String url, final String username, final String password, final boolean suppressClose)\n
    (final String url, final boolean suppressClose)\n
    (final Connection target, final boolean suppressClose)\n
    (final Connection target)\n
    '''
def setSuppressClose():
    '''returns None\n\n
    setSuppressClose(final boolean suppressClose)\n
    '''
def isSuppressClose():
    '''returns boolean\n\n
    isSuppressClose()\n
    '''
def shouldClose():
    '''returns boolean\n\n
    shouldClose(final Connection con)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    getConnection(final String username, final String password)\n
    '''
def invoke():
    '''returns Object\n\n
    invoke(final Object proxy, final Method method, final Object[] args)\n
    '''
