def InstructionList():
    '''    public InstructionList()
    public InstructionList(final Instruction i)
    public InstructionList(final byte[] code)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def findHandle():
    '''    public static InstructionHandle findHandle(final InstructionHandle[] ihs, final int[] pos, final int count, final int target)
    public static InstructionHandle findHandle(final InstructionHandle[] ihs, final int[] pos, final int count, final int target, final boolean returnClosestIfNoExactMatch)
    public InstructionHandle findHandle(final int pos)
    public InstructionHandle findHandle(final int pos, final InstructionHandle[] instructionArray)
    public InstructionHandle findHandle(final int pos, final InstructionHandle[] instructionArray, final boolean useClosestApproximationIfNoExactFound)
    '''
def getInstructionsAsArray():
    '''    public InstructionHandle[] getInstructionsAsArray()
    '''
def append():
    '''    public InstructionHandle append(final InstructionHandle appendTo, final InstructionList appendee)
    public InstructionHandle append(final Instruction i, final InstructionList il)
    public InstructionHandle append(final InstructionList il)
    public InstructionHandle append(final Instruction i)
    public BranchHandle append(final InstructionBranch i)
    public InstructionHandle append(final Instruction i, final Instruction j)
    public InstructionHandle append(final InstructionHandle ih, final Instruction i)
    public BranchHandle append(final InstructionHandle ih, final InstructionBranch i)
    '''
def appendDUP():
    '''    public InstructionHandle appendDUP()
    '''
def appendNOP():
    '''    public InstructionHandle appendNOP()
    '''
def appendPOP():
    '''    public InstructionHandle appendPOP()
    '''
def insert():
    '''    public InstructionHandle insert(final InstructionHandle ih, final InstructionList il)
    public InstructionHandle insert(final InstructionList il)
    public InstructionHandle insert(final Instruction i, final InstructionList il)
    public InstructionHandle insert(final Instruction i)
    public BranchHandle insert(final InstructionBranch i)
    public InstructionHandle insert(final Instruction i, final Instruction j)
    public InstructionHandle insert(final InstructionHandle ih, final Instruction i)
    public BranchHandle insert(final InstructionHandle ih, final InstructionBranch i)
    '''
def move():
    '''    public void move(final InstructionHandle start, final InstructionHandle end, final InstructionHandle target)
    public void move(final InstructionHandle ih, final InstructionHandle target)
    '''
def delete():
    '''    public void delete(final InstructionHandle ih)
    public void delete(final InstructionHandle from, final InstructionHandle to)
    public void delete(final Instruction from, final Instruction to)
    '''
def contains():
    '''    public boolean contains(final InstructionHandle i)
    public boolean contains(final Instruction i)
    '''
def setPositions():
    '''    public void setPositions()
    public void setPositions(final boolean check)
    '''
def getByteCode():
    '''    public byte[] getByteCode()
    '''
def getInstructions():
    '''    public Instruction[] getInstructions()
    '''
def toString():
    '''    public String toString()
    public String toString(final boolean verbose)
    '''
def iterator():
    '''    public Iterator iterator()
    '''
def next():
    '''    public Object next()
    '''
def remove():
    '''    public void remove()
    '''
def hasNext():
    '''    public boolean hasNext()
    '''
def getInstructionHandles():
    '''    public InstructionHandle[] getInstructionHandles()
    '''
def getInstructionPositions():
    '''    public int[] getInstructionPositions()
    '''
def copy():
    '''    public InstructionList copy()
    '''
def replaceConstantPool():
    '''    public void replaceConstantPool(final ConstantPool old_cp, final ConstantPool new_cp)
    '''
def dispose():
    '''    public void dispose()
    '''
def getStart():
    '''    public InstructionHandle getStart()
    '''
def getEnd():
    '''    public InstructionHandle getEnd()
    '''
def getLength():
    '''    public int getLength()
    '''
def size():
    '''    public int size()
    '''
def redirectBranches():
    '''    public void redirectBranches(final InstructionHandle old_target, final InstructionHandle new_target)
    '''
def redirectLocalVariables():
    '''    public void redirectLocalVariables(final LocalVariableGen[] lg, final InstructionHandle old_target, final InstructionHandle new_target)
    '''
def redirectExceptionHandlers():
    '''    public void redirectExceptionHandlers(final CodeExceptionGen[] exceptions, final InstructionHandle old_target, final InstructionHandle new_target)
    '''
