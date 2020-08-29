<!DOCTYPE html>
<html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>大海彤心 SUN &amp; OCEAN</title> 
        <link rel="stylesheet" href="https://image.hawkhai.com/3.3.4_bootstrap.min.css" /> 
        <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no" />
        <link rel="stylesheet" type="text/css" href="assets/tools.css">
    </head>
    <body>

        <div id="jsref">

            <table class="dataintable browsersupport">
                <tr>
                    <th style="width:10%">修改时间</th>
                    <th style="width:5%">文件大小</th>
                    <!--<th style="width:10%">文件 MD5</th>-->
                    <th style="width:10%">文件名</th>
                    <th style="width:5%">下载</th>
                    <th style="width:20%">备注</th>
                </tr>
                <?php
                $curdir = dirname(__FILE__);
                $files = scandir($curdir);

                $comments = parse_ini_file("assets/tools.ini", true);

                function byteformat($size, $dec = 2) {
                    $a = array("B", "KB", "MB", "GB", "TB", "PB");
                    $pos = 0;
                    while ($size >= 1024) {
                        $size /= 1024;
                        $pos++;
                    }
                    return round($size, $dec) . " " . $a[$pos];
                }

                foreach ($files as $key => $value) {
                    if ($value == "." || $value == "..") {
                        continue;
                    }
                    if (!is_file($value)) {
                        continue;
                    }
                    $platform = $comments["platform"][$value];;
                    $mtime = date("Y-m", filemtime($value));
                    if ($_GET["mtime"] || true) {
                        $mtime = date("Y-m-d H:i:s", filemtime($value));
                    }
                    $fsize = byteformat(filesize($value));
                    $fname = "$value";
                    $comment = $comments["tools"][$value];
                    $icon = $comments["icons"][$value];
                    $download = "<a href='$value' target='_blank'>$platform</a>";
                    if ($comment) {
                        $md5 = file_get_contents("_md5dir/" . $value . ".md5");
                        echo "<tr>";
                        echo "<td>$mtime</td>";
                        echo "<td>$fsize</td>";
                        // echo "<td>$md5</td>";
                        echo "<td><img src=\"assets/$icon\" style=\"width:50px;height:50px\" />&nbsp;$fname</td>";
                        echo "<td>$download</td>";
                        echo "<td>$comment</td>";
                        echo "</tr>\n";
                    }
                }
                ?>
            </table>

        </div>

        <div class="container" style="margin-top:9%;margin-bottom:9%;"> 
            <div id="copyright" style="color:red;text-align:center;"> 
                <div style="color:#888;" class="sitkatext">
                    朝霞沐春风，大海映彤心
                </div>大海彤心 &middot; 
                <a href="http://www.sunocean.life/">WWW.SUNOCEAN.LIFE</a> 
                <br /> 
                <a style="color:#999;" href="http://www.beian.miit.gov.cn/">粤ICP备17134686号-2</a> 
            </div> 
        </div>  

    </body>
</html>
