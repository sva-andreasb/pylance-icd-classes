def ():
    '''returns IloOplFactory\n\n
    ()\n
    '''
def createOplCompiler():
    '''returns IloOplCompiler\n\n
    createOplCompiler()\n
    '''
def createCplex():
    '''returns IloCplex\n\n
    createCplex()\n
    '''
def createCP():
    '''returns IloCP\n\n
    createCP()\n
    '''
def createOplModelDefinition():
    '''returns IloOplModelDefinition\n\n
    createOplModelDefinition(final IloOplModelSource source, final IloOplErrorHandler handler)\n
    createOplModelDefinition(final IloOplModelSource source, final IloOplSettings settings)\n
    '''
def createOplProject():
    '''returns IloOplProject\n\n
    createOplProject(final String projectPath)\n
    createOplProject(final InputStream input, final String name)\n
    '''
def createOplRunConfiguration():
    '''returns IloOplRunConfiguration\n\n
    createOplRunConfiguration(final String modPath, final String datPath)\n
    createOplRunConfiguration(final String modPath)\n
    createOplRunConfiguration(final String modPath, final String[] datPaths)\n
    createOplRunConfiguration(final IloOplModelDefinition def)\n
    createOplRunConfiguration(final IloOplModelDefinition def, final IloOplDataElements dataElements)\n
    '''
def createOplErrorHandler():
    '''returns IloOplErrorHandler\n\n
    createOplErrorHandler(final OutputStream outs)\n
    createOplErrorHandler()\n
    '''
def createOplSettings():
    '''returns IloOplSettings\n\n
    createOplSettings(final IloOplErrorHandler handler)\n
    '''
def createOplModel():
    '''returns IloOplModel\n\n
    createOplModel(final IloOplModelDefinition definition, final IloCplex cplex)\n
    createOplModel(final IloOplModelDefinition definition, final IloCP cp)\n
    '''
def createOplModelSource():
    '''returns IloOplModelSource\n\n
    createOplModelSource(final String filename, final boolean compiled)\n
    createOplModelSource(final String filename)\n
    '''
def createOplDataElements():
    '''returns IloOplDataElements\n\n
    createOplDataElements()\n
    '''
def createOplModelSourceFromString():
    '''returns IloOplModelSource\n\n
    createOplModelSourceFromString(final String modelText, final String modelName)\n
    createOplModelSourceFromString(final String modelText, final String modelName, final boolean compiled)\n
    '''
def createOplModelSourceFromStream():
    '''returns IloOplModelSource\n\n
    createOplModelSourceFromStream(final InputStream modelStream, final String modelName)\n
    '''
def createOplDataSource():
    '''returns IloOplDataSource\n\n
    createOplDataSource(final String filename)\n
    '''
def createOplDataSourceFromString():
    '''returns IloOplDataSource\n\n
    createOplDataSourceFromString(final String dataText, final String name)\n
    '''
def createOplDataSourceFromStream():
    '''returns IloOplDataSource\n\n
    createOplDataSourceFromStream(final InputStream dataStream, final String name)\n
    '''
def createOplDataSerializer():
    '''returns IloOplDataSerializer\n\n
    createOplDataSerializer(final OutputStream outs)\n
    createOplDataSerializer(final IloOplSettings settings, final OutputStream outs)\n
    '''
def IloOplDataSerializer():
    '''returns IloOplDataSerializer\n\n
    IloOplDataSerializer(final IloOplSettings settings, final OutputStream outs, final boolean header)\n
    '''
def createOplCplexBasis():
    '''returns IloOplCplexBasis\n\n
    createOplCplexBasis()\n
    '''
def createOplCplexVectors():
    '''returns IloOplCplexVectors\n\n
    createOplCplexVectors()\n
    '''
def createOplRelaxationIterator():
    '''returns IloOplRelaxationIterator\n\n
    createOplRelaxationIterator(final IloOplModel model)\n
    '''
def createOplConflictIterator():
    '''returns IloOplConflictIterator\n\n
    createOplConflictIterator(final IloOplModel model)\n
    '''
def createOplProfiler():
    '''returns IloOplProfiler\n\n
    createOplProfiler()\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final OutputStream outputStream)\n
    '''
def setError():
    '''returns None\n\n
    setError(final OutputStream errorStream)\n
    '''
def setWarning():
    '''returns None\n\n
    setWarning(final OutputStream warningStream)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getEnv():
    '''returns IloEnv\n\n
    getEnv()\n
    '''
def getEnvImpl():
    '''returns IloEnv\n\n
    getEnvImpl()\n
    '''
def mapIndexArray():
    '''returns IloMapIndexArray\n\n
    mapIndexArray(final int initialSize)\n
    '''
def intRange():
    '''returns IloIntRange\n\n
    intRange(final int lb, final int ub)\n
    '''
def symbolSet():
    '''returns IloSymbolSet\n\n
    symbolSet()\n
    '''
def numSet():
    '''returns IloNumSet\n\n
    numSet()\n
    '''
def intSet():
    '''returns IloIntSet\n\n
    intSet()\n
    '''
