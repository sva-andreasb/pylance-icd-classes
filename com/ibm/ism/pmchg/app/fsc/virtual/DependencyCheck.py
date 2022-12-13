COPYRIGHT = "String \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
def DependencyCheck():
'''public DependencyCheck()
'''
pass
def isSuccessful():
'''public boolean isSuccessful()
'''
pass
def getError():
'''public ScheduleError getError()
'''
pass
def computeScheduleOrder():
'''public List<MboRemote> computeScheduleOrder(final MboSetRemote siblingTasks)
'''
pass
def ProductInstance():
'''public ProductInstance(final String name, final boolean loaded, final MboRemote mbo)
'''
pass
def addDependency():
'''public void addDependency(final String dependsClause, final HashMap<String, ProductInstance> productMap, final HashMap<String, MboRemote> mboMap)
'''
pass
def walkDependences():
'''public boolean walkDependences(final ProductVisitor visitor)
'''
pass
def getName():
'''public String getName()
'''
pass
def isLoaded():
'''public boolean isLoaded()
'''
pass
def getMbo():
'''public MboRemote getMbo()
'''
pass
def hasNoDependences():
'''public boolean hasNoDependences()
'''
pass
def hasNoDependents():
'''public boolean hasNoDependents()
'''
pass
def markAsVisited():
'''public void markAsVisited()
'''
pass
def isVisited():
'''public boolean isVisited()
'''
pass
def ProductVisitor():
'''public ProductVisitor(final List<String> installList)
'''
pass
def install():
'''public void install(final ProductInstance product)
'''
pass
def push():
'''public void push(final ProductInstance product)
'''
pass
def pop():
'''public ProductInstance pop()
'''
pass
def isCycle():
'''public boolean isCycle(final ProductInstance product)
'''
pass
