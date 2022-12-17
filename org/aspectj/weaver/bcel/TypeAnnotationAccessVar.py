def ():
    '''returns TypeAnnotationAccessVar\n\n
    (final ResolvedType type, final BcelVar theAnnotatedTargetIsStoredHere)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def createLoad():
    '''returns Instruction\n\n
    createLoad(final InstructionFactory fact)\n
    '''
def createStore():
    '''returns Instruction\n\n
    createStore(final InstructionFactory fact)\n
    '''
def createCopyFrom():
    '''returns InstructionList\n\n
    createCopyFrom(final InstructionFactory fact, final int oldSlot)\n
    '''
def appendLoad():
    '''returns None\n\n
    appendLoad(final InstructionList il, final InstructionFactory fact)\n
    '''
def createLoadInstructions():
    '''returns InstructionList\n\n
    createLoadInstructions(final ResolvedType toType, final InstructionFactory fact)\n
    '''
def appendLoadAndConvert():
    '''returns None\n\n
    appendLoadAndConvert(final InstructionList il, final InstructionFactory fact, final ResolvedType toType)\n
    '''
def insertLoad():
    '''returns None\n\n
    insertLoad(final InstructionList il, final InstructionFactory fact)\n
    '''
