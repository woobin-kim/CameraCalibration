import os
import multiprocessing


class install_eigen:
    def __init__(self, d, version, password, pwd):
        self.d = d
        self.version = version
        self.install_dir = "./thirdparty/eigen"
        self.pw = password
        self.pwd = pwd

    def run(self):

        # Remove any pre-installed Eigen
        os.system(self.pw.sudo() + "rm -rf ./thirdparty/eigen")

        # Download Eigen source code
        os.system("mkdir " + self.install_dir)
        os.system("wget -O " + self.install_dir + "/eigen.zip https://gitlab.com/libeigen/eigen/-/archive/" +
                  self.version + "/eigen-" + self.version + ".zip")
        os.system("unzip " + self.install_dir +
                  "/eigen.zip -d " + self.install_dir)

        # CMake configure
        os.system("mkdir " + self.install_dir + "/build")
        os.system("mkdir " + self.install_dir + "/install")
        os.chdir(self.install_dir + "/build")

        exec_string = "cmake ../eigen-" + self.version + " -DCMAKE_INSTALL_PREFIX=../install"

        if self.d:
            exec_string += " -DCMAKE_BUILD_TYPE=Debug"

        return_code = os.system(exec_string)
        if return_code != 0:
            print("Error occured in building eigen!")
            return

        # Build
        num_cpu_cores = multiprocessing.cpu_count()
        os.system(self.pw.sudo() + "make -j" + str(num_cpu_cores-1))
        os.system(self.pw.sudo() + "sudo make install")

        # Delete source files
        os.chdir("../")
        os.system("rm -rf eigen.zip")

        os.chdir(self.pwd)
