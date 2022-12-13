def Instruction():
    '''    public Instruction(final short opcode, final short length)
    '''
def dump():
    '''    public void dump(final DataOutputStream out)
    '''
def getName():
    '''    public String getName()
    '''
def toString():
    '''    public String toString(final boolean verbose)
    public String toString()
    public String toString(final ConstantPool cp)
    '''
def copy():
    '''    public Instruction copy()
    '''
def readInstruction():
    '''    public static final Instruction readInstruction(final ByteSequence bytes)
    '''
def consumeStack():
    '''    public int consumeStack(final ConstantPoolGen cpg)
    '''
def produceStack():
    '''    public int produceStack(final ConstantPoolGen cpg)
    '''
def getOpcode():
    '''    public short getOpcode()
    '''
def getLength():
    '''    public int getLength()
    '''
def getComparator():
    '''    public static InstructionComparator getComparator()
    '''
def setComparator():
    '''    public static void setComparator(final InstructionComparator c)
    '''
def equals():
    '''    public boolean equals(final Object that)
    '''
