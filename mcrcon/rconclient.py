import asyncio
from mcrcon import MCRcon

loop = asyncio.get_event_loop()
inp = True

def get_info():
    host = input("Enter the host: ")
    if not host:
        raise Exception("host is a required")
    
    port = input("Enter the port (Default 25575): ")
    if not port:
        port = 25575
    else:
        if not port.isdigit():
            raise TypeError("port must be a int")
    
    passwd = input("Enter the password: ")
    if not passwd:
        raise Exception("password is a required")
    
    return {
        "host": host,
        "port": int(port),
        "passwd": passwd
    }

async def main():
    global inp
    
    try:
        r = get_info()
    except Exception as exc:
        print(exc)
        return
    
    try:
        client = MCRcon(r["host"], r["passwd"], r["port"])
        client.connect()
    except Exception as exc:
        print(exc)
        return
    
    while inp is True:
        cmd = input(">> ")
    
        if cmd == "exit":
            inp = False
            client.disconnect()
            break
        elif (cmd == "" or cmd == None):
            print("Type `exit` or Ctrl+C to exit rcon console")
            continue
        else:
            print(client.command(cmd))

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        inp = False