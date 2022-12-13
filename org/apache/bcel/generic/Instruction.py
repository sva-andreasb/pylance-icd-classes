def Instruction():
'''public Instruction(final short opcode, final short length)
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
def toString():
'''public String toString(final boolean verbose)
public String toString()
public String toString(final ConstantPool cp)
'''
pass
def copy():
'''public Instruction copy()
'''
pass
def readInstruction():
'''public static final Instruction readInstruction(final ByteSequence bytes)
'''
pass
def consumeStack():
'''public int consumeStack(final ConstantPoolGen cpg)
'''
pass
def produceStack():
'''public int produceStack(final ConstantPoolGen cpg)
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
def getComparator():
'''public static InstructionComparator getComparator()
'''
pass
def setComparator():
'''public static void setComparator(final InstructionComparator c)
'''
pass
def equals():
'''public boolean equals(final Object that)
'''
pass
