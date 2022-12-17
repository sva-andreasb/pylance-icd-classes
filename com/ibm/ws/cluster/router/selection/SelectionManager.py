def ():
    '''returns SelectionManager\n\n
    (final ORB wlmorb)\n
    '''
def getTarget():
    '''returns IOR\n\n
    getTarget(final Delegate key)\n
    '''
def targetForwarded():
    '''returns None\n\n
    targetForwarded(final org.omg.CORBA.Object forwardReference)\n
    '''
def getCorrespondingServer():
    '''returns ClusterMemberDescription\n\n
    getCorrespondingServer(final Object key, final IOR ior)\n
    '''
def cacheIOR():
    '''returns None\n\n
    cacheIOR(final Delegate key, final WLMIOR wlmIOR)\n
    '''
def postInvoke():
    '''returns ClusterMemberDescription\n\n
    postInvoke(final Object key, final IOR ior)\n
    '''
def handleRemoteException():
    '''returns None\n\n
    handleRemoteException(final ClusterMemberDescription member, final ConnectionExceptionHelper re)\n
    '''
