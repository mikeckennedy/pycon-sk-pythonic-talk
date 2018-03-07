
def connect_v1(user, server, replicate, use_ssl):
    print("Connect v1, called with: ")
    print(f"User = {user}")
    print(f"Server = {server}")
    print(f"Replicate = {replicate}")
    print(f"Use SSL = {use_ssl}")
    print()

def connect_v2(*, user, server, replicate, use_ssl):
    print("Connect v2, called with: ")
    print(f"User = {user}")
    print(f"Server = {server}")
    print(f"Replicate = {replicate}")
    print(f"Use SSL = {use_ssl}")
    print()


print("******************* V1 *******************")
print("*")
connect_v1('mkennedy', 'db_svr', True, False)
connect_v1(user='mkennedy', server='db_svr', replicate=True, use_ssl=False)

print()
print("******************* V2 *******************")
print("*")
connect_v2(user='mkennedy', server='db_svr', replicate=True, use_ssl=False)
connect_v2('mkennedy', 'db_svr', True, False)

print("done")
