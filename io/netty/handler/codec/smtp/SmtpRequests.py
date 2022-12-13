def helo():
    '''public static SmtpRequest helo(final CharSequence hostname)
    '''
def ehlo():
    '''public static SmtpRequest ehlo(final CharSequence hostname)
    '''
def empty():
    '''public static SmtpRequest empty(final CharSequence... parameter)
    '''
def auth():
    '''public static SmtpRequest auth(final CharSequence... parameter)
    '''
def noop():
    '''public static SmtpRequest noop()
    '''
def data():
    '''public static SmtpRequest data()
    '''
def rset():
    '''public static SmtpRequest rset()
    '''
def help():
    '''public static SmtpRequest help(final String cmd)
    '''
def quit():
    '''public static SmtpRequest quit()
    '''
def mail():
    '''public static SmtpRequest mail(final CharSequence sender, final CharSequence... mailParameters)
    '''
def rcpt():
    '''public static SmtpRequest rcpt(final CharSequence recipient, final CharSequence... rcptParameters)
    '''
def expn():
    '''public static SmtpRequest expn(final CharSequence mailingList)
    '''
def vrfy():
    '''public static SmtpRequest vrfy(final CharSequence user)
    '''
