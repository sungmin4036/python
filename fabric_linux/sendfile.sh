#!/bin/sh
CONNIP="192.168.1.11"
USID="ncss3709"
USPW="hsck1009"
Local_Dir="/python_test" 
Remote_Dir="KSM"
BACKUPFILE="full.csv"

function FTP_UP()
{
    ftp -n -v ${CONNIP} <<EOF
    user $USID $USPW
    bin
    prompt
    cd ${Remote_Dir}
    put ${BACKUPFILE}
    bye
EOF
return
}

FTP_UP

# ascii : 전송모드를 ASCII모드로 설정한다.(ascii또는 as)
# binary : 전송모드를 BINARY모드로 설정한다.( binary또는 bi)
# bell : 명령어 완료시에 벨소리를 나게한다.(bell)
# bye : ftp접속을 종료하고 빠져나간다.(bye)
# cd : remote시스템의 디렉토리를 변경한다.(cd 디렉토리명)
# cdup : remote시스템에서 한단계 상위디렉토리로 이동한다.(cdup)
# chmod : remote시스템의 파일퍼미션을 변경한다.(chmod 755 index.html)
# close : ftp접속을 종료한다. (close)
# delete : remote시스템의 파일을 삭제한다.(delete index.old)
# dir : remote시스템의 디렉토리 내용을 디스플레이한다.(dir)
# disconnect : ftp접속을 종료한다.(disconnect)
# exit : ftp접속을 종료하고 빠져나간다.(exit)
# get : 지정된 파일하나를 가져온다.(get index.html)
# hash : 파일전송 도중에 "#"표시를 하여 전송중임을 나타낸다.(hash)
# help : ftp명령어 도움말을 볼 수 있다.(help또는 help 명령어)
# lcd : local시스템의 디렉토리를 변경한다.(lcd 디렉토리명)
# ls : remote시스템의 디렉토리 내용을 디스플레이한다. (ls 또는 ls -l)
# mdelete : 여러개의 파일을 한꺼번에 지울 때 사용한다.( mdelete *.old)
# mget : 여러개의 파일을 한꺼번에 가져오려할 때 사용한다. ( mget *.gz)
# mput : 한꺼번에 여러개의 파일을 remote시스템에 올린다.(mput *.html)
# open : ftp접속을 시도한다.(open 168.126.72.51또는 open ftp.kornet.net)
# prompt : 파일전송시에 확인과정을 거친다. on/off 토글 (prompt)
# put : 하나의 파일을 remote시스템에 올린다.(put index.html)
# pwd : remote시스템의 현재 작업디렉토리를 표시한다.(pwd)
# quit : ftp접속을 종료하고 빠져나간다.(quit)
# rstatus : remote시스템의 상황(version, 어디서, 접속ID등)을 표시한다.(rstatus)
# rename : remote시스템의 파일명을 바꾼다.(remote 현재파일명 바꿀파일명)
# rmdir : remote시스템의 디렉토리을 삭제한다.(rmdir 디렉토리명)
# size :remote시스템에있는 파일의 크기를 byte단위로 표시한다.(size index.html)
# status : 현재 연결된 ftp세션가지 모드에 대한 설정을 보여준다.(status)
# type : 전송모드를 설정한다.(type 또는 type ascii 또는 type binary)