# CLI
- Command line Interface
- 새 폴더 만들기
    1. mkdir = make directory 만들기
    2. 작업 위치를 new_ folder로 이동 (cd = change directory)

- 팁 목록
    1. CLI에서 . 은 자신의 위치(상대경로에서의 현재 위치)
    2. code . <- 현재 폴더를 vscode로 열어줘 ex)code . README.md
```bash

mkdir cd new_folder

```

- 현재 작업 위치의 파일 목록
```bash
$ ls
```

- 파일의 이름을 바꾸거나 위치를 옮길때
```bash
$ mv {이동할 대상} {이동할 위치}
$ mv {이름 바꿀 대상} {바꿀 이름}
```

### 상대 경로 절대 경로
1. 절대 경로
/c/Users/SSAFY/Desktop/new_folder
2. 상대 경로
- 나를 기준으로 경로를 지정 (.을 기준으로 .은 지금위치, ..은 한단계 전)
- 삭제 (remove)
```bash
$ rm {파일 명}
$ rm -r {폴더 명}
```