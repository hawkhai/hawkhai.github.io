// lanczos.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
#include <algorithm>
#include <opencv\cv.h>
#include <opencv\highgui.h>
#include "opencv2/core/core_c.h"
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc_c.h"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/video/tracking.hpp"
#include "opencv2/features2d/features2d.hpp"
#include "opencv2/flann/flann.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/objdetect/objdetect.hpp"
#include <opencv2/opencv.hpp>

// 实现 OPENCV AREA 算法。
int resizeArea(cv::Mat& matSrc, cv::Mat& matDst1, double scale_x, double scale_y)
{
	double inv_scale_x = 1. / scale_x;
	double inv_scale_y = 1. / scale_y;
	int iscale_x = cv::saturate_cast<int>(scale_x);
	int iscale_y = cv::saturate_cast<int>(scale_y);
	bool is_area_fast = std::abs(scale_x - iscale_x) < DBL_EPSILON && std::abs(scale_y - iscale_y) < DBL_EPSILON;

	if (scale_x >= 1 && scale_y >= 1) //zoom out
	{
		if (is_area_fast) //integer multiples
		{
			for (int j = 0; j < matDst1.rows; ++j)
			{
				int sy = j * scale_y;


				for (int i = 0; i < matDst1.cols; ++i)
				{
					int sx = i * scale_x;

					matDst1.at<cv::Vec3b>(j, i) = matSrc.at<cv::Vec3b>(sy, sx);
				}
			}
			return 0;
		}


		for (int j = 0; j < matDst1.rows; ++j)
		{
			double fsy1 = j * scale_y;
			double fsy2 = fsy1 + scale_y;
			double cellHeight = cv::min(scale_y, matSrc.rows - fsy1);


			int sy1 = cvCeil(fsy1), sy2 = cvFloor(fsy2);


			sy2 = std::min(sy2, matSrc.rows - 1);
			sy1 = std::min(sy1, sy2);


			float cbufy[2];
			cbufy[0] = (float)((sy1 - fsy1) / cellHeight);
			cbufy[1] = (float)(std::min(std::min(fsy2 - sy2, 1.), cellHeight) / cellHeight);


			for (int i = 0; i < matDst1.cols; ++i)
			{
				double fsx1 = i * scale_x;
				double fsx2 = fsx1 + scale_x;
				double cellWidth = std::min(scale_x, matSrc.cols - fsx1);


				int sx1 = cvCeil(fsx1), sx2 = cvFloor(fsx2);


				sx2 = std::min(sx2, matSrc.cols - 1);
				sx1 = std::min(sx1, sx2);


				float cbufx[2];
				cbufx[0] = (float)((sx1 - fsx1) / cellWidth);
				cbufx[1] = (float)(std::min(std::min(fsx2 - sx2, 1.), cellWidth) / cellWidth);


				for (int k = 0; k < matSrc.channels(); ++k)
				{
					matDst1.at<cv::Vec3b>(j, i)[k] = (uchar)(matSrc.at<cv::Vec3b>(sy1, sx1)[k] * cbufx[0] * cbufy[0] +
						matSrc.at<cv::Vec3b>(sy1 + 1, sx1)[k] * cbufx[0] * cbufy[1] +
						matSrc.at<cv::Vec3b>(sy1, sx1 + 1)[k] * cbufx[1] * cbufy[0] +
						matSrc.at<cv::Vec3b>(sy1 + 1, sx1 + 1)[k] * cbufx[1] * cbufy[1]);
				}
			}
		}
		return 0;
	}

	// zoom in,it is emulated using some variant of bilinear interpolation
	for (int j = 0; j < matDst1.rows; ++j)
	{
		int  sy = cvFloor(j * scale_y);
		float fy = (float)((j + 1) - (sy + 1) * inv_scale_y);
		fy = fy <= 0 ? 0.f : fy - cvFloor(fy);


		short cbufy[2];
		cbufy[0] = cv::saturate_cast<short>((1.f - fy) * 2048);
		cbufy[1] = 2048 - cbufy[0];


		for (int i = 0; i < matDst1.cols; ++i)
		{
			int sx = cvFloor(i * scale_x);
			float fx = (float)((i + 1) - (sx + 1) * inv_scale_x);
			fx = fx < 0 ? 0.f : fx - cvFloor(fx);


			if (sx < 0) {
				fx = 0, sx = 0;
			}


			if (sx >= matSrc.cols - 1) {
				fx = 0, sx = matSrc.cols - 2;
			}


			short cbufx[2];
			cbufx[0] = cv::saturate_cast<short>((1.f - fx) * 2048);
			cbufx[1] = 2048 - cbufx[0];


			for (int k = 0; k < matSrc.channels(); ++k)
			{
				matDst1.at<cv::Vec3b>(j, i)[k] = (matSrc.at<cv::Vec3b>(sy, sx)[k] * cbufx[0] * cbufy[0] +
					matSrc.at<cv::Vec3b>(sy + 1, sx)[k] * cbufx[0] * cbufy[1] +
					matSrc.at<cv::Vec3b>(sy, sx + 1)[k] * cbufx[1] * cbufy[0] +
					matSrc.at<cv::Vec3b>(sy + 1, sx + 1)[k] * cbufx[1] * cbufy[1]) >> 22;
			}
		}
	}
}

