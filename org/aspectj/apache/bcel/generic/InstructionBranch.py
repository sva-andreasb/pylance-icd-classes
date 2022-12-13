def InstructionBranch():
'''public InstructionBranch(final short opcode, final InstructionHandle target)
public InstructionBranch(final short opcode, final int index)
public InstructionBranch(final short opcode)
'''
pass
def dump():
'''public void dump(final DataOutputStream out)
'''
pass
def toString():
'''public String toString(final boolean verbose)
'''
pass
def getIndex():
'''public final int getIndex()
'''
pass
def getTarget():
'''public InstructionHandle getTarget()
'''
pass
def setTarget():
'''public void setTarget(final InstructionHandle target)
'''
pass
def updateTarget():
'''public void updateTarget(final InstructionHandle oldHandle, final InstructionHandle newHandle)
'''
pass
def containsTarget():
'''public boolean containsTarget(final InstructionHandle ih)
'''
pass
def getType():
'''public Type getType(final ConstantPool cp)
'''
pass
def physicalSuccessor():
'''public InstructionHandle physicalSuccessor()
'''
pass
def isIfInstruction():
'''public boolean isIfInstruction()
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
