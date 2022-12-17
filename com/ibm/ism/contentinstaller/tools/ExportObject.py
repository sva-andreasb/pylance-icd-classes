def ():
    '''returns ExportObject\n\n
    ()\n
    '''
def getObjectData():
    '''returns None\n\n
    getObjectData(final Connection c, final Element objectElement, final Element targetParentElement, final int depth)\n
    '''
def getObjectWhereClause():
    '''returns String\n\n
    getObjectWhereClause(final Connection c, final String tableName)\n
    '''
def exportFiles():
    '''returns None\n\n
    exportFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)\n
    '''
def exportToFile():
    '''returns None\n\n
    exportToFile(final String structureFilename, final String whereClause, final String outFileName)\n
    exportToFile(final String structureFilename, final String inWhereClause, final String outFileName, final ExportOptions options, final IProgressMonitor monitor, final MaximoResolver maximoResolver)\n
    exportToFile(final String structureFilename, final String inWhereClause, final String outFileName, final MaximoResolver maximoResolver)\n
    '''
def exportToDocument():
    '''returns Document\n\n
    exportToDocument(final String structureFilename, final String inWhereClause, final MaximoResolver maximoResolver)\n
    '''
def runExtension():
    '''returns boolean\n\n
    runExtension(final String extensionNames, final int mode, final Connection con, final Element e)\n
    '''
def setUpdate():
    '''returns None\n\n
    setUpdate(final boolean shouldUpdate)\n
    '''
def setAddKeyColumns():
    '''returns None\n\n
    setAddKeyColumns(final boolean shouldAddKeyColumns)\n
    '''
def setUserDefinedKeyColumns():
    '''returns None\n\n
    setUserDefinedKeyColumns(final boolean shouldUse)\n
    '''
