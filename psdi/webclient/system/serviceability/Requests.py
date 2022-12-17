def clear():
    '''returns None\n\n
    clear()\n
    clear()\n
    '''
def getLimit():
    '''returns int\n\n
    getLimit()\n
    '''
def setLimit():
    '''returns None\n\n
    setLimit(final int limit)\n
    '''
def setEnabled():
    '''returns None\n\n
    setEnabled(final boolean enabled)\n
    '''
def isEnabled():
    '''returns boolean\n\n
    isEnabled()\n
    '''
def log():
    '''returns EventEntry\n\n
    log(final HttpServletRequest request, final HttpServletResponse response)\n
    log(final WebClientEvent event)\n
    '''
def getRequests():
    '''returns RequestEntry[]\n\n
    getRequests()\n
    '''
def setRequestEvent():
    '''returns None\n\n
    setRequestEvent(final WebClientEvent event, final boolean isRequestEvent)\n
    '''
def setHandling():
    '''returns None\n\n
    setHandling(final WebClientEvent event, final boolean handling)\n
    '''
def addHandledBy():
    '''returns None\n\n
    addHandledBy(final WebClientEvent event, final Object handler)\n
    '''
