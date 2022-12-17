def ():
    '''returns TokenInformation\n\n
    (final String tokenId, final KafkaPrincipal owner, final Collection<KafkaPrincipal> renewers, final long issueTimestamp, final long maxTimestamp, final long expiryTimestamp)\n
    '''
def owner():
    '''returns KafkaPrincipal\n\n
    owner()\n
    '''
def ownerAsString():
    '''returns String\n\n
    ownerAsString()\n
    '''
def renewers():
    '''returns Collection<KafkaPrincipal>\n\n
    renewers()\n
    '''
def renewersAsString():
    '''returns Collection<String>\n\n
    renewersAsString()\n
    '''
def issueTimestamp():
    '''returns long\n\n
    issueTimestamp()\n
    '''
def expiryTimestamp():
    '''returns long\n\n
    expiryTimestamp()\n
    '''
def setExpiryTimestamp():
    '''returns None\n\n
    setExpiryTimestamp(final long expiryTimestamp)\n
    '''
def tokenId():
    '''returns String\n\n
    tokenId()\n
    '''
def maxTimestamp():
    '''returns long\n\n
    maxTimestamp()\n
    '''
def ownerOrRenewer():
    '''returns boolean\n\n
    ownerOrRenewer(final KafkaPrincipal principal)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
