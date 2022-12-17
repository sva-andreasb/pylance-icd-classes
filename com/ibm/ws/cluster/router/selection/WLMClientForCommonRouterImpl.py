def ():
    '''returns WLMClientForCommonRouterImpl\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final ORB orb)\n
    '''
def initialize():
    '''returns boolean\n\n
    initialize(final Delegate targetObjectProxy, final IOR ior)\n
    '''
def getNextTarget():
    '''returns IOR\n\n
    getNextTarget(final Delegate targetObjectProxy, final IOR locatedIOR)\n
    getNextTarget(final byte[] objectKey)\n
    '''
def postInvoke():
    '''returns None\n\n
    postInvoke(final Delegate targetObjectProxy, final IOR locatedIOR)\n
    '''
def handleRemoteException():
    '''returns IOR\n\n
    handleRemoteException(final Delegate targetObjectProxy, final IOR locatedIOR, final Exception exception)\n
    '''
def getORB():
    '''returns ORB\n\n
    getORB()\n
    '''
