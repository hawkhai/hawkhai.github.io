<!DOCTYPE html>
<head>
  <title>OpenCV 3   Signal Processing with NumPy II - Image Fourier Transform : FFT & DFT - 2020</title>
  <meta content="OpenCV 3  Signal Processing with NumPy II - Image Fourier Transform : FFT & DFT" name="description" />
  <meta content="OpenCV 3 with Python Tutorial: Fourier Transform : FFT & DFT, NumPy" name="keywords" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="//netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.no-icons.min.css" rel="stylesheet">
  <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css" rel="stylesheet">
  <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Alice|Open+Sans:400,300,700">
  <link rel="stylesheet" href="/public/css/app.css">
  <link rel="stylesheet" href="/public/css/styles.css">
  <link rel="stylesheet" href="/public/css/bogostyleWidePreNew.css">
</head>

<body class="home">
    <nav class="navbar navbar-default navbar-fixed-top">
    <div class="container-fluid">      
      <div class="navbar-header">
        <!--<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar"> -->
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target=".navbar-collapse" aria-expanded="false" aria-controls="navbar"> 
          <span class="sr-only">Toggle navigation</span> 
          <span class="icon-bar"></span> 
          <span class="icon-bar"></span> 
          <span class="icon-bar"></span> 
        </button>
        <a class="navbar-brand" href="/index.php">BogoToBogo</a>
      </div>
      
      <div class="navbar-collapse collapse">
        
        <ul class="nav navbar-nav">
          <li class="active"><a href="/index.php">Home</a></li>
          <li><a href="/about_us.php">About</a></li>
          <li><a href="/Hadoop/BigData_hadoop_Install_on_ubuntu_single_node_cluster.php">Big Data</a></li>
          <li><a href="/python/scikit-learn/Artificial-Neural-Network-ANN-1-Introduction.php">Machine Learning</a></li>
          <li><a href="/AngularJS/AngularJS_Introduction.php">AngularJS</a></li> 
          <li><a href="/python/pytut.php">Python</a></li>
          <li><a href="/cplusplus/cpptut.php">C++</a></li>
          <li><a href="/GoLang/GoLang_Closures_Anonymous_Functions.php">go</a></li>
          <li><a href="/DevOps/DevOps_Jenkins_Chef_Puppet_Graphite_Logstash.php">DevOps </a></li>
          <li><a href="/DevOps/Docker/Docker-from-Monolithic-to-Micro-services-GCP-Kubernetes.php">Kubernetes </a></li>
          <li><a href="/Algorithms/algorithms.php">Algorithms</a></li> 
          <li class="dropdown">
            <a href="#" class="dropdown-toggle" data-toggle="dropdown">More...<b class="caret"></b></a>
            <ul class="dropdown-menu">
           
              <li><a href="/Qt/Qt5_Creating_QtQuick2_QML_Application_Animation_A.php">Qt 5</a></li>                           
              <li><a href="/Android/android.php">Android</a></li>
              
              <li><a href="/Linux/linux_tips1.php">Linux</a></li>
              <li><a href="/Java/tutorials/on_java.php">Java</a></li>
              <li><a href="/CSharp/.netframework.php">CSharp</a></li>
              <li><a href="/VideoStreaming/videostreaming_etc.php">Video Streaming</a></li>
              <li><a href="/FFMpeg/ffmpeg_fade_in_fade_out_transitions_effects_filters_slideshow_concat.php">FFmpeg</a></li>
              <li><a href="/Matlab/Matlab_Tutorial_Manipulating_Audio_I_Reverse_Delay_Tone_Control_Changing_Speed_Removing_Vocals.php">Matlab</a></li>
              <li><a href="/python/Django/Python_Django_Forums_Shared_Host.php">Django 1.8</a></li>
              <li><a href="/Laravel5/Laravel5_ToDo_List_Sample.php">Laravel 5.2</a></li>
              <li><a href="/RubyOnRails/RubyOnRails.php">Ruby On Rails</a></li>
              <li><a href="/HTML5/HTML5_Tutorial.php">HTML5 & CSS</a></li>
              <!--<li><a href="/AmazingPlaces/index.php" target="_blank">
<img src="/Menus/MenuIcons/Earth_8px_transparent_background.png"
width="24" height="24"/>Earth</a> </li>-->
            </ul>
          </li>
        </ul>      
      </div>
    </div>  
  </nav>  

  <div id="main">
    <div class="container">
      <div class="row section featured topspace">
        <div class="row">
          <div class="col-sm-9 col-md-9 col-xs-9">
            <h2 class="section-title">Signal Processing with NumPy II - Image Fourier Transform : FFT & DFT        <g:plusone></g:plusone></h2>
            <div class="icon-image">
                <img src="/python/images/OpenCV_Logo.png" alt="OpenCV_Logo.png"/>
            </div>
            <div class="SocialLinks">
  <span class='st__large' displayText=''></span>
  <br><br>
  <div align="center">
  <span class='st_facebook_large' displayText='Facebook'></span>
  <span class='st_twitter_large' displayText='Tweet'></span>
  <span class='st_linkedin_large' displayText='LinkedIn'></span>
  </div>
  <br><br>
  <script type="text/javascript" src="//w.sharethis.com/button/buttons.js"></script>
  <script type="text/javascript">stLight.options({publisher: "b9569c43-5f56-4501-92f0-4bf4aa8fceb0", doNotHash: false, doNotCopy: true, hashAddressBar: false});</script>
</div>

<div id="bookmarkshare">
  <script type="text/javascript">var addthis_config = {"data_track_clickback":true};</script>
  <a class="addthis_button" href="http://www.addthis.com/bookmark.php?v=250&amp;username=khhong7"><img src="//s7.addthis.com/static/btn/v2/lg-share-en.gif" width="125" height="16" alt="Bookmark and Share" style="border:0"/></a>
  <script type="text/javascript" src="//s7.addthis.com/js/250/addthis_widget.js#username=khhong7"></script>
</div>

<br>
<hr>
<br>


<!-- Google bogo1 ad -->
<!-- Google search box -->



