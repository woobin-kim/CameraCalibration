#include <iostream>
#include <opencv2/opencv.hpp>

int main()
{
    std::cout << "Hello world!" << std::endl;
    cv::Mat img = cv::imread("./resources/lego.png");
    cv::imshow("Image Viewer", img);
    cv::waitKey(0);
    return 0;
}