FROM hashicorp/terraform:latest@sha256:7fdead7bc85e34f9bb42086a43b50a769c7d7601099aa44e44b07815388d41f9
RUN apk add python3 socat
WORKDIR /home/challenger
RUN adduser -D challenger
USER challenger
ENV TF_VAR_FLAG="0xL4ugh{Tf_sT4t3_AnDr0_T4t3}"
COPY entrypoint.sh .
COPY terraform-challenge .
COPY challenge.py .
COPY banner.py .
COPY exec.sh .
RUN terraform init && terraform apply -auto-approve
ENTRYPOINT ["sh","exec.sh"]