<!-- bogo1 -->
<div>
  <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo1 -->
  <ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-4716428189734495"
     data-ad-slot="6542308167"></ins>
  <script>
   (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>


<!-- Google search box -->
<div class="AdSenseSearch">
  bogotobogo.com site search:
  <form action="//www.google.com" id="cse-search-box" target="_blank">
    <div>
      <input type="hidden" name="cx" value="partner-pub-4716428189734495:1794050961" />
      <input type="hidden" name="ie" value="UTF-8" />
      <!--<input type="text" name="q" size="55" />-->
      <input type="text" name="q" size="" width="90%"/>
      <input type="submit" name="sa" value="Search" />
    </div>
  </form>
  <script type="text/javascript" src="//www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
</div>




<hr>
<div class="subtitle_2nd" id="NumPyFFT">Functions and values of NumPy FFT</div>
<p>The DFT (Discrete Fourier Transform) is defined as
$$A_k = \sum_{m=0}^{n-1} a_m exp\{ -2\pi i \frac{mk}{n} \} \quad\quad k=0,...,n-1.$$
The DFT is in general defined for <b>complex</b> inputs and outputs, and a single-frequency component at linear frequency f is represented by a complex exponential $a_m = exp\{2\pi i f m \Delta t \}$, where $\Delta t$ is the interval for sampling.</p>
<p>Here are the NumPy's fft functions and the values in the result:</p>
<ol>
<li><b>$A=fft(a,n)$</b> <br/>
    $A[0]$ contains the zero-frequency term which is the mean of the signal. It is always purely real for real inputs.<br/>
    $A[1:n/2]$ contains the positive-frequency terms.<br/>
    $A[n/2+1:]$ contains the negative-frequency terms in the order of decreasing negative frequency
    $A[n/2]$ represents both positive and negative Nyquist frequency for an even number of input points. It is also purely real for real input. <br/>
    $A[(n-1)/2]$ contains the largest positive frequency for an odd number of input points. <br/>
    $A[(n+1)/2]$ contains the largest negative frequency.<br/>
</li>
<li><b>$fftfreq(n)$</b> <br/> 
    returns an array giving the frequencies of corresponding elements in the output.
  </li>
<li><b>$fftshift(A)$</b> <br/> 
    shifts transforms and their frequencies to put the zero-frequency components in the middle.
  </li>
<li><b>$ifftshift(A)$</b> <br/> 
    undoes the shift done by $fftshift(A)$.
  </li>
</ol>
<br/><br/>
<p>When <b>$a$</b> is a time-domain signal in $A = fft(a)$ </p>
<ol>
<li><b>$abs(A)$</b> : its amplitude spectrum </li>
<li><b>$\{ abs(A) \}^2$</b> : its power spectrum </li>
<li><b>$angle(A)$</b> : its phase spectrum </li>
</ol>
<br/>
<br/>


<!-- bogo1 -->
<div>
  <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo1 -->
  <ins class="adsbygoogle"
     style="display:inline-block;width:728px;height:90px"
     data-ad-client="ca-pub-4716428189734495"
     data-ad-slot="6542308167"></ins>
  <script>
   (adsbygoogle = window.adsbygoogle || []).push({});
  </script>
</div>


<!-- Google search box -->
<div class="AdSenseSearch">
  bogotobogo.com site search:
  <form action="//www.google.com" id="cse-search-box" target="_blank">
    <div>
      <input type="hidden" name="cx" value="partner-pub-4716428189734495:1794050961" />
      <input type="hidden" name="ie" value="UTF-8" />
      <!--<input type="text" name="q" size="55" />-->
      <input type="text" name="q" size="" width="90%"/>
      <input type="submit" name="sa" value="Search" />
    </div>
  </form>
  <script type="text/javascript" src="//www.google.com/coop/cse/brand?form=cse-search-box&amp;lang=en"></script>
</div>


<br/>
<br/>
<div class="subtitle_2nd" id="imageFFT">Image FFT</div>
<pre>
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xfiles.jpg',0)
f = np.<font color="red">fft.fft2</font>(img)
fshift = np.<font color="red">fft.fftshift</font>(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()          
</pre>
<p>The '2' in $fft2()$ indicates that we're using 2-D fft. The $fft2()$ provides us the frequency transform which will be a complex array. Its first argument is the input image, which is grayscale. Second argument is optional which decides the size of output array.</p>
<p>If we use interactive shell, the $f$ looks like this:</p>
<pre>
&gt;&gt;&gt; f.shape
(194, 259)
</pre>
<br/>
<p>We can see $fft2()$ returns a complex array:</p>
<pre>
&gt;&gt;&gt; f
array([[ 842784.00000000    +0.j        , -517752.56442341 -3696.20384447j,
          91285.56071617 +4921.45028062j, ...,
         -46601.18635079 -4814.84303878j,   91285.56071617 -4921.45028062j,
        -517752.56442341 +3696.20384447j],
       [ 123232.14686474+22090.02037498j,    -856.26680325 +9182.45344817j,
        -136191.25175358-51466.45725155j, ...,
          71425.20605824+14903.15993681j, -158452.77640809-31181.5124568j ,
          -3060.27297752+19352.80159523j],
       [ -36743.19890402-14189.86326576j,   28037.83427034+45830.48236385j,
          -5472.34460100  +751.10794956j, ...,
         -17431.81487318-56998.95644394j,  -27977.32223743-17396.44346126j,
          55230.60393901+23180.07097916j],
       ..., 
       [-107889.78457811+41341.29205987j,   15392.03432529 +8349.74473343j,
          61145.55093605-59049.02715308j, ...,
          40527.83113022+19449.36030634j,   73913.64630259-52167.06835863j,
          -7173.60813531 +8395.54640485j],
       [ -36743.19890402+14189.86326576j,   55230.60393901-23180.07097916j,
         -27977.32223743+17396.44346126j, ...,
         -29773.75673263+47038.82271301j,   -5472.34460100  -751.10794956j,
          28037.83427034-45830.48236385j],
       [ 123232.14686474-22090.02037498j,   -3060.27297752-19352.80159523j,
        -158452.77640809+31181.5124568j , ...,
          58992.94700240 +3233.35145839j, -136191.25175358+51466.45725155j,
           -856.26680325 -9182.45344817j]])
</pre>
<p>We did $ffshift()$ because we want to place the zero-frequency component to the center of the spectrum. In other words, once we got the result, zero frequency component (DC component) will be at top left corner. Because we want to bring it to center, we needed to shift the result by $\frac{n}{2}$ in both the directions using $np.fft.fftshift()$.</p>
<p>Once we found the frequency transform, we can find the magnitude spectrum:</p>
<pre>
magnitude_spectrum = 20*np.log(np.abs(fshift))
</pre>
<br/>
<img alt="NumPyFFT_xfiles.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_xfiles.png"/>
<br/>
<p>Now we can see more whiter region at the center showing we have more low frequency content.</p>
<br/>
<br/>

<!-- Google bogo_square_ad -->
<div>
  <script type="text/javascript">
    google_ad_client = "ca-pub-4716428189734495";
    /* bogo_LargeRectangle_336_280 */
    google_ad_slot = "2712696561";
    google_ad_width = 336;
    google_ad_height = 280;
  </script>
  <script type="text/javascript"
    src="//pagead2.googlesyndication.com/pagead/show_ads.js">
  </script>
</div>
<br>





<br/>
<br/>
<p>If we undo the shift using $ffshift()$:</p>
<pre>
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
fshift = np.fft.<font color="blue">ifftshift</font>(fshift)
</pre>
<p>The picture will look like this:</p>
<img alt="NumPyFFT_xfiles_No_Shift.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_xfiles_No_Shift.png"/>
<br/>
<br/>
<br/>
<br/>
<br/>
<div class="subtitle_2nd" id="more_samples">More Samples</div>
<p>Here are more fft samples:</p>
<img alt="NumPyFFT_snow.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_snow.png"/>
<br/>
<br/>
<img alt="NumPyFFT_green.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_green.png"/>
<br/>
<br/>
<img alt="NumPyFFT_black.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_black.png"/>
<br/>
<br/>
<img alt="NumPyFFT_checker.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_checker.png"/>
<br/>
<br/>
<img alt="NumPyFFT_maze.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_maze.png"/>
<br/>
<br/>
<img alt="NumPyFFT_vlines.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_vlines.png"/>
<br/>
<br/>
<img alt="NumPyFFT_hlines.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_hlines.png"/>
<br/>
<br/>
<img alt="NumPyFFT_circle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_circle.png"/>
<br/>
<br/>
<img alt="NumPyFFT_whitecircle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_whitecircle.png"/>
<br/>
<br/>
<img alt="NumPyFFT_blackcircle.png" src="/python/OpenCV_Python/images/FFT/NumPyFFT_blackcircle.png"/>
<br/>
<br/>
<br/>
<br/>
<div class="subtitle_2nd" id="DFT">DFT and inverse DFT</div>
<p>We found the frequency transform for an image in the previous section. So, now we can do some operations in frequency domain, like high pass filtering (HPF) and reconstruct the image using inverse DFT.</p>
<p>We can simply remove the low frequencies by masking with a rectangular window of size 60x60. Then, apply the inverse shift using $ifftshift()$ so that DC component again come at the top-left corner. Then, find inverse FFT using $ifft2()$ function. The result, again, will be a complex number. We can take its absolute value.</p>
<p>The DFT (Discrete Fourier Transform) is defined as:
$$A_k = \sum_{m=0}^{n-1} a_m exp\{ -2\pi i \frac{mk}{n} \} \quad\quad k=0,...,n-1.$$
The inverse DFT is defined as this:
$$A_m = \frac{1}{n} \sum_{k=0}^{n-1} A_k exp\{ 2\pi i \frac{mk}{n} \} \quad\quad m=0,...,n-1.$$

<div class="subtitle_2nd" id='code"'>Code</div>
<pre>
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xfiles.jpg',0)

# fft to convert the image to freq domain 
f = np.fft.fft2(img)

# shift the center
fshift = np.fft.fftshift(f)

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# remove the low frequencies by masking with a rectangular window of size 60x60
# High Pass Filter (HPF)
<font color="blue">fshift[crow-30:crow+30, ccol-30:ccol+30] = 0</font>

# shift back (we shifted the center before)
f_ishift = np.fft.<font color="red">ifftshift</font>(fshift)

# inverse fft to get the image back 
img_back = np.fft.<font color="red">ifft2</font>(f_ishift)

img_back = np.<font color="red">abs</font>(img_back)

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
plt.subplot(133),plt.imshow(img_back)
plt.title('Fianl Result'), plt.xticks([]), plt.yticks([])

plt.show()
</pre>
<br/>
<img alt="IDFT.png" src="/python/OpenCV_Python/images/FFT/IDFT.png"/>
<br/>
<p>The result shows High Pass Filtering (HPF) is an edge detection operation. This also shows that most of the image data is present in the Low frequency region of the spectrum. </p>
<p>If we watch the result more closely, especially the last image, we can see some artifacts which shows some ripple like structures there, and it is called <b>ringing effects</b>. It is caused by the rectangular window we used for masking. This mask is converted to sine shape which causes this problem. So rectangular windows is not used for filtering. Better option is Gaussian Windows.</p>
<p>Now that we know how to find DFT, IDFT etc. in Numpy. So, let's do it with OpenCV but in next chapter.</p>
<br/>
<br/>
<div class="subtitle_2nd" id="refs">References</div>
<ol>
<li><a href="http://docs.opencv.org/trunk/doc/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html#fourier-transform" target="_blank">Fourier Transform</a></li>
</ol>
<br/><br/>
<br/>
<br/>

<br/>
<br />
<h1>OpenCV 3 Tutorial </h1>
<h1>image & video processing</h1>
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_ubuntu14_install_cmake.php" target="_blank">Installing on Ubuntu 13</a> 
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_mat_object_image_matrix_image_container.php" target="_blank">Mat(rix) object (Image Container)</a> 
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_creating_mat_objects.php" target="_blank">Creating Mat objects</a>
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_load_convert_save_image.php" target="_blank">The core : Image - load, convert, and save</a> 
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_imgproc_gausian_median_blur_bilateral_filter_image_smoothing.php" target="_blank">Smoothing Filters A - Average, Gaussian</a>
  <br><br>
  <a href="/OpenCV/opencv_3_tutorial_imgproc_gausian_median_blur_bilateral_filter_image_smoothing_B.php" target="_blank">Smoothing Filters B - Median, Bilateral</a>
  <br><br>

<br/>
<br><br><br>
<h1>OpenCV 3 image and video processing with Python</h1>

   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3.php" target="_blank">OpenCV 3 with Python</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php" target="_blank">Image - OpenCV BGR : Matplotlib RGB</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php" target="_blank">Basic image operations - pixel access</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php" target="_blank">iPython - Signal Processing with NumPy</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT.php" target="_blank">Signal Processing with NumPy I - FFT and DFT for sine, square waves, unitpulse, and random signal</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" target="_blank">Signal Processing with NumPy II - Image Fourier Transform : FFT & DFT</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Fourier_Transform_FFT_DFT.php" target="_blank">Inverse Fourier Transform of an Image with low pass filter: cv2.idft() </a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php" target="_blank">Image Histogram</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Changing_ColorSpaces_RGB_HSV_HLS.php" target="_blank">Video Capture and Switching colorspaces - RGB / HSV</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Global_Thresholding_Adaptive_Thresholding_Otsus_Binarization_Segmentations.php" target="_blank">Adaptive Thresholding - Otsu's clustering-based image thresholding</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php" target="_blank">Edge Detection - Sobel and Laplacian Kernels</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Canny_Edge_Detection.php" target="_blank">Canny Edge Detection</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php" target="_blank">Hough Transform - Circles</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation.php" target="_blank">Watershed Algorithm : Marker-based Segmentation I</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation_2.php" target="_blank">Watershed Algorithm : Marker-based Segmentation II</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php" target="_blank">Image noise reduction : Non-local Means denoising algorithm</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php" target="_blank">Image object detection : Face detection using Haar Cascade Classifiers</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Segmentation_by_Foreground_Extraction_Grabcut_Algorithm_based_on_Graph_cuts.php" target="_blank">Image segmentation - Foreground extraction Grabcut algorithm based on graph cuts</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_reconstruction_Inpainting_Interpolation.php" target="_blank">Image Reconstruction - Inpainting (Interpolation) - Fast Marching Methods</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_mean_shift_tracking_segmentation.php" target="_blank">Video : Mean shift object tracking</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization.php" target="_blank">Machine Learning : Clustering - K-Means clustering I</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization_2.php" target="_blank">Machine Learning : Clustering - K-Means clustering II</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Classification_K-nearest_neighbors_k-NN.php" target="_blank">Machine Learning : Classification - k-nearest neighbors (k-NN) algorithm</a> 


<br />
<br/>
<br/>
<br/>
<br/>

</p>
<div>
    
<div class="custom-disqus">
<!-- Disqus -->
<div id="disqus_thread"></div>
<script>
    /**
     *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
     *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
     */
     
/* Disabling Disqus 4/26/2017
    var disqus_config = function () {
        this.page.url = window.location.href;
        this.page.identifier = document.title;
    };
    
    (function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
        var d = document, s = d.createElement('script');
        
        s.src = '//bogotobogocom.disqus.com/embed.js';  // IMPORTANT: Replace EXAMPLE with your forum shortname!
        
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
 Disabling Disqus */    
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>

<!-- Disqus ends here -->
</div>

<br>
<br>
<br>
<br></div>
          </div>
          <div class="col-sm-3 col-md-3 col-xs-3">
  	    <div class="g-person" data-width="1" data-href="//plus.google.com/111664369941456137911" data-rel="author">
  	    </div>
            <div class="resume">
              <p>Ph.D. / Golden Gate Ave, San Francisco / Seoul National Univ / Carnegie Mellon / UC Berkeley / DevOps / Deep Learning / Visualization</p>
            </div>
  	    <div>
                
<div class="skyscraper">
  <br>


<div class="skyscraper">

  <div class="bogo-paypal">
    <!-- Paypal Donate button -->
    <p><i>Sponsor Open Source development activities and free contents for everyone.</i></p>

    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----MIIHRwYJKoZIhvcNAQcEoIIHODCCBzQCAQExggEwMIIBLAIBADCBlDCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb20CAQAwDQYJKoZIhvcNAQEBBQAEgYC0In+maN+zseQtRj6SJqP9kj2LLvKf0yFklTm01uHY7UwgB3YJ0MZwvi6iERXfh4x2/KVYyMzY6elATG68c3gd6gb0Pqca380dXCg2Xua8jlW0pTZ3UabUNkpYi0iIwMSUsvWKbIw9eX8cBljOrYU1CXNuk46c0Yz2J3lGG+xCZTELMAkGBSsOAwIaBQAwgcQGCSqGSIb3DQEHATAUBggqhkiG9w0DBwQI23eIgGIDbFqAgaDMolOA+os0Y06D0j9NgHZJahDCSSl3deolhu6gz8hNd0SKwNAMBDPd5LBjJ7v6QgReCprB9L2E6CVpXZwgyLnzPC/wHbQG0Qd9sc/CqbiFy2FaJodDtPbRS8mOh+aHph0pNXgZ2kRA8uqVGIRF5gc0d6wqx7+NrPK5FehCMWoGGTmfTTMlykPVQhwDAY8+QFNSbCnqih5GXX62XpkmMJWFoIIDhzCCA4MwggLsoAMCAQICAQAwDQYJKoZIhvcNAQEFBQAwgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMB4XDTA0MDIxMzEwMTMxNVoXDTM1MDIxMzEwMTMxNVowgY4xCzAJBgNVBAYTAlVTMQswCQYDVQQIEwJDQTEWMBQGA1UEBxMNTW91bnRhaW4gVmlldzEUMBIGA1UEChMLUGF5UGFsIEluYy4xEzARBgNVBAsUCmxpdmVfY2VydHMxETAPBgNVBAMUCGxpdmVfYXBpMRwwGgYJKoZIhvcNAQkBFg1yZUBwYXlwYWwuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBR07d/ETMS1ycjtkpkvjXZe9k+6CieLuLsPumsJ7QC1odNz3sJiCbs2wC0nLE0uLGaEtXynIgRqIddYCHx88pb5HTXv4SZeuv0Rqq4+axW9PLAAATU8w04qqjaSXgbGLP3NmohqM6bV9kZZwZLR/klDaQGo1u9uDb9lr4Yn+rBQIDAQABo4HuMIHrMB0GA1UdDgQWBBSWn3y7xm8XvVk/UtcKG+wQ1mSUazCBuwYDVR0jBIGzMIGwgBSWn3y7xm8XvVk/UtcKG+wQ1mSUa6GBlKSBkTCBjjELMAkGA1UEBhMCVVMxCzAJBgNVBAgTAkNBMRYwFAYDVQQHEw1Nb3VudGFpbiBWaWV3MRQwEgYDVQQKEwtQYXlQYWwgSW5jLjETMBEGA1UECxQKbGl2ZV9jZXJ0czERMA8GA1UEAxQIbGl2ZV9hcGkxHDAaBgkqhkiG9w0BCQEWDXJlQHBheXBhbC5jb22CAQAwDAYDVR0TBAUwAwEB/zANBgkqhkiG9w0BAQUFAAOBgQCBXzpWmoBa5e9fo6ujionW1hUhPkOBakTr3YCDjbYfvJEiv/2P+IobhOGJr85+XHhN0v4gUkEDI8r2/rNk1m0GA8HKddvTjyGw/XqXa+LSTlDYkqI8OwR8GEYj4efEtcRpRYBxV8KxAW93YDWzFGvruKnnLbDAF6VR5w/cCMn5hzGCAZowggGWAgEBMIGUMIGOMQswCQYDVQQGEwJVUzELMAkGA1UECBMCQ0ExFjAUBgNVBAcTDU1vdW50YWluIFZpZXcxFDASBgNVBAoTC1BheVBhbCBJbmMuMRMwEQYDVQQLFApsaXZlX2NlcnRzMREwDwYDVQQDFAhsaXZlX2FwaTEcMBoGCSqGSIb3DQEJARYNcmVAcGF5cGFsLmNvbQIBADAJBgUrDgMCGgUAoF0wGAYJKoZIhvcNAQkDMQsGCSqGSIb3DQEHATAcBgkqhkiG9w0BCQUxDxcNMTUwOTA2MTYwNDAxWjAjBgkqhkiG9w0BCQQxFgQUuyx70nay4O6eJQs3x4WiAm4/7DkwDQYJKoZIhvcNAQEBBQAEgYAN7yS/34G8dBK6CfFf5g4rQk/H8s7D/aUmIzppGWOoXR7nZuXQo99wSBlQsPdeFtB+a+NNapf6lC4ibUTjgSpbu1gscGHH4Y+QtXl03bt5qgaSoFhZsCJKubwRHPHGHDGVx+tQmQ2DHk09lXjjL61FpB6iqkiFFvw4vfixsoeI6g==-----END PKCS7-----
    ">
    <input type="image" src="https://www.paypalobjects.com/webstatic/en_US/btn/btn_donate_pp_142x27.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>
    <p><i>Thank you.</i></p>
    <p>- <a href="http://bogotobogo.com/about_us.php" target="_blank">K Hong</a></p>
    <!-- End of Paypal Donate button   -->
  </div>


  <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo_skyscraper -->
  <ins class="adsbygoogle"
       style="display:inline-block;width:160px;height:600px"
       data-ad-client="ca-pub-4716428189734495"
       data-ad-slot="5321096966"></ins>
  <script>
  (adsbygoogle = window.adsbygoogle || []).push({});
  </script>


  <br><br>





</div></div>




<!-- Place this tag after the last widget tag. -->
<script type="text/javascript">
        (function() {
          var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
          po.src = 'https://apis.google.com/js/platform.js';
          var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
        })();
</script>
  	    </div>
  	    <div class="side_menu">
                
<br><br>

<br><br><br>
<h1>OpenCV 3 image and video processing with Python</h1>

   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3.php" target="_blank">OpenCV 3 with Python</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php" target="_blank">Image - OpenCV BGR : Matplotlib RGB</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_basic_image_operations_pixel_access_image_load.php" target="_blank">Basic image operations - pixel access</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php" target="_blank">iPython - Signal Processing with NumPy</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT.php" target="_blank">Signal Processing with NumPy I - FFT and DFT for sine, square waves, unitpulse, and random signal</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Signal_Processing_with_NumPy_Fourier_Transform_FFT_DFT_2.php" target="_blank">Signal Processing with NumPy II - Image Fourier Transform : FFT & DFT</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Fourier_Transform_FFT_DFT.php" target="_blank">Inverse Fourier Transform of an Image with low pass filter: cv2.idft() </a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_image_histogram_calcHist.php" target="_blank">Image Histogram</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Changing_ColorSpaces_RGB_HSV_HLS.php" target="_blank">Video Capture and Switching colorspaces - RGB / HSV</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Global_Thresholding_Adaptive_Thresholding_Otsus_Binarization_Segmentations.php" target="_blank">Adaptive Thresholding - Otsu's clustering-based image thresholding</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Gradient_Sobel_Laplacian_Derivatives_Edge_Detection.php" target="_blank">Edge Detection - Sobel and Laplacian Kernels</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Canny_Edge_Detection.php" target="_blank">Canny Edge Detection</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Hough%20Circle_Transform.php" target="_blank">Hough Transform - Circles</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation.php" target="_blank">Watershed Algorithm : Marker-based Segmentation I</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Watershed_Algorithm_Marker_Based_Segmentation_2.php" target="_blank">Watershed Algorithm : Marker-based Segmentation II</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Non-local_Means_Denoising_Algorithm_Noise_Reduction.php" target="_blank">Image noise reduction : Non-local Means denoising algorithm</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Object_Detection_Face_Detection_Haar_Cascade_Classifiers.php" target="_blank">Image object detection : Face detection using Haar Cascade Classifiers</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_Segmentation_by_Foreground_Extraction_Grabcut_Algorithm_based_on_Graph_cuts.php" target="_blank">Image segmentation - Foreground extraction Grabcut algorithm based on graph cuts</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Image_reconstruction_Inpainting_Interpolation.php" target="_blank">Image Reconstruction - Inpainting (Interpolation) - Fast Marching Methods</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_mean_shift_tracking_segmentation.php" target="_blank">Video : Mean shift object tracking</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization.php" target="_blank">Machine Learning : Clustering - K-Means clustering I</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Clustering_K-Means_Clustering_Vector_Quantization_2.php" target="_blank">Machine Learning : Clustering - K-Means clustering II</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_Machine_Learning_Classification_K-nearest_neighbors_k-NN.php" target="_blank">Machine Learning : Classification - k-nearest neighbors (k-NN) algorithm</a> 


<br>

<div class="skyscraper">
  <br>


<div class="skyscraper">

  <div class="bogo-paypal">
    <!-- Paypal Donate button -->
    <p><i>Sponsor Open Source development activities and free contents for everyone.</i></p>

    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
    <input type="hidden" name="cmd" value="_s-xclick">
    <input type="hidden" name="encrypted" value="-----BEGIN PKCS7-----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-----END PKCS7-----
    ">
    <input type="image" src="https://www.paypalobjects.com/webstatic/en_US/btn/btn_donate_pp_142x27.png" border="0" name="submit" alt="PayPal - The safer, easier way to pay online!">
    <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>
    <p><i>Thank you.</i></p>
    <p>- <a href="http://bogotobogo.com/about_us.php" target="_blank">K Hong</a></p>
    <!-- End of Paypal Donate button   -->
  </div>


  <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
  <!-- bogo_skyscraper -->
  <ins class="adsbygoogle"
       style="display:inline-block;width:160px;height:600px"
       data-ad-client="ca-pub-4716428189734495"
       data-ad-slot="5321096966"></ins>
  <script>
  (adsbygoogle = window.adsbygoogle || []).push({});
  </script>


  <br><br>





</div></div>

<br>
<div>
<br><br>
<h1>Python tutorial</h1>
   <br><br>
   <a href="/python/pytut.php">Python Home</a> 
   <br><br>
   <a href="/python/python_introduction.php">Introduction</a> 
   <br><br>
   <a href="/python/python_running.php">Running Python Programs (os, sys, import)</a> 
   <br><br>
   <a href="/python/python_modules_idle.php">Modules and IDLE (Import, Reload, exec)</a> 
   <br><br>
   <a href="/python/python_numbers_strings.php">Object Types - Numbers, Strings, and None</a> 
   <br><br>
   <a href="/python/python_strings.php">Strings - Escape Sequence, Raw String, and Slicing</a> 
   <br><br>
   <a href="/python/python_strings_method.php">Strings - Methods</a> 
   <br><br>
   <a href="/python/python_string_formatting.php">Formatting Strings - expressions and method calls</a> 
   <br><br>
   <a href="/python/python_files.php">Files and os.path</a> 
   <br><br>
   <a href="/python/python_traversing_directory_tree_recursively_os_walk.php">Traversing directories recursively</a> 
   <br><br>
   <a href="/python/python_subprocess_module.php">Subprocess Module</a> 
   <br><br>
   <a href="/python/python_regularExpressions.php">Regular Expressions with Python</a> 
   <br><br>
   <a href="/python/python_lists.php">Object Types - Lists</a> 
   <br><br>
   <a href="/python/python_dictionaries_tuples.php">Object Types - Dictionaries and Tuples</a> 
   <br><br>
   <a href="/python/python_functions_def.php">Functions def, *args, **kargs</a> 
   <br><br>
   <a href="/python/python_functions_lambda.php">Functions lambda</a> 
   <br><br>
   <a href="/python/python_functions_built_in.php">Built-in Functions</a> 
   <br><br>
   <a href="/python/python_fncs_map_filter_reduce.php">map, filter, and reduce</a> 
   <br><br>
   <a href="/python/python_decorators.php">Decorators</a> 
   <br><br>
   <a href="/python/python_list_comprehension.php">List Comprehension</a> 
   <br><br>
   <a href="/python/python_sets_union_intersection.php">Sets (union/intersection) and itertools - Jaccard coefficient and shingling to check plagiarism</a> 
   <br><br>
   <a href="/python/python_hash_tables_hashing_dictionary_associated_arrays.php">Hashing (Hash tables and hashlib)</a> 
   <br><br>
   <a href="/python/python_dictionary_comprehension_with_zip_from_list.php">Dictionary Comprehension with zip</a> 
   <br><br>
   <a href="/python/python_function_with_yield_keyword_is_a_generator_iterator_next.php">The yield keyword</a> 
   <br><br>
   <a href="/python/python_generators.php">Generator Functions and Expressions</a> 
   <br><br>
   <a href="/python/python_function_with_generator_send_method_yield_keyword_iterator_next.php">generator.send() method</a> 
   <br><br>
   <a href="/python/python_iterators.php">Iterators</a> 
   <br><br>
   <a href="/python/python_classes_instances.php">Classes and Instances (__init__, __call__, etc.)</a>
   <br><br>
   <a href="/python/python_if__name__equals__main__.php">if__name__ == '__main__'</a>
   <br><br>
   <a href="/python/python_argparse.php">argparse</a>
   <br><br>
   <a href="/python/python_try_except_finally_raise_syntax_error.php">Exceptions</a>
   <br><br>
   <a href="/python/python_differences_between_static_method_and_class_method_instance_method.php">@static method vs class method</a>
   <br><br>
   <a href="/python/python_private_attributes_methods.php">Private attributes and private methods</a>
   <br><br>
   <a href="/python/python_bits_bytes_bitstring_constBitStream.php">bits, bytes, bitstring, and constBitStream</a>
   <br><br>
   <a href="/python/python-json-dumps-loads-file-read-write.php">json.dump(s) and json.load(s)</a>
   <br><br>
   <a href="/python/python_serialization_pickle_json.php">Python Object Serialization - pickle and json</a>
   <br><br>
   <a href="/python/python_yaml_json_conversion.php">Python Object Serialization - yaml and json</a>
   <br><br>
   <a href="/python/python_PriorityQueue_heapq_Data_Structure.php">Priority queue and heap queue data structure</a>
   <br><br>
   <a href="/python/python_graph_data_structures.php">Graph data structure</a>
   <br><br>
   <a href="/python/python_Dijkstras_Shortest_Path_Algorithm.php">Dijkstra's shortest path algorithm</a>
   <br><br>
   <a href="/python/python_Prims_Spanning_Tree_Data_Structure.php">Prim's spanning tree algorithm</a>
   <br><br>
   <a href="/python/python_closure.php">Closure</a>
   <br><br>
   <a href="/python/python_functional_programming.php">Functional programming in Python</a>
   <br><br>
   <a href="/python/python_ssh_remote_run.php">Remote running a local file using ssh </a>
   <br><br>
   <a href="/python/python_sqlite_connect_create_drop_table.php">SQLite 3 - A. Connecting to DB, create/drop table, and insert data into a table</a>
   <br><br>
   <a href="/python/python_sqlite_select_update_delete.php">SQLite 3 - B. Selecting, updating and deleting data</a>
   <br><br>
   <a href="/python/MongoDB_PyMongo/python_MongoDB_pyMongo_tutorial_installing.php">MongoDB with PyMongo I - Installing MongoDB ...</a>
   <br><br>
   <a href="/python/python_http_web_services.php">Python HTTP Web Services - urllib, httplib2</a>
   <br><br>
   <a href="/python/python_Web_scraping_with_selenium_for_domain_availability.php">Web scraping with Selenium for checking domain availability</a>
   <br><br>
   <a href="/python/python-REST-API-Http-Requests-for-Humans-with-Flask.php">REST API : Http Requests for Humans with Flask</a>
   <br><br>
   <a href="/python/Tornado/Python_Tornado_Blog_App.php">Blog app with Tornado</a>
   <br><br>
   <a href="/python/Multithread/python_multithreading_creating_threads.php">Multithreading ...</a>
   <br><br>
   <a href="/python/python_network_programming_server_client.php">Python Network Programming I - Basic Server / Client : A Basics</a>
   <br><br>
   <a href="/python/python_network_programming_server_client_file_transfer.php">Python Network Programming I - Basic Server / Client : B File Transfer</a>
   <br><br>
   <a href="/python/python_network_programming_tcp_server_client_chat_server_chat_client_select.php">Python Network Programming II - Chat Server / Client</a>
   <br><br>
   <a href="/python/python_network_programming_socketserver_framework_for_network_servers.php">Python Network Programming III - Echo Server using socketserver network framework</a>
   <br><br>
   <a href="/python/python_network_programming_socketserver_framework_for_network_servers_asynchronous_request_ThreadingMixIn_ForkingMixIn.php">Python Network Programming IV - Asynchronous Request Handling : ThreadingMixIn and ForkingMixIn</a>
   <br><br>
   <a href="/python/python_interview_questions.php">Python Interview Questions I</a> 
   <br><br>
   <a href="/python/python_interview_questions_2.php">Python Interview Questions II</a> 
   <br><br>
   <a href="/python/python_interview_questions_3.php">Python Interview Questions III</a> 
   <br><br>
   <a href="/python/python_interview_questions_4.php">Python Interview Questions IV</a> 
   <br><br>
   <a href="/python/python_interview_questions_5.php">Python Interview Questions V</a> 
   <br><br>
   <a href="/python/python_interview_questions_6.php">Python Interview Questions VI</a> 
   <br><br>
   <a href="/python/python_interview_questions_7.php">Python Interview Questions VII</a> 
   <br><br>
   <a href="/python/python_image_processing_with_Pillow_library.php">Image processing with Python image library Pillow</a> 
   <br><br>
   <a href="/python/python_cpp_sip.php">Python and C++ with SIP</a> 
   <br><br>
   <a href="/python/pydev_eclipse_plugin_install_python_IDE.php">PyDev with Eclipse</a> 
   <br><br>
   <a href="/python/python_matplotlib.php">Matplotlib</a> 
   <br><br>
   <a href="/python/python_redis_with_python.php">Redis with Python</a> 
   <br><br>
   <a href="/python/python_numpy_array_tutorial_basic_A.php">NumPy array basics A</a> 
   <br><br>
   <a href="/python/python_numpy_matrix_tutorial.php">NumPy Matrix and Linear Algebra</a> 
   <br><br>
   <a href="/python/python_Pandas_NumPy_Matplotlib.php">Pandas with NumPy and Matplotlib</a> 
   <br><br>
   <a href="/python/python_cellular_automata.php">Celluar Automata</a> 
   <br><br>
   <a href="/python/python_numpy_batch_gradient_descent_algorithm.php">Batch gradient descent algorithm</a> 
   <br><br>
   <a href="/python/python_longest_common_substring_lcs_algorithm_generalized_suffix_tree.php">Longest Common Substring Algorithm</a> 
   <br><br>
   <a href="/python/python_unit_testing.php">Python Unit Test - TDD using unittest.TestCase class</a> 
   <br><br>
   <a href="/python/python_site_page_ranking_by_keywords.php">Simple tool - Google page ranking by keywords</a> 
   <br><br>
   <a href="/python/GoogleApp/python_GoogleApp_HelloWorld.php">Google App Hello World</a> 
   <br><br>
   <a href="/python/GoogleApp/python_GoogleApp_WebApp2_WSGI.php">Google App webapp2 and WSGI</a>
   <br><br>
   <a href="/python/GoogleApp/python_GoogleApp_Uploading_HelloWorld.php">Uploading Google App Hello World</a> 
   <br><br>
   <a href="/python/python_differences_Python2_vs_Python3_port.php">Python 2 vs Python 3</a> 
   <br><br>
   <a href="/python/python_virtualenv_virtualenvwrapper.php">virtualenv and virtualenvwrapper</a> 
   <br><br>
   <a href="/DevOps/AWS/aws_S3_uploading_large_file.php">Uploading a big file to AWS S3 using boto module</a> 
   <br><br>
   <a href="/DevOps/AWS/aws_stopping_starting_instances.php">Scheduled stopping and starting an AWS instance</a> 
   <br><br>
   <a href="/Hadoop/BigData_hadoop_CDH5_stop_start_services.php">Cloudera CDH5 - Scheduled stopping and starting services</a> 
   <br><br>
   <a href="/python/python_Rackspace_API_curl_subprocess_Cloud_Files.php">Removing Cloud Files - Rackspace API with curl and subprocess</a> 
   <br><br>
   <a href="/python/python-Windows-Check-if-a-Process-is-Running-Hanging-Schtasks-Run-Stop.php">Checking if a process is running/hanging and stop/run a scheduled task on Windows</a> 
   <br><br>
   <a href="/Hadoop/BigData_hadoop_Apache_Spark_PySpark.php">Apache Spark 1.3 with PySpark (Spark Python API) Shell</a> 
   <br><br>
   <a href="/Hadoop/BigData_hadoop_Apache_Spark_Streaming.php">Apache Spark 1.2 Streaming</a> 
   <br><br>
   <a href="/python/Bottle/Python_Bottle_Framework.php">bottle 0.12.7 - Fast and simple WSGI-micro framework for small web-applications ...</a> 
   <br><br>
   <a href="/python/Flask/Python_Flask_Blog_App_Production_with_MongoDB_and_Apache_WSGI.php">Flask app with Apache WSGI on Ubuntu14/CentOS7 ...</a> 
   <br><br>
   <a href="/python/python_Selenium_WebDriver.php">Selenium WebDriver</a> 
   <br><br>
   <a href="/python/Fabric/python_Fabric.php">Fabric - streamlining the use of SSH for application deployment</a> 
   <br><br>
   <a href="/DevOps/Ansible/Ansible_SettingUp_Webservers_Nginx_Install_Env_Configure_Deploy_App.php" target="_blank">Ansible Quick Preview - Setting up web servers with Nginx, configure enviroments, and deploy an App</a>
   <br><br>
   <a href="/python/python_Neural_Networks_Backpropagation_for_XOR_using_one_hidden_layer.php">Neural Networks with backpropagation for XOR using one hidden layer</a> 
   <br><br>
   <a href="/python/NLTK/NLTK_install.php">NLP - NLTK (Natural Language Toolkit) ...</a> 
   <br><br>
   <a href="/python/RabbitMQ_Celery/python_Installing_RabbitMQ_Celery.php">RabbitMQ(Message broker server) and Celery(Task queue) ...</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_matplotlib_rgb_brg_image_load_display_save.php">OpenCV3 and Matplotlib ...</a> 
   <br><br>
   <a href="/FFMpeg/ffmpeg_fade_in_fade_out_transitions_effects_filters_slideshow_concat.php">Simple tool - Concatenating slides using FFmpeg ...</a> 
   <br><br>
   <a href="/python/OpenCV_Python/python_opencv3_NumPy_Arrays_Signal_Processing_iPython.php">iPython - Signal Processing with NumPy</a> 
   <br><br>
   <a href="/python/IPython/IPython_Jupyter_Install_iPython_Notebook_Matplotlib_Publishing_it_to_Github.php">iPython and Jupyter - Install Jupyter, iPython Notebook, drawing with Matplotlib, and publishing it to Github</a> 
   <br><br>
   <a href="/python/IPython/iPython_Jupyter_Notebook_with_Embedded_D3.php">iPython and Jupyter Notebook with Embedded D3.js</a> 
   <br><br>
   <a href="/VideoStreaming/YouTube/youtube-dl-embedding.php">Downloading YouTube videos using youtube-dl embedded with Python</a> 
   <br><br>
   <a href="/python/scikit-learn/scikit_machine_learning_Supervised_Learning_Unsupervised_Learning.php">Machine Learning : scikit-learn ...</a> 
   <br><br>
   <a href="/python/Django/Python_Django_tutorial_introduction.php">Django 1.6/1.8 Web Framework ...</a> 
</div>
<br>

  		
  	    </div>
          </div>
        </div>
      </div> <!-- / section -->
    </div>
  </div>

  <br>
<br>
<br>
<br>

<div class="custom-disqus">
<!-- Disqus -->
<!-- Disqus disabled Oct 17, 2016 
<div id="disqus_thread"></div>
<script>
    /**
     *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
     *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
     */
     
    var disqus_config = function () {
        this.page.url = window.location.href;
        this.page.identifier = document.title;
    };
    
    (function() {  // REQUIRED CONFIGURATION VARIABLE: EDIT THE SHORTNAME BELOW
        var d = document, s = d.createElement('script');
        
        s.src = '//bogotobogocom.disqus.com/embed.js';  // IMPORTANT: Replace EXAMPLE with your forum shortname!
        
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
    })();
     
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
---- Disable -->
<!-- Disqus ends here -->
</div>

<br>
<br>
<br>
<br>


<!-- footer starts here -->
<footer id="footer">
  <div class="container">
    <div class="row">
      <div class="col-md-4 widget">
        <h3 class="widget-title">Contact</h3>
        <div class="widget-body">
          <p>BogoToBogo<br>
            <a href="mailto:contactus@bogotobogo.com">contactus@bogotobogo.com</a><br>
          </p>  
        </div>
      </div>

      <div class="col-md-4 widget">
        <h3 class="widget-title">Follow Bogotobogo</h3>
        <div class="widget-body">

          <!--
          <ul>
            <li><a href="https://www.facebook.com/KHongSanFrancisco" target="_unknown"><i class="fa fa-facebook"></i></a></li>
            <li><a href="https://twitter.com/KHongTwit" target="_unknown"><i class="fa fa-twitter"></i></a></li>
            <li><a href="https://plus.google.com/u/0/+KHongSanFrancisco/posts" target="_unknown"><i class="fa fa-google-plus"></i> </a></li>
          </ul>
          -->
             <h3>
             <a href="https://www.facebook.com/KHongSanFrancisco" target="_unknown"><i class="fa fa-facebook"></i></a> 
             <a href="https://twitter.com/KHongTwit" target="_unknown"><i class="fa fa-twitter"></i></a> 
             <!--<a href="https://plus.google.com/u/0/+KHongSanFrancisco/posts" target="_unknown"><i class="fa fa-google-plus"></i> </a> -->
             </h3>

        </div>
      </div>

      <div class="col-md-4 widget">
        <h3 class="widget-title"><a href="/about_us.php">About Us</a></h3>
        <div class="widget-body">
            <a href="mailto:contactus@bogotobogo.com">contactus@bogotobogo.com</a><br>
            <br>
            Golden Gate Ave, San Francisco, CA 94115
          </p>  
        </div>
      </div>

    </div> 
  </div>
</footer>

<footer id="underfooter">
  <div class="container">
    <div class="row">
      
      <div class="col-md-6 widget">
        <div class="widget-body">
          <p>Golden Gate Ave, San Francisco, CA 94115 </p>
        </div>
      </div>

      <div class="col-md-6 widget">
        <div class="widget-body">
          <p class="text-right">
            Copyright &copy; 2020, bogotobogo<br> 
            Design: <a href="http://www.bogotobogo.com" rel="designer">Web Master</a> </p>
        </div>
      </div>

    </div>
  </div>
</footer>

  <!-- JavaScript libs are placed at the end of the document so the pages load faster -->
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min.js"></script>
<script type="text/javascript"
     src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
<!-- D3.js -->
<script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>

<!-- Google Analytics -->
<script type="text/javascript">
    var _gaq = _gaq || [];
    _gaq.push(['_setAccount', 'UA-12016988-2']);
    _gaq.push(['_trackPageview']);
    
    (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
    })();
</script>

<!-- Google Analytics --> 
<!-- We need this for Analytics -->
<script>
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

  ga('create', 'UA-43017326-1', 'bogotobogo.com');
  ga('send', 'pageview');

</script>
  
<!-- Google+ -->
<script type="text/javascript" src="//apis.google.com/js/plusone.js"></script>

  <!-- CDN MathJax -->
  <script type="text/x-mathjax-config">
    MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
  </script>
  <script type="text/javascript"
    src="//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
  </script>

</body>
</html>

