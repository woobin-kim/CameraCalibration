#!/usr/bin/python3
import argparse
import os
import sys

from scripts.thirdparty_script.install_opencv import install_opencv
from scripts.thirdparty_script.install_eigen import install_eigen

pwd = os.path.dirname(os.path.abspath(__file__))

class Password:
    def __init__(self, password):
        self.value = password
    
    def sudo(self):
        if self.value == "":
            return "sudo "
        return "echo " + self.value + " | sudo -S "


def main():
    # Setup parser
    parser = argparse.ArgumentParser()

    parser.add_argument('--d', action='store_true',
                        help='Flag for DebugMode')
    
    parser.add_argument('--opencv', type=str, default="",
                        help='OpenCV version. e.g. --opencv 4.5.0')

    parser.add_argument('--eigen', type=str, default="",
                        help='Flag for installing Eigen of specified version. (e.g. --eigen 3.3.9)')

    parser.add_argument('--password', type=str, default="",
                        help='Linux password')
    args = parser.parse_args()

    if len(sys.argv) == 1:
        parser.print_help()
        return

    # Set password
    if args.password != "":
        pw = Password(args.password)

    # Install essentials
    exec_string = "apt-get -y install"
    exec_string += " unzip"
    exec_string += " wget"
    exec_string += " curl"
    exec_string += " git"
    exec_string += " build-essential"
    exec_string += " cmake"
    exec_string += " gcc"
    exec_string += " clang-format"
    os.system(pw.sudo() + exec_string)

    # Install OpenCV
    if args.opencv != "":
        installer = install_opencv(args.d, args.opencv, pw, pwd)
        installer.run()

    if args.eigen != "":
        installer = install_eigen(args.d, args.eigen, pw, pwd)
        installer.run()


if __name__ == '__main__':
    main()
