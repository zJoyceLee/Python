#include <iostream>
#include <string>
#include <opencv2/opencv.hpp>
#include <opencv2/stitching.hpp>

using namespace std;
using namespace cv;

string IMAGE_PATH_PREFIX = "/home/joyce/Code/Python/openCV/lab03Img/";

bool try_use_gpu = false;
vector<Mat> imgs;
string result_name = "result.jpg";


int main()
{
/*
    Mat img = imread(IMAGE_PATH_PREFIX + "part5.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part1.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part8.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part3.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part6.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part4.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part7.jpg");
    imgs.push_back(img);
    img=imread(IMAGE_PATH_PREFIX+"part2.jpg");
    imgs.push_back(img);
*/
    Mat img;
    for (auto i = 1; i < 4; ++i) {
      std::string path = "t" + std::to_string(i) + ".jpg";
      std::cout << "add: " + path << std::endl;
      img = imread(path);
      imgs.push_back(img);
    }

    Mat pano;
    //Stitcher stitcher = Stitcher::createDefault(try_use_gpu);
    Stitcher stitcher = Stitcher::createDefault();
    Stitcher::Status status = stitcher.stitch(imgs, pano);

    if (status != Stitcher::OK)
    {
        cout << "Can't stitch images, error code = " << int(status) << endl;
        return -1;
    }

    imwrite(result_name, pano);
    return 0;
}

