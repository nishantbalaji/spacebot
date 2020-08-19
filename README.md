# Spacebot
This is a simple Discord bot created to implement NASA data into Discord. Using the [NASA API](https://api.nasa.gov/) and [Discord API](https://discord.com/developers/docs/intro), the program collects data and displays it in response to the user's commands. 

## Installation
  1. Go to the [Discord developer portal](https://discord.com/developers/applications) and log in.
  2. Navigate to the applications tab and click "New Application". Give this application a name.
  3. Click the Bot button on the left bar, and then click "Add Bot".
  4. Download the code if you haven't already, and then create a new file in the same directory called *.env*.
  5. Put the following lines in the *.env* file 
  ``` 
  DISCORD_TOKEN={YOUR_DISCORD_TOKEN}
  API_KEY={YOUR_API_KEY}
  NASA_KEY={YOUR_NASA_KEY}
  ```
  6. Go back to the Discord bot page and click copy to copy your Bot token. Replace `{YOUR_DISCORD_TOKEN}` with this token.
  7. Click the "General Information" tab on the left and copy your Client secret. Replace `{YOUR_API_KEY}` with this secret. 
  8. Go to the [NASA API](https://api.nasa.gov/) website and create an API Key. Replace `{YOUR_NASA_KEY}` with this key. 
  9. Invite the bot to your Discord server. 
  10. Run the code, and enjoy!
  
  ## Commands
   - `!apod [YYYY MM DD]` - displays the astronomy picture of the date specified, or current date if no date is specified, with associated its associated author and caption.
   - `!echo [text] - returns back the text sent to it, and deletes the message containing the command.
