def ():
    '''returns _RegistrarStub\n\n
    ()\n
    (final Delegate delegate)\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final String[] key, final byte[] extrinsicDescription)\n
    '''
def pull():
    '''returns byte[]\n\n
    pull(final String[] key, final byte[] format)\n
    '''
def pullCurrentVersion():
    '''returns byte[]\n\n
    pullCurrentVersion(final String[] key, final byte[] format)\n
    '''
def pullDescriptionKey():
    '''returns String[]\n\n
    pullDescriptionKey(final String clusterName)\n
    '''
def registerClusterListener():
    '''returns None\n\n
    registerClusterListener(final String[] key, final StateTransfer listener, final byte[] contract)\n
    '''
def registerCurrentVersionBackupClusterListener():
    '''returns None\n\n
    registerCurrentVersionBackupClusterListener(final String[] key, final StateTransfer listener, final byte[] contract)\n
    '''
def deregisterClusterListener():
    '''returns None\n\n
    deregisterClusterListener(final String[] key, final StateTransfer listener)\n
    '''
def _ids():
    '''returns String[]\n\n
    _ids()\n
    '''
