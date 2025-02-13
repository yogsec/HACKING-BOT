import subprocess
import sys
import shutil
import concurrent.futures
import argparse
import time
from termcolor import colored


def print_banner():
    banner = """
    =======================================
    🔧 HACKING BOT | Designed by YogSec 🔧
    =======================================
    """
    print(colored(banner, "cyan"))


def load_tools_list(file_path):
    try:
        with open(file_path, 'r') as file:
            tools = [line.strip() for line in file.readlines() if line.strip() and not line.startswith('#')]
        return tools
    except FileNotFoundError:
        print(colored(f"⚠️ Error: {file_path} not found.", "red"))
        sys.exit(1)


def check_tool_installed(tool_name):
    if shutil.which(tool_name) is None:
        print(colored(f"⚠️ Warning: {tool_name} is not installed. Skipping...", "yellow"))
        return False
    return True


def execute_tool(command, output_file, progress, total):
    print(colored(f"⏳ Running: {command.split()[0]}...", "blue"))
    try:
        with open(output_file, 'w') as out:
            subprocess.run(command, shell=True, check=True, stdout=out, stderr=out)
    except subprocess.CalledProcessError as e:
        with open(output_file, 'a') as out:
            out.write(f"\n⚠️ Error executing {command}: {e}\n")
    progress[0] += 1
    percent_done = (progress[0] / total) * 100
    print(colored(f"🌟 {int(percent_done)}% done...", "green"))


def execute_tools_concurrently(domain, tools):
    progress = [0]
    total = len(tools)
    commands = {tool.replace("(domain here)", domain): f"{tool.split()[0]}_scan.txt" for tool in tools}

    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(execute_tool, commands.keys(), commands.values(), [progress] * len(commands),
                     [total] * len(commands))


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="🔧 HACKING BOT | Automated Bug Bounty Tool")
    parser.add_argument("-d", "--domain", help="Specify the target domain", required=True)
    parser.add_argument("-c", "--config", help="Specify a custom tools list file", default="tools-list.txt")
    parser.add_argument("-v", "--version", action="version", version="🔧 HACKING BOT v1.0 by YogSec")
    args = parser.parse_args()

    domain = args.domain
    tools_list_file = args.config
    tools = load_tools_list(tools_list_file)

    installed_tools = []
    for tool in tools:
        tool_name = tool.split()[0]
        if check_tool_installed(tool_name):
            installed_tools.append(tool)

    execute_tools_concurrently(domain, installed_tools)


if __name__ == "__main__":
    main()
