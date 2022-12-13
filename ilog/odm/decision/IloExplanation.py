COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloExplanation():
    '''    public IloExplanation()
    public IloExplanation(final boolean hasFailed, final String[] propertyList)
    '''
def getProperties():
    '''    public String[] getProperties()
    public Serializable[] getProperties()
    '''
def getPropertyIndex():
    '''    public int getPropertyIndex(String prop)
    '''
def complete():
    '''    public void complete()
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def addElement():
    '''    public void addElement(final Element element)
    public void addElement(final Element child)
    '''
def removeElement():
    '''    public boolean removeElement(final Element element)
    '''
def removeRequirement():
    '''    public boolean removeRequirement(final Requirement req)
    '''
def insertRequirementCopy():
    '''    public Requirement insertRequirementCopy(final Requirement oreq, final boolean force, final boolean copyProperties)
    '''
def getRequirement():
    '''    public Requirement getRequirement(final IloRequirementId id)
    '''
def getSameRequirement():
    '''    public Requirement getSameRequirement(final Requirement oreq)
    '''
def getObjective():
    '''    public Objective getObjective(final IloObjectiveId id)
    public Objective getObjective(final String name)
    '''
def print():
    '''    public void print(final OutputStream os)
    '''
def Element():
    '''    public Element(final String name, final Serializable[] properties)
    '''
def getName():
    '''    public String getName()
    '''
def getParent():
    '''    public Element getParent()
    '''
def getExplanation():
    '''    public IloExplanation getExplanation()
    '''
def getProperty():
    '''    public Serializable getProperty(final int idx)
    '''
def setClosed():
    '''    public void setClosed(final boolean status)
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def Requirement():
    '''    public Requirement(final String name, final Serializable[] properties)
    '''
def getPriority():
    '''    public IloPriority getPriority()
    '''
def setPriority():
    '''    public void setPriority(final IloPriority prio)
    '''
def getRequirementId():
    '''    public IloRequirementId getRequirementId()
    '''
def getParentRequirement():
    '''    public Requirement getParentRequirement()
    '''
def Objective():
    '''    public Objective(final String name, final Serializable[] properties)
    '''
def getObjectiveId():
    '''    public IloObjectiveId getObjectiveId()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def next():
    '''    public Object next()
    '''
def remove():
    '''    public void remove()
    '''
