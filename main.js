const Discord = require('discord.js');
const client = new Discord.Client(); 
var Long = require("long");

client.once('ready', () => {
    console.log('Stock Bot is online!');
    client.channels.cache.get('CHANNEL ID').send("MESSAGE") //Enter your channel ID (right click the text channel and select copy id) and customize the message
    
});
 
client.on('message', message =>{
});

client.login('TOKEN'); //ENTER YOUR TOKEN