def ():
    '''returns Entry\n\n
    (final boolean reweavable)\n
    (final UnresolvedType aspectType, final ResolvedTypeMunger typeMunger)\n
    '''
def write():
    '''returns None\n\n
    write(final CompressingDataOutputStream s)\n
    '''
def addConcreteMunger():
    '''returns None\n\n
    addConcreteMunger(final ConcreteTypeMunger munger)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getTypeMungers():
    '''returns List<ConcreteTypeMunger>\n\n
    getTypeMungers(final ResolvedType onType)\n
    '''
def isOldStyle():
    '''returns boolean\n\n
    isOldStyle()\n
    '''
def getUnwovenClassFileData():
    '''returns byte[]\n\n
    getUnwovenClassFileData(final byte[] wovenClassFile)\n
    '''
def setUnwovenClassFileData():
    '''returns None\n\n
    setUnwovenClassFileData(final byte[] data)\n
    '''
def isReweavable():
    '''returns boolean\n\n
    isReweavable()\n
    '''
def setReweavable():
    '''returns None\n\n
    setReweavable(final boolean rw)\n
    '''
def addAspectsAffectingType():
    '''returns None\n\n
    addAspectsAffectingType(final Collection<String> aspects)\n
    '''
def addAspectAffectingType():
    '''returns None\n\n
    addAspectAffectingType(final String aspectSignature)\n
    '''
def getAspectsAffectingType():
    '''returns Set<String>\n\n
    getAspectsAffectingType()\n
    '''
def replaceKeyWithDiff():
    '''returns byte[]\n\n
    replaceKeyWithDiff(byte[] wovenClassFile)\n
    '''
def isAspectAlreadyApplied():
    '''returns boolean\n\n
    isAspectAlreadyApplied(final ResolvedType someAspect)\n
    '''
