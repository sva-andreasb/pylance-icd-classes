def Instruction():
'''public Instruction(final short opcode)
'''
pass
def dump():
'''public void dump(final DataOutputStream out)
'''
pass
def getName():
'''public String getName()
'''
pass
def copy():
'''public final Instruction copy()
'''
pass
def readInstruction():
'''public static final Instruction readInstruction(final ByteSequence bytes)
'''
pass
def consumeStack():
'''public int consumeStack(final ConstantPool cpg)
'''
pass
def produceStack():
'''public int produceStack(final ConstantPool cpg)
'''
pass
def getOpcode():
'''public short getOpcode()
'''
pass
def getLength():
'''public int getLength()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def getType():
'''public Type getType()
public Type getType(final ConstantPool cp)
'''
pass
def getValue():
'''public Number getValue()
public Object getValue(final ConstantPool cpg)
'''
pass
def getIndex():
'''public int getIndex()
'''
pass
def setIndex():
'''public void setIndex(final int i)
'''
pass
def isLoadInstruction():
'''public boolean isLoadInstruction()
'''
pass
def isASTORE():
'''public boolean isASTORE()
'''
pass
def isALOAD():
'''public boolean isALOAD()
'''
pass
def isStoreInstruction():
'''public boolean isStoreInstruction()
'''
pass
def isJsrInstruction():
'''public boolean isJsrInstruction()
'''
pass
def isConstantInstruction():
'''public boolean isConstantInstruction()
'''
pass
def isConstantPoolInstruction():
'''public boolean isConstantPoolInstruction()
'''
pass
def isStackProducer():
'''public boolean isStackProducer()
'''
pass
def isStackConsumer():
'''public boolean isStackConsumer()
'''
pass
def isIndexedInstruction():
'''public boolean isIndexedInstruction()
'''
pass
def isArrayCreationInstruction():
'''public boolean isArrayCreationInstruction()
'''
pass
def getLoadClassType():
'''public ObjectType getLoadClassType(final ConstantPool cpg)
'''
pass
def isReturnInstruction():
'''public boolean isReturnInstruction()
'''
pass
def isLocalVariableInstruction():
'''public boolean isLocalVariableInstruction()
'''
pass
def toString():
'''public String toString(final boolean verbose)
public String toString()
'''
pass
