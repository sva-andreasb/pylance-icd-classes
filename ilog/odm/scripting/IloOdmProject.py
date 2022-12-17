COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloOdmProject\n\n
    (final String path)\n
    '''
def call():
    '''returns IloOplDecisionService\n\n
    call()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def login():
    '''returns None\n\n
    login(final String login, final String password, final boolean force)\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def getAllWorkspaces():
    '''returns Collection\n\n
    getAllWorkspaces()\n
    '''
def newWorkspace():
    '''returns IloWorkspace\n\n
    newWorkspace(final String name)\n
    '''
def populateDefaultScenario():
    '''returns None\n\n
    populateDefaultScenario(final IloScenario scenario)\n
    '''
def check():
    '''returns boolean\n\n
    check(final IloScenario scenario)\n
    '''
def solve():
    '''returns None\n\n
    solve(final IloScenario scenario)\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final int seconds)\n
    '''
def setUsingSolveAnyway():
    '''returns None\n\n
    setUsingSolveAnyway(final boolean useSolveAnyway)\n
    '''
def findGoalBounds():
    '''returns None\n\n
    findGoalBounds(final IloScenario scenario, final String goal)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getSchemaCatalog():
    '''returns IloSchemaCatalog\n\n
    getSchemaCatalog()\n
    '''
