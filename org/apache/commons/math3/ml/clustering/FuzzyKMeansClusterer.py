def ():
    '''returns FuzzyKMeansClusterer\n\n
    (final int k, final double fuzziness)\n
    (final int k, final double fuzziness, final int maxIterations, final DistanceMeasure measure)\n
    (final int k, final double fuzziness, final int maxIterations, final DistanceMeasure measure, final double epsilon, final RandomGenerator random)\n
    '''
def getK():
    '''returns int\n\n
    getK()\n
    '''
def getFuzziness():
    '''returns double\n\n
    getFuzziness()\n
    '''
def getMaxIterations():
    '''returns int\n\n
    getMaxIterations()\n
    '''
def getEpsilon():
    '''returns double\n\n
    getEpsilon()\n
    '''
def getRandomGenerator():
    '''returns RandomGenerator\n\n
    getRandomGenerator()\n
    '''
def getMembershipMatrix():
    '''returns RealMatrix\n\n
    getMembershipMatrix()\n
    '''
def getDataPoints():
    '''returns List<T>\n\n
    getDataPoints()\n
    '''
def getClusters():
    '''returns List<CentroidCluster<T>>\n\n
    getClusters()\n
    '''
def getObjectiveFunctionValue():
    '''returns double\n\n
    getObjectiveFunctionValue()\n
    '''
def cluster():
    '''returns List<CentroidCluster<T>>\n\n
    cluster(final Collection<T> dataPoints)\n
    '''
