def InstructionBranch():
    '''    public InstructionBranch(final short opcode, final InstructionHandle target)
    public InstructionBranch(final short opcode, final int index)
    public InstructionBranch(final short opcode)
    '''
def dump():
    '''    public void dump(final DataOutputStream out)
    '''
def toString():
    '''    public String toString(final boolean verbose)
    '''
def getIndex():
    '''    public final int getIndex()
    '''
def getTarget():
    '''    public InstructionHandle getTarget()
    '''
def setTarget():
    '''    public void setTarget(final InstructionHandle target)
    '''
def updateTarget():
    '''    public void updateTarget(final InstructionHandle oldHandle, final InstructionHandle newHandle)
    '''
def containsTarget():
    '''    public boolean containsTarget(final InstructionHandle ih)
    '''
def getType():
    '''    public Type getType(final ConstantPool cp)
    '''
def physicalSuccessor():
    '''    public InstructionHandle physicalSuccessor()
    '''
def isIfInstruction():
    '''    public boolean isIfInstruction()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
