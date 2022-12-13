def LocalVariableTable():
    '''public LocalVariableTable(final LocalVariableTable c)
    public LocalVariableTable(final int name_index, final int length, final LocalVariable[] local_variable_table, final ConstantPool constant_pool)
    '''
def accept():
    '''public void accept(final Visitor v)
    '''
def dump():
    '''public final void dump(final DataOutputStream file)
    '''
def getLocalVariableTable():
    '''public final LocalVariable[] getLocalVariableTable()
    '''
def getLocalVariable():
    '''public final LocalVariable getLocalVariable(final int index)
    public final LocalVariable getLocalVariable(final int index, final int pc)
    '''
def setLocalVariableTable():
    '''public final void setLocalVariableTable(final LocalVariable[] local_variable_table)
    '''
def toString():
    '''public final String toString()
    '''
def copy():
    '''public Attribute copy(final ConstantPool _constant_pool)
    '''
def getTableLength():
    '''public final int getTableLength()
    '''
