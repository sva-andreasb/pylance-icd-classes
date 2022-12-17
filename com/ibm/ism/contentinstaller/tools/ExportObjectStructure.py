def ():
    '''returns ExportObjectStructure\n\n
    ()\n
    (final MaximoResolver mxeResolver)\n
    '''
def getObjects():
    '''returns None\n\n
    getObjects(final Connection c)\n
    '''
def getSequences():
    '''returns None\n\n
    getSequences(final Connection c, final String tablename, final Element parentElement)\n
    '''
def getParentValue():
    '''returns None\n\n
    getParentValue(final Element element, final String columnName, String parentColumnName)\n
    '''
def getParentSequence():
    '''returns None\n\n
    getParentSequence(final Connection c, final Element element, final String parentTable, final String columnName)\n
    '''
def listRelatedTables():
    '''returns None\n\n
    listRelatedTables(final Connection c, final Element parentElement, final int indent)\n
    '''
def exportObjectStructure():
    '''returns Document\n\n
    exportObjectStructure(final String objectName, final int maxDepth, final String outFileName, final boolean addKeyColumns)\n
    exportObjectStructure(String objectName, final int maxDepth, final boolean addKeyColumns)\n
    '''
