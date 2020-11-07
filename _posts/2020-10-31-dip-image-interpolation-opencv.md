---
layout: post
title: "“数字图像处理”笔记 -- OpenCV 中 resize 函数五种插值算法的实现过程"
author:
location: "珠海"
categories: ["图像处理"]
tags: ["图像处理"]
toc: true
toclistyle:
comments:
visibility:
mathjax: true
mermaid:
glslcanvas:
---

老版本的 OpenCV 代码还能扣出来跑一下，最新版本，已经基本上没这个可能了。

<table class="tablestyle" ntablew="1:3"></table>

| interpolation 选项 | 所用的插值方法 |
| ---- | ---- |
| INTER_NEAREST | 最近邻插值 |
| INTER_LINEAR | 双线性插值（默认设置） |
| INTER_AREA | 使用像素区域关系进行重采样。它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。但是当图像缩放时，它类似于 INTER_NEAREST 方法。 |
| INTER_CUBIC | 4x4 像素邻域的双三次插值 |
| INTER_LANCZOS4 | 8x8 像素邻域的 Lanczos 插值 |


## 原理简述

最新版 OpenCV 2.4.7 中，cv::resize 函数有五种插值算法：最近邻、双线性、双三次、基于像素区域关系、兰索斯插值。
下面用 for 循环代替 cv::resize 函数来说明其详细的插值实现过程，其中部分代码摘自于 cv::resize 函数中的源代码。

1. 最近邻
2. 双线性：由相邻的四像素 (2*2) 计算得出
3. 双三次：由相邻的 (4*4) 像素计算得出，公式类似于双线性
4. 基于像素区域关系：共分三种情况，图像放大时类似于双线性插值，图像缩小（x 轴、y 轴同时缩小）又分两种情况，此情况下可以避免波纹出现。
5. 兰索斯插值：由相邻的 (8*8) 像素计算得出，公式类似于双线性

以上代码的实现结果与 cv::resize 函数相同，但是执行效率非常低，只是为了详细说明插值过程。
OpenCV 中默认采用 C++ Concurrency 进行优化加速，你也可以采用 TBB、OpenMP 等进行优化加速。


## OpenCV 插值代码

