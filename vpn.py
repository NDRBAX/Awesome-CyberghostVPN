import asyncio
import subprocess
import pyfiglet
from simple_term_menu import TerminalMenu
from prettytable import PrettyTable

#Color
R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset

logo = pyfiglet.figlet_format("CyberghostVPN", font = "slant"  )
print(logo)

# REGULAR WEB
countryData = PrettyTable(["Country","a","s","d","f","r"])
countryData.add_row([ Y+"Austria"+N, R+"AT"+N, Y+"Belgium"+N, R+"BE"+N, Y+"Germany"+N, R+"DE"+N ])
countryData.add_row([ Y+"United-Kingdom"+N, R+"GB"+N, Y+"Finland"+N, R+"FI"+N, Y+"China"+N, R+"CN"+N ])
countryData.add_row([ Y+"Russia"+N, R+"RU"+N, Y+"Lithuania"+N, R+"LT"+N, Y+"Ukraine"+N, R+"UK"+N ])

# STREAMING
streamingData = PrettyTable(["Service", "Country Code","d", "e", "a", "m"])
streamingData.add_row([Y+"RTBF Auvio BE"+N, R+"BE"+N, Y+"YouTube SE"+N, R+"SE"+N, Y+"Crunchyroll"+N, R+"US"+N])
streamingData.add_row([Y+"Sky Go UK"+N, R+"GB"+N, Y+"Fox Sport"+N, R+"BR"+N, Y+"SRF TV"+N, R+"CH"+N])

# P2P TORRENT
torrentData = PrettyTable(["Country","a","s","d","f","r"])
torrentData.add_row([ Y+"Belarus"+N, R+"BY"+N, Y+"Bosnia"+N, R+"BA"+N, Y+"Bulgaria"+N, R+"BG"+N,  ])
torrentData.add_row([ Y+"Estonia"+N, R+"EE"+N, Y+"Finland"+N, R+"FI"+N, Y+"Croatia"+N, R+"HR"+N ])
torrentData.add_row([ Y+"Kazakhstan"+N, R+"KZ"+N, Y+"Lithuania"+N, R+"LT"+N, Y+"Latvia"+N, R+"LV"+N ])
torrentData.add_row([ Y+"Moldova"+N, R+"MD"+N, Y+"Montenegro"+N, R+"ME"+N, Y+"Mongolia"+N, R+"MN"+N ])
torrentData.add_row([ Y+"Poland"+N, R+"PL"+N, Y+"Romania"+N, R+"RE"+N, Y+"Serbia"+N, R+"RS"+N ])
torrentData.add_row([ Y+"Russia"+N, R+"RU"+N, Y+"Slovakia"+N, R+"SK"+N, Y+"Ukraine"+N, R+"UA"+N ])

