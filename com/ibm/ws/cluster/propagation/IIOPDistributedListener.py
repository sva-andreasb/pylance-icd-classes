routeTableStreamVersion = "int  0"
remote = "String  \"ClusterListenerService\""
def ():
    '''returns IIOPDistributedListener\n\n
    (final DescriptionKey key)\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def push():
    '''returns None\n\n
    push(final String[] key, final byte[] clusterInformation)\n
    '''
def reregister():
    '''returns None\n\n
    reregister(final DescriptionKey key, final URL location)\n
    '''
def register():
    '''returns None\n\n
    register(final Description description, final Contract contract, final Format format, final URL location)\n
    '''
def update():
    '''returns None\n\n
    update(final DescriptionKey key, final byte[] clusterInformation)\n
    '''
def setContract():
    '''returns boolean\n\n
    setContract(final DescriptionKey key, final Contract contract, final URL location)\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final ExtrinsicDescription extrinsicDescription)\n
    aggregate(final IntrinsicDescription intrinsicDescription)\n
    '''
def getContract():
    '''returns Contract\n\n
    getContract(final DescriptionKey key)\n
    '''
def invokeRegistration():
    '''returns None\n\n
    invokeRegistration(final String[] registrarName, final Registrar registrar)\n
    '''
def checkForPeerAccessPoint():
    '''returns None\n\n
    checkForPeerAccessPoint(final String cellName)\n
    '''
