def ():
    '''returns InstructionList\n\n
    ()\n
    (final Instruction i)\n
    (final BranchInstruction i)\n
    (final CompoundInstruction c)\n
    (final byte[] code)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def findHandle():
    '''returns InstructionHandle\n\n
    findHandle(final int pos)\n
    '''
def append():
    '''returns BranchHandle\n\n
    append(final InstructionHandle ih, final InstructionList il)\n
    append(final Instruction i, final InstructionList il)\n
    append(final InstructionList il)\n
    append(final Instruction i)\n
    append(final BranchInstruction i)\n
    append(final Instruction i, final Instruction j)\n
    append(final Instruction i, final CompoundInstruction c)\n
    append(final CompoundInstruction c)\n
    append(final InstructionHandle ih, final CompoundInstruction c)\n
    append(final InstructionHandle ih, final Instruction i)\n
    append(final InstructionHandle ih, final BranchInstruction i)\n
    '''
def insert():
    '''returns BranchHandle\n\n
    insert(final InstructionHandle ih, final InstructionList il)\n
    insert(final InstructionList il)\n
    insert(final Instruction i, final InstructionList il)\n
    insert(final Instruction i)\n
    insert(final BranchInstruction i)\n
    insert(final Instruction i, final Instruction j)\n
    insert(final Instruction i, final CompoundInstruction c)\n
    insert(final CompoundInstruction c)\n
    insert(final InstructionHandle ih, final Instruction i)\n
    insert(final InstructionHandle ih, final CompoundInstruction c)\n
    insert(final InstructionHandle ih, final BranchInstruction i)\n
    '''
def move():
    '''returns None\n\n
    move(final InstructionHandle start, final InstructionHandle end, final InstructionHandle target)\n
    move(final InstructionHandle ih, final InstructionHandle target)\n
    '''
def delete():
    '''returns None\n\n
    delete(final InstructionHandle ih)\n
    delete(final Instruction i)\n
    delete(final InstructionHandle from, final InstructionHandle to)\n
    delete(final Instruction from, final Instruction to)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final InstructionHandle i)\n
    contains(final Instruction i)\n
    '''
def setPositions():
    '''returns None\n\n
    setPositions()\n
    setPositions(final boolean check)\n
    '''
def getByteCode():
    '''returns byte[]\n\n
    getByteCode()\n
    '''
def getInstructions():
    '''returns Instruction[]\n\n
    getInstructions()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final boolean verbose)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def getInstructionHandles():
    '''returns InstructionHandle[]\n\n
    getInstructionHandles()\n
    '''
def getInstructionPositions():
    '''returns int[]\n\n
    getInstructionPositions()\n
    '''
def copy():
    '''returns InstructionList\n\n
    copy()\n
    '''
def replaceConstantPool():
    '''returns None\n\n
    replaceConstantPool(final ConstantPoolGen old_cp, final ConstantPoolGen new_cp)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getStart():
    '''returns InstructionHandle\n\n
    getStart()\n
    '''
def getEnd():
    '''returns InstructionHandle\n\n
    getEnd()\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def redirectBranches():
    '''returns None\n\n
    redirectBranches(final InstructionHandle old_target, final InstructionHandle new_target)\n
    '''
def redirectLocalVariables():
    '''returns None\n\n
    redirectLocalVariables(final LocalVariableGen[] lg, final InstructionHandle old_target, final InstructionHandle new_target)\n
    '''
def redirectExceptionHandlers():
    '''returns None\n\n
    redirectExceptionHandlers(final CodeExceptionGen[] exceptions, final InstructionHandle old_target, final InstructionHandle new_target)\n
    '''
def addObserver():
    '''returns None\n\n
    addObserver(final InstructionListObserver o)\n
    '''
def removeObserver():
    '''returns None\n\n
    removeObserver(final InstructionListObserver o)\n
    '''
def update():
    '''returns None\n\n
    update()\n
    '''
