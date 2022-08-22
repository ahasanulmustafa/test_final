from login.login import Login
from creating_bot.creating_bot import Bot
from bot_operation.botOperation import BotOp


''' User login by providing email and password '''
user = Login
user.loginGoogle("ahasanautomation@gmail.com", "noitamotuanasaha")

''' Creating a Bot '''
create_bot = Bot
Bot.creating_a_bot()

''' Bot operations '''
bot_operations = BotOp
BotOp.bot_operation()
BotOp.rename()

