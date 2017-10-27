import weechat

weechat.register("jackScript", "FlashCode", "1.0", "GPL3", "Test script", "", "")
weechat.prnt("", "Use without jack2 permition is not allowed")

#process messages 
def message(data, bufferp, tm, tags, display, is_hilight, prefix, msg):
	name = weechat.buffer_get_string(bufferp,"name")
	server = weechat.buffer_get_string(bufferp, "localvar_server")
	channel = weechat.buffer_get_string(bufferp, "localvar_channel")
	#add the tiecoon reponse 
	if "tiecoon" in msg:
		buffer = weechat.info_get("irc_buffer", "rpisec," + channel)
		weechat.command(buffer, "tiecoon: is the worst")

	#if in psoft do subtractions 
	if channel == "#psoft":
		buffer = weechat.info_get("irc_buffer", "rpisec,#psoft")
		if "+a" in msg and "jack2" in msg:
			weechat.command(buffer, "/mode -aaa tiecoon Hawkheart kevin")
			weechat.prnt("", "/mode -aaa tiecoon Hawkheart kevin")
		if "+q" in msg and "kevin" in msg:
			weechat.command(buffer, "/mode -q kevin")
			weechat.prnt("", "/mode -aaa tiecoon Hawkheart kevin")
	return weechat.WEECHAT_RC_OK


weechat.hook_print("", "", "", 1, "message", "") # catch all messages

