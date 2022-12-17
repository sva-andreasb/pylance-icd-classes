def ():
    '''returns SoftKey\n\n
    ()\n
    (final Identity cluster, final Map key, final ReferenceQueue queue)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def select():
    '''returns Target\n\n
    select(final Identity clusterIdentity)\n
    select(final SelectionCriteria criteria)\n
    '''
def getCriteria():
    '''returns SelectionCriteria\n\n
    getCriteria(final Identity clusterIdentity, final boolean process, final boolean host, final Map matchingEndpoints, final Set matchingAttributes)\n
    getCriteria(final Identity clusterIdentity, final Map context)\n
    '''
def getRule():
    '''returns SelectionRule\n\n
    getRule(final String ruleName)\n
    '''
def registerResolver():
    '''returns None\n\n
    registerResolver(final ClusterIdentityResolver resolver)\n
    '''
def unregisterResolver():
    '''returns None\n\n
    unregisterResolver(final ClusterIdentityResolver resolver)\n
    '''
def getOrderedSequence():
    '''returns ClusterIdentityResolver[]\n\n
    getOrderedSequence()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
