# ==================================================
# ALARIC NYX SECURITY SCANNER v1.0
# Author: Alaric Nyx
# Purpose: Defensive Network Scanner
# ==================================================

import nmap
import datetime
from colorama import Fore, Style, init

init()


# Banner
print(Fore.RED + r"""

    █████╗ ██╗      █████╗ ██████╗ ██╗ ██████╗
   ██╔══██╗██║     ██╔══██╗██╔══██╗██║██╔════╝
   ███████║██║     ███████║██████╔╝██║██║     
   ██╔══██║██║     ██╔══██║██╔══██╗██║██║     
   ██║  ██║███████╗██║  ██║██║  ██║██║╚██████╗
   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝


        ALARIC NYX SECURITY SCANNER

        Cybersecurity | DFIR | SOC Tool

""" + Style.RESET_ALL)



# Nmap Check

print(Fore.YELLOW + "[+] Checking Nmap...")


try:
    scanner = nmap.PortScanner()

except Exception as error:

    print(Fore.RED)
    print("Nmap Error Found:")
    print(error)

    input("\nPress Enter to exit...")
    exit()



print(Fore.GREEN + "[+] Nmap Ready")



# Target Input

target = input(
    Fore.CYAN +
    "\nEnter Authorized Target IP: "
)



print(
    Fore.YELLOW +
    "\n[+] Starting Scan..."
)



start_time = datetime.datetime.now()



# Scan Function

try:

    scanner.scan(
        target,
        arguments="-sV"
    )


except Exception as error:

    print(Fore.RED)

    print("\nScan Failed:")
    print(error)

    input("\nPress Enter to exit...")
    exit()



end_time = datetime.datetime.now()



# Report

print(
    Fore.GREEN +
    "\n\n========== SCAN REPORT =========="
)



print(
    Fore.WHITE +
    f"""
Target      : {target}
Start Time  : {start_time}
End Time    : {end_time}
Duration    : {end_time-start_time}
"""
)



# Hosts Found

hosts = scanner.all_hosts()



if len(hosts) == 0:

    print(
        Fore.RED +
        "\nNo hosts found!"
    )


else:


    for host in hosts:


        print(
            Fore.RED +
            f"\nHost: {host}"
        )


        host_state = scanner[host].state()

        print(
            Fore.WHITE +
            f"Status: {host_state}"
        )



        for protocol in scanner[host].all_protocols():


            print(
                Fore.YELLOW +
                f"\nProtocol: {protocol}"
            )


            ports = scanner[host][protocol].keys()



            for port in ports:


                service = scanner[host][protocol][port]


                print(
                    Fore.GREEN +
                    f"""
----------------------------

Port     : {port}
State    : {service.get('state')}
Service  : {service.get('name')}
Product  : {service.get('product')}
Version  : {service.get('version')}

----------------------------
"""
                )



print(
    Fore.RED +
    "\n================================"
)

print(
    Fore.RED +
    " Scan Completed Successfully "
)

print(
    Fore.WHITE +
    " Created By: Alaric Nyx "
)


print(
    Fore.RED +
    "================================"
)



input(
    "\nPress Enter to close..."
)