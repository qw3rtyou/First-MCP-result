# Command Injection CTF Challenge

## 문제 설명
이 CTF 문제는 command injection 취약점을 포함하고 있는 웹 애플리케이션입니다. 사용자는 까다로운 필터링을 우회하여 시스템 명령을 실행하고 플래그를 획득해야 합니다.

## 도전 과제
- 웹 인터페이스를 통해 호스트/IP 주소에 대한 ping 요청을 보낼 수 있습니다.
- 입력값에 대한 엄격한 필터링이 적용되어 있습니다.
- 목표는 필터링을 우회하여 `/flag.txt` 파일의 내용을 읽는 것입니다.

## 설치 및 실행 방법
```bash
# 도커 컴포즈로 실행
docker-compose up --build

# 또는 도커로 직접 실행
docker build -t ctf-challenge .
docker run -p 5555:5555 ctf-challenge
```

## 접속 방법
- 웹 브라우저에서 `http://localhost:5555` 접속
- 입력창에 호스트명이나 IP 주소를 입력하여 ping 테스트

## 보안 특징
- 입력값 필터링
  - 특수문자 제한
  - 위험한 명령어 블랙리스트
  - 길이 제한
  - 인코딩 필터링
- 컨테이너 보안
  - 최소 권한 원칙 적용
  - 읽기 전용 파일시스템
  - 권한 상승 방지
  - 모든 Linux capabilities 제거

## 힌트
1. 기본적인 command injection 시도는 모두 차단됩니다.
2. 블랙리스트를 우회할 수 있는 방법을 찾아보세요.
3. Linux 명령어에는 여러 가지 대체 방법이 있습니다.