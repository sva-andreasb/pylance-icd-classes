def ():
    '''returns CrosscuttingMembersSet\n\n
    (final World world)\n
    '''
def addOrReplaceAspect():
    '''returns boolean\n\n
    addOrReplaceAspect(final ResolvedType aspectType)\n
    addOrReplaceAspect(final ResolvedType aspectType, final boolean inWeavingPhase)\n
    '''
def addAdviceLikeDeclares():
    '''returns None\n\n
    addAdviceLikeDeclares(final ResolvedType aspectType)\n
    '''
def deleteAspect():
    '''returns boolean\n\n
    deleteAspect(final UnresolvedType aspectType)\n
    '''
def containsAspect():
    '''returns boolean\n\n
    containsAspect(final UnresolvedType aspectType)\n
    '''
def addFixedCrosscuttingMembers():
    '''returns None\n\n
    addFixedCrosscuttingMembers(final ResolvedType aspectType)\n
    '''
def getShadowMungers():
    '''returns List<ShadowMunger>\n\n
    getShadowMungers()\n
    '''
def getTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getTypeMungers()\n
    '''
def getTypeMungersOfKind():
    '''returns List<ConcreteTypeMunger>\n\n
    getTypeMungersOfKind(final ResolvedTypeMunger.Kind kind)\n
    '''
def getLateTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getLateTypeMungers()\n
    '''
def getDeclareSofts():
    '''returns List<DeclareSoft>\n\n
    getDeclareSofts()\n
    '''
def getDeclareParents():
    '''returns List<DeclareParents>\n\n
    getDeclareParents()\n
    '''
def getDeclareAnnotationOnTypes():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnTypes()\n
    '''
def getDeclareAnnotationOnFields():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnFields()\n
    '''
def getDeclareAnnotationOnMethods():
    '''returns List<DeclareAnnotation>\n\n
    getDeclareAnnotationOnMethods()\n
    '''
def getDeclareTypeEows():
    '''returns List<DeclareTypeErrorOrWarning>\n\n
    getDeclareTypeEows()\n
    '''
def getDeclareDominates():
    '''returns List<Declare>\n\n
    getDeclareDominates()\n
    '''
def findAspectDeclaringParents():
    '''returns ResolvedType\n\n
    findAspectDeclaringParents(final DeclareParents p)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def hasChangedSinceLastReset():
    '''returns boolean\n\n
    hasChangedSinceLastReset()\n
    '''
def recordNecessaryCheck():
    '''returns None\n\n
    recordNecessaryCheck(final IVerificationRequired verification)\n
    '''
def verify():
    '''returns None\n\n
    verify()\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream stream)\n
    '''
