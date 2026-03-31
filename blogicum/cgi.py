# Compatibility shim for Python 3.13+ where the stdlib cgi module was removed.
from email.message import Message
import re


def parse_header(line):
    if not line:
        return '', {}
    msg = Message()
    msg['content-type'] = line
    params = msg.get_params(header='content-type', unquote=True) or []
    if not params:
        return line, {}
    key = params[0][0]
    pdict = {k: v for k, v in params[1:]}
    return key, pdict


def valid_boundary(s):
    if isinstance(s, bytes):
        try:
            s = s.decode('ascii')
        except Exception:
            return False
    return re.match(r'^[ -~]{0,200}[!-~]$', s) is not None
