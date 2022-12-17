QUEUE_SIZE = "int  500"
def ():
    '''returns XMPPTCPConnection\n\n
    (final XMPPTCPConnectionConfiguration config)\n
    (final CharSequence jid, final String password)\n
    (final CharSequence username, final String password, final String serviceName)\n
    '''
def connectionClosedOnError():
    '''returns None\n\n
    connectionClosedOnError(final Exception e)\n
    '''
def isSecureConnection():
    '''returns boolean\n\n
    isSecureConnection()\n
    '''
def sendNonza():
    '''returns None\n\n
    sendNonza(final Nonza element)\n
    '''
def isUsingCompression():
    '''returns boolean\n\n
    isUsingCompression()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def setUseStreamManagement():
    '''returns None\n\n
    setUseStreamManagement(final boolean useSm)\n
    '''
def setUseStreamManagementResumption():
    '''returns None\n\n
    setUseStreamManagementResumption(final boolean useSmResumption)\n
    '''
def setPreferredResumptionTime():
    '''returns None\n\n
    setPreferredResumptionTime(final int resumptionTime)\n
    '''
def addRequestAckPredicate():
    '''returns boolean\n\n
    addRequestAckPredicate(final StanzaFilter predicate)\n
    '''
def removeRequestAckPredicate():
    '''returns boolean\n\n
    removeRequestAckPredicate(final StanzaFilter predicate)\n
    '''
def removeAllRequestAckPredicates():
    '''returns None\n\n
    removeAllRequestAckPredicates()\n
    '''
def requestSmAcknowledgement():
    '''returns None\n\n
    requestSmAcknowledgement()\n
    '''
def sendSmAcknowledgement():
    '''returns None\n\n
    sendSmAcknowledgement()\n
    '''
def addStanzaAcknowledgedListener():
    '''returns None\n\n
    addStanzaAcknowledgedListener(final StanzaListener listener)\n
    '''
def removeStanzaAcknowledgedListener():
    '''returns boolean\n\n
    removeStanzaAcknowledgedListener(final StanzaListener listener)\n
    '''
def removeAllStanzaAcknowledgedListeners():
    '''returns None\n\n
    removeAllStanzaAcknowledgedListeners()\n
    '''
def addStanzaDroppedListener():
    '''returns None\n\n
    addStanzaDroppedListener(final StanzaListener listener)\n
    '''
def removeStanzaDroppedListener():
    '''returns boolean\n\n
    removeStanzaDroppedListener(final StanzaListener listener)\n
    '''
def addStanzaIdAcknowledgedListener():
    '''returns StanzaListener\n\n
    addStanzaIdAcknowledgedListener(final String id, final StanzaListener listener)\n
    '''
def removeStanzaIdAcknowledgedListener():
    '''returns StanzaListener\n\n
    removeStanzaIdAcknowledgedListener(final String id)\n
    '''
def removeAllStanzaIdAcknowledgedListeners():
    '''returns None\n\n
    removeAllStanzaIdAcknowledgedListeners()\n
    '''
def isSmAvailable():
    '''returns boolean\n\n
    isSmAvailable()\n
    '''
def isSmEnabled():
    '''returns boolean\n\n
    isSmEnabled()\n
    '''
def streamWasResumed():
    '''returns boolean\n\n
    streamWasResumed()\n
    '''
def isDisconnectedButSmResumptionPossible():
    '''returns boolean\n\n
    isDisconnectedButSmResumptionPossible()\n
    '''
def isSmResumptionPossible():
    '''returns boolean\n\n
    isSmResumptionPossible()\n
    '''
def getMaxSmResumptionTime():
    '''returns int\n\n
    getMaxSmResumptionTime()\n
    '''
def setBundleandDeferCallback():
    '''returns None\n\n
    setBundleandDeferCallback(final BundleAndDeferCallback bundleAndDeferCallback)\n
    '''
