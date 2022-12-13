COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def publish():
    '''public void publish(final Object publishable)
    '''
def isSilent():
    '''public boolean isSilent()
    '''
def setSilent():
    '''public void setSilent(final boolean status)
    '''
def getEngineReport():
    '''public IloEngineReport getEngineReport()
    '''
def explainAllObjectives():
    '''public IloExplanation explainAllObjectives(String[] properties)
    '''
def explainObjectives():
    '''public IloExplanation explainObjectives(final IloDecisionObjective[] objectives, String[] properties)
    '''
def explainRequirements():
    '''public IloExplanation explainRequirements(final Iterator<?> reqIt, String[] properties, final int depth, final boolean explainParents)
    '''
def getDecisionModel():
    '''public IloDecisionModel getDecisionModel()
    '''
def getFormattedProperty():
    '''public Serializable getFormattedProperty(final IloDecisionModel.Element elt, final int index, final IloPropertiesDef propDefs)
    '''
def interpretInput():
    '''public Object interpretInput(final Object value, final Class<?> requiredType)
    public Object[] interpretInput(final Object[] values, final Class<?>[] requiredTypes)
    '''
def objectiveIterator():
    '''public Iterator<IloDecisionObjective> objectiveIterator()
    '''
def formatValue():
    '''public Serializable formatValue(final Object value)
    '''
def formatValues():
    '''public Serializable[] formatValues(final Object[] values)
    '''
def interpretDataAccess():
    '''public Object interpretDataAccess(final IloDataAccess path, final Class<?> requiredType)
    '''
def declareObjectHandle():
    '''public void declareObjectHandle(final Object o, final IloObjectHandle handle)
    '''
def getObject():
    '''public Object getObject(final IloObjectHandle handle)
    '''
def getObjectHandle():
    '''public IloObjectHandle getObjectHandle(final Object obj)
    '''
def undeclareObjectHandle():
    '''public Object undeclareObjectHandle(final IloObjectHandle handle)
    '''
def getCurrentModel():
    '''public IloDecisionModel getCurrentModel()
    '''
def selectSharedScope():
    '''public void selectSharedScope(final boolean isShared)
    '''
def isSharedScope():
    '''public boolean isSharedScope()
    '''
def print():
    '''public void print(final OutputStream os, final Iterator<?> modelEltIt)
    '''
def nextTmplInstId():
    '''public String nextTmplInstId(final String templateNm)
    '''
def end():
    '''public void end()
    '''
def getRequirement():
    '''public IloRequirement getRequirement(final String name)
    public IloRequirement getRequirement(final String name, final IloCompositeRequirement parent)
    '''
def runEngine():
    '''public boolean runEngine(final int mode, final int explainDepth, final int timeLimitSeconds)
    '''
def getRequirementConnector():
    '''public IloRequirementConnector getRequirementConnector()
    '''
def getDefaultPriorityMananger():
    '''public IloDefaultPriorityManager getDefaultPriorityMananger()
    '''
def getMessageEvaluatorManager():
    '''public IloMessageEvaluatorManager getMessageEvaluatorManager()
    '''
def hasNext():
    '''public boolean hasNext()
    public boolean hasNext()
    public boolean hasNext()
    '''
def next():
    '''public IloRequirement next()
    public IloRequirement next()
    public IloRequirement next()
    '''
def remove():
    '''public void remove()
    public void remove()
    public void remove()
    '''
def ReqIterator():
    '''public ReqIterator(final Iterator<?> it, final IloRequirement.Status status)
    public ReqIterator(final Iterator<?> it, final IloRequirement.Status[] statusArray)
    '''
