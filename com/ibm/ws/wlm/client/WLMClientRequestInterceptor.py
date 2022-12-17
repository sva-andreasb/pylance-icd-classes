def ():
    '''returns WLMClientRequestInterceptor\n\n
    ()\n
    '''
def pre_init():
    '''returns None\n\n
    pre_init(final ORBInitInfo info)\n
    '''
def post_init():
    '''returns None\n\n
    post_init(final ORBInitInfo info)\n
    '''
def send_request():
    '''returns None\n\n
    send_request(final ClientRequestInfo cri)\n
    '''
def receive_reply():
    '''returns None\n\n
    receive_reply(final ClientRequestInfo cri)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def name():
    '''returns String\n\n
    name()\n
    '''
def send_poll():
    '''returns None\n\n
    send_poll(final ClientRequestInfo cri)\n
    '''
def receive_exception():
    '''returns None\n\n
    receive_exception(final ClientRequestInfo cri)\n
    '''
def receive_other():
    '''returns None\n\n
    receive_other(final ClientRequestInfo cri)\n
    '''
def registerServiceContextListener():
    '''returns None\n\n
    registerServiceContextListener(final ORB orb, final WLMServiceClientContextListener context_listener)\n
    '''
def deregisterServiceContextListener():
    '''returns None\n\n
    deregisterServiceContextListener(final ORB orb, final WLMServiceClientContextListener context_listener)\n
    '''
