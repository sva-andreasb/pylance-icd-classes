def ():
    '''returns Factory\n\n
    ()\n
    (final boolean initialise)\n
    (final PropertyList properties)\n
    (final DateTime start, final DateTime end)\n
    (final DateTime start, final DateTime end, final TemporalAmount duration)\n
    (final VFreeBusy request, final ComponentList<CalendarComponent> components)\n
    ()\n
    '''
def start():
    '''returns FreeTimeBuilder\n\n
    start(final DateTime start)\n
    start(final DateTime start)\n
    '''
def end():
    '''returns FreeTimeBuilder\n\n
    end(final DateTime end)\n
    end(final DateTime end)\n
    '''
def components():
    '''returns FreeTimeBuilder\n\n
    components(final ComponentList<CalendarComponent> components)\n
    components(final ComponentList<CalendarComponent> components)\n
    '''
def build():
    '''returns FreeBusy\n\n
    build()\n
    build()\n
    '''
def createComponent():
    '''returns VFreeBusy\n\n
    createComponent()\n
    createComponent(final PropertyList properties)\n
    createComponent(final PropertyList properties, final ComponentList subComponents)\n
    '''
