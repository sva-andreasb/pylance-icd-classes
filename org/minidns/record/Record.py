def parse():
'''public static Record<Data> parse(final DataInputStream dis, final byte[] data)
'''
pass
def Record():
'''public Record(final DnsName name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)
public Record(final String name, final TYPE type, final CLASS clazz, final long ttl, final D payloadData, final boolean unicastQuery)
public Record(final String name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)
public Record(final DnsName name, final TYPE type, final int clazzValue, final long ttl, final D payloadData)
'''
pass
def toOutputStream():
'''public void toOutputStream(final DataOutputStream dos)
'''
pass
def toByteArray():
'''public byte[] toByteArray()
'''
pass
def toString():
'''public String toString()
'''
pass
def isAnswer():
'''public boolean isAnswer(final Question q)
'''
pass
def isUnicastQuery():
'''public boolean isUnicastQuery()
'''
pass
def getPayload():
'''public D getPayload()
'''
pass
def getTtl():
'''public long getTtl()
'''
pass
def getQuestion():
'''public Question getQuestion()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object other)
'''
pass
def ifPossibleAs():
'''public <E extends Data> Record<E> ifPossibleAs(final Class<E> dataClass)
'''
pass
def filter():
'''public static <E extends Data> void filter(final Collection<Record<E>> result, final Class<E> dataClass, final Collection<Record<? extends Data>> input)
public static <E extends Data> List<Record<E>> filter(final Class<E> dataClass, final Collection<Record<? extends Data>> input)
'''
pass
def getValue():
'''public int getValue()
public int getValue()
'''
pass
def getDataClass():
'''public <D extends Data> Class<D> getDataClass()
'''
pass
def getType():
'''public static TYPE getType(final int value)
public static <D extends Data> TYPE getType(final Class<D> dataClass)
'''
pass
def getClass():
'''public static CLASS getClass(final int value)
'''
pass
