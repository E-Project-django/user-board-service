# User boad Service



## 👋🏻 팀원 및 업무분담

|윤성문|이승현|정병휘|한송희|
|:------:|:------:|:------:|:------:|
|[Github](https://github.com/tjdans1201) | [Github](https://github.com/blessian) | [Github](https://github.com/byeonghwijeong) | [Github](https://github.com/song-hee-1) |
|회원 API 개발|통계 API 개발|문서화|게시판 API 개발|


</br>

## ⏳ 개발 기간
2022.08.31 ~ 2022.09.05   

</br>
  
## 🖥️ 프로젝트


#### 프로젝트 주체 

![웨인힐스브라이언트에이아이](https://user-images.githubusercontent.com/83492367/188452413-d9898495-f2a4-49a1-988b-261d02d24e83.png)

[Wayne Hills Bryant A.I](https://www.waynehills.co/)


#### 프로젝트 설명

회원 정보 내용을 포함하는 테이블을 설계하고 다음과 같은 기능을 제공하는 서버 개발

- **회원 정보**
  - 고객명, 회원등급, 성별, 나이, 연락처, 가입일, 마지막 접속일
 
- **REST API 기능**
  - 공지사항, 자유게시판, 운영자 게시판
  - 회원 등급에 따른 게시판 기능 접근제어
  - 회원가입, 로그인, 회원탈퇴
  - 이용 통계집계 ( 남 · 여 / 나이 / 접속시간 별)



<br/>

## 🧹 사용된 기술
- **Back-End** : Python, Django, Django REST framework
, Pandas
- **ETC** : Git, Github

<br>

## ⚙️ ERD
<img width="608" alt="image" src="https://user-images.githubusercontent.com/95831345/188399711-3305c014-9a1f-4485-ad1f-240c75bd0213.png">
</div>

</br>
## 🛠 Unit test

- 핵심 기능이라 판단한 **게시판**과 **통계 분석 api** 에 대해 **총 29개**의 테스트 코드를 작성 ( 게시판테스트 18개, 통계 분석 테스트 11개 )

![image](https://user-images.githubusercontent.com/83492367/188457691-4f931106-3ddb-44ee-8e55-38c96b9c061e.png)

</br>

## ✍🏻 프로젝트 구현사항

- **유저 로그인 / 회원가입 / 회원탈퇴 API**
    -  회원가입 시 생성되는  `DRF auth token`을 바탕으로 **로그인 시 유효성 검증**
    -  회원탈퇴 시 DB에서 직접 삭제되지 않고 `is_active`를 비활성화함으로써 **soft delete** 구현

- **자유게시판, 공지사항, 운영자게시판 API**
   - 각 게시판의 list view에서는 `수정시간` 필드 제외 
   - `제목`과 `본문` 내용을 토대로 **검색 기능** 구현
   - `cusor pagination`을 이용한 **pagination** 구현


- **권한 부여**
	- 회원  ( `사용자(User)`, `관리자(Staff)`, `운영자(SuperUser)` )
   		- 회원 가입은 누구나 가능하지만, 회원 목록은 관리자만 접근 가능
   		- 회원 정보 수정은 본인만 가능
   		- 관리자 임명은 관리자만 접근 가능
   		- 회원 탈퇴는 관리자와 본인 접근 가능

   - 게시판
		- 자유게시판 : 작성자와 관리자는 게시글에 대한 전체 액세스 권한, 운영자는 게시판을 삭제하되 편집 할 수 없음
		- 공지사항 : 운영자와 관리자는 게시글에 대한 전체 액세스 권한, 사용자는 읽기 권한만 가짐
		- 운영자 게시판 : 운영자와 관리자는 게시글에 대한 전체 액세스 권한, 사용자는 모든 권한을 가지지 않음 (읽기 불가)




- **사이트 이용 통계 집계 API**
	-  **Pandas**를 이용하여 남 · 여 / 나이 / 접속시간을 이용한 다양한 통계 구현
	-  DAU, WAU, MAU 서비스 측정을 위해 전체 회원 중 **집계 기간 내 로그인한 사용자 비율** 구현
    -  구현한 통계 사항들
    
  		- 전체 회원 중 집계 기간 내 로그인한 사용자 비율
  		- 집계 기간 내 로그인한 사용자의 성별 비율
  		- 집계 기간 내 로그인한 사용자의 나이대 비율
  		- 집계 기간 내 로그인한 사용자의 성별과 나이대 비율
  		- 집계 기간 내 로그인한 사용자 유저의 나이대 비율
  		- 집계 기간 내 로그인한 사용자 유저의 나이대 비율
  		- 집계 기간 내 로그인한 사용자의 매 시간 별 비율

