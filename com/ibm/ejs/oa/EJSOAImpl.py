def registerServantManager():
    '''returns None\n\n
    registerServantManager(final ServantManager servantManager)\n
    '''
def registerServant():
    '''returns None\n\n
    registerServant(final CSIServant servant, final byte[] key)\n
    registerServant(final CSIServant servant, final byte[] key, final boolean useLsd)\n
    registerServant(final CSIServant servant, final ByteArray key, final boolean useLsd)\n
    registerServant(final Remote servant, final byte[] key, final boolean wlmable, final boolean useLsd)\n
    registerServant(final Remote servant, final ByteArray key, final boolean wlmable, final boolean useLsd)\n
    registerServant(final Remote servant, final ByteArray key, final Identity cluster, final boolean useLsd)\n
    registerServant(final org.omg.CORBA.Object servant)\n
    registerServant(final org.omg.CORBA.Object servant, final byte[] key)\n
    registerServant(final org.omg.CORBA.Object servant, final byte[] key, final boolean wlmable)\n
    registerServant(final org.omg.CORBA.Object servant, final byte[] key, final Identity cluster)\n
    '''
def unregisterServant():
    '''returns None\n\n
    unregisterServant(final CSIServant servant)\n
    unregisterServant(final org.omg.CORBA.Object servant)\n
    '''
def createIOR():
    '''returns IOR\n\n
    createIOR(final ByteArray key, final Identity cluster, final boolean useLsd, final String typeid)\n
    '''
