COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def makeDecisionExecutionEncoder():
    '''    public static IloDecisionExecutionController makeDecisionExecutionEncoder(final IloEngineExecutionController target)
    '''
def makeDecisionExecutionDecoder():
    '''    public static IloEngineExecutionController makeDecisionExecutionDecoder(final IloDecisionExecutionController controller)
    '''
def isAbortOrder():
    '''    public static boolean isAbortOrder(final String orderType)
    '''
def isAcceptSolutionOrder():
    '''    public static boolean isAcceptSolutionOrder(final String orderType)
    '''
def isSkipCurrentGoalSearch():
    '''    public static boolean isSkipCurrentGoalSearch(final String orderType)
    '''
def Encoder():
    '''    public Encoder(final IloEngineExecutionController controller)
    '''
def skipCurrentGoalBoundSearch():
    '''    public void skipCurrentGoalBoundSearch()
    '''
def skipRelaxationMinimization():
    '''    public void skipRelaxationMinimization()
    '''
def skipRelaxationPriority():
    '''    public void skipRelaxationPriority()
    '''
def acceptCurrentSolution():
    '''    public void acceptCurrentSolution()
    '''
def abort():
    '''    public void abort()
    '''
def sendControllingOrder():
    '''    public void sendControllingOrder(final long orderId, final String orderType, final Serializable[] orderParameter)
    public void sendControllingOrder(final long orderId, final String orderType, final Serializable[] orderParameter)
    '''
def Decoder():
    '''    public Decoder(final IloDecisionExecutionController controller)
    '''
