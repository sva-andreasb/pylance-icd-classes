def RouterMediator():
    '''    public RouterMediator()
    '''
def setObservedWeight():
    '''    public void setObservedWeight(final Identity cluster, final Identity member, final int weight)
    '''
def getObservedWeight():
    '''    public int getObservedWeight(final Identity cluster, final Identity member)
    '''
def setErrorWeight():
    '''    public void setErrorWeight(final Identity cluster, final Identity member, final int error)
    '''
def getErrorWeight():
    '''    public int getErrorWeight(final Identity cluster, final Identity member)
    '''
def tareErrorWeights():
    '''    public void tareErrorWeights(final Identity cluster)
    '''
def setAvailable():
    '''    public void setAvailable(final Identity member)
    '''
def setUnavailable():
    '''    public void setUnavailable(final Identity member)
    '''
def isAvailable():
    '''    public boolean isAvailable(final Identity member)
    '''
def tareObservedWeights():
    '''    public void tareObservedWeights(final Identity cluster)
    '''
def registerMembershipAdvisor():
    '''    public void registerMembershipAdvisor(final MembershipAdvisor advisor)
    '''
def deregisterMembershipAdvisor():
    '''    public void deregisterMembershipAdvisor(final MembershipAdvisor advisor)
    '''
def registerFeedback():
    '''    public void registerFeedback(final WeightBasedFeedback feedback, final Identity cluster)
    '''
def setForceFeedback():
    '''    public static void setForceFeedback(final boolean bool)
    '''
