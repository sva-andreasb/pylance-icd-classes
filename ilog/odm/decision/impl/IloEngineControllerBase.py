COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def publish():
'''public void publish(final Object publishable)
'''
pass
def isSilent():
'''public boolean isSilent()
'''
pass
def setSilent():
'''public void setSilent(final boolean status)
'''
pass
def getEngineReport():
'''public IloEngineReport getEngineReport()
'''
pass
def explainAllObjectives():
'''public IloExplanation explainAllObjectives(String[] properties)
'''
pass
def explainObjectives():
'''public IloExplanation explainObjectives(final IloDecisionObjective[] objectives, String[] properties)
'''
pass
def explainRequirements():
'''public IloExplanation explainRequirements(final Iterator<?> reqIt, String[] properties, final int depth, final boolean explainParents)
'''
pass
def getDecisionModel():
'''public IloDecisionModel getDecisionModel()
'''
pass
def getFormattedProperty():
'''public Serializable getFormattedProperty(final IloDecisionModel.Element elt, final int index, final IloPropertiesDef propDefs)
'''
pass
def interpretInput():
'''public Object interpretInput(final Object value, final Class<?> requiredType)
public Object[] interpretInput(final Object[] values, final Class<?>[] requiredTypes)
'''
pass
def objectiveIterator():
'''public Iterator<IloDecisionObjective> objectiveIterator()
'''
pass
def formatValue():
'''public Serializable formatValue(final Object value)
'''
pass
def formatValues():
'''public Serializable[] formatValues(final Object[] values)
'''
pass
def interpretDataAccess():
'''public Object interpretDataAccess(final IloDataAccess path, final Class<?> requiredType)
'''
pass
def declareObjectHandle():
'''public void declareObjectHandle(final Object o, final IloObjectHandle handle)
'''
pass
def getObject():
'''public Object getObject(final IloObjectHandle handle)
'''
pass
def getObjectHandle():
'''public IloObjectHandle getObjectHandle(final Object obj)
'''
pass
def undeclareObjectHandle():
'''public Object undeclareObjectHandle(final IloObjectHandle handle)
'''
pass
def getCurrentModel():
'''public IloDecisionModel getCurrentModel()
'''
pass
def selectSharedScope():
'''public void selectSharedScope(final boolean isShared)
'''
pass
def isSharedScope():
'''public boolean isSharedScope()
'''
pass
def print():
'''public void print(final OutputStream os, final Iterator<?> modelEltIt)
'''
pass
def nextTmplInstId():
'''public String nextTmplInstId(final String templateNm)
'''
pass
def end():
'''public void end()
'''
pass
def getRequirement():
'''public IloRequirement getRequirement(final String name)
public IloRequirement getRequirement(final String name, final IloCompositeRequirement parent)
'''
pass
def runEngine():
'''public boolean runEngine(final int mode, final int explainDepth, final int timeLimitSeconds)
'''
pass
def getRequirementConnector():
'''public IloRequirementConnector getRequirementConnector()
'''
pass
def getDefaultPriorityMananger():
'''public IloDefaultPriorityManager getDefaultPriorityMananger()
'''
pass
def getMessageEvaluatorManager():
'''public IloMessageEvaluatorManager getMessageEvaluatorManager()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
public boolean hasNext()
'''
pass
def next():
'''public IloRequirement next()
public IloRequirement next()
public IloRequirement next()
'''
pass
def remove():
'''public void remove()
public void remove()
public void remove()
'''
pass
def ReqIterator():
'''public ReqIterator(final Iterator<?> it, final IloRequirement.Status status)
public ReqIterator(final Iterator<?> it, final IloRequirement.Status[] statusArray)
'''
pass
