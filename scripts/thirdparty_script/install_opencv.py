import os
import multiprocessing


class install_opencv:
    def __init__(self, d, version, password, pwd):
        self.d = d
        self.version = version
        self.dir = "./thirdparty/opencv"
        self.pwd = pwd
        self.pw = password
    
    def run(self):
        # Remove any pre-installed OpenCV
        os.system(self.pw.sudo() + "rm -rf ./thirdparty/opencv*")

        # Install dependant libraries 
        os.system(self.pw.sudo() + "apt-get -y install ffmpeg libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev")

        # Download opencv source code
        os.system("mkdir " + self.dir)
        os.system("wget -O " + self.dir + 
                  "/opencv.zip https://github.com/opencv/opencv/archive/" + self.version + ".zip")
        os.system("unzip " + self.dir + "/opencv.zip -d" + self.dir)

        # CMake configure
        os.system("mkdir " + self.dir + "/build")
        os.chdir(self.dir + "/build")

        # CMake options
        exec_string = "cmake ../opencv-" + self.version

        if self.d: 
            exec_string += " -DCMAKE_BUILD_TYPE=Debug"

        ret = os.system(exec_string)
        if ret != 0:
            print("Error while building OpenCV in 'install_opencv.py'")
            return
        
        # Build
        Ncores = multiprocessing.cpu_count()
        os.system(self.pw.sudo() + "make -j" + str(Ncores - 2))

        # Delete source files
        os.chdir("../")
        os.system(self.pw.sudo() + "rm -rf opencv.zip")

        os.chdir(self.pwd)