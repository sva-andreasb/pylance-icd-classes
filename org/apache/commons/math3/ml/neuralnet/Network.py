def Network():
    '''    public Network(final long initialIdentifier, final int featureSize)
    '''
def copy():
    '''    public synchronized Network copy()
    '''
def iterator():
    '''    public Iterator<Neuron> iterator()
    '''
def getNeurons():
    '''    public Collection<Neuron> getNeurons(final Comparator<Neuron> comparator)
    '''
def createNeuron():
    '''    public long createNeuron(final double[] features)
    '''
def deleteNeuron():
    '''    public void deleteNeuron(final Neuron neuron)
    '''
def getFeaturesSize():
    '''    public int getFeaturesSize()
    '''
def addLink():
    '''    public void addLink(final Neuron a, final Neuron b)
    '''
def deleteLink():
    '''    public void deleteLink(final Neuron a, final Neuron b)
    '''
def getNeuron():
    '''    public Neuron getNeuron(final long id)
    '''
def getNeighbours():
    '''    public Collection<Neuron> getNeighbours(final Iterable<Neuron> neurons)
    public Collection<Neuron> getNeighbours(final Iterable<Neuron> neurons, final Iterable<Neuron> exclude)
    public Collection<Neuron> getNeighbours(final Neuron neuron)
    public Collection<Neuron> getNeighbours(final Neuron neuron, final Iterable<Neuron> exclude)
    '''
def compare():
    '''    public int compare(final Neuron a, final Neuron b)
    '''
