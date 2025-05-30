from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
from colorama import init, Fore
import os, time
import subprocess
import sys
required_packages = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "rich": "rich",
    "bs4": "beautifulsoup4",
    "cloudscraper": "cloudscraper"
}
missing = False
for module_name, pip_name in required_packages.items():
    try:
        __import__(module_name)
    except ImportError:
        print(f"Đang cài đặt thư viện thiếu: {pip_name} ...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
            missing = True
        except Exception as e:
            print(f"Cài thư viện {pip_name} thất bại: {e}")
            missing = True
if missing:
    print("\nĐã cài đặt thư viện cần thiết.")
    print("Vui lòng **chạy lại tool**.")
    sys.exit()
import os
import sys
import json
import base64
import uuid
import time
import socket
import random
import string
from datetime import datetime, timedelta
from random import randint
from time import sleep, strftime
import requests
import cloudscraper
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from pystyle import Write, Colors
from rich.console import Console
from rich.text import Text
init(autoreset=True)
def kiem_tra_mang():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
    except OSError:
        print("Mạng không ổn định hoặc bị mất kết nối. Vui lòng kiểm tra lại mạng.")
kiem_tra_mang()
def banner():
    print(f"""{Fore.YELLOW}╔══════════════════════════════════════════════════════╗
{Fore.YELLOW}║                                                      {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}████████╗██╗  ██╗ ████████╗ █████╗  █████╗ ██╗      {Fore.YELLOW}║
{Fore.YELLOW}║  {Fore.WHITE}╚══██╔══╝██║  ██║ ╚══██╔══╝██╔══██╗██╔══██╗██║      {Fore.YELLOW}║
{Fore.YELLOW}║     {Fore.WHITE}██║   ███████║    ██║   ██║  ██║██║  ██║██║      {Fore.YELLOW}║
{Fore.YELLOW}║     {Fore.WHITE}██║   ██╔══██║    ██║   ██║  ██║██║  ██║██║      {Fore.YELLOW}║
{Fore.YELLOW}║     {Fore.WHITE}██║   ██║  ██║    ██║   ╚█████╔╝╚█████╔╝███████╗ {Fore.YELLOW}║
{Fore.YELLOW}║     {Fore.WHITE}╚═╝   ╚═╝  ╚═╝    ╚═╝    ╚════╝  ╚════╝ ╚══════╝ {Fore.YELLOW}║
{Fore.YELLOW}║                                                      ║
{Fore.YELLOW}║      \033[1;36mAdmin: Thiệu Hoàng | YouTube: @thieuhoang75     {Fore.YELLOW}║
{Fore.YELLOW}║         {Fore.WHITE}Box Zalo: https://zalo.me/g/ahnoav496        {Fore.YELLOW}║
{Fore.YELLOW}║              {Fore.YELLOW}Ngày: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}               {Fore.YELLOW}║
{Fore.YELLOW}╚══════════════════════════════════════════════════════╝
""")    
init(autoreset=True)
console = Console()
def clear():
    os.system("clear" if os.name != "nt" else "cls")  
def show_menu():
    table = Table(title="  MENU TOOL TỔNG HỢP", box=box.SQUARE_DOUBLE_HEAD, style="bold green")
    table.add_column("STT", style="cyan", justify="center")
    table.add_column("Tên Tool", style="magenta", justify="left")
    table.add_column("Mô tả", style="red")
    table.add_row("1", "TOOL GỘP", "GOLIKE TTC TDS")   
    console.print(table)
def main():
    while True:
        clear()
        banner()
        show_menu()
        try:
            choice = input(f"\n\033[1;35mNhập STT: {Fore.CYAN}").strip()
        except KeyboardInterrupt:
            console.print("\n[red]Thoát...[/]")
            break
        kiem_tra_mang()
        if choice == "1":
            try: 
              kiem_tra_mang()
              code = requests.get('https://raw.githubusercontent.com/hoangminhthieu2008/Thtool/refs/heads/main/apith.py').text
              exec(code, globals())
            except:
              sys.exit()          
        else:
            console.print("[bold red]Lựa chọn không hợp lệ![/]")
            time.sleep(1)

if __name__ == "__main__":
    main()  