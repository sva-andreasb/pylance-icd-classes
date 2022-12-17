def ():
    '''returns ConfigKey\n\n
    ()\n
    (final ConfigDef base)\n
    (final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents, final Recommender recommender, final boolean internalConfig)\n
    '''
def names():
    '''returns Set<String>\n\n
    names()\n
    '''
def define():
    '''returns ConfigDef\n\n
    define(final ConfigKey key)\n
    define(final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents, final Recommender recommender)\n
    define(final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents)\n
    define(final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final Recommender recommender)\n
    define(final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName)\n
    define(final String name, final Type type, final Object defaultValue, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents, final Recommender recommender)\n
    define(final String name, final Type type, final Object defaultValue, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents)\n
    define(final String name, final Type type, final Object defaultValue, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final Recommender recommender)\n
    define(final String name, final Type type, final Object defaultValue, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName)\n
    define(final String name, final Type type, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents, final Recommender recommender)\n
    define(final String name, final Type type, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final List<String> dependents)\n
    define(final String name, final Type type, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName, final Recommender recommender)\n
    define(final String name, final Type type, final Importance importance, final String documentation, final String group, final int orderInGroup, final Width width, final String displayName)\n
    define(final String name, final Type type, final Object defaultValue, final Validator validator, final Importance importance, final String documentation)\n
    define(final String name, final Type type, final Object defaultValue, final Importance importance, final String documentation)\n
    define(final String name, final Type type, final Importance importance, final String documentation)\n
    '''
def defineInternal():
    '''returns ConfigDef\n\n
    defineInternal(final String name, final Type type, final Object defaultValue, final Importance importance)\n
    '''
def groups():
    '''returns List<String>\n\n
    groups()\n
    '''
def withClientSslSupport():
    '''returns ConfigDef\n\n
    withClientSslSupport()\n
    '''
def withClientSaslSupport():
    '''returns ConfigDef\n\n
    withClientSaslSupport()\n
    '''
def validate():
    '''returns List<ConfigValue>\n\n
    validate(final Map<String, String> props)\n
    '''
def toHtmlTable():
    '''returns String\n\n
    toHtmlTable()\n
    toHtmlTable(final Map<String, String> dynamicUpdateModes)\n
    '''
def toRst():
    '''returns String\n\n
    toRst()\n
    '''
def toEnrichedRst():
    '''returns String\n\n
    toEnrichedRst()\n
    '''
def compare():
    '''returns int\n\n
    compare(final ConfigKey k1, final ConfigKey k2)\n
    '''
def embed():
    '''returns None\n\n
    embed(final String keyPrefix, final String groupPrefix, final int startingOrd, final ConfigDef child)\n
    '''
def ensureValid():
    '''returns None\n\n
    ensureValid(final String name, final Object value)\n
    ensureValid(final String name, final Object o)\n
    ensureValid(final String name, final Object value)\n
    ensureValid(final String name, final Object o)\n
    ensureValid(final String name, final Object value)\n
    ensureValid(final String name, final Object value)\n
    ensureValid(final String name, final Object o)\n
    ensureValid(final String name, final Object value)\n
    '''
def validValues():
    '''returns List<Object>\n\n
    validValues(final String name, final Map<String, Object> parsedConfig)\n
    '''
def visible():
    '''returns boolean\n\n
    visible(final String name, final Map<String, Object> parsedConfig)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
def hasDefault():
    '''returns boolean\n\n
    hasDefault()\n
    '''
