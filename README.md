# Muse

## Description
Muse is a Discord bot that sends an embed containing information about a song's title, artist, and release country and date based the user inputted country and decade.  The idea of this bot is inspired by Radiooooo.com, which uses a similar method to determine songs to play.  In other words, it's like Radiooooo but as a music library bot.  Additionally, Muse keeps track of the most searched terms and recently liked songs among all servers.  It is built using Discord's and various other APIs that will be described in its usage in a later section of this ReadME. \
**Language(s):** Python \
**Developer:** Helen Ma


## Usage
### Inviting to Server
The invite link for Muse is in the line below:\
```https://tinyurl.com/muse-bot```
#### Intructions:
1. Click the link above to get to the invite page of Muse.
2. Select the server you would like to invite Muse to.^
<img src="https://i.imgur.com/lUXrmsT.png" alt="landing" width="414" height="896" />
3. Click authorize and follow proceeding steps.
<img src="https://i.imgur.com/Cm00s2c.png" alt="authentication" width="414" height="896" />
4. The bot can now be used in the server. 
<img src="https://i.imgur.com/eJxFuKo.jpg" alt="server" width="414" height="404" /> 

### Commands
#### +help
```+help``` \
Pulls up the help page
#### +list
```+list [decade]``` \
Sends a list of countries in the world by decade ranging from 1900 to 2020
#### +song
```+song [country] [decade]``` \
Sends a song released from the input country during the specified decade
(ex: +song Japan 1980)
#### +top
```+top terms``` \
Shows the top 3 most searched terms \
```+top songs``` \
Shows the 3 most recently liked songs in the server
#### Error Handling
The program uses try-catch blocks where it outlines if/else statements to determine whether the input is valid.  In the try block, if the input is determined to be invalid, the program throws an error, which will be caught and sent as a regular message in Discord.

## Advanced
### APIs
#### Discord py
The Discord.py API provides a general framework for handling commands and running bots.  For Muse, it sends the appropriate message according to the user's request and allows it to run by using a randomly generated token from the developer portal.  Commands are established using ```@client.command(...)``` and async functions process inputs.
#### Musicbrainzngs
Musicbrainzngs is a module that searches for songs based on the inputted country and decade and gathers data on other details about the song such as its title, artist, and year and country released.  The mentioned fields are essential details for searching for MP4s of songs on YouTube.  Musicbrainz is a music encyclopedia and its associated module, musicbrainszngs, is derived from its Python API.
#### Unidecode
Unidecode is a module used to convert non-ASCII characters into ASCII characters.  In the context of Muse, to search for videos on YouTube using re and URL Lib, using non-ASCII strings will generate an error.  Non-ASCII values are used in languages that do not use Roman letters such as Chinese and Russian, and Unidecode Romanizes them so Muse can search for songs.
#### URL Lib and Re
When searching for songs, URL lib searches for songs based on a URL, which in this case is a YouTube search link that uses inputted search terms.  Then, re finds the ID of videos on the search page and the first one is selected to be part of the embed.
### Classes
#### Cog
Cogs in the program are used to organize multiple commands under one class and help organize the program.  
#### Menu
Menu uses the Cog structure and contains commands ```+help``` and ```+list```, which pull up essential information for using Muse.
#### Music
Music is also a part of the Cog structure and contains commands ```+song``` and ```+top```, which send songs and keeps track of search terms and recently liked songs.
#### Info
Info is a non-Cog class that keeps track of all and top 3 search terms.

## Development 
### Shift in Purpose
Initially, Muse was called Jukebox since it was meant to play songs in Discord voice channels, but music bots like Rhythm that serve the same purpose shut down due to receiving cease and desist orders from YouTube.  Like Rhythm, Muse downloads MP4s from YouTube and plays them in Discord channels.  This procedure had to be scrapped to prevent potential lawsuits, so the bot was renamed Muse after Greek goddesses of art and was turned into a music library bot.
### Troubleshooting
Throught the development of Muse, the bot was tested in my Discord server called Snecc island.  

## Closing


^*The profile picture here is the one used before Muse was finalized
