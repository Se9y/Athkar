try:
    import requests
    import random
    import time
    from os import system
    system("title " + "Soud Was Here - @_agf - Soud#0737")

except Exception as m:
    print(m)
    input("Press Any Key To Exit...\n")
    exit()
############################################
#                                          #
#   Bot Athkar By Soud                     #
#   Instagram: @_agf                       #
#   Discord: Soud#0737                     #
#   Idea & Thanks To @0xDwas - @Dwa9       #
#                                          #
############################################

se = 0

re = requests.get("https://pastebin.com/raw/AmRLni6r")  # اذكار و احاديث
ree = re.json()
na = int(input("[Pls Enter Mode]\n\n1) Telegram Bot\n2) Discord Webhook\n3) Exit\n\n>> "))

if na == 1:
    token = input("Pleae Enter Bot Token: ")
    print("Checking Token...\n")
    stt = requests.get(f"https://api.telegram.org/bot{token}/getMe")

    if 'ok":false' in stt.text:
        print("Wrong Bot Token\n")
        time.sleep(2)
        exit()

    elif 'ok":true' in stt.text:
        print("Correct Bot Token\n")

        idd = input("Please Enter Chat ID: ")
        print("Checking ID...\n")

        if 'ok":false' in stt.text:
            print("Wrong ID\n")
            time.sleep(2)
            exit()

        elif 'ok":true' in stt.text:
            print("Correct ID\n")
            while 1:
                rn = random.choice(ree)
                url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text={rn}"
                tele = requests.get(url)
                se += 1
                print(f"Sent to Telegram | {se}")
                time.sleep(60)

        else:
            print("Something Wrong\n")
            time.sleep(2)
            exit()

    else:
        print("Something Wrong\n")
        time.sleep(2)
        exit()

elif na == 2:
    webhook = input("Please Enter Your Webhook: ")
    print("Checking Webhook...\n")
    des = requests.get(webhook)

    if "Unknown Webhook" in des.text:
        print("Wrong Webhook\n")
        time.sleep(2)
        exit()

    elif "token" in des.text:
        print("Correct Webhook\n")
        while 1:
            rn = random.choice(ree)

            data = {
                "content": "سبحان الله وبحمده عدد خلقه ورضا نفسه وزنة عرشه ومداد كلماته",
                "embeds": [
                    {
                        "title": "أَسْتَغْفِرُ اللَّهَ الْعَظِيمَ الَّذِي لَا إِلَهَ إِلَّا هُوَ الْحَيُّ الْقَيُّومُ ، وَأَتُوبُ إِلَيْهِ",
                        "description": rn,
                        "color": 65331,
                        "author": {
                            "name": "سورة البقرة كاملة بصوت الشيخ عبد الباسط عبد الصمد Surah Al Baqarah",
                            "url": "https://www.youtube.com/watch?v=IEC8wi6wpGg",
                            "icon_url": "https://i.ytimg.com/vi/IEC8wi6wpGg/hqdefault.jpg"
                        }
                    }
                ],
                "username": "اذكار 🌹",
                "avatar_url": "https://a.top4top.io/p_18623e0571.jpg"
            }
            dis = requests.post(webhook, json=data)
            se += 1
            print(f"Sent to Discord | {se}")
            time.sleep(60)

    else:
        print("Something Wrong\n")
        time.sleep(2)
        exit()


elif na == 3:
    print("bye")
    exit()

else:
    print("Wrong Number")
    time.sleep(4)
    exit()
