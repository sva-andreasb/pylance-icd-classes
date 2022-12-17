NO_TRANSACTION_TIMEOUT_MS = "int  Integer.MAX_VALUE"
def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final String transactionalId)\n
    (final String transactionalId, final int transactionTimeoutMs)\n
    '''
def getErrorResponse():
    '''returns AbstractResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def transactionalId():
    '''returns String\n\n
    transactionalId()\n
    '''
def transactionTimeoutMs():
    '''returns int\n\n
    transactionTimeoutMs()\n
    '''
def build():
    '''returns InitProducerIdRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
