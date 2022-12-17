def ():
    '''returns BcelVar\n\n
    (final ResolvedType type, final int slot)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getSlot():
    '''returns int\n\n
    getSlot()\n
    '''
def createLoad():
    '''returns Instruction\n\n
    createLoad(final InstructionFactory fact)\n
    '''
def createStore():
    '''returns Instruction\n\n
    createStore(final InstructionFactory fact)\n
    '''
def appendStore():
    '''returns None\n\n
    appendStore(final InstructionList il, final InstructionFactory fact)\n
    '''
def appendLoad():
    '''returns None\n\n
    appendLoad(final InstructionList il, final InstructionFactory fact)\n
    '''
def appendLoadAndConvert():
    '''returns None\n\n
    appendLoadAndConvert(final InstructionList il, final InstructionFactory fact, final ResolvedType toType)\n
    '''
def insertLoad():
    '''returns None\n\n
    insertLoad(final InstructionList il, final InstructionFactory fact)\n
    '''
def createCopyFrom():
    '''returns InstructionList\n\n
    createCopyFrom(final InstructionFactory fact, final int oldSlot)\n
    '''
def getPositionInAroundState():
    '''returns int\n\n
    getPositionInAroundState()\n
    '''
def setPositionInAroundState():
    '''returns None\n\n
    setPositionInAroundState(final int positionInAroundState)\n
    '''
