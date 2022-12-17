def ():
    '''returns Builder\n\n
    (final Struct struct, final short version)\n
    (final String transactionalId, final long producerId, final short producerEpoch, final TransactionResult result)\n
    '''
def transactionalId():
    '''returns String\n\n
    transactionalId()\n
    '''
def producerId():
    '''returns long\n\n
    producerId()\n
    '''
def producerEpoch():
    '''returns short\n\n
    producerEpoch()\n
    '''
def command():
    '''returns TransactionResult\n\n
    command()\n
    '''
def getErrorResponse():
    '''returns EndTxnResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def result():
    '''returns TransactionResult\n\n
    result()\n
    '''
def build():
    '''returns EndTxnRequest\n\n
    build(final short version)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
