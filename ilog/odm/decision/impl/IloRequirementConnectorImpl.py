COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns Association\n\n
    ()\n
    (final IloRequirementConnectorImpl parent)\n
    (final IloRequirement req, final String datasetId, final int colIndex, final IloRowKey key)\n
    '''
def getParent():
    '''returns IloRequirementConnectorImpl\n\n
    getParent()\n
    '''
def associateRequirement():
    '''returns None\n\n
    associateRequirement(final IloRequirement requirement, final String datasetId, final int colIndex, final IloRowKey rowKey)\n
    '''
def makeTable():
    '''returns IloOrderedTableImpl\n\n
    makeTable(final IloRequirement.Status[] statusList, final IloSolutionReport solutionReport)\n
    '''
def removeRequirementAssociations():
    '''returns None\n\n
    removeRequirementAssociations(final IloRequirementId id)\n
    '''
def getRequirements():
    '''returns Collection<IloRequirement>\n\n
    getRequirements(final String datasetId, final int colIndex, final IloRowKey key)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getColIndex():
    '''returns int\n\n
    getColIndex()\n
    '''
def getDatasetId():
    '''returns String\n\n
    getDatasetId()\n
    '''
def getKey():
    '''returns IloRowKey\n\n
    getKey()\n
    '''
def getReq():
    '''returns IloRequirement\n\n
    getReq()\n
    '''
