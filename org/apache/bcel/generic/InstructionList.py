def InstructionList():
    '''public InstructionList()
    public InstructionList(final Instruction i)
    public InstructionList(final BranchInstruction i)
    public InstructionList(final CompoundInstruction c)
    public InstructionList(final byte[] code)
    '''
def isEmpty():
    '''public boolean isEmpty()
    '''
def findHandle():
    '''public static InstructionHandle findHandle(final InstructionHandle[] ihs, final int[] pos, final int count, final int target)
    public InstructionHandle findHandle(final int pos)
    '''
def append():
    '''public InstructionHandle append(final InstructionHandle ih, final InstructionList il)
    public InstructionHandle append(final Instruction i, final InstructionList il)
    public InstructionHandle append(final InstructionList il)
    public InstructionHandle append(final Instruction i)
    public BranchHandle append(final BranchInstruction i)
    public InstructionHandle append(final Instruction i, final Instruction j)
    public InstructionHandle append(final Instruction i, final CompoundInstruction c)
    public InstructionHandle append(final CompoundInstruction c)
    public InstructionHandle append(final InstructionHandle ih, final CompoundInstruction c)
    public InstructionHandle append(final InstructionHandle ih, final Instruction i)
    public BranchHandle append(final InstructionHandle ih, final BranchInstruction i)
    '''
def insert():
    '''public InstructionHandle insert(final InstructionHandle ih, final InstructionList il)
    public InstructionHandle insert(final InstructionList il)
    public InstructionHandle insert(final Instruction i, final InstructionList il)
    public InstructionHandle insert(final Instruction i)
    public BranchHandle insert(final BranchInstruction i)
    public InstructionHandle insert(final Instruction i, final Instruction j)
    public InstructionHandle insert(final Instruction i, final CompoundInstruction c)
    public InstructionHandle insert(final CompoundInstruction c)
    public InstructionHandle insert(final InstructionHandle ih, final Instruction i)
    public InstructionHandle insert(final InstructionHandle ih, final CompoundInstruction c)
    public BranchHandle insert(final InstructionHandle ih, final BranchInstruction i)
    '''
def move():
    '''public void move(final InstructionHandle start, final InstructionHandle end, final InstructionHandle target)
    public void move(final InstructionHandle ih, final InstructionHandle target)
    '''
def delete():
    '''public void delete(final InstructionHandle ih)
    public void delete(final Instruction i)
    public void delete(final InstructionHandle from, final InstructionHandle to)
    public void delete(final Instruction from, final Instruction to)
    '''
def contains():
    '''public boolean contains(final InstructionHandle i)
    public boolean contains(final Instruction i)
    '''
def setPositions():
    '''public void setPositions()
    public void setPositions(final boolean check)
    '''
def getByteCode():
    '''public byte[] getByteCode()
    '''
def getInstructions():
    '''public Instruction[] getInstructions()
    '''
def toString():
    '''public String toString()
    public String toString(final boolean verbose)
    '''
def iterator():
    '''public Iterator iterator()
    '''
def next():
    '''public Object next()
    '''
def remove():
    '''public void remove()
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def getInstructionHandles():
    '''public InstructionHandle[] getInstructionHandles()
    '''
def getInstructionPositions():
    '''public int[] getInstructionPositions()
    '''
def copy():
    '''public InstructionList copy()
    '''
def replaceConstantPool():
    '''public void replaceConstantPool(final ConstantPoolGen old_cp, final ConstantPoolGen new_cp)
    '''
def dispose():
    '''public void dispose()
    '''
def getStart():
    '''public InstructionHandle getStart()
    '''
def getEnd():
    '''public InstructionHandle getEnd()
    '''
def getLength():
    '''public int getLength()
    '''
def size():
    '''public int size()
    '''
def redirectBranches():
    '''public void redirectBranches(final InstructionHandle old_target, final InstructionHandle new_target)
    '''
def redirectLocalVariables():
    '''public void redirectLocalVariables(final LocalVariableGen[] lg, final InstructionHandle old_target, final InstructionHandle new_target)
    '''
def redirectExceptionHandlers():
    '''public void redirectExceptionHandlers(final CodeExceptionGen[] exceptions, final InstructionHandle old_target, final InstructionHandle new_target)
    '''
def addObserver():
    '''public void addObserver(final InstructionListObserver o)
    '''
def removeObserver():
    '''public void removeObserver(final InstructionListObserver o)
    '''
def update():
    '''public void update()
    '''
