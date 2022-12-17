def ():
    '''returns Jetty6Continuation\n\n
    (final ServletRequest request, final org.mortbay.util.ajax.Continuation continuation)\n
    '''
def addContinuationListener():
    '''returns None\n\n
    addContinuationListener(final ContinuationListener listener)\n
    '''
def complete():
    '''returns None\n\n
    complete()\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final String name)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final Object attribute)\n
    '''
def getServletResponse():
    '''returns ServletResponse\n\n
    getServletResponse()\n
    '''
def isExpired():
    '''returns boolean\n\n
    isExpired()\n
    '''
def isInitial():
    '''returns boolean\n\n
    isInitial()\n
    '''
def isResumed():
    '''returns boolean\n\n
    isResumed()\n
    '''
def isSuspended():
    '''returns boolean\n\n
    isSuspended()\n
    '''
def resume():
    '''returns None\n\n
    resume()\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final long timeoutMs)\n
    '''
def suspend():
    '''returns None\n\n
    suspend(final ServletResponse response)\n
    suspend()\n
    '''
def isResponseWrapped():
    '''returns boolean\n\n
    isResponseWrapped()\n
    '''
def undispatch():
    '''returns None\n\n
    undispatch()\n
    '''
def enter():
    '''returns boolean\n\n
    enter(final ServletResponse response)\n
    '''
def exit():
    '''returns boolean\n\n
    exit()\n
    '''
