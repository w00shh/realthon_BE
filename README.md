<div align="center">
<h2>[2024 RE:ALThon] AquaLens 💻</h2>
SDGs 14. Life Below Water
</div>


## Index
  - [서비스 소개](#서비스-소개) 
  - [솔루션 소개](#솔루션-소개)
  - [기능적 구현](#기능적-구현)
  - [API 설명](#API-설명)
  - [팀원소개](#팀원-소개)


## 서비스 소개
  
### 배경
- SDGs 14. 해양 생태계 보존
  해양 자원을 보존하고 지속 가능하게 사용하는 것을 목표로 한다.
  불법 어업 활동으로 인하여 보호해야 할 수중 생태 자원들의 개체수 감소로 인하여, 환경이 파괴되고 있습니다. 수중 생태계의 균형을 깨뜨리고 결국 특정 종이 멸망한다면 돌이킬 수 없습니다.

### 해결 방안 제안
- 어업 활동 시 해당 포획에 문제가 없는지 곧바로 확인할 수 있다면? → 수중 생태계 보호!

## 솔루션 소개
- 어업 활동 시 해당 포획에 문제가 없는지 곧바로 확인 가능한 어플리케이션



### 라이센스
MIT


## 기능적 구현
![image.png](https://github.com/realthon-team1/realthon_FE/blob/main/image.png?raw=true)

## 기대 효과
- GPS를 연동하여 사용자 위치가 낚시 금지·제한 구역으로부터 특정 거리 이내에 해당할 시 어업 활동이 불가하다는 알림을 보낸다. 생태 보호 구역에 대한 경각심을 높여주는 효과를 기대한다. 

## API 설명
### 코드 구조

```cpp
└── realthon_BE
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── controller
    │   │   └── main_controller.py
    │   ├── core
    │   │   ├── gemini.py
    │   │   └── image.py
    │   ├── db
    │   │   └── session.py
    │   ├── main.py
    │   ├── schema
    │   │   └── main_schema.py
    │   └── util
    │       └── geo.py
    └── requirements.txt
```
```cpp
📦lib
 ┣ 📂app
 ┃ ┣ 📂data
 ┃ ┃ ┣ 📂api
 ┃ ┃ ┣ 📂extension
 ┃ ┃ ┣ 📂model
 ┃ ┃ ┣ 📂service
 ┃ ┣ 📂feature
 ┃ ┃ ┣ 📂chatbot
 ┃ ┃ ┃ ┣ 📂logic
 ┃ ┃ ┃ ┣ 📂widget
 ┃ ┃ ┣ 📂error
 ┃ ┃ ┣ 📂history
 ┃ ┃ ┃ ┣ 📂logic
 ┃ ┃ ┣ 📂home
 ┃ ┃ ┃ ┣ 📂logic
 ┃ ┃ ┃ ┣ 📂widget
 ┃ ┣ 📂widget
 ┃ ┃ ┣ 📂dialog
 ┣ 📜main.dart
 ┣ 📜secret.dart
 ┗ 📜service.dart
```

## 기능적 구현

0. 데이터베이스 연결
환경 변수(`dotenv`)에서 불러온 정보를 바탕으로, 데이터베이스에 연결되는 Pymongo 엔진을 생성합니다. client 객체를 만들어 데이터 세션 관리를 지원합니다.

1. 낚시 가능 구역 판별
최단거리를 구하는 공식인 하버사인 공식을 이용하여 정부24의 낚시 금지 구역 데이터와의 거리를 비교합니다. 데이터와의 거리가 5km 이내이면, 어획 불가능한 구역임을 반환하고, 그렇지 않으면 어획 가능함을 반환합니다.

2. 물고기 판별
업로드 된 이미지를 읽어 Gemini API를 통해 분석하고, 물고기에 대한 정보를 받습니다. 결과를 DB에 저장하고, 결과를 클라이언트에 반환합니다.

3. 추가 프롬프팅 진행
기존 프롬프트와 현재 프롬프트를 기반으로 추가 프롬프팅을 진행합니다. 분석 결과를 db에 업데이트합니다.

4. 유저 히스토리 반환
요청한 유저에게 질의한 히스토리를 반환합니다.

5. Gemini API
업로드된 이미지를 분석하여 물고기의 이름, 낚시 가능 여부, 설명, 추가 질문 목록 등의 정보를 반환하거나, 물고기가 아닌 경우 "ERROR"를 반환합니다. 또한, 이전 질문과 현재 질문을 기반으로 추가 프롬프팅을 진행합니다.

## 팀원 소개

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/25a80d8b-c81c-4889-ac1d-18981739e84a" width="60" height="60" alt="민준"> <strong>고려대 - 김민준</strong></td>
    <td>모바일 앱 개발</td>
  </tr>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/56007468?s=96&v=4" width="60" height="60" alt="우석"> <strong>성균관대 - 정우석</strong></td>
    <td>백엔드 개발</td>
  </tr>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/170783713?s=96&v=4" width="60" height="60" alt="효림"> <strong>고려대 - 손효림</strong></td>
    <td>Data 엔지니어링 & 기획</td>
  </tr>
  <tr>
    <td><img src="https://avatars.githubusercontent.com/u/190504308?s=96&v=4" width="60" height="60" alt="누르무시라"> <strong>고려대 - 누르무시라</strong></td>
    <td>Data 엔지니어링 & 기획</td>
  </tr>
</table>