// 实现 OPENCV Lanczos 算法。
int resizeLanczos(cv::Mat& matSrc, cv::Mat& matDst1, float scale_x, float scale_y)
{
	int iscale_x = cv::saturate_cast<int>(scale_x);
	int iscale_y = cv::saturate_cast<int>(scale_y);


	for (int j = 0; j < matDst1.rows; ++j)
	{
		float fy = (float)((j + 0.5) * scale_y - 0.5);
		int sy = cvFloor(fy);
		fy -= sy;
		sy = std::min(sy, matSrc.rows - 5);
		sy = std::max(3, sy);


		const double s45 = 0.70710678118654752440084436210485;
		const double cs[][2] = { {1, 0}, {-s45, -s45}, {0, 1}, {s45, -s45}, {-1, 0}, {s45, s45}, {0, -1}, {-s45, s45} };
		float coeffsY[8];


		if (fy < FLT_EPSILON) {
			for (int t = 0; t < 8; t++)
				coeffsY[t] = 0;
			coeffsY[3] = 1;
		}
		else {
			float sum = 0;
			double y0 = -(fy + 3) * CV_PI * 0.25, s0 = sin(y0), c0 = cos(y0);


			for (int t = 0; t < 8; ++t)
			{
				double dy = -(fy + 3 - t) * CV_PI * 0.25;
				coeffsY[t] = (float)((cs[t][0] * s0 + cs[t][1] * c0) / (dy * dy));
				sum += coeffsY[t];
			}


			sum = 1.f / sum;
			for (int t = 0; t < 8; ++t)
				coeffsY[t] *= sum;
		}


		short cbufY[8];
		cbufY[0] = cv::saturate_cast<short>(coeffsY[0] * 2048);
		cbufY[1] = cv::saturate_cast<short>(coeffsY[1] * 2048);
		cbufY[2] = cv::saturate_cast<short>(coeffsY[2] * 2048);
		cbufY[3] = cv::saturate_cast<short>(coeffsY[3] * 2048);
		cbufY[4] = cv::saturate_cast<short>(coeffsY[4] * 2048);
		cbufY[5] = cv::saturate_cast<short>(coeffsY[5] * 2048);
		cbufY[6] = cv::saturate_cast<short>(coeffsY[6] * 2048);
		cbufY[7] = cv::saturate_cast<short>(coeffsY[7] * 2048);


		for (int i = 0; i < matDst1.cols; ++i)
		{
			float fx = (float)((i + 0.5) * scale_x - 0.5);
			int sx = cvFloor(fx);
			fx -= sx;


			if (sx < 3) {
				fx = 0, sx = 3;
			}
			if (sx >= matSrc.cols - 5) {
				fx = 0, sx = matSrc.cols - 5;
			}


			float coeffsX[8];


			if (fx < FLT_EPSILON) {
				for (int t = 0; t < 8; t++)
					coeffsX[t] = 0;
				coeffsX[3] = 1;
			}
			else {
				float sum = 0;
				double x0 = -(fx + 3) * CV_PI * 0.25, s0 = sin(x0), c0 = cos(x0);


				for (int t = 0; t < 8; ++t)
				{
					double dx = -(fx + 3 - t) * CV_PI * 0.25;
					coeffsX[t] = (float)((cs[t][0] * s0 + cs[t][1] * c0) / (dx * dx));
					sum += coeffsX[t];
				}


				sum = 1.f / sum;
				for (int t = 0; t < 8; ++t)
					coeffsX[t] *= sum;
			}


			short cbufX[8];
			cbufX[0] = cv::saturate_cast<short>(coeffsX[0] * 2048);
			cbufX[1] = cv::saturate_cast<short>(coeffsX[1] * 2048);
			cbufX[2] = cv::saturate_cast<short>(coeffsX[2] * 2048);
			cbufX[3] = cv::saturate_cast<short>(coeffsX[3] * 2048);
			cbufX[4] = cv::saturate_cast<short>(coeffsX[4] * 2048);
			cbufX[5] = cv::saturate_cast<short>(coeffsX[5] * 2048);
			cbufX[6] = cv::saturate_cast<short>(coeffsX[6] * 2048);
			cbufX[7] = cv::saturate_cast<short>(coeffsX[7] * 2048);


			for (int k = 0; k < matSrc.channels(); ++k)
			{
				matDst1.at<cv::Vec3b>(j, i)[k] = abs((matSrc.at<cv::Vec3b>(sy - 3, sx - 3)[k] * cbufX[0] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx - 3)[k] * cbufX[0] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx - 3)[k] * cbufX[0] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx - 3)[k] * cbufX[0] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx - 3)[k] * cbufX[0] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx - 3)[k] * cbufX[0] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx - 3)[k] * cbufX[0] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx - 3)[k] * cbufX[0] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx - 2)[k] * cbufX[1] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx - 2)[k] * cbufX[1] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx - 2)[k] * cbufX[1] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx - 2)[k] * cbufX[1] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx - 2)[k] * cbufX[1] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx - 2)[k] * cbufX[1] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx - 2)[k] * cbufX[1] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx - 2)[k] * cbufX[1] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx - 1)[k] * cbufX[2] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx - 1)[k] * cbufX[2] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx - 1)[k] * cbufX[2] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx - 1)[k] * cbufX[2] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx - 1)[k] * cbufX[2] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx - 1)[k] * cbufX[2] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx - 1)[k] * cbufX[2] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx - 1)[k] * cbufX[2] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx)[k] * cbufX[3] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx)[k] * cbufX[3] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx)[k] * cbufX[3] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx)[k] * cbufX[3] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx)[k] * cbufX[3] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx)[k] * cbufX[3] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx)[k] * cbufX[3] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx)[k] * cbufX[3] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx + 1)[k] * cbufX[4] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx + 1)[k] * cbufX[4] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx + 1)[k] * cbufX[4] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx + 1)[k] * cbufX[4] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx + 1)[k] * cbufX[4] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx + 1)[k] * cbufX[4] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx + 1)[k] * cbufX[4] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx + 1)[k] * cbufX[4] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx + 2)[k] * cbufX[5] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx + 2)[k] * cbufX[5] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx + 2)[k] * cbufX[5] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx + 2)[k] * cbufX[5] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx + 2)[k] * cbufX[5] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx + 2)[k] * cbufX[5] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx + 2)[k] * cbufX[5] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx + 2)[k] * cbufX[5] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx + 3)[k] * cbufX[6] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx + 3)[k] * cbufX[6] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx + 3)[k] * cbufX[6] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx + 3)[k] * cbufX[6] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx + 3)[k] * cbufX[6] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx + 3)[k] * cbufX[6] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx + 3)[k] * cbufX[6] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx + 3)[k] * cbufX[6] * cbufY[7] +


					matSrc.at<cv::Vec3b>(sy - 3, sx + 4)[k] * cbufX[7] * cbufY[0] + matSrc.at<cv::Vec3b>(sy - 2, sx + 4)[k] * cbufX[7] * cbufY[1] +
					matSrc.at<cv::Vec3b>(sy - 1, sx + 4)[k] * cbufX[7] * cbufY[2] + matSrc.at<cv::Vec3b>(sy, sx + 4)[k] * cbufX[7] * cbufY[3] +
					matSrc.at<cv::Vec3b>(sy + 1, sx + 4)[k] * cbufX[7] * cbufY[4] + matSrc.at<cv::Vec3b>(sy + 2, sx + 4)[k] * cbufX[7] * cbufY[5] +
					matSrc.at<cv::Vec3b>(sy + 3, sx + 4)[k] * cbufX[7] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx + 4)[k] * cbufX[7] * cbufY[7]) >> 22);// 4194304
			}
		}
	}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	//KFFTAlpha alpah;
	//alpah.main_alpha();
	using namespace std;
	using namespace cv;
	Mat img = imread(".\\input_images\\phase2\\phase2_broken.jpg", -1);
	Mat imgdst = Mat();
	//imgdst.create(img.rows * 1, img.cols * 2, CV_8UC3);
	//resizeLanczos(img, imgdst, 0.5, 1);
	imgdst.create(img.rows * 3, img.cols * 3, CV_8UC3);
	resizeLanczos(img, imgdst, 1.0 / 3, 1.0 / 3);
	imshow("Lanczos", imgdst);
	imwrite(".\\output_images\\phase2\\phase2_broken_Lanczos.jpg", imgdst);
	waitKey();
	return 0;
}
