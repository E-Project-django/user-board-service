<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=150&section=header&text=E-Board&fontSize=40&animation=fadeIn&fontAlignY=38&desc=&descAlignY=51&descAlign=62" /><br/>
  
## <b> 프로젝트 주제 🖥️</br>
사용자 권한에 따른 게시판 권한(CRUD)제어</br> 
로그인 유저의 나이/시간/성별에 따른 통계 분석</br>

## <b> Team members 👋🏻 </br>

|윤성문|이승현|정병휘|한송희|
|:------:|:------:|:------:|:------:|
|[Github](https://github.com/tjdans1201) | [Github](https://github.com/blessian) | [Github](https://github.com/byeonghwijeong) | [Github](https://github.com/song-hee-1) |

<br />
</div>

## ⏳ 개발 기간
2022.08.31 ~ 2022.09.06    

## ⚙️ ERD
<div align="center">
<img width="608" alt="image" src="https://user-images.githubusercontent.com/95831345/188399711-3305c014-9a1f-4485-ad1f-240c75bd0213.png">
</div>

## ✍🏻 프로젝트 구현사항

- 유저 로그인 / 회원가입 / 회원탈퇴 구현 <br/>
    ▶️ token을 이용한 인증
    
- [3가지 게시판] User/Staff/Superuser의 게시판 ACCESS 제어
   - 자유게시판 <br/>
    ▶️ `User`와 `Superuser`는 게시글 ACCESS⭕  & `staff` UPDATE❌  
   - 운영게시판 <br/>
    ▶️ `Staff`와 `Superuser`는 게시글 ACCESS⭕ & `User`는 ACCESS❌  
   - 공지 <br/>
    ▶️ `Staff`와 `Superuser`는 게시글 ACCESS⭕ & `User`는 READ⭕   

- 사이트 이용 통계 집계 <br/>
    ▶️ pandas를 이용한 통계 분석
    
  - 전체 회원 중 집계 기간 내 로그인 유저 비율
  - 집계 기간 내 로그인 유저의 성별 비율
  - 집계 기간 내 로그인 유저의 나이대 비율
  - 집계 기간 내 로그인 유저의 성별과 나이대 비율
  - 집계 기간 내 로그인 남성 유저의 나이대 비율
  - 집계 기간 내 로그인 여성 유저의 나이대 비율
  - 집계 기간 내 로그인 유저의 매 시간 별 비율


