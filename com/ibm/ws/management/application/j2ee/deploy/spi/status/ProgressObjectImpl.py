def ():
    '''returns ProgressObjectImpl\n\n
    (final CommandType command)\n
    (final CommandType command, final StateType state)\n
    '''
def getDeploymentStatus():
    '''returns DeploymentStatus\n\n
    getDeploymentStatus()\n
    '''
def getResultTargetModuleIDs():
    '''returns TargetModuleID[]\n\n
    getResultTargetModuleIDs()\n
    '''
def getClientConfiguration():
    '''returns ClientConfiguration\n\n
    getClientConfiguration(final TargetModuleID targetModule)\n
    '''
def isCancelSupported():
    '''returns boolean\n\n
    isCancelSupported()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def isStopSupported():
    '''returns boolean\n\n
    isStopSupported()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def addProgressListener():
    '''returns None\n\n
    addProgressListener(final ProgressListener listener)\n
    '''
def removeProgressListener():
    '''returns None\n\n
    removeProgressListener(final ProgressListener listener)\n
    '''
def setFinalStateAndNotify():
    '''returns boolean\n\n
    setFinalStateAndNotify(final StateType state)\n
    '''
def setMessage():
    '''returns None\n\n
    setMessage(final String messageId, final Object[] arguments)\n
    '''
def setTranslatedMessage():
    '''returns None\n\n
    setTranslatedMessage(final String message)\n
    '''
def setState():
    '''returns None\n\n
    setState(final StateType state)\n
    '''
def sendModuleEvent():
    '''returns None\n\n
    sendModuleEvent(final TargetModuleID targetModule, final StateType state, final String messageId, final Object[] arguments)\n
    '''
def sendTranslatedModuleEvent():
    '''returns None\n\n
    sendTranslatedModuleEvent(final TargetModuleID targetModule, final StateType state, final String message)\n
    '''
def addSuccessfulResult():
    '''returns None\n\n
    addSuccessfulResult(final TargetModuleID targetModule)\n
    '''
def addFailedResult():
    '''returns None\n\n
    addFailedResult(final TargetModuleID targetModule)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
