def ExportObject():
    '''public ExportObject()
    '''
def getObjectValue():
    '''public static Object getObjectValue(final Element objectElement, final String columnName)
    public static Object getObjectValue(final XMLObject objectElement, final String columnName)
    public static Object getObjectValue(final Element columnElement)
    public static Object getObjectValue(final XMLColumn columnElement)
    '''
def getObjectData():
    '''public void getObjectData(final Connection c, final Element objectElement, final Element targetParentElement, final int depth)
    '''
def getObjectWhereClause():
    '''public String getObjectWhereClause(final Connection c, final String tableName)
    '''
def exportFiles():
    '''public void exportFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
    '''
def exportToFile():
    '''public void exportToFile(final String structureFilename, final String whereClause, final String outFileName)
    public void exportToFile(final String structureFilename, final String inWhereClause, final String outFileName, final ExportOptions options, final IProgressMonitor monitor, final MaximoResolver maximoResolver)
    public void exportToFile(final String structureFilename, final String inWhereClause, final String outFileName, final MaximoResolver maximoResolver)
    '''
def exportToDocument():
    '''public Document exportToDocument(final String structureFilename, final String inWhereClause, final MaximoResolver maximoResolver)
    '''
def main():
    '''public static void main(final String[] args)
    '''
def runExtension():
    '''public boolean runExtension(final String extensionNames, final int mode, final Connection con, final Element e)
    '''
def setUpdate():
    '''public void setUpdate(final boolean shouldUpdate)
    '''
def setAddKeyColumns():
    '''public void setAddKeyColumns(final boolean shouldAddKeyColumns)
    '''
def setUserDefinedKeyColumns():
    '''public void setUserDefinedKeyColumns(final boolean shouldUse)
    '''
