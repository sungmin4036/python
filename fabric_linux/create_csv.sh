#!/bin/bash
# 필드 나누는 단위 (,) 쉼표
# source ./IP_address.sh
#리눅스에서는 리스트형 () 로 묶어줘야되고, 중간에 "," 없이 스페이스바로 해야함.
address=('IP주소' 'IP주소' 'IP주소' 'IP주소')
# echo $address

# READ=[$address] # 입력될 IP 주소 디렉터리
SAVE=full.csv # csv 생성

# for IP in "${address[@]}"
# do
#         count=$(($count+1))
#         echo $IP
#         echo $count
        
# done

for IP in "${address[@]}"
do
        echo "===============================================================================" >> $SAVE
        echo "===============================================================================" >> $SAVE
        
        echo "$IP,,,data" >> $SAVE
        cat /python_test/$IP/full.txt >> $SAVE

        # for LINE in $(cat /python_test/$IP/full.txt)
        # do
        #         echo "$IP,$LINE" >> $SAVE
        # done

        # while read LINE; do
        #         echo "$IP,$LINE" >> $SAVE
        # done #< /python_test/$IP/full.txt 


done
