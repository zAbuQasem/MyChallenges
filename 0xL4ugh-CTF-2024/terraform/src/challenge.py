import subprocess
from banner import monkey

BLACKLIST = ["|","'",";", "$", "\\", "#", "*", "&", "^", "@", "!", "<", ">", "%", ":", ",", "?", "{", "}", "`","diff","/dev/null","patch","./","alias","push"]

def is_valid_utf8(text):
    try:
        text.encode('utf-8').decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False

def get_terraform_commands():
    commands = []
    print("Enter terraform console commands (Enter an empty line to end):")
    while True:
        try:
            user_input = input("")
        except (EOFError, KeyboardInterrupt):
            break

        if not user_input:
            break

        if not is_valid_utf8(user_input):
            print(monkey)
            exit(1337)

        for command in user_input.split(" "):
            for blacklist in BLACKLIST:
                if blacklist in command:
                    print(monkey)
                    exit(1337)
        commands.append(user_input)
        
        if len(commands) > 1:
            print(monkey)
            exit(1337)

    return commands

def execute_terraform_commands(commands):
    for command in commands:
        cmd = f"echo '{command}' | terraform console"
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()

        if "0xL4ugh{Tf_sT4t3_AnDr0_T4t3}" in output:
            print(monkey)
            exit(1337)
        else:
            print(output)

commands = get_terraform_commands()
execute_terraform_commands(commands)
