COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def ():
    '''returns ProductVisitor\n\n
    ()\n
    (final String name, final boolean loaded, final MboRemote mbo)\n
    (final List<String> installList)\n
    '''
def isSuccessful():
    '''returns boolean\n\n
    isSuccessful()\n
    '''
def getError():
    '''returns ScheduleError\n\n
    getError()\n
    '''
def computeScheduleOrder():
    '''returns List<MboRemote>\n\n
    computeScheduleOrder(final MboSetRemote siblingTasks)\n
    '''
def addDependency():
    '''returns None\n\n
    addDependency(final String dependsClause, final HashMap<String, ProductInstance> productMap, final HashMap<String, MboRemote> mboMap)\n
    '''
def walkDependences():
    '''returns boolean\n\n
    walkDependences(final ProductVisitor visitor)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isLoaded():
    '''returns boolean\n\n
    isLoaded()\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo()\n
    '''
def hasNoDependences():
    '''returns boolean\n\n
    hasNoDependences()\n
    '''
def hasNoDependents():
    '''returns boolean\n\n
    hasNoDependents()\n
    '''
def markAsVisited():
    '''returns None\n\n
    markAsVisited()\n
    '''
def isVisited():
    '''returns boolean\n\n
    isVisited()\n
    '''
def install():
    '''returns None\n\n
    install(final ProductInstance product)\n
    '''
def push():
    '''returns None\n\n
    push(final ProductInstance product)\n
    '''
def pop():
    '''returns ProductInstance\n\n
    pop()\n
    '''
def isCycle():
    '''returns boolean\n\n
    isCycle(final ProductInstance product)\n
    '''
