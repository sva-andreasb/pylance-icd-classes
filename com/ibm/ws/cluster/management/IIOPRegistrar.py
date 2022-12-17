remote = "String  \"ClusterRegistrarService\""
def forward():
    '''returns None\n\n
    forward(final String[] key, final byte[] clusterInformation)\n
    '''
def pullDescriptionKey():
    '''returns String[]\n\n
    pullDescriptionKey(final String clusterName)\n
    '''
def pullCurrentVersion():
    '''returns byte[]\n\n
    pullCurrentVersion(final String[] key, final byte[] format)\n
    '''
def pull():
    '''returns byte[]\n\n
    pull(final String[] key, final byte[] format)\n
    '''
def pullKey():
    '''returns DescriptionKey\n\n
    pullKey(final String clusterName, final URL location)\n
    '''
def registerCurrentVersionBackupClusterListener():
    '''returns None\n\n
    registerCurrentVersionBackupClusterListener(final String[] key, final StateTransfer listener, final byte[] contract)\n
    '''
def registerClusterListener():
    '''returns None\n\n
    registerClusterListener(final String[] key, final StateTransfer listener, final byte[] contract)\n
    '''
def deregisterClusterListener():
    '''returns None\n\n
    deregisterClusterListener(final String[] key, final StateTransfer listener)\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final String[] key, final byte[] description)\n
    '''
def handleNotification():
    '''returns None\n\n
    handleNotification(final DescriptionKey key, final String type, final Object data, final Object handback)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def keyToObject():
    '''returns Object\n\n
    keyToObject(final byte[] key)\n
    '''
def addServant():
    '''returns None\n\n
    addServant(final org.omg.CORBA.Object listener, final String key)\n
    '''
