def ():
    '''returns Record\n\n
    (final DnsName name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)\n
    (final String name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)\n
    (final String name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)\n
    (final DnsName name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)\n
    '''
def toOutputStream():
    '''returns None\n\n
    toOutputStream(final DataOutputStream dos)\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def isAnswer():
    '''returns boolean\n\n
    isAnswer(final Question q)\n
    '''
def isUnicastQuery():
    '''returns boolean\n\n
    isUnicastQuery()\n
    '''
def getPayload():
    '''returns D\n\n
    getPayload()\n
    '''
def getTtl():
    '''returns long\n\n
    getTtl()\n
    '''
def getQuestion():
    '''returns Question\n\n
    getQuestion()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def getValue():
    '''returns int\n\n
    getValue()\n
    getValue()\n
    '''
