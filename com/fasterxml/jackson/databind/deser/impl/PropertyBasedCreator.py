def construct():
'''public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps, final BeanPropertyMap allProperties)
public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps, final boolean caseInsensitive)
public static PropertyBasedCreator construct(final DeserializationContext ctxt, final ValueInstantiator valueInstantiator, final SettableBeanProperty[] srcCreatorProps)
'''
pass
def properties():
'''public Collection<SettableBeanProperty> properties()
'''
pass
def findCreatorProperty():
'''public SettableBeanProperty findCreatorProperty(final String name)
public SettableBeanProperty findCreatorProperty(final int propertyIndex)
'''
pass
def startBuilding():
'''public PropertyValueBuffer startBuilding(final JsonParser p, final DeserializationContext ctxt, final ObjectIdReader oir)
'''
pass
def build():
'''public Object build(final DeserializationContext ctxt, final PropertyValueBuffer buffer)
'''
pass
def get():
'''public SettableBeanProperty get(final Object key0)
'''
pass
def put():
'''public SettableBeanProperty put(String key, final SettableBeanProperty value)
'''
pass
