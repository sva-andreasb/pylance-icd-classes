def Instruction():
    '''    public Instruction(final short opcode)
    '''
def dump():
    '''    public void dump(final DataOutputStream out)
    '''
def getName():
    '''    public String getName()
    '''
def copy():
    '''    public final Instruction copy()
    '''
def readInstruction():
    '''    public static final Instruction readInstruction(final ByteSequence bytes)
    '''
def consumeStack():
    '''    public int consumeStack(final ConstantPool cpg)
    '''
def produceStack():
    '''    public int produceStack(final ConstantPool cpg)
    '''
def getOpcode():
    '''    public short getOpcode()
    '''
def getLength():
    '''    public int getLength()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def getType():
    '''    public Type getType()
    public Type getType(final ConstantPool cp)
    '''
def getValue():
    '''    public Number getValue()
    public Object getValue(final ConstantPool cpg)
    '''
def getIndex():
    '''    public int getIndex()
    '''
def setIndex():
    '''    public void setIndex(final int i)
    '''
def isLoadInstruction():
    '''    public boolean isLoadInstruction()
    '''
def isASTORE():
    '''    public boolean isASTORE()
    '''
def isALOAD():
    '''    public boolean isALOAD()
    '''
def isStoreInstruction():
    '''    public boolean isStoreInstruction()
    '''
def isJsrInstruction():
    '''    public boolean isJsrInstruction()
    '''
def isConstantInstruction():
    '''    public boolean isConstantInstruction()
    '''
def isConstantPoolInstruction():
    '''    public boolean isConstantPoolInstruction()
    '''
def isStackProducer():
    '''    public boolean isStackProducer()
    '''
def isStackConsumer():
    '''    public boolean isStackConsumer()
    '''
def isIndexedInstruction():
    '''    public boolean isIndexedInstruction()
    '''
def isArrayCreationInstruction():
    '''    public boolean isArrayCreationInstruction()
    '''
def getLoadClassType():
    '''    public ObjectType getLoadClassType(final ConstantPool cpg)
    '''
def isReturnInstruction():
    '''    public boolean isReturnInstruction()
    '''
def isLocalVariableInstruction():
    '''    public boolean isLocalVariableInstruction()
    '''
def toString():
    '''    public String toString(final boolean verbose)
    public String toString()
    '''
