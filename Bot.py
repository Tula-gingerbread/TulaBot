# Библиотеки
import discord
from discord_slash import SlashCommand, SlashContext
import discord.ext.commands as commands
import random
from time import sleep

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)

# Сообщение при запуске
@client.event
async def on_ready():
    print(f'Succesfuly logged in as {client.user} (ID: {client.user.id})')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')



# команда - pingcheck. Отправляет задержку Discord API
@slash.slash(name="ping", description="Проверить задержку Discord API")
async def ping(ctx: SlashContext):
    await ctx.send(f"Задержка Discord API: {round(client.latency*1000)}ms")
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда ping. Запросил - {user_name} (UserID: {user_id})')


# Команда - rickrool. Просто кидает рандомный рикролл из списка
@slash.slash(name="rickroll", description="?!")
async def rick(ctx: SlashContext):
    roll = ['https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://clck.ru/3vyXS', 'https://goo.su/WGcxU']
    random_roll = random.choice(roll)
    await ctx.send(random_roll)
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда rickroll. Запросил - {user_name} (UserID: {user_id})')



# Команда - SL. в ctx.send все понятно...
@slash.slash(name="SCPSL", description="спойлер к SCP SL...")
async def sl(ctx: SlashContext):
    await ctx.send('''Не пов, а рил:
Когда понял смысл SCP SL:
https://cdn.discordapp.com/attachments/1101107578336980992/1122915610523877477/Timeline-1.mp4''')
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда SCPSL. Запросил - {user_name} (UserID: {user_id})')



# Команда - say. Отправляет сообщение от имени бота
@slash.slash(name="say", description="Произнести что либо от имени бота. Нужна роль \"sayer\"")
@commands.has_role("sayer")
async def say(ctx: SlashContext, text: str):
    await ctx.send(text)
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда say. Запросил - {user_name} (UserID: {user_id})')



# Команда - установить_статус. Меняет статус бота
@slash.slash(name="установить_статус", description="Изменить статус бота. Три варианта: online, idle, dnd")
async def status(ctx: SlashContext, status: str):
    if status == 'online':
        await client.change_presence(status=discord.Status.online)
        await ctx.send('Успешно установлен статус на "В сети"')
    elif status == 'idle':
        await client.change_presence(status=discord.Status.idle)
        await ctx.send('Успешно установлен статус на "Неактивен"')
    elif status == 'dnd':
        await client.change_presence(status=discord.Status.do_not_disturb)
        await ctx.send('Успешно установлен статус на "Не беспокоить"')
    else:
        await ctx.send('Неизвестный статус!')
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда установить_статус. Запросил - {user_name} (UserID: {user_id})')



# Команда - колесо_фартуны
@slash.slash(name="Колесо_фартуны", description="Рандомный выбор из трех вариантов")
async def roll(ctx: SlashContext, first: str, second: str, third: str=None):
    if third is not None:
        result = random.choice([first, second, third])
    else:
        result = random.choice([first, second])

    await ctx.send(f'Выбор пал на... "{result}"')
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда колесо_фартуны. Запросил - {user_name} (UserID: {user_id})')



# Команда - hack. Взламывает роль "sayer" при правильном пароле (ilovebebra)
@slash.slash(name="hack", description="Возможность взломать роль \"sayer\"! Подсказка: шдщмуиуикф")
async def hack(ctx: SlashContext, password: str):
    user_id = ctx.author.id; user_name = ctx.author.name
    if password == 'ilovebebra':
        role = discord.utils.get(ctx.guild.roles, name='sayer')
        await ctx.author.add_roles(role)
        await ctx.send('Успешно! Вы получили роль "sayer"')
        print(f'Команда hack. Верный пароль. Запросил - {user_name} (UserID: {user_id})')
    else:
        await ctx.send('Неверный пароль! Блокировка системы... ')
        mute_duration = 60 
        await ctx.author.edit(mute=True, mute_duration=mute_duration)
        print(f'Команда hack. Неверный пароль. Запросил - {user_name} (UserID: {user_id})')



@slash.slash(name="993", description="Я умер... прости")
async def dead(ctx: SlashContext):
    alpha = 1007
    delta = 7
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда 993. Запросил - {user_name} (UserID: {user_id}) Он дед! Бейте его!')
    await ctx.send('Я умер, прости')
    while alpha>0: 
        omicron = alpha - delta
        await ctx.channel.send(str(omicron))
        alpha = omicron
        sleep(1)




@slash.slash(name='help', description='Показать инфо о командах')
async def help(ctx: SlashContext):
    await ctx.send('''```/ping - показывает задержку Discord API
/rickroll - ?!
/scpsl - спойлер к SCP SL
/say - говорит что либо от имени бота. Нужна роль 'sayer'
/установить_статус - Три варианта: online, idle, dnd - в сети, неактивен и не беспокоить соответственно
/колесо_фартуны - выбирает одно из трех (или двух) 
/hack - позволяет взломать роль 'sayer'. Подсказка: шдщмуиуикф. Мьютит при неверном пароле на одну минуту
/993 - ни нада дядя, не пиши эту команду
/info - показывает инфо о вас``` ''')
    user_id = ctx.author.id; user_name = ctx.author.name
    print(f'Команда help. Запросил - {user_name} (UserID: {user_id})')



@slash.slash(name='info', description='Показать инфо о вас')
async def info(ctx: SlashContext):
    user_id = ctx.author.id
    user_name = ctx.author.name
    user_avatar = ctx.author.avatar_url
    user_create = ctx.author.created_at
    user_roles = ctx.author.roles
    await ctx.send(f'''Ваше имя: {user_name}
UserID: {user_id}
URL на ваш аватар: {user_avatar}
Акаунт создан: {user_create}
Роли: ```{user_roles}```''')
    print(f'Команда info. Запросил - {user_name} (UserID: {user_id})')




# Запуск бота
if __name__ == '__main__':
    client.run('DONT FORGIVE TOKEN')
