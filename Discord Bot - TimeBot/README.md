## hello again,
This is TimeBot (it used to be Bjoerk/Rickle Pick), hes my analytics tracking discord bot, he logs when people join and leave discord channels.
Along with these files, theres also a .env file containing the secret api keys used for interfacing with the discord api, it is however, part of the gitignore and as such will not be uploaded

#### UPDATE: Rickle Pick
This is the update for the rickle pick rework.  In addtion to changing the bots name, a scoreboard function has been introduced, accessible through "#tscore" along with a massive folder structure rework.  All of the folders have been changed to use user descriminators, or the four numbers after a users name.  This allows users to change their name, without losing their tracked time.
Lastly, the bot has also been modified to send its updates to two channels on two seperate servers, this is really jank at the moment and I am hopeful a better fix will be right around the corner.

#### UPDATE: Jun 23, 2021
The purpose of this bot was to use the analytics in order to predict when people are most likley to join and leave channels on discord, after having this bot for a number of months, I think enough data has been collected to start this process.  
However, after much thinking, I think I may have not been collecting all of the data I need, and as such along with the RICKLE PICK rewrite, I will be soon reworking the entire folder structure once again, this time to use discriminators as well as id's, and collecting more data such as the channel and server they joined to.
I have a lot of other things going on at the moment, so this may have to wait, at least until I get the prediction software working correctly.

#### UPDATE: July 5, 2021
This is the MortyBot update.  Included in this update is file organisation changes as well as the migration from bot.py to sysCore.  More information to come later

#### UPDATE: TimeBot
Hi,
Just letting you know that TimeBot has gotten some new updates..

First,
TimeBot has gotten a reworked Help command, type #help to get a list of all of the commands or #help [command] to get help with a specific command.

Second,
TimeBot's update channel messaging has now been completely reworked.. TimeBot now only messages VC join/leave updates to channels called "timebot".  Timebot also only messages updates from a server to that server, No more getting updates from other servers.

Third,
As of this update, stats.csv has been officially depreciated in favor of UsrLogs.  UsrLogs contains more information than stats.csv as well as a fix for the line spacing

Fourth,
You now have 5 mins to leave and rejoin a channel after the bot comes back online to save your time

Lastly, The smaller updates,
@ everyone pings for when someone hits ten days have been removed, in fact, all @ everone pings have been removed
The bot still tracks when you hit ten dats, it just no longer notifies you
Also, the 10 command has been removed from help, but it is not gone, you can still use #10 to see when you hit ten days
I've added a new command!! Use the rm command to generate a random rick and morty quote

For ADMINS;
The authorize command has been restored to its full potential, use authorize to add a new ADMIN to give them access to bot backups
