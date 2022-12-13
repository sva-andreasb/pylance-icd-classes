def PatternTable():
    '''public PatternTable(final String tableName)
    '''
def add():
    '''public void add(final Node property, final String colname)
    '''
def getCols():
    '''public Map<Node, String> getCols()
    '''
def hasColumn():
    '''public boolean hasColumn(final String colName)
    '''
def colNames():
    '''public Iterator<String> colNames()
    '''
def trigger():
    '''public boolean trigger(final Quad quad)
    '''
def process():
    '''public SqlStage process(final int i, final QuadBlock quadBlock)
    '''
def SqlStagePatternTable():
    '''public SqlStagePatternTable(final Node graphNode, final Node subject, final QuadBlock tableQuads)
    '''
def build():
    '''public SqlNode build(final SDBRequest request, final SlotCompiler slotCompiler)
    '''
def toString():
    '''public String toString()
    '''
def output():
    '''public void output(final IndentedWriter out)
    '''
