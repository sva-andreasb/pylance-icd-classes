def ():
    '''returns ExceptionRange\n\n
    (final InstructionList body, final UnresolvedType exceptionType, final int priority)\n
    (final InstructionList body, final UnresolvedType exceptionType, final boolean insideExisting)\n
    '''
def associateWithTargets():
    '''returns None\n\n
    associateWithTargets(final InstructionHandle start, final InstructionHandle end, final InstructionHandle handler)\n
    '''
def getHandler():
    '''returns InstructionHandle\n\n
    getHandler()\n
    '''
def getCatchType():
    '''returns UnresolvedType\n\n
    getCatchType()\n
    '''
def getPriority():
    '''returns int\n\n
    getPriority()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def updateTarget():
    '''returns None\n\n
    updateTarget(final InstructionHandle oldIh, final InstructionHandle newIh, final InstructionList newBody)\n
    '''
