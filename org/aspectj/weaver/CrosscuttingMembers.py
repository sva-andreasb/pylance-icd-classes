def ():
    '''returns CrosscuttingMembers\n\n
    (final ResolvedType inAspect, final boolean shouldConcretizeIfNeeded)\n
    '''
def addConcreteShadowMunger():
    '''returns None\n\n
    addConcreteShadowMunger(final ShadowMunger m)\n
    '''
def addShadowMungers():
    '''returns None\n\n
    addShadowMungers(final Collection<ShadowMunger> c)\n
    '''
def addTypeMungers():
    '''returns None\n\n
    addTypeMungers(final Collection<ConcreteTypeMunger> c)\n
    '''
def addTypeMunger():
    '''returns None\n\n
    addTypeMunger(final ConcreteTypeMunger m)\n
    '''
def addLateTypeMungers():
    '''returns None\n\n
    addLateTypeMungers(final Collection<ConcreteTypeMunger> c)\n
    '''
def addLateTypeMunger():
    '''returns None\n\n
    addLateTypeMunger(final ConcreteTypeMunger m)\n
    '''
def addDeclares():
    '''returns None\n\n
    addDeclares(final Collection<Declare> declares)\n
    '''
def addDeclare():
    '''returns None\n\n
    addDeclare(final Declare declare)\n
    '''
def exposeTypes():
    '''returns None\n\n
    exposeTypes(final List<UnresolvedType> typesToExpose)\n
    '''
def exposeType():
    '''returns None\n\n
    exposeType(UnresolvedType typeToExpose)\n
    '''
def addPrivilegedAccesses():
    '''returns None\n\n
    addPrivilegedAccesses(final Collection<ResolvedMember> accessedMembers)\n
    '''
def getCflowEntries():
    '''returns Collection<ShadowMunger>\n\n
    getCflowEntries()\n
    '''
def replaceWith():
    '''returns boolean\n\n
    replaceWith(final CrosscuttingMembers other, final boolean careAboutShadowMungers)\n
    '''
def setPerClause():
    '''returns None\n\n
    setPerClause(final PerClause perClause)\n
    '''
def getDeclareDominates():
    '''returns List<Declare>\n\n
    getDeclareDominates()\n
    '''
def getDeclareParents():
    '''returns Collection<DeclareParents>\n\n
    getDeclareParents()\n
    '''
def getDeclareSofts():
    '''returns Collection<DeclareSoft>\n\n
    getDeclareSofts()\n
    '''
def getShadowMungers():
    '''returns List<ShadowMunger>\n\n
    getShadowMungers()\n
    '''
def getTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getTypeMungers()\n
    '''
def getLateTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getLateTypeMungers()\n
    '''
def getDeclareAnnotationOnTypes():
    '''returns Collection<DeclareAnnotation>\n\n
    getDeclareAnnotationOnTypes()\n
    '''
def getDeclareAnnotationOnFields():
    '''returns Collection<DeclareAnnotation>\n\n
    getDeclareAnnotationOnFields()\n
    '''
def getDeclareAnnotationOnMethods():
    '''returns Collection<DeclareAnnotation>\n\n
    getDeclareAnnotationOnMethods()\n
    '''
def getDeclareTypeErrorOrWarning():
    '''returns Collection<DeclareTypeErrorOrWarning>\n\n
    getDeclareTypeErrorOrWarning()\n
    '''
def clearCaches():
    '''returns None\n\n
    clearCaches()\n
    '''
