import requests

# renk
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'

# xss payloadlarını alacağımız url
payloads_url = 'https://raw.githubusercontent.com/payloadbox/xss-payload-list/master/Intruder/xss-payload-list.txt'

# test edilecek url input
base_url = input("Test edilecek URL'yi girin (örn. http://www.example.com/search.php?query=): ").strip()

# github üzerinden payloadları alma / belirleme
def get_xss_payloads(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # her satırda bir payload şeklinde ayırma
            payloads = response.text.strip().split('\n')
            return payloads
        else:
            print(color.YELLOW + f"Hata: GitHub üzerinden payload'lar indirilemedi. Status Code: {response.status_code}" + color.END)
            return None
    except Exception as e:
        print(color.YELLOW + f"Hata: GitHub üzerinden payload'lar alınırken bir hata oluştu: {str(e)}" + color.END)
        return None

# payloadları al
xss_payloads = get_xss_payloads(payloads_url)

if xss_payloads:
    print(color.BLUE + f"GitHub'dan {len(xss_payloads)} adet XSS payload başarıyla alındı." + color.END)

    # bütün payloadlarla urlyi test et
    for payload in xss_payloads:
        full_url = base_url + payload
        response = requests.get(full_url)
        
        # yanıtı kontrol et ve xss payloadının çalışıp çalışmadığını söyle
        if payload in response.text:
            print(color.GREEN + f"XSS açığı bulundu! Payload: {payload}" + color.END)
        else:
            print(color.RED + f"XSS açığı bulunamadı! Payload: {payload}" + color.END)

else:
    print(color.YELLOW + "XSS payload'ları alınamadı. Lütfen tekrar deneyin veya GitHub URL'sini kontrol edin." + color.END)
