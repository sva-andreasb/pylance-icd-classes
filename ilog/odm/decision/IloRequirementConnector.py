COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloRequirementConnector\n\n
    (final IloEngineController controller)\n
    '''
def associateRequirement():
    '''returns None\n\n
    associateRequirement(final IloRequirement requirement, final String datasetId, final int colIndex, final IloRowKey rowKey)\n
    '''
def makeTable():
    '''returns IloOrderedTableImpl\n\n
    makeTable(final IloRequirement.Status[] statusList, final IloSolutionReport solutionReport)\n
    '''
def getRequirements():
    '''returns Collection<IloRequirement>\n\n
    getRequirements(final String datasetId, final int colIndex, final IloRowKey key)\n
    '''
def removeRequirementAssociations():
    '''returns None\n\n
    removeRequirementAssociations(final IloRequirementId id)\n
    '''
