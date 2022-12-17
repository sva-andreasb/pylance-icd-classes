def ():
    '''returns AnnotationAccessVar\n\n
    (final BcelShadow shadow, final Shadow.Kind kind, final ResolvedType annotationType, final UnresolvedType theTargetIsStoredHere, final Member sig, final boolean isWithin)\n
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
def appendLoadAndConvert():
    '''returns None\n\n
    appendLoadAndConvert(final InstructionList il, final InstructionFactory fact, final ResolvedType toType)\n
    '''
def insertLoad():
    '''returns None\n\n
    insertLoad(final InstructionList il, final InstructionFactory fact)\n
    '''
def getMember():
    '''returns Member\n\n
    getMember()\n
    '''
def getAccessorForValue():
    '''returns Var\n\n
    getAccessorForValue(final ResolvedType valueType, final String formalName)\n
    '''
