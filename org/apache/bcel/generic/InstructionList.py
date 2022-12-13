def InstructionList():
'''public InstructionList()
public InstructionList(final Instruction i)
public InstructionList(final BranchInstruction i)
public InstructionList(final CompoundInstruction c)
public InstructionList(final byte[] code)
'''
pass
def isEmpty():
'''public boolean isEmpty()
'''
pass
def findHandle():
'''public static InstructionHandle findHandle(final InstructionHandle[] ihs, final int[] pos, final int count, final int target)
public InstructionHandle findHandle(final int pos)
'''
pass
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
pass
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
pass
def move():
'''public void move(final InstructionHandle start, final InstructionHandle end, final InstructionHandle target)
public void move(final InstructionHandle ih, final InstructionHandle target)
'''
pass
def delete():
'''public void delete(final InstructionHandle ih)
public void delete(final Instruction i)
public void delete(final InstructionHandle from, final InstructionHandle to)
public void delete(final Instruction from, final Instruction to)
'''
pass
def contains():
'''public boolean contains(final InstructionHandle i)
public boolean contains(final Instruction i)
'''
pass
def setPositions():
'''public void setPositions()
public void setPositions(final boolean check)
'''
pass
def getByteCode():
'''public byte[] getByteCode()
'''
pass
def getInstructions():
'''public Instruction[] getInstructions()
'''
pass
def toString():
'''public String toString()
public String toString(final boolean verbose)
'''
pass
def iterator():
'''public Iterator iterator()
'''
pass
def next():
'''public Object next()
'''
pass
def remove():
'''public void remove()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def getInstructionHandles():
'''public InstructionHandle[] getInstructionHandles()
'''
pass
def getInstructionPositions():
'''public int[] getInstructionPositions()
'''
pass
def copy():
'''public InstructionList copy()
'''
pass
def replaceConstantPool():
'''public void replaceConstantPool(final ConstantPoolGen old_cp, final ConstantPoolGen new_cp)
'''
pass
def dispose():
'''public void dispose()
'''
pass
def getStart():
'''public InstructionHandle getStart()
'''
pass
def getEnd():
'''public InstructionHandle getEnd()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def size():
'''public int size()
'''
pass
def redirectBranches():
'''public void redirectBranches(final InstructionHandle old_target, final InstructionHandle new_target)
'''
pass
def redirectLocalVariables():
'''public void redirectLocalVariables(final LocalVariableGen[] lg, final InstructionHandle old_target, final InstructionHandle new_target)
'''
pass
def redirectExceptionHandlers():
'''public void redirectExceptionHandlers(final CodeExceptionGen[] exceptions, final InstructionHandle old_target, final InstructionHandle new_target)
'''
pass
def addObserver():
'''public void addObserver(final InstructionListObserver o)
'''
pass
def removeObserver():
'''public void removeObserver(final InstructionListObserver o)
'''
pass
def update():
'''public void update()
'''
pass
