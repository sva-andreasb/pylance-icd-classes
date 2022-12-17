def ():
    '''returns BeanPropertyMap\n\n
    (final boolean caseInsensitive, final Collection<SettableBeanProperty> props, final Map<String, List<PropertyName>> aliasDefs)\n
    (final boolean caseInsensitive, final Collection<SettableBeanProperty> props)\n
    '''
def withCaseInsensitivity():
    '''returns BeanPropertyMap\n\n
    withCaseInsensitivity(final boolean state)\n
    '''
def withProperty():
    '''returns BeanPropertyMap\n\n
    withProperty(final SettableBeanProperty newProp)\n
    '''
def assignIndexes():
    '''returns BeanPropertyMap\n\n
    assignIndexes()\n
    '''
def renameAll():
    '''returns BeanPropertyMap\n\n
    renameAll(final NameTransformer transformer)\n
    '''
def withoutProperties():
    '''returns BeanPropertyMap\n\n
    withoutProperties(final Collection<String> toExclude)\n
    '''
def replace():
    '''returns None\n\n
    replace(final SettableBeanProperty newProp)\n
    replace(final SettableBeanProperty origProp, final SettableBeanProperty newProp)\n
    '''
def remove():
    '''returns None\n\n
    remove(final SettableBeanProperty propToRm)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def isCaseInsensitive():
    '''returns boolean\n\n
    isCaseInsensitive()\n
    '''
def hasAliases():
    '''returns boolean\n\n
    hasAliases()\n
    '''
def iterator():
    '''returns Iterator<SettableBeanProperty>\n\n
    iterator()\n
    '''
def getPropertiesInInsertionOrder():
    '''returns SettableBeanProperty[]\n\n
    getPropertiesInInsertionOrder()\n
    '''
def find():
    '''returns SettableBeanProperty\n\n
    find(final int index)\n
    find(String key)\n
    '''
def findDeserializeAndSet():
    '''returns boolean\n\n
    findDeserializeAndSet(final JsonParser p, final DeserializationContext ctxt, final Object bean, final String key)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
