# https://stepik.org/lesson/24460/step/10?unit=6766

def create(namespace, parent):
    scopes[namespace] = {'parent': parent, 'variables': set()}
def add(namespace, var):
    scopes[namespace]['variables'].add(var)
def get(namespace, var):
    if namespace == None:
        return None
    if var in scopes[namespace]['variables']:
        return namespace
    return get(scopes[namespace]['parent'], var)
 
n = int(input())
scopes = {'global': {'parent': None, 'variables': set()}}
for _ in range(n):
    cmd, namesp, arg = input().split()
    if cmd == 'create':
        create(namesp, arg)
    elif cmd == 'add':
        add(namesp, arg)
    elif cmd == 'get':
        print(get(namesp, arg))
