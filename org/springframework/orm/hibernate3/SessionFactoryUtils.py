SESSION_SYNCHRONIZATION_ORDER = "int  900"
def ():
    '''returns JtaSessionSynchronization\n\n
    (final SessionHolder sessionHolder, final SessionFactory sessionFactory, final SQLExceptionTranslator jdbcExceptionTranslator, final boolean newSession)\n
    (final SpringSessionSynchronization springSessionSynchronization, final TransactionManager jtaTransactionManager)\n
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
def beforeCommit():
    '''returns None\n\n
    beforeCommit(final boolean readOnly)\n
    '''
def beforeCompletion():
    '''returns None\n\n
    beforeCompletion()\n
    beforeCompletion()\n
    '''
def afterCompletion():
    '''returns None\n\n
    afterCompletion(final int status)\n
    afterCompletion(final int status)\n
    '''
