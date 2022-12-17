def ():
    '''returns DistributedListenerRepImpl\n\n
    (final StateTransfer listener)\n
    (final BulletinBoard bb, final String subjectName)\n
    '''
def update():
    '''returns None\n\n
    update(final DescriptionKey key, final byte[] clusterInformation)\n
    '''
def push():
    '''returns None\n\n
    push(final DescriptionKey key, final byte[] clusterInformation)\n
    '''
def reregister():
    '''returns None\n\n
    reregister(final DescriptionKey key, final URL location)\n
    '''
def register():
    '''returns None\n\n
    register(final Description description, final Contract contract, final Format format, final URL location)\n
    '''
def setContract():
    '''returns boolean\n\n
    setContract(final DescriptionKey key, final Contract contract, final URL location)\n
    '''
def aggregate():
    '''returns None\n\n
    aggregate(final ExtrinsicDescription extriniscDescription)\n
    aggregate(final IntrinsicDescription intrinsicDescription)\n
    '''
def getContract():
    '''returns Contract\n\n
    getContract(final DescriptionKey key)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def deregister():
    '''returns None\n\n
    deregister()\n
    '''
