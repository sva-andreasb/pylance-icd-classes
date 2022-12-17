def ():
    '''returns AdvisedSupport\n\n
    ()\n
    (final Class[] interfaces)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final AdvisedSupportListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final AdvisedSupportListener listener)\n
    '''
def setTarget():
    '''returns None\n\n
    setTarget(final Object target)\n
    '''
def setTargetSource():
    '''returns None\n\n
    setTargetSource(final TargetSource targetSource)\n
    '''
def getTargetSource():
    '''returns TargetSource\n\n
    getTargetSource()\n
    '''
def setAdvisorChainFactory():
    '''returns None\n\n
    setAdvisorChainFactory(final AdvisorChainFactory advisorChainFactory)\n
    '''
def getAdvisorChainFactory():
    '''returns AdvisorChainFactory\n\n
    getAdvisorChainFactory()\n
    '''
def setInterfaces():
    '''returns None\n\n
    setInterfaces(final Class[] interfaces)\n
    '''
def addInterface():
    '''returns None\n\n
    addInterface(final Class newInterface)\n
    '''
def getProxiedInterfaces():
    '''returns Class[]\n\n
    getProxiedInterfaces()\n
    '''
def removeInterface():
    '''returns boolean\n\n
    removeInterface(final Class intf)\n
    '''
def addAdvice():
    '''returns None\n\n
    addAdvice(final Advice advice)\n
    addAdvice(final int pos, final Advice advice)\n
    '''
def isInterfaceProxied():
    '''returns boolean\n\n
    isInterfaceProxied(final Class intf)\n
    '''
def indexOf():
    '''returns int\n\n
    indexOf(final Advice advice)\n
    indexOf(final Advisor advisor)\n
    '''
def removeAdvisor():
    '''returns None\n\n
    removeAdvisor(final int index)\n
    '''
def addAdvisor():
    '''returns None\n\n
    addAdvisor(final int pos, final IntroductionAdvisor advisor)\n
    addAdvisor(final int pos, final Advisor advisor)\n
    addAdvisor(final Advisor advisor)\n
    '''
def toProxyConfigString():
    '''returns String\n\n
    toProxyConfigString()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
