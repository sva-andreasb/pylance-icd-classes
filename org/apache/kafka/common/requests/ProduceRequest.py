def ():
    '''returns ProduceRequest\n\n
    (final Struct struct, final short version)\n
    '''
def toStruct():
    '''returns Struct\n\n
    toStruct()\n
    '''
def toString():
    '''returns String\n\n
    toString(final boolean verbose)\n
    toString()\n
    '''
def getErrorResponse():
    '''returns ProduceResponse\n\n
    getErrorResponse(final int throttleTimeMs, final Throwable e)\n
    '''
def acks():
    '''returns short\n\n
    acks()\n
    '''
def timeout():
    '''returns int\n\n
    timeout()\n
    '''
def transactionalId():
    '''returns String\n\n
    transactionalId()\n
    '''
def isTransactional():
    '''returns boolean\n\n
    isTransactional()\n
    '''
def isIdempotent():
    '''returns boolean\n\n
    isIdempotent()\n
    '''
def clearPartitionRecords():
    '''returns None\n\n
    clearPartitionRecords()\n
    '''
def build():
    '''returns ProduceRequest\n\n
    build(final short version)\n
    '''
