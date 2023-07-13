# GIT 이란...
> 분산 버전 관리 시스템

# GIT 초기화
```bash
$ git init
```

### 상태 확인 명령어

```bash
$ git status
```

#### stating aread에 추가
```bash
$ git add {path}<folder_name> / {file_name}
```

### Repository에 저장하기
```bash
$ git commit -m "commit message"
```

### GIt 기초 설정
```bash
git config --global user.email "chiru7080@daum.net"
git congif --global user.name "장현욱"
git config --global --list
```

### 커밋 기록 확인하기
```bash
$ git log
```
## 직전에 올린 파일(커밋) 이름 바꾸는법

```bash
$ git commit --amend
```

그 후 'insert' 버튼 누르고 원하는 부분 고친 후 ESC

:wq 입력 (write quit)

## git log 에서 나오는법
:q

## git 설정 초기화
```bash
# vim을 활용하여 설정 제거하기
# vim 으로 git 설정 파일 열기 바탕화면의 전 단계에서.
$ vim ~/. gitconfig
# insert -> : 누르기 -> 
$
```