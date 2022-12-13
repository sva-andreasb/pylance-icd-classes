def DescriptionManagerA():
    '''    public DescriptionManagerA()
    '''
def getDescription():
    '''    public synchronized Description getDescription(final DescriptionKey key)
    public synchronized Description getDescription(final DescriptionKey key, final String implKey)
    '''
def stream():
    '''    public void stream(final Map formatsToKeys, final ObjectOutput out)
    '''
def update():
    '''    public void update(final ObjectInput in)
    public void update(final String identifier, final byte[][] data)
    '''
def publish():
    '''    public boolean publish(final Description description)
    '''
def keyToString():
    '''    public static String keyToString(final DescriptionKey key)
    '''
def stringToKey():
    '''    public DescriptionKey stringToKey(final String keyString)
    '''
