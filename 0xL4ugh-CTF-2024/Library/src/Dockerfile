FROM alpine:latest@sha256:51b67269f354137895d43f3b3d810bfacd3945438e94dc5ac55fdac340352f48
ENV PAGER=''
ENV FLAG='0xL4ugh{TrU5t_M3_LiF3_I5_H4rD3r!}'
RUN apk add socat python3 py3-pip
RUN adduser -D challenger
RUN pip3 install rich  --break-system-packages
WORKDIR /home/challenger
USER challenger
COPY challenge.py .
COPY exec.sh . 
ENTRYPOINT ["sh","exec.sh"]
