[TOC]

# Git

>  Git은 분산버전관리시스템(DVCS, Distributed Version Control System)이다. 

>  소스코드의 버전 및 이력을 관리할 수 있다.

## 기본 설정

- 윈도우에서 git을 활용하기 위해서 git bash를 설치한다.

- git을 활용하기 위해서 GUI 툴인 `source tree`,`github desktop`등을 활용할 수도 있다.

- 초기 설치를 완료한 이후에 컴퓨터에 `author`정보를 입력한다.

```bash
$ git config --global user.email "메일주소"
$ git config --global user.name "유저네임"
```

지정된 설정 확인

```bash
$ git config --global -l
# $ git config --global --list
```

## 로컬 저장소(repository) 활용하기

### 저장소 초기화

```bash
$ git init

Initialized empty Git repository in C:/Users/student/Desktop/git_class
student@M172 MINGW64 ~/Desktop/git_class (master)
```

* `.git`폴더가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.

* git bash에 `(master)` 라고 표시되는데, 이는 현재 `master` branch에 있다는 뜻이다.

>  주의사항

>  - git 저장소 내에 또다른 git 저장소를 만들면 안됨 !!

>  - `git init` 명령어를 입력할 때, `(master)`가 있으면 절대! 입력하지 말 것!

### add

>  `working directory`, 즉 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야한다.

```bash
$ git add 파일명

$ git add . # 현재 디렉토리(하위 디렉토리)

$ git add a.txt # 특정 파일

$ git add my_folder/ # 특정 폴더
```

* `add` 전 상태

```bash
$ git status

On branch master
No commits yet

# 트래킹 되고 있지 않는 파일들
# => commit 이력에 한번도 담기지 않은 파일들
Untracked files:

# 커밋될 것들에 포함시키려면 add 명령어를 사용
  (use "git add <file>..." to include in what will be committed
        markdown.md

# 아직 커밋될 것들은 없지만
# untracked files은 존재한다.
nothing added to commit but untracked files present (use "git add" to track)
```

* `add` 후 상태

```bash
$ git status

On branch master
No commits yet
# 커밋될 변화들

# => staging area에 있는 파일들
Changes to be committed:
  (use "git rm --cached <file>..." to unstage
        new file:   markdown.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        git.md
```

### commit

>  commit은 이력을 확정짓는 명령어로, 해당 시점의 스냅샷을 기록한다.

>  commit 시에는 반드시 메시지를 작성 해야하며, 메시지는 변경사항을 알 수 있도록 명확하게 작성한다.

```bash
$ git commit -m '마크다운 정리'

[master (root-commit) 5313249] 마크다운 정리
 1 files changed, 104 insertions(+)
 create mode 100644 markdown.md
```

- 커밋 이후에는 아래의 명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log

commit 5313249e0c5aa5e9a2c5d77d44b3e73434617cfc (HEAD -> master)
Author: sinclairjang <viktor-hugo@gmail.com>
Date:   Thu Dec 26 14:34:35 2019 +0900
    마크다운 정리

$ git log --oneline

5313249 (HEAD -> master) 마크다운 정리
```

- 커밋은 해시값을 바탕으로 구분된다.

- 커밋 목록은 `git log`를 통해서 확인할 수 있다.

---

# 원격 저장소 (remote repository)

## 기본 설정

1. 로컬 git 저장소 준비

2. Github repository 생성

3. Repository default branch 변경 (settings -> repositories)

- main -> master로 변경

<br>

## 명령어

### 원격 저장소 주소 추가

```bash
$ git remote add origin 저장소URL
```

- origin은 추가하는 원격 저장소 이름!

<br>

### 원격 저장소 목록 보기

```bash
$ git remote -v

origin  https://github.com/viktor-hugo/TIL.git (fetch)
origin  https://github.com/viktor-hugo/TIL.git (push)
```

>  잘못 add 한 경우 삭제하기

```bash
 $ git remote rm origin
```

### push

>  원격 저장소에 업로드

```bash
$ git push -u origin master

Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 12 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (8/8), 645 bytes | 645.00 KiB/s, done.
Total 8 (delta 0), reused 0 (delta 0), pack-reused 0
To https://github.com/viktor-hugo/TIL.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
```

>  **원격 저장소에는 commit이 올라간다 !**

>  즉, commit 이력이 없다면 push 할 수 없다.

- 두번째 push 부터는 `-u` 생략 가능

<br>

### pull

>  원격 저장소의 변경사항만을 받아옴 (업데이트)

```bash
$ git pull origin master
```

<br>

### clone

>  원격 저장소 전체를 복제

```bash
$ git clone 저장소URL
```

>  **[주의사항]**

>  - clone 받은 프로젝트는 이미 `git init`이 되어있음 (`remote` 도 추가되어 있음)
