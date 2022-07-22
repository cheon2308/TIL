# GIT

### Repository

> 특정 디렉토리를 버전 관리하는 저장소
> 
> `git init` 명령어로 로컬 저장소를 생성
> 
> `.git` 디렉토리에 버전 관리에 필요한 모든 것이 들어있음
> 
> **폴더 안에서 관리하자** -> 바탕화면에서 하면 원하는 대로 폴더 별이 아닌 하나의 git으로 관리됨

## 명령어

1. git init으로 시작

2. git status로 현재 상태 확인 가능

3. git add로 추가 
   
   > git add 파일이름 파일이름 파일이름

4. commit
   
   > git config --global user.email "you@example.com"
   > 
   > git config --global user.name "Your Name"
   > 
   > 이용하여 저장
   > git commit -m " 내용 "

5. git log 로 변경 내용 확인가능
   
   > ​    git log --oneline으로 간편히 보기 가능
   > 
   > ​    이 때 나오는 5b794c6 이런 숫자가 컴퓨터 인식 이름
   > 
   > ​    head -> master 에서 head는 branch 이름 

​    **저장 후 수정하고 다시 log확인 시 저장되었던 파일에서 only 수정된 내용이 나타나는 것**

6. 원격 저장소
   
   > 위에 저장 한 것을 다른 곳에서도 볼 수 있게 하는 ''원격저장소''
   > 
   > git remote add origin https://github.com/cheon2308/TIL.git
   > 
   > git remote -v 원격저장 주소 보기

7. 단축 명령어
   
   > -u = upload, -v = view4

8. Git에서 가져 오기 
   
   > 최초로 가져올시 git clone 주소
   > 그 뒤 수정사항 가져올 때는 git pull 저장장소 master

## 기본기

1. Working Directory - 내가 작업하고 있는 실제 디렉토리
   
   (untracked)

2. Staging Area - 커밋으로 남기고 싶은, 특정 버전으로 고나리하고 싶은 파일이 있는 곳
   
   (staged)

3. Repository - 커밋들이 저장되는 곳
   
   (committed)
   
   > 위 3가지를 바탕으로 커밋(commit) 동작
   > 
   > 1 -> 2 = `git add`하면 2번으로 track되어 수정사항 반영
   > 
   > 2 ->3 = git commit -m " 메모 내용 | 메모 내용 "
   
   ###### why ??
   
   > 1 -> 3 으로 바로 commit하면 버전 세분화가 쉽지않다
   > 
   > 즉, 관리하고 싶지 않은 문서도 commit된다 .

### GIT HUB

###### -> TIL = TODAY I LEARNED