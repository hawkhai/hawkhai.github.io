<!DOCTYPE html>
<html>

    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>大海彤昕 SUN &amp; OCEAN</title> 
        <meta name="viewport" content="width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no" />
        <link rel="stylesheet" href="../css/main.css" />
        <link rel='stylesheet' href="../css/scope-one.css" />
        <link rel="stylesheet" href="../css/font-awesome.min.css" />
    </head>
    <body>

        <div id="jsref" class="post">

            <table class="dataintable browsersupport">
                <tr>
                    <th>修改时间</th>
                    <th>文件大小</th>
                    <th>文件</th>
                </tr>
                <?php
                $curdir = dirname(__FILE__);
                $files = scandir($curdir);

                $htmlist = parse_ini_file("htmlist.ini", true);

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

                    $mtime = date("Y-m-d H:i:s", filemtime($value));
                    $fsize = byteformat(filesize($value));
                    $target = $htmlist["htmlist"][$value];
                    $download = "<a href='$value' target='_blank'>$value</a>";
                    if ($target) {
                        echo "<tr>";
                        echo "<td style='padding: 5px 10px;'>$mtime</td>";
                        echo "<td style='padding: 5px 10px;'>$fsize</td>";
                        echo "<td style='padding: 5px 10px;'>$download</td>";
                        echo "</tr>\n";
                    }
                }
                ?>
            </table>

        </div>

    </body>
</html>
