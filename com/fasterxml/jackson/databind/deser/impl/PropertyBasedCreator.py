def properties():
    '''returns Collection<SettableBeanProperty>\n\n
    properties()\n
    '''
def findCreatorProperty():
    '''returns SettableBeanProperty\n\n
    findCreatorProperty(final String name)\n
    findCreatorProperty(final int propertyIndex)\n
    '''
def startBuilding():
    '''returns PropertyValueBuffer\n\n
    startBuilding(final JsonParser p, final DeserializationContext ctxt, final ObjectIdReader oir)\n
    '''
def build():
    '''returns Object\n\n
    build(final DeserializationContext ctxt, final PropertyValueBuffer buffer)\n
    '''
def get():
    '''returns SettableBeanProperty\n\n
    get(final Object key0)\n
    '''
def put():
    '''returns SettableBeanProperty\n\n
    put(String key, final SettableBeanProperty value)\n
    '''
