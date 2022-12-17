def ():
    '''returns TaskResult\n\n
    (final Status s, final int rc, final String message)\n
    (final int rc, final String message)\n
    ()\n
    '''
def setStatus():
    '''returns TaskResult\n\n
    setStatus(final Status s)\n
    '''
def getStatus():
    '''returns Status\n\n
    getStatus()\n
    '''
def isSuccess():
    '''returns boolean\n\n
    isSuccess()\n
    '''
def isFailure():
    '''returns boolean\n\n
    isFailure()\n
    '''
def isWarning():
    '''returns boolean\n\n
    isWarning()\n
    '''
def getReturnCode():
    '''returns int\n\n
    getReturnCode()\n
    '''
def setReturnCode():
    '''returns None\n\n
    setReturnCode(final int rc)\n
    '''
def getCompletionMessage():
    '''returns String\n\n
    getCompletionMessage()\n
    '''
def setCompletionMessage():
    '''returns None\n\n
    setCompletionMessage(final String message)\n
    '''
def getStdOut():
    '''returns String\n\n
    getStdOut()\n
    '''
def updateStdOut():
    '''returns None\n\n
    updateStdOut(final String stdout)\n
    '''
def getStdErr():
    '''returns String\n\n
    getStdErr()\n
    '''
def updateStdErr():
    '''returns None\n\n
    updateStdErr(final String stderr)\n
    '''
def publish():
    '''returns TaskResult\n\n
    publish()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
