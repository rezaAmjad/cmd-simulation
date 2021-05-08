class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.direc = []
        self.file = []


root = Directory(None, 'root')
current = root
path = 'root'


def mkdir(name):
    exist = False
    global current
    for n in current.direc:
        if name == n.name:
            exist = True
    if exist:
        return print("mkdir: {}: folder exists".format(name))
    else:
        d = Directory(current, name)
        current.direc.append(d)
        return


def ls():
    global current
    for j in range(len(current.file)):
        print(current.file[j])
    for i in current.direc:
        print(i.name)


def touch(name):
    global current
    exist = False
    for file in current.file:
        if file == name:
            exist = True
            break
    if exist:
        return print(" This file already exists in the directory")
    else:
        current.file.append(name)
        return


def cd(name):
    global path, current
    if name == "..":
        if current.parent is not None:
            current = current.parent
            path = current.name
    elif name == "~" and path != "root":
        path = "root"
    else:
        for d in current.direc:
            if d.name == name:
                current = d
                path = str(name)
                return
        return print('No such file or directory')


def main():
    while True:
        print(path,  end='$ ')
        command = input().split(' ')
        if command[0] == 'mkdir':

            mkdir(command[1])

        elif command[0] == 'ls':
            ls()

        elif command[0] == 'touch':
            touch(command[1])

        elif command[0] == 'cd':
            cd(command[1])

        else:
            print('{} is not the correct command'.format(command[0]))


if __name__ == '__main__':

    main()