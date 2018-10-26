# *   c05 ,        ,
# *   /(_,    ,_)\
# *   \ _/    \_ /
# *   //        \\
# *   \\ c15(c08@c15)(c08@c15)c05 //
# *    \'=\"==\"='/
# *  ,===/       \===,
# * \",===\      /===,\"
# *  \" ,==='------'===,\"         FUCK YOU MAX
# *   \"                 \"

import weechat as w
import random
import re

SCRIPT_NAME = "prism"
SCRIPT_AUTHOR = "Luke"
SCRIPT_VERSION = "0.0.0"
SCRIPT_LICENSE = "WTFPL"
SCRIPT_DESC = "get crabbed"

if w.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE,
              SCRIPT_DESC, "", ""):
    w.hook_command("crab", SCRIPT_DESC, '', '', '', "prism_cmd_cb", '')


def prism_cmd_cb(data, buffer, args):

    input = args.decode("UTF-8")
    input_method = "command"

    output = ""
    output += u'\x03' + '05' + 'GET CRABBED\n'
    output += u'\x0f'
    output +="    /(_,    ,_)\\\n"
    output +="    \ _/    \_ /\n"
    output +="    //        \\\\\n"
    output +="    \\\\        //\n"
    output +="     \\\\=\"==\"=//\n"
    output +="  ===/        \===\n"
    output +=" \===\        /===\\\n"
    output +="  \===\\------/ === \\\n"         
    output +="   \                \\\n"



    w.command(buffer, output.encode("UTF-8"))
    return w.WEECHAT_RC_OK
