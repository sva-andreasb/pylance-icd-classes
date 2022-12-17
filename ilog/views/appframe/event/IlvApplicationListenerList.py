def ():
    '''returns IlvApplicationListenerList\n\n
    ()\n
    '''
def applicationEventReceived():
    '''returns None\n\n
    applicationEventReceived(final ApplicationEvent applicationEvent)\n
    '''
def getApplicationListeners():
    '''returns ApplicationListener[]\n\n
    getApplicationListeners()\n
    '''
def addApplicationListener():
    '''returns None\n\n
    addApplicationListener(final ApplicationListener applicationListener)\n
    addApplicationListener(final String s, final ApplicationListener e)\n
    '''
def removeApplicationListener():
    '''returns boolean\n\n
    removeApplicationListener(final ApplicationListener o)\n
    removeApplicationListener(final String key, final ApplicationListener o)\n
    '''
def fireApplicationEvent():
    '''returns None\n\n
    fireApplicationEvent(final ApplicationEvent applicationEvent)\n
    '''