```cpp
#include "stdafx.h"
#include <algorithm>
#include <opencv\cv.h>
#include <opencv\highgui.h>
#include <opencv2/opencv.hpp>
#include "opencv2/core/core_c.h"
#include "opencv2/core/core.hpp"
#include "opencv2/imgproc/imgproc_c.h"
#include "opencv2/imgproc/imgproc.hpp"

// INTER_NEAREST 最近邻插值
int resizeNearest(cv::Mat& matSrc, cv::Mat& matDst1, cv::Mat& matDst2, double scale_x, double scale_y) {

    for (int i = 0; i < matDst1.cols; ++i)
    {
        int sx = cvFloor(i * scale_x);
        sx = std::min(sx, matSrc.cols - 1);
        for (int j = 0; j < matDst1.rows; ++j)
        {
            int sy = cvFloor(j * scale_y);
            sy = std::min(sy, matSrc.rows - 1);
            matDst1.at<cv::Vec3b>(j, i) = matSrc.at<cv::Vec3b>(sy, sx);
        }
    }
    cv::imwrite("nearest_1.jpg", matDst1);

    cv::resize(matSrc, matDst2, matDst1.size(), 0, 0, 0);
    cv::imwrite("nearest_2.jpg", matDst2);

    return 0;
}

// INTER_LINEAR 双线性插值（默认设置）
int resizeLinear(cv::Mat& matSrc, cv::Mat& matDst1, cv::Mat& matDst2, double scale_x, double scale_y) {
    uchar* dataDst = matDst1.data;
    int stepDst = matDst1.step;
    uchar* dataSrc = matSrc.data;
    int stepSrc = matSrc.step;
    int iWidthSrc = matSrc.cols;
    int iHiehgtSrc = matSrc.rows;

    for (int j = 0; j < matDst1.rows; ++j)
    {
        float fy = (float)((j + 0.5) * scale_y - 0.5);
        int sy = cvFloor(fy);
        fy -= sy;
        sy = std::min(sy, iHiehgtSrc - 2);
        sy = std::max(0, sy);

        short cbufy[2];
        cbufy[0] = cv::saturate_cast<short>((1.f - fy) * 2048);
        cbufy[1] = 2048 - cbufy[0];

        for (int i = 0; i < matDst1.cols; ++i)
        {
            float fx = (float)((i + 0.5) * scale_x - 0.5);
            int sx = cvFloor(fx);
            fx -= sx;

            if (sx < 0) {
                fx = 0, sx = 0;
            }
            if (sx >= iWidthSrc - 1) {
                fx = 0, sx = iWidthSrc - 2;
            }

            short cbufx[2];
            cbufx[0] = cv::saturate_cast<short>((1.f - fx) * 2048);
            cbufx[1] = 2048 - cbufx[0];

            for (int k = 0; k < matSrc.channels(); ++k)
            {
                *(dataDst + j * stepDst + 3 * i + k) = (*(dataSrc + sy * stepSrc + 3 * sx + k) * cbufx[0] * cbufy[0] +
                    *(dataSrc + (sy + 1) * stepSrc + 3 * sx + k) * cbufx[0] * cbufy[1] +
                    *(dataSrc + sy * stepSrc + 3 * (sx + 1) + k) * cbufx[1] * cbufy[0] +
                    *(dataSrc + (sy + 1) * stepSrc + 3 * (sx + 1) + k) * cbufx[1] * cbufy[1]) >> 22;
            }
        }
    }
    cv::imwrite("linear_1.jpg", matDst1);

    cv::resize(matSrc, matDst2, matDst1.size(), 0, 0, 1);
    cv::imwrite("linear_2.jpg", matDst2);

    return 0;
}

// INTER_AREA 使用像素区域关系进行重采样。
// 它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。
// 但是当图像缩放时，它类似于 INTER_NEAREST 方法。
int resizeArea(cv::Mat& matSrc, cv::Mat& matDst1, cv::Mat& matDst2, double scale_x, double scale_y) {

    cv::resize(matSrc, matDst2, matDst1.size(), 0, 0, 3);
    cv::imwrite("area_2.jpg", matDst2);

    double inv_scale_x = 1. / scale_x;
    double inv_scale_y = 1. / scale_y;
    int iscale_x = cv::saturate_cast<int>(scale_x);
    int iscale_y = cv::saturate_cast<int>(scale_y);
    bool is_area_fast = std::abs(scale_x - iscale_x) < DBL_EPSILON && std::abs(scale_y - iscale_y) < DBL_EPSILON;

    if (scale_x >= 1 && scale_y >= 1) // zoom out
    {
        if (is_area_fast) // integer multiples
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
            cv::imwrite("area_1.jpg", matDst1);
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
        cv::imwrite("area_1.jpg", matDst1);
        return 0;
    }

    // zoom in, it is emulated using some variant of bilinear interpolation
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
            if (sy >= matSrc.rows - 1) {
                sy = matSrc.rows - 2;
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
    cv::imwrite("area_1.jpg", matDst1);
    return 0;
}

// INTER_CUBIC 4x4 像素邻域的双三次插值
int resizeCubic(cv::Mat& matSrc, cv::Mat& matDst1, cv::Mat& matDst2, double scale_x, double scale_y) {
    int iscale_x = cv::saturate_cast<int>(scale_x);
    int iscale_y = cv::saturate_cast<int>(scale_y);

    for (int j = 0; j < matDst1.rows; ++j)
    {
        float fy = (float)((j + 0.5) * scale_y - 0.5);
        int sy = cvFloor(fy);
        fy -= sy;
        sy = std::min(sy, matSrc.rows - 3);
        sy = std::max(1, sy);

        const float A = -0.75f;

        float coeffsY[4];
        coeffsY[0] = ((A * (fy + 1) - 5 * A) * (fy + 1) + 8 * A) * (fy + 1) - 4 * A;
        coeffsY[1] = ((A + 2) * fy - (A + 3)) * fy * fy + 1;
        coeffsY[2] = ((A + 2) * (1 - fy) - (A + 3)) * (1 - fy) * (1 - fy) + 1;
        coeffsY[3] = 1.f - coeffsY[0] - coeffsY[1] - coeffsY[2];

        short cbufY[4];
        cbufY[0] = cv::saturate_cast<short>(coeffsY[0] * 2048);
        cbufY[1] = cv::saturate_cast<short>(coeffsY[1] * 2048);
        cbufY[2] = cv::saturate_cast<short>(coeffsY[2] * 2048);
        cbufY[3] = cv::saturate_cast<short>(coeffsY[3] * 2048);

        for (int i = 0; i < matDst1.cols; ++i)
        {
            float fx = (float)((i + 0.5) * scale_x - 0.5);
            int sx = cvFloor(fx);
            fx -= sx;

            if (sx < 1) {
                fx = 0, sx = 1;
            }
            if (sx >= matSrc.cols - 3) {
                fx = 0, sx = matSrc.cols - 3;
            }

            float coeffsX[4];
            coeffsX[0] = ((A * (fx + 1) - 5 * A) * (fx + 1) + 8 * A) * (fx + 1) - 4 * A;
            coeffsX[1] = ((A + 2) * fx - (A + 3)) * fx * fx + 1;
            coeffsX[2] = ((A + 2) * (1 - fx) - (A + 3)) * (1 - fx) * (1 - fx) + 1;
            coeffsX[3] = 1.f - coeffsX[0] - coeffsX[1] - coeffsX[2];

            short cbufX[4];
            cbufX[0] = cv::saturate_cast<short>(coeffsX[0] * 2048);
            cbufX[1] = cv::saturate_cast<short>(coeffsX[1] * 2048);
            cbufX[2] = cv::saturate_cast<short>(coeffsX[2] * 2048);
            cbufX[3] = cv::saturate_cast<short>(coeffsX[3] * 2048);

            if (sx < 1) {
                sx = 1;
            }
            if (sx > matSrc.cols - 3) {
                sx = matSrc.cols - 3;
            }
            if (sy < 1) {
                sy = 1;
            }
            if (sy > matSrc.rows - 3) {
                sy = matSrc.rows - 3;
            }

            for (int k = 0; k < matSrc.channels(); ++k)
            {
                matDst1.at<cv::Vec3b>(j, i)[k] = abs((matSrc.at<cv::Vec3b>(sy - 1, sx - 1)[k] * cbufX[0] * cbufY[0] + matSrc.at<cv::Vec3b>(sy, sx - 1)[k] * cbufX[0] * cbufY[1] +
                    matSrc.at<cv::Vec3b>(sy + 1, sx - 1)[k] * cbufX[0] * cbufY[2] + matSrc.at<cv::Vec3b>(sy + 2, sx - 1)[k] * cbufX[0] * cbufY[3] +
                    matSrc.at<cv::Vec3b>(sy - 1, sx)[k] * cbufX[1] * cbufY[0] + matSrc.at<cv::Vec3b>(sy, sx)[k] * cbufX[1] * cbufY[1] +
                    matSrc.at<cv::Vec3b>(sy + 1, sx)[k] * cbufX[1] * cbufY[2] + matSrc.at<cv::Vec3b>(sy + 2, sx)[k] * cbufX[1] * cbufY[3] +
                    matSrc.at<cv::Vec3b>(sy - 1, sx + 1)[k] * cbufX[2] * cbufY[0] + matSrc.at<cv::Vec3b>(sy, sx + 1)[k] * cbufX[2] * cbufY[1] +
                    matSrc.at<cv::Vec3b>(sy + 1, sx + 1)[k] * cbufX[2] * cbufY[2] + matSrc.at<cv::Vec3b>(sy + 2, sx + 1)[k] * cbufX[2] * cbufY[3] +
                    matSrc.at<cv::Vec3b>(sy - 1, sx + 2)[k] * cbufX[3] * cbufY[0] + matSrc.at<cv::Vec3b>(sy, sx + 2)[k] * cbufX[3] * cbufY[1] +
                    matSrc.at<cv::Vec3b>(sy + 1, sx + 2)[k] * cbufX[3] * cbufY[2] + matSrc.at<cv::Vec3b>(sy + 2, sx + 2)[k] * cbufX[3] * cbufY[3]) >> 22);
            }
        }
    }
    cv::imwrite("cubic_1.jpg", matDst1);

    cv::resize(matSrc, matDst2, matDst1.size(), 0, 0, 2);
    cv::imwrite("cubic_2.jpg", matDst2);

    return 0;
}

// INTER_LANCZOS4 8x8 像素邻域的 Lanczos 插值
int resizeLanczos4(cv::Mat& matSrc, cv::Mat& matDst1, cv::Mat& matDst2, double scale_x, double scale_y) {

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
                    matSrc.at<cv::Vec3b>(sy + 3, sx + 4)[k] * cbufX[7] * cbufY[6] + matSrc.at<cv::Vec3b>(sy + 4, sx + 4)[k] * cbufX[7] * cbufY[7]) >> 22); // 4194304
            }
        }
    }
    cv::imwrite("Lanczos_1.jpg", matDst1);

    cv::resize(matSrc, matDst2, matDst1.size(), 0, 0, 4);
    cv::imwrite("Lanczos_2.jpg", matDst2);

    return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
    cv::Mat matSrc, matDst1, matDst2;

    matSrc = cv::imread("C:\\kSource\\pythonx\\toyimg\\image\\imori.jpg", 2 | 4);

    matDst1 = cv::Mat(cv::Size(500, 500), matSrc.type(), cv::Scalar::all(0));
    matDst2 = cv::Mat(matDst1.size(), matSrc.type(), cv::Scalar::all(0));

    double scale_x = (double)matSrc.cols / matDst1.cols;
    double scale_y = (double)matSrc.rows / matDst1.rows;

    resizeNearest(matSrc, matDst1, matDst2, scale_x, scale_y);
    resizeLinear(matSrc, matDst1, matDst2, scale_x, scale_y);
    resizeArea(matSrc, matDst1, matDst2, scale_x, scale_y);
    resizeCubic(matSrc, matDst1, matDst2, scale_x, scale_y);
    resizeLanczos4(matSrc, matDst1, matDst2, scale_x, scale_y);
    return 0;
}

```


## 参考

* [Source code for obspy.signal.interpolation](https://docs.obspy.org/_modules/obspy/signal/interpolation.html)
* <https://blog.csdn.net/iteye_13202/article/details/82553682>
* <https://blog.csdn.net/jningwei/article/details/78822026>