def main():
    # MAIN MENU
    main_menu_title = " \n\n 📋 MAIN MENU\n"
    main_menu_items = ["    🚀 Quick connect        ",
                       "    🎛️ Advance connect      ",
                       "    🧾 Availables servers   ",
                       "    4. VPN Status           ",
                       "    5. Turn off VPN         ",
                       "    👋 Exit                 "]
    main_menu_cursor = "ᐉᐉᐉ "
    main_menu_cursor_style = ("fg_green", "bold")
    main_menu_style = ("bg_green", "fg_black")
    main_menu_exit = False

    main_menu = TerminalMenu(
        menu_entries=main_menu_items,
        title=main_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > QUICK CONNECT
    quick_menu_title = " \n\n 🚀 QUICK CONNECT\n"
    quick_menu_items = [ "    🌐 Regular Web Traffic      ",
                         "    📺 Streaming                ",
                         "    🍻 P2P Torrent              ",
                         "    👈 Go to back Main Menu     " ]
    quick_menu_back = False
    quick_menu = TerminalMenu(
        quick_menu_items,
        title=quick_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    ) 

    reg_menu_title = " \n\n 🌐 REGULAR WEB TRAFFIC\n"
    reg_menu_items = [ "    💻 Internet Surfing, gaming, streaming, VoIP services...    ",
                       "    🍻 Download or transfer data                                ",
                       "    👈 Go back                                                  " ]
    reg_menu_back = False
    reg_menu_exit = False
    reg_menu = TerminalMenu(
        reg_menu_items,
        title=reg_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > ADVANCE CONNECT
    advance_menu_title = " \n\n 🎛️ ADVANCE CONNECT\n"
    advance_menu_items = [ "    1️⃣   VPN Protocol             ",
                           "    2️⃣   Traffic Protocol         ",
                           "    3️⃣   Connection Type          ",
                           "    ✅  Click to confirm         ",
                           "    👈  Go back to Main Menu     " ]
    advance_menu_back = False
    advance_menu = TerminalMenu(
        advance_menu_items,
        title=advance_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > ADVANCE CONNECT > VPN PROTOCOL
    protocol_menu_title = " \n\n VPN PROTOCOL\n"
    protocol_menu_items = [ "OpenVPN", "WireGuard" ]
    protocol_menu_back = False
    protocol_menu = TerminalMenu(
        protocol_menu_items,
        title=protocol_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > ADVANCE CONNECT > TRAFFIC PROTOCOL
    traffic_menu_title = " \n\n TRAFFIC PROTOCOL\n"
    traffic_menu_items = [ "TCP", "UDP" ]
    traffic_menu_back = False
    traffic_menu = TerminalMenu(
        traffic_menu_items,
        title=traffic_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

     # MAIN MENU > ADVANCE CONNECT > CONNECTION TYPE
    type_menu_title = " \n\n CONNECTION TYPE\n"
    type_menu_items = [ "Regular Web", "Streaming", "P2P Torrent" ]
    type_menu_back = False
    type_menu = TerminalMenu(
        type_menu_items,
        title=type_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > AVAILABLE SERVERS
    list_menu_title = " \n\n AVAILABLES SERVERS\n"
    list_menu_items = ["1. Regular web traffic",
                       "2. Streaming",
                       "3. P2P Torrent",
                       "4. Go back"]
    list_menu_back = False
    list_menu = TerminalMenu(
        list_menu_items,
        title=list_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > AVAILABLE SERVERS > REGULAR WEB TRAFFIC
    regular_menu_title = " \n\n REGULAR WEB TRAFFIC LIST\n"
    regular_menu_items = [ "1. Show all countries",
                           "2. Cities / Countries",
                           "3. Servers / Cities",
                           "4. Go Back"]
    regular_menu_back = False
    regular_menu = TerminalMenu(
        regular_menu_items,
        title=regular_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > AVAILABLE SERVERS > STREAMING
    streaming_menu_title = " \n\n STREAMING LIST\n"
    streaming_menu_items = [ "1) Show all countries",
                             "2) Cities / Countries",
                             "~~~~~~~~~ BACK ~~~~~~~~~"]
    streaming_menu_back = False
    streaming_menu = TerminalMenu(
        streaming_menu_items,
        title=streaming_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    # MAIN MENU > AVAILABLE SERVERS > TORRENT
    torrent_menu_title = " \n\n P2P TORRENT LIST\n"
    torrent_menu_items = [ "1) Show all countries",
                           "2) Cities / Countries",
                           "~~~~~~~~~ BACK ~~~~~~~~~"]
    torrent_menu_back = False
    torrent_menu = TerminalMenu(
        torrent_menu_items,
        title=torrent_menu_title,
        menu_cursor=main_menu_cursor,
        menu_cursor_style=main_menu_cursor_style,
        menu_highlight_style=main_menu_style,
        cycle_cursor=True,
    )

    while not main_menu_exit:
        main_sel = main_menu.show()
        
        # VARIABLES
        PROTOCOL = None
        TRAFFIC = None
        TYPE = None
        CODE = None
        SERVICE = None

        if main_sel == 0:   # QUICK CONNECT
            while not quick_menu_back:
                edit_sel = quick_menu.show()

                # REGULAR WEB
                if edit_sel == 0:
                    while not reg_menu_back:
                        edit_sel = reg_menu.show()
                        # SURF
                        if edit_sel == 0:
                            print(countryData.get_string(title=G+"Cyberghost VPN ~ Regular"+N,
                                        header=False))
                            def surfConnect():
                                CODE = input("\n\t      ENTER COUNTRY CODE: ")
                                if CODE is None or len(CODE) > 2:
                                    print(R + "\nCode should conteins two characters ..." + N)
                                else : 
                                    async def main():
                                        print( G + "\nQuick connect selected ...\n" + N)
                                        process = subprocess.run(["sudo", "cyberghostvpn", "--country-code", CODE, "--openvpn", "--udp", "--connect"], shell=False , check=True, text=True)
                                        await asyncio.sleep(1)
                                        print(G + "\nWell done ! You're now connected to Cyberghost VPN at " + CODE + " !" + N)
                                    asyncio.run(main())
                            surfConnect()
                            reg_menu_back = False
                        # DOWNLOADS
                        elif edit_sel == 1:
                            print(countryData.get_string(title=G+"Cyberghost VPN ~ Regular"+N,
                                        header=False))
                            def downloadConnect():
                                CODE = input("\n\t      ENTER COUNTRY CODE: ")
                                if CODE is None or len(CODE) > 2:
                                    print(R + "\nCode should conteins two characters ..." + N)
                                else : 
                                    async def main():
                                        print( G + "\nQuick connect selected ...\n" + N)
                                        process = subprocess.run(["sudo", "cyberghostvpn", "--country-code", CODE, "--openvpn", "--tcp", "--connect"], shell=False , check=True, text=True)
                                        await asyncio.sleep(1)
                                        print(G + "\nWell done ! You're now connected to Cyberghost VPN at " + CODE + " !" + N)
                                    asyncio.run(main())
                            downloadConnect()
                        elif edit_sel == 2:
                            reg_menu_back = True
                    reg_menu_back = False

                # STREAMING
                elif edit_sel == 1:
                    print(streamingData.get_string(title=G+"Cyberghost VPN ~ Streaming"+N,
                                        header=False))
                    def streamingConnect():
                        CODE = input("\n\t      ENTER COUNTRY CODE: ")
                        SERVICE = input("\n\t      ENTER SERVICE NAME: ")
                        if CODE is None or len(CODE) > 2 and SERVICE is None or len(SERVICE) < 0:
                            print(R + "\nWrong Code or Service Name ..." + N)
                        else : 
                            async def main():
                                print( G + "\nStreaming connect selected ...\n" + N)
                                process = subprocess.run(["sudo", "cyberghostvpn", "--streaming", SERVICE, "--country-code", CODE, "--connect"], shell=False , check=True, text=True)
                                await asyncio.sleep(1)
                                print(G + "\nWell done ! You're now connected to Cyberghost VPN at " + SERVICE + "-" + CODE + " !" + N)
                            asyncio.run(main())
                            edit_sel = quick_menu.show()
                    streamingConnect()
                # P2P Torrent
                elif edit_sel == 2:
                    print(torrentData.get_string(title=G+"Cyberghost VPN ~ Torrent"+N,
                                        header=False))
                    def torrentConnect():
                        CODE = input("\n\t      ENTER COUNTRY CODE: ")
                        if CODE is None or len(CODE) > 2:
                            print(R + "\nCode should conteins two characters ..." + N)
                        else : 
                            async def main():
                                print( G + "\nQuick connect selected ...\n" + N)
                                process = subprocess.run(["sudo", "cyberghostvpn", "--torrent", "--country-code", CODE, "--connect"], shell=False , check=True, text=True)
                                await asyncio.sleep(1)
                                print(G + "\nWell done ! You're now connected to Cyberghost VPN at " + CODE + " !" + N)
                            asyncio.run(main())
                            edit_sel = quick_menu.show()
                    torrentConnect()
                elif edit_sel == 3:
                                quick_menu_back = True
                                clear_screen = True
            quick_menu_back = False

        elif main_sel == 1:   # ADVANCE CONNECT
            while not advance_menu_back:
                edit_sel = advance_menu.show()
                # PROTOCOL
                if edit_sel == 0:
                    while not protocol_menu_back:
                            edit_sel = protocol_menu.show()
                            if edit_sel == 0:
                                PROTOCOL = "--openvpn"
                                print(G + "OpenVPN selected ..." + N)
                                protocol_menu_back = True
                            elif edit_sel == 1:
                                PROTOCOL = "--wireguard"
                                print(G + "WireGuard selected ..." + N)
                                protocol_menu_back = True
                    protocol_menu_back = False
                
                # TRAFFIC PROTOCOL
                elif edit_sel == 1:
                    while not traffic_menu_back:
                            edit_sel = traffic_menu.show()
                            if edit_sel == 0:
                                TRAFFIC = "--tcp"
                                print(G + "TCP selected ..." + N)
                                traffic_menu_back = True
                            elif edit_sel == 1:
                                TRAFFIC = "--udp"
                                print(G + "UDP selected ..." + N)
                                traffic_menu_back = True
                    traffic_menu_back = False
                
                # CONNECTION TYPE
                elif edit_sel == 2:
                    while not type_menu_back:
                        edit_sel = type_menu.show()
                        if edit_sel == 0:
                            print(countryData.get_string(title=G+"Cyberghost VPN ~ Regular"+N,
                                        header=False))
                            # CITY = input("\n\t      ENTER CITY NAME: ")
                            TYPE = "--traffic"
                            print(G + "Regular Web selected ..." + N)
                            type_menu_back = True
                        elif edit_sel == 1:
                            print(streamingData.get_string(title=G+"Cyberghost VPN ~ Streaming"+N,
                                                          header=False))
                            CODE = input("\n\t      ENTER COUNTRY CODE: ")
                            SERVICE = input("\n\t      ENTER SERVICE NAME: ")
                            TYPE = "--streaming"
                            print(G + "Streaming selected ..." + N)
                            type_menu_back = True
                        elif edit_sel == 2:
                            print(torrentData.get_string(title=G+"Cyberghost VPN ~ Torrent"+N,
                                                        header=False))
                            TYPE = "--torrent"
                            print(G + "P2P Torrent selected ..." + N)
                            type_menu_back = True
                    type_menu_back = False

                # CONNECT
                elif edit_sel == 3:
                    if PROTOCOL is None and TRAFFIC is None and TYPE is None:
                        print(R + "\nPlease select a protocol and a traffic type ..." + N)
                        advance_menu_back = False
                    elif SERVICE is not None and TYPE == "--streaming":
                        print(G + "\nStreaming connect to " + SERVICE + " ...\n" + N)
                        subprocess.run(["sudo", "cyberghostvpn", "--streaming", SERVICE, "--country-code", CODE, "--connect"], shell=False , check=True, text=True)
                    else:
                        CODE = input("\n\t      ENTER COUNTRY CODE: ")
                        print( G + "\nYou choose " + CODE + " server ...\n" + N) 
                        subprocess.run(["sudo", "cyberghostvpn", TYPE, "--country-code", CODE, PROTOCOL, TRAFFIC, "--connect"], shell=False , check=True, text=True)
                        print(G + "\nWell done ! You're now connected to Cyberghost VPN at " + CODE + " !" + N)
                # BACK
                elif edit_sel == 4:
                    advance_menu_back = True
            advance_menu_back = False

        elif main_sel == 2:   # AVAILABLES SERVERS
            while not list_menu_back:
                edit_sel = list_menu.show()
                # REGULAR WEB
                if edit_sel == 0:
                    while not regular_menu_back:
                        edit_sel = regular_menu.show()

                        if edit_sel == 0:
                            # ALL COUNTRIES
                            process = subprocess.run(["sudo","cyberghostvpn", "--traffic", "--country-code"], shell=False, check=True, text=True)
                        elif edit_sel == 1:
                            # ONE COUNTRY // Country name 
                            CODE = input("\n\t      ENTER COUNTRY CODE: ")
                            process = subprocess.run(["sudo", "cyberghostvpn", "--traffic", "--country-code", CODE], shell=False, check=True, text=True)
                        elif edit_sel == 2:
                            # ONE CITY // Country name / City Name 
                            CODE = input("\n\t      ENTER COUNTRY CODE: ")
                            CITY = input("\n\t      ENTER CITY NAME: ")
                            process = subprocess.run(["sudo", "cyberghostvpn", "--traffic", "--country-code", CODE, "--city", CITY], shell=False, check=True, text=True)
                        elif edit_sel == 3:
                            regular_menu_back = True
                            clear_screen = True
                    regular_menu_back = False                    
                # STREAMING
                elif edit_sel == 1:
                    while not streaming_menu_back:
                        edit_sel = streaming_menu.show()

                        if edit_sel == 0:
                             # ALL COUNTRIES
                            process = subprocess.run(["sudo", "cyberghostvpn", "--streaming", "--country-code"], shell=False, check=True, text=True)
                        elif edit_sel == 1:
                            # ONE COUNTRY // Country Name
                            CODE = input("\n\t      ENTER COUNTRY CODE: ")
                            process = subprocess.run(["sudo", "cyberghostvpn", "--streaming", "--country-code", CODE], shell=False, check=True, text=True)
                        elif edit_sel == 2:
                            streaming_menu_back = True
                            clear_screen = True
                    streaming_menu_back = False
                # TORRENT
                elif edit_sel == 2:
                    while not torrent_menu_back:
                        edit_sel = torrent_menu.show()
                        if edit_sel == 0:
                            # ALL COUNTRIES
                            process = subprocess.run(["sudo", "cyberghostvpn", "--torrent", "--country-code"], shell=False, check=True, text=True)
                        elif edit_sel == 1:
                            # ONE COUNTRY // Country Name
                            CODE = input("\n\t      ENTER COUNTRY CODE: ")
                            process = subprocess.run(["sudo", "cyberghostvpn", "--torrent", "--country-code", CODE], shell=False, check=True, text=True)
                        elif edit_sel == 2:
                            torrent_menu_back = True
                            clear_screen = True
                    torrent_menu_back = False
                elif edit_sel == 3:
                    list_menu_back = True      
            list_menu_back = False
        elif main_sel == 3:   # QUIT
            main_menu_exit = True
            print("Quit Selected")

if __name__ == "__main__":
    main()
