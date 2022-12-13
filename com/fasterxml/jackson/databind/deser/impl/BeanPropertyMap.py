def BeanPropertyMap():
'''public BeanPropertyMap(final boolean caseInsensitive, final Collection<SettableBeanProperty> props, final Map<String, List<PropertyName>> aliasDefs)
public BeanPropertyMap(final boolean caseInsensitive, final Collection<SettableBeanProperty> props)
'''
pass
def withCaseInsensitivity():
'''public BeanPropertyMap withCaseInsensitivity(final boolean state)
'''
pass
def construct():
'''public static BeanPropertyMap construct(final Collection<SettableBeanProperty> props, final boolean caseInsensitive, final Map<String, List<PropertyName>> aliasMapping)
public static BeanPropertyMap construct(final Collection<SettableBeanProperty> props, final boolean caseInsensitive)
'''
pass
def withProperty():
'''public BeanPropertyMap withProperty(final SettableBeanProperty newProp)
'''
pass
def assignIndexes():
'''public BeanPropertyMap assignIndexes()
'''
pass
def renameAll():
'''public BeanPropertyMap renameAll(final NameTransformer transformer)
'''
pass
def withoutProperties():
'''public BeanPropertyMap withoutProperties(final Collection<String> toExclude)
'''
pass
def replace():
'''public void replace(final SettableBeanProperty newProp)
public void replace(final SettableBeanProperty origProp, final SettableBeanProperty newProp)
'''
pass
def remove():
'''public void remove(final SettableBeanProperty propToRm)
'''
pass
def size():
'''public int size()
'''
pass
def isCaseInsensitive():
'''public boolean isCaseInsensitive()
'''
pass
def hasAliases():
'''public boolean hasAliases()
'''
pass
def iterator():
'''public Iterator<SettableBeanProperty> iterator()
'''
pass
def getPropertiesInInsertionOrder():
'''public SettableBeanProperty[] getPropertiesInInsertionOrder()
'''
pass
def find():
'''public SettableBeanProperty find(final int index)
public SettableBeanProperty find(String key)
'''
pass
def findDeserializeAndSet():
'''public boolean findDeserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object bean, final String key)
'''
pass
def toString():
'''public String toString()
'''
pass
