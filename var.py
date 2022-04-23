# actually I don't know who is the real creator of this file ...
# I got from xditya's telebot
# full credit full respect
# now in TufaanBot by @AkHiL_SI

import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as Config
else:
    from local_config import Development as Config


Var = Config

