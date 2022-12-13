def JsonResultsReader():
    '''public JsonResultsReader(final File jsonResultsFile)
    '''
def getTablesName():
    '''public List<String> getTablesName()
    '''
def getTablesDescriptor():
    '''public List<TableDescriptor> getTablesDescriptor()
    '''
def getTableDescriptor():
    '''public TableDescriptor getTableDescriptor(final String tableName)
    '''
def getAllTablesRowsIterator():
    '''public TableRowIterator getAllTablesRowsIterator()
    '''
def TableRowIteratorImpl():
    '''public TableRowIteratorImpl(final JsonResultsReader reader)
    '''
def hasNext():
    '''public boolean hasNext()
    '''
def next():
    '''public TableRow next()
    '''
def TableRowImpl():
    '''public TableRowImpl(final TableDescriptor tableDesc)
    '''
def getTableDesc():
    '''public TableDescriptor getTableDesc()
    '''
def setColumnValue():
    '''public void setColumnValue(final String columnName, final Object value)
    '''
def getColumnValue():
    '''public Object getColumnValue(final int index)
    public Object getColumnValue(final String columnName)
    '''
def ColumnDescriptorImpl():
    '''public ColumnDescriptorImpl(final int index, final String name, final Class<T> type)
    '''
def getName():
    '''public String getName()
    public String getName()
    '''
def getIndex():
    '''public int getIndex()
    '''
def TableDescriptorImpl():
    '''public TableDescriptorImpl(final String name)
    '''
def addColumnDescriptor():
    '''public void addColumnDescriptor(final ColumnDescriptor<?> desc)
    '''
def getColumnsName():
    '''public List<String> getColumnsName()
    '''
