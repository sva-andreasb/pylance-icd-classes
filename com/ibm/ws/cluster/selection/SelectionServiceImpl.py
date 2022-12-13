def SelectionServiceImpl():
    '''    public SelectionServiceImpl()
    '''
def toString():
    '''    public String toString()
    '''
def select():
    '''    public Target select(final Identity clusterIdentity)
    public Target select(final SelectionCriteria criteria)
    '''
def getCriteria():
    '''    public SelectionCriteria getCriteria(final Identity clusterIdentity, final boolean process, final boolean host, final Map matchingEndpoints, final Set matchingAttributes)
    public SelectionCriteria getCriteria(final Identity clusterIdentity, final Map context)
    '''
def getRule():
    '''    public SelectionRule getRule(final String ruleName)
    '''
def registerResolver():
    '''    public void registerResolver(final ClusterIdentityResolver resolver)
    '''
def unregisterResolver():
    '''    public void unregisterResolver(final ClusterIdentityResolver resolver)
    '''
def getOrderedSequence():
    '''    public ClusterIdentityResolver[] getOrderedSequence()
    '''
def SoftKey():
    '''    public SoftKey(final Identity cluster, final Map key, final ReferenceQueue queue)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
