def ():
    '''returns Network\n\n
    (final long initialIdentifier, final int featureSize)\n
    '''
def iterator():
    '''returns Iterator<Neuron>\n\n
    iterator()\n
    '''
def getNeurons():
    '''returns Collection<Neuron>\n\n
    getNeurons(final Comparator<Neuron> comparator)\n
    '''
def createNeuron():
    '''returns long\n\n
    createNeuron(final double[] features)\n
    '''
def deleteNeuron():
    '''returns None\n\n
    deleteNeuron(final Neuron neuron)\n
    '''
def getFeaturesSize():
    '''returns int\n\n
    getFeaturesSize()\n
    '''
def addLink():
    '''returns None\n\n
    addLink(final Neuron a, final Neuron b)\n
    '''
def deleteLink():
    '''returns None\n\n
    deleteLink(final Neuron a, final Neuron b)\n
    '''
def getNeuron():
    '''returns Neuron\n\n
    getNeuron(final long id)\n
    '''
def getNeighbours():
    '''returns Collection<Neuron>\n\n
    getNeighbours(final Iterable<Neuron> neurons)\n
    getNeighbours(final Iterable<Neuron> neurons, final Iterable<Neuron> exclude)\n
    getNeighbours(final Neuron neuron)\n
    getNeighbours(final Neuron neuron, final Iterable<Neuron> exclude)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Neuron a, final Neuron b)\n
    '''
