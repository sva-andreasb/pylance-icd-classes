def parse():
    '''    public static Record<Data> parse(final DataInputStream dis, final byte[] data)
    '''
def Record():
    '''    public Record(final DnsName name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)
    public Record(final String name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)
    public Record(final String name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)
    public Record(final DnsName name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)
    '''
def toOutputStream():
    '''    public void toOutputStream(final DataOutputStream dos)
    '''
def toByteArray():
    '''    public byte[] toByteArray()
    '''
def toString():
    '''    public String toString()
    '''
def isAnswer():
    '''    public boolean isAnswer(final Question q)
    '''
def isUnicastQuery():
    '''    public boolean isUnicastQuery()
    '''
def getPayload():
    '''    public D getPayload()
    '''
def getTtl():
    '''    public long getTtl()
    '''
def getQuestion():
    '''    public Question getQuestion()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object other)
    '''
def ifPossibleAs():
    '''    public <E extends Data> Record<E> ifPossibleAs(final Class<E> dataClass)
    '''
def filter():
    '''    public static <E extends Data> void filter(final Collection<Record<E>> result, final Class<E> dataClass, final Collection<Record<? extends Data>> input)
    public static <E extends Data> List<Record<E>> filter(final Class<E> dataClass, final Collection<Record<? extends Data>> input)
    '''
def getValue():
    '''    public int getValue()
    public int getValue()
    '''
def getDataClass():
    '''    public <D extends Data> Class<D> getDataClass()
    '''
def getType():
    '''    public static TYPE getType(final int value)
    public static <D extends Data> TYPE getType(final Class<D> dataClass)
    '''
def getClass():
    '''    public static CLASS getClass(final int value)
    '''
