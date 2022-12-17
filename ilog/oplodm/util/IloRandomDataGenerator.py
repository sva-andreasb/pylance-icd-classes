COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns DefaultValueGenerator\n\n
    ()\n
    ()\n
    '''
def getGenerator():
    '''returns ValueGenerator\n\n
    getGenerator()\n
    '''
def setGenerator():
    '''returns None\n\n
    setGenerator(final ValueGenerator generator)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def setRowCount():
    '''returns None\n\n
    setRowCount(final int rowCount)\n
    '''
def getMaxRowCount():
    '''returns int\n\n
    getMaxRowCount()\n
    '''
def setMaxRowCount():
    '''returns None\n\n
    setMaxRowCount(final int maxRowCount)\n
    '''
def newTableProvider():
    '''returns IloTableProvider\n\n
    newTableProvider(final IloNameSpaceProfileManager nspm)\n
    newTableProvider(final URL relationalModel)\n
    newTableProvider(final InputStream relationalModel, final String locDescription)\n
    '''
def populate():
    '''returns None\n\n
    populate(final IloTableContainer tables)\n
    '''
def execute():
    '''returns None\n\n
    execute(final IloTableId tableId)\n
    execute(final IloTableId tableId)\n
    execute(final IloTableId tableId)\n
    execute(final IloTableId tableId)\n
    '''
def generateValue():
    '''returns Serializable\n\n
    generateValue(final ilog.odm.datasvc.IloTable table, final ilog.odm.datasvc.IloRow row, final int rowIndex, final IloColumn column, final int columnIndex, final boolean isPrimaryKey, final IloColumn targetColumn)\n
    generateValue(final ilog.odm.datasvc.IloTable table, final ilog.odm.datasvc.IloRow row, final int rowIndex, final IloColumn column, final int columnIndex, final boolean isPrimaryKey, final IloColumn targetColumn)\n
    '''
