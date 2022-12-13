def LocalVariableTable():
'''public LocalVariableTable(final LocalVariableTable c)
public LocalVariableTable(final int name_index, final int length, final LocalVariable[] local_variable_table, final ConstantPool constant_pool)
'''
pass
def accept():
'''public void accept(final Visitor v)
'''
pass
def dump():
'''public final void dump(final DataOutputStream file)
'''
pass
def getLocalVariableTable():
'''public final LocalVariable[] getLocalVariableTable()
'''
pass
def getLocalVariable():
'''public final LocalVariable getLocalVariable(final int index)
public final LocalVariable getLocalVariable(final int index, final int pc)
'''
pass
def setLocalVariableTable():
'''public final void setLocalVariableTable(final LocalVariable[] local_variable_table)
'''
pass
def toString():
'''public final String toString()
'''
pass
def copy():
'''public Attribute copy(final ConstantPool _constant_pool)
'''
pass
def getTableLength():
'''public final int getTableLength()
'''
pass
