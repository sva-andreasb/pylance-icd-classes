CONNECTION_SYNCHRONIZATION_ORDER = "int  1000"
def ():
    '''returns ConnectionSynchronization\n\n
    (final ConnectionHolder connectionHolder, final DataSource dataSource)\n
    '''
def getOrder():
    '''returns int\n\n
    getOrder()\n
    '''
def suspend():
    '''returns None\n\n
    suspend()\n
    '''
def resume():
    '''returns None\n\n
    resume()\n
    '''
def beforeCompletion():
    '''returns None\n\n
    beforeCompletion()\n
    '''
def afterCompletion():
    '''returns None\n\n
    afterCompletion(final int status)\n
    '''
