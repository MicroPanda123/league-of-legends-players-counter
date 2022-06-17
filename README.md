# League of Legends detector
this bot detects league of legends and makes leaderboard of how long someone is playing

## Config Explanation

[defaults]
- updatetime sets time between embed update
- savetime sets time between saving data to file
- savefile sets file to save data to
- intent.members sets if your discord bot has intent members turned on (for this purpose leave this on)
- intent.presences sets if your discord bot has intent presences turned on (also leave this on)
- mode sets which mode should work (useful for testing)
- messageid sets if there is already message that just needs to be edited, at first launch it will automatically be set to message id of it's message

[MODE]
- token sets discord bots token (again, useful for testing on different servers)
- main_chat is left after some old code that I didn't bother to remove
- guild is id of a guild (testing)
- matixbot_chat sets chat dedicated for bot to post embed to
- app sets for what app should bot look for

## Warning
Yeah it's not rly production ready code, maybe I'll work on it later and try to make it into actually good discord bot that will be inviteable to servers, but for now it's good enough for me.