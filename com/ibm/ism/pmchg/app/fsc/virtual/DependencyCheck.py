COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
def DependencyCheck():
    '''public DependencyCheck()
    '''
def isSuccessful():
    '''public boolean isSuccessful()
    '''
def getError():
    '''public ScheduleError getError()
    '''
def computeScheduleOrder():
    '''public List<MboRemote> computeScheduleOrder(final MboSetRemote siblingTasks)
    '''
def ProductInstance():
    '''public ProductInstance(final String name, final boolean loaded, final MboRemote mbo)
    '''
def addDependency():
    '''public void addDependency(final String dependsClause, final HashMap<String, ProductInstance> productMap, final HashMap<String, MboRemote> mboMap)
    '''
def walkDependences():
    '''public boolean walkDependences(final ProductVisitor visitor)
    '''
def getName():
    '''public String getName()
    '''
def isLoaded():
    '''public boolean isLoaded()
    '''
def getMbo():
    '''public MboRemote getMbo()
    '''
def hasNoDependences():
    '''public boolean hasNoDependences()
    '''
def hasNoDependents():
    '''public boolean hasNoDependents()
    '''
def markAsVisited():
    '''public void markAsVisited()
    '''
def isVisited():
    '''public boolean isVisited()
    '''
def ProductVisitor():
    '''public ProductVisitor(final List<String> installList)
    '''
def install():
    '''public void install(final ProductInstance product)
    '''
def push():
    '''public void push(final ProductInstance product)
    '''
def pop():
    '''public ProductInstance pop()
    '''
def isCycle():
    '''public boolean isCycle(final ProductInstance product)
    '''
