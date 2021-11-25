import aiomysql
import asyncio

loop = asyncio.get_event_loop()
inp = True


def get_info():
    host = input("Enter the host: ")
    if not host:
        raise Exception("host is a required")
    
    port = input("Enter the port (Default 3306): ")
    if not port:
        port = 3306
    else:
        if not port.isdigit():
            raise TypeError("port must be a int")
    
    user = input("Enter the user: ")
    if not user:
        raise Exception("user is a required")
    
    passwd = input("Enter the password: ")
    if not passwd:
        raise Exception("password is a required")
    
    db = input("Enter the database: ")
    
    return {
        "host": host,
        "port": int(port),
        "user": user,
        "passwd": passwd,
        "db": db,
    }

async def main():
    global inp
    
    try:
        r = get_info()
    except Exception as exc:
        print(exc)
        return
    
    try:
        pool = await aiomysql.create_pool(host=r["host"], port=r["port"], user=r["user"], password=r["passwd"], db=r["db"], autocommit=True, cursorclass=aiomysql.cursors.DictCursor)
    except Exception as exc:
        print(exc)
        return
    
    while inp is True:
        sql = input(">> ")
    
        if sql == "exit":
            inp = False
            break
        elif (sql == "" or sql == None):
            print("Type `exit` or Ctrl+C to exit sql console")
            continue
        else:
            async with pool.acquire() as con:
                async with con.cursor() as c:
                    try:
                        await c.execute(sql)
                    except Exception as exc:
                        print(exc)
                    else:
                        print(await c.fetchall())
    
    pool.close()
    await pool.wait_closed()

if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        inp = False