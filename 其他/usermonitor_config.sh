#!/bin/sh

USER_MONITOR_FILE=/var/log/usermonitor/usermonitor.log

if [ -e "${USER_MONITOR_FILE}" ];then
    return 1
fi

mkdir -p $(dirname "${USER_MONITOR_FILE}") && \
    touch "${USER_MONITOR_FILE}"

chown nobody:nobody "${USER_MONITOR_FILE}" && \
    chmod 002 "${USER_MONITOR_FILE}" && \
    chattr +a "${USER_MONITOR_FILE}"

echo export USER_MONITOR_FILE="${USER_MONITOR_FILE}" >> /etc/profile
echo export PROMPT_COMMAND='{ date "+%y-%m-%d %T %z ## $(who am i |awk "{print \$1\" \"\$2\" \"\$5}") ## $(whoami) ## $(history 1 | { read x cmd; echo "$cmd"; })"; } >>$USER_MONITOR_FILE' >> /etc/profile
source  /etc/profile
