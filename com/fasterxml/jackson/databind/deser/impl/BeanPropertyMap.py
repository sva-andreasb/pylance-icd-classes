def BeanPropertyMap():
    '''    public BeanPropertyMap(final boolean caseInsensitive, final Collection<SettableBeanProperty> props, final Map<String, List<PropertyName>> aliasDefs)
    public BeanPropertyMap(final boolean caseInsensitive, final Collection<SettableBeanProperty> props)
    '''
def withCaseInsensitivity():
    '''    public BeanPropertyMap withCaseInsensitivity(final boolean state)
    '''
def construct():
    '''    public static BeanPropertyMap construct(final Collection<SettableBeanProperty> props, final boolean caseInsensitive, final Map<String, List<PropertyName>> aliasMapping)
    public static BeanPropertyMap construct(final Collection<SettableBeanProperty> props, final boolean caseInsensitive)
    '''
def withProperty():
    '''    public BeanPropertyMap withProperty(final SettableBeanProperty newProp)
    '''
def assignIndexes():
    '''    public BeanPropertyMap assignIndexes()
    '''
def renameAll():
    '''    public BeanPropertyMap renameAll(final NameTransformer transformer)
    '''
def withoutProperties():
    '''    public BeanPropertyMap withoutProperties(final Collection<String> toExclude)
    '''
def replace():
    '''    public void replace(final SettableBeanProperty newProp)
    public void replace(final SettableBeanProperty origProp, final SettableBeanProperty newProp)
    '''
def remove():
    '''    public void remove(final SettableBeanProperty propToRm)
    '''
def size():
    '''    public int size()
    '''
def isCaseInsensitive():
    '''    public boolean isCaseInsensitive()
    '''
def hasAliases():
    '''    public boolean hasAliases()
    '''
def iterator():
    '''    public Iterator<SettableBeanProperty> iterator()
    '''
def getPropertiesInInsertionOrder():
    '''    public SettableBeanProperty[] getPropertiesInInsertionOrder()
    '''
def find():
    '''    public SettableBeanProperty find(final int index)
    public SettableBeanProperty find(String key)
    '''
def findDeserializeAndSet():
    '''    public boolean findDeserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object bean, final String key)
    '''
def toString():
    '''    public String toString()
    '''
