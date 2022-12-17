def ():
    '''returns SqlStagePatternTable\n\n
    (final String tableName)\n
    (final Node graphNode, final Node subject, final QuadBlock tableQuads)\n
    '''
def add():
    '''returns None\n\n
    add(final Node property, final String colname)\n
    '''
def hasColumn():
    '''returns boolean\n\n
    hasColumn(final String colName)\n
    '''
def colNames():
    '''returns Iterator<String>\n\n
    colNames()\n
    '''
def trigger():
    '''returns boolean\n\n
    trigger(final Quad quad)\n
    '''
def process():
    '''returns SqlStage\n\n
    process(final int i, final QuadBlock quadBlock)\n
    '''
def build():
    '''returns SqlNode\n\n
    build(final SDBRequest request, final SlotCompiler slotCompiler)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def output():
    '''returns None\n\n
    output(final IndentedWriter out)\n
    '''
