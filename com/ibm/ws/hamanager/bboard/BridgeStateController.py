HAM_CORESTACK_VIEW_CHANGE_INTO_SYNC = "int  0"
HAM_CORESTACK_VIEW_CHANGE_OUTOF_SYNC = "int  1"
FOREIGN_STATE_UNSYNCHRONONIZED_INTO_SYNC = "int  2"
FOREIGN_STATE_UNSYNCHRONONIZED_OUTOF_SYNC = "int  3"
FOREIGN_STATE_SYNCHRONIZED = "int  4"
INITIALIZE_NONBRIDGED_PROCESS = "int  5"
INITIALIZE_BRIDGED_PROCESS_IN_SINGLE_MEMBER_APG = "int  6"
INITIALIZE_BRIDGED_PROCESS_IN_MULTI_MEMBER_APG = "int  7"
def ():
    '''returns CrossCoreStackStateMachine\n\n
    (final BridgeStateManager observer, final Set configuredBridges, final String thisMembersDCSName)\n
    (final int eventIndex, final boolean isHamGSRViewChange)\n
    (final BridgeStateManager stateObserver, final int numberOfConfiguredBridges)\n
    '''
def bridgeStateSynchronized():
    '''returns None\n\n
    bridgeStateSynchronized()\n
    '''
def getEventIndex():
    '''returns int\n\n
    getEventIndex()\n
    '''
def isLocalViewChangeEvent():
    '''returns boolean\n\n
    isLocalViewChangeEvent()\n
    '''
def isGSRViewChange():
    '''returns boolean\n\n
    isGSRViewChange()\n
    '''
def initializeStateMachine():
    '''returns None\n\n
    initializeStateMachine(final int numberOfConfiguredBridges)\n
    '''
def processEvent():
    '''returns None\n\n
    processEvent(final CrossCoreStackEvent event)\n
    '''
