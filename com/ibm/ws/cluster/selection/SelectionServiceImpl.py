def SelectionServiceImpl():
'''public SelectionServiceImpl()
'''
pass
def toString():
'''public String toString()
'''
pass
def select():
'''public Target select(final Identity clusterIdentity)
public Target select(final SelectionCriteria criteria)
'''
pass
def getCriteria():
'''public SelectionCriteria getCriteria(final Identity clusterIdentity, final boolean process, final boolean host, final Map matchingEndpoints, final Set matchingAttributes)
public SelectionCriteria getCriteria(final Identity clusterIdentity, final Map context)
'''
pass
def getRule():
'''public SelectionRule getRule(final String ruleName)
'''
pass
def registerResolver():
'''public void registerResolver(final ClusterIdentityResolver resolver)
'''
pass
def unregisterResolver():
'''public void unregisterResolver(final ClusterIdentityResolver resolver)
'''
pass
def getOrderedSequence():
'''public ClusterIdentityResolver[] getOrderedSequence()
'''
pass
def SoftKey():
'''public SoftKey(final Identity cluster, final Map key, final ReferenceQueue queue)
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
