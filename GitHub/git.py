import subprocess
from pyfiglet import figlet_format
from termcolor import cprint
import yaml
from multiprocessing import Pool
import os
import requests


logo = 'Git-Commands'
api = "https://circuitalminds.herokuapp.com/api/"
token = "circuitalminds"


class Color:
    NOTICE = '\033[91m'
    END = '\033[0m'


info = Color.NOTICE + '''
Automate the process of using commands such as clone, commit, branch, pull, merge, blame and stash.\n''' + Color.END


def run(*args):
    return subprocess.check_call(['git'] + list(args))


def clone():
    print("\nYou will be asked for the user first and then the repository name.\n")

    user = input("User: ")
    __user__ = f'{user}'
    repo = input("Repository: ")
    __repo__ = f'{repo}'

    print("\nChoose the local path for your clone.")
    local = input("Local path: ")
    local_path = f'{local}'

    subprocess.Popen(['git', 'clone', "https://github.com/" + __user__ + "/" + __repo__ + ".git", local_path])


def commit():
    message = input("\nType in your commit message: ")
    commit_message = f'{message}'

    run("commit", "-am", commit_message)
    run("push", "-u", "origin", "master")


def branch():
    branch = input("\nType in the name of the branch you want to make: ")
    br = f'{branch}'

    run("checkout", "-b", br)

    choice = input("\nDo you want to push the branch right now to GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("push", "-u", "origin", br)

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def pull():
    print("\nPulls changes from the current folder if *.git is initialized.")

    choice = input("\nDo you want to pull the changes from GitHub? (y/n): ")
    choice = choice.lower()

    if choice == "y":
        run("pull")

    elif choice == "n":
        print("\nOkay, goodbye!\n")

    else:
        print("\nInvalid command! Use y or n.\n")


def fetch():
    print("\nFetches changes from the current folder.")
    run("fetch")


def merge():
    branch = input("\nType in the name of your branch: ")
    br = f'{branch}'

    run("merge", br)


def reset():
    filename = input("\nType in the name of your file: ")
    fl = f'{filename}'

    run("reset", fl)


def blame():
    file = input("\nType in the name of the file: ")
    fi = f'{file}'

    run("blame", fi)


def stash():
    print("\nDo you want to save, list, pop, show, branch, clear or drop? ")

    cmd = 'save, li, pop, show, branch, clear and drop'

    print("\nCommands to use: " + cmd)

    choice = input("\nType in the command you want to use: ")
    choice = choice.lower()

    if choice == "save":
        message = input("\nType in your stash message: ")
        stash_message = f'{message}'

        run("stash", "save", stash_message)

    elif choice == "li":
        run("stash", "li")

    elif choice == "pop":
        run("stash", "pop")

    elif choice == "show":
        run("stash", "show", "-p")

    elif choice == "branch":
        branch = input("\nType in the name of the branch you want to stash: ")
        br = f'{branch}'

        run("stash", "branch", br)

    elif choice == "clear":
        run("stash", "clear")

    elif choice == "drop":
        run("stash", "drop")

    else:
        print("\nNot a valid command!")
        print("\nUse " + cmd)


def get_info():
    repos = requests.get(api + "repos?token=" + token + "&option=get").json()
    for repo in list(repos.keys()):
        print(repo + " : " + repos[repo]["url"] + "\n")


def clone_simultaneously():
    containers = yaml.load(requests.get(
        api + "repos?token=" + token + "&name=alanmatzumiya/containers&option=get").text, Loader=yaml.FullLoader
                           ).get("alanmatzumiya/containers")
    options = ["img", "music"]
    processes = tuple(
        "git clone -b " + "music_" + str(j) + " " + containers.get("url") + " music_" + str(j) for j in range(1, 11))
    '''''
    def run_process(process):
        os.system('git clone {}'.format(process))

    pool = Pool(processes=len(processes))
    pool.map(run_process, processes)
    '''''
    print(processes)


def main():
    cprint(figlet_format(logo, font='slant'), 'green')
    print(info + "\n")

    choices = 'get info, clone, clone containers, commit, branch, pull, fetch, merge, reset, blame and stash'
    print("Commands to use: " + choices)

    choose_command = input("Type in the command you want to use: ")
    choose_command = choose_command.lower()

    if choose_command == "clone":
        clone()

    elif choose_command == "get info":
        get_info()

    elif choose_command == "clone containers":
        clone_simultaneously()

    elif choose_command == "commit":
        commit()

    elif choose_command == "branch":
        branch()

    elif choose_command == "pull":
        pull()

    elif choose_command == "fetch":
        fetch()

    elif choose_command == "merge":
        merge()

    elif choose_command == "reset":
        reset()

    elif choose_command == "blame":
        blame()

    elif choose_command == "stash":
        stash()

    else:
        print("\nNot a valid command!")
        print("\nUse " + choices)


if __name__ == '__main__':
    main()
