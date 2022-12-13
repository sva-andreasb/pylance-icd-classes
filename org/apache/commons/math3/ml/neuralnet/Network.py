def Network():
'''public Network(final long initialIdentifier, final int featureSize)
'''
pass
def copy():
'''public synchronized Network copy()
'''
pass
def iterator():
'''public Iterator<Neuron> iterator()
'''
pass
def getNeurons():
'''public Collection<Neuron> getNeurons(final Comparator<Neuron> comparator)
'''
pass
def createNeuron():
'''public long createNeuron(final double[] features)
'''
pass
def deleteNeuron():
'''public void deleteNeuron(final Neuron neuron)
'''
pass
def getFeaturesSize():
'''public int getFeaturesSize()
'''
pass
def addLink():
'''public void addLink(final Neuron a, final Neuron b)
'''
pass
def deleteLink():
'''public void deleteLink(final Neuron a, final Neuron b)
'''
pass
def getNeuron():
'''public Neuron getNeuron(final long id)
'''
pass
def getNeighbours():
'''public Collection<Neuron> getNeighbours(final Iterable<Neuron> neurons)
public Collection<Neuron> getNeighbours(final Iterable<Neuron> neurons, final Iterable<Neuron> exclude)
public Collection<Neuron> getNeighbours(final Neuron neuron)
public Collection<Neuron> getNeighbours(final Neuron neuron, final Iterable<Neuron> exclude)
'''
pass
def compare():
'''public int compare(final Neuron a, final Neuron b)
'''
pass
