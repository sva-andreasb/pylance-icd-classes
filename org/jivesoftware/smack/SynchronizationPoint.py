def ():
    '''returns SynchronizationPoint\n\n
    (final AbstractXMPPConnection connection, final String waitFor)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def sendAndWaitForResponse():
    '''returns Exception\n\n
    sendAndWaitForResponse(final TopLevelStreamElement request)\n
    '''
def sendAndWaitForResponseOrThrow():
    '''returns None\n\n
    sendAndWaitForResponseOrThrow(final Nonza request)\n
    '''
def checkIfSuccessOrWaitOrThrow():
    '''returns None\n\n
    checkIfSuccessOrWaitOrThrow()\n
    '''
def checkIfSuccessOrWait():
    '''returns Exception\n\n
    checkIfSuccessOrWait()\n
    '''
def reportSuccess():
    '''returns None\n\n
    reportSuccess()\n
    '''
def reportFailure():
    '''returns None\n\n
    reportFailure()\n
    reportFailure(final E failureException)\n
    '''
def reportGenericFailure():
    '''returns None\n\n
    reportGenericFailure(final SmackException.SmackWrappedException exception)\n
    '''
def wasSuccessful():
    '''returns boolean\n\n
    wasSuccessful()\n
    '''
def isNotInInitialState():
    '''returns boolean\n\n
    isNotInInitialState()\n
    '''
def requestSent():
    '''returns boolean\n\n
    requestSent()\n
    '''
def getFailureException():
    '''returns E\n\n
    getFailureException()\n
    '''
