def ():
    '''returns RouterMediator\n\n
    ()\n
    '''
def setObservedWeight():
    '''returns None\n\n
    setObservedWeight(final Identity cluster, final Identity member, final int weight)\n
    '''
def getObservedWeight():
    '''returns int\n\n
    getObservedWeight(final Identity cluster, final Identity member)\n
    '''
def setErrorWeight():
    '''returns None\n\n
    setErrorWeight(final Identity cluster, final Identity member, final int error)\n
    '''
def getErrorWeight():
    '''returns int\n\n
    getErrorWeight(final Identity cluster, final Identity member)\n
    '''
def tareErrorWeights():
    '''returns None\n\n
    tareErrorWeights(final Identity cluster)\n
    '''
def setAvailable():
    '''returns None\n\n
    setAvailable(final Identity member)\n
    '''
def setUnavailable():
    '''returns None\n\n
    setUnavailable(final Identity member)\n
    '''
def isAvailable():
    '''returns boolean\n\n
    isAvailable(final Identity member)\n
    '''
def tareObservedWeights():
    '''returns None\n\n
    tareObservedWeights(final Identity cluster)\n
    '''
def registerMembershipAdvisor():
    '''returns None\n\n
    registerMembershipAdvisor(final MembershipAdvisor advisor)\n
    '''
def deregisterMembershipAdvisor():
    '''returns None\n\n
    deregisterMembershipAdvisor(final MembershipAdvisor advisor)\n
    '''
def registerFeedback():
    '''returns None\n\n
    registerFeedback(final WeightBasedFeedback feedback, final Identity cluster)\n
    '''
