from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 2GBGB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 23 ind /🌎 0.35$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 45 ind /🌎 0.59$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 69 ind /🌎 0.83$  per Month
	
	
	Pay Using Upi I'd `madflixofficial@axl`
	
	After Payment Send Screenshots Of 
        Payment To Admin @calladminrobot"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("Admin",url = "https://t.me/Otaku_Library_Support_Bot")], 
        			[InlineKeyboardButton("Sacne Code",url = "https://telegra.ph/file/396977d1b4a2e37c3e36d.jpg"),
        			InlineKeyboardButton("Scan/UPI",url = "https://telegra.ph/file/396977d1b4a2e37c3e36d.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🪙 Basic** 
	Daily  Upload  limit 20GB
	Price Rs 23  ind /🌎 0.35$  per Month
	
	**⚡ Standard**
	Daily Upload limit 50GB
	Price Rs 45  ind /🌎 0.59$  per Month
	
	**💎 Pro**
	Daily Upload limit 100GB
	Price Rs 69  ind /🌎 0.83$  per Month
	
	
	Pay Using Upi I'd `ogbhargav@fam`
	
	After Payment Send Screenshots Of 
        Payment To Admin @Otaku_Library_Support_Bot"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("👤 Admin",url = "https://t.me/Otaku_Library_Support_Bot")], 
        			[InlineKeyboardButton("Scan Code",url = "https://telegra.ph/file/396977d1b4a2e37c3e36d.jpg"),
        			InlineKeyboardButton("Sacn/UPI",url = "https://telegra.ph/file/396977d1b4a2e37c3e36d.jpg")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Developer @JishuDeveloper
