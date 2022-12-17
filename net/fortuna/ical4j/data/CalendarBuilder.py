def ():
    '''returns CalendarBuilder\n\n
    ()\n
    (final CalendarParser parser)\n
    (final TimeZoneRegistry tzRegistry)\n
    (final CalendarParser parser, final TimeZoneRegistry tzRegistry)\n
    (final CalendarParser parser, final PropertyFactoryRegistry propertyFactoryRegistry, final ParameterFactoryRegistry parameterFactoryRegistry, final TimeZoneRegistry tzRegistry)\n
    (final CalendarParser parser, final Supplier<List<ParameterFactory<?>>> parameterFactorySupplier, final Supplier<List<PropertyFactory<?>>> propertyFactorySupplier, final Supplier<List<ComponentFactory<?>>> componentFactorySupplier, final TimeZoneRegistry tzRegistry)\n
    '''
def accept():
    '''returns None\n\n
    accept(final Calendar calendar)\n
    '''
def build():
    '''returns Calendar\n\n
    build(final InputStream in)\n
    build(final Reader in)\n
    build(final UnfoldingReader uin)\n
    '''
