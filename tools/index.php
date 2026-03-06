<?php
$dir = dirname(__FILE__) . '/files';
if (!is_dir($dir)) {
    mkdir($dir, 0755, true);
}

function reltime($ts) {
    $diff = time() - $ts;
    if ($diff < 60)           return ' 刚刚 ';
    if ($diff < 3600)         return intval($diff / 60) . ' 分钟前 ';
    if ($diff < 86400)        return intval($diff / 3600) . ' 小时前 ';
    if ($diff < 86400 * 2)    return ' 昨天 ' . date('H:i', $ts);
    if ($diff < 86400 * 7)    return intval($diff / 86400) . ' 天前 ';
    return date('m-d H:i', $ts);
}

function byteformat($size) {
    $units = array('B', 'KB', 'MB', 'GB', 'TB');
    $pos = 0;
    while ($size >= 1024 && $pos < 4) {
        $size /= 1024;
        $pos++;
    }
    return round($size, 2) . ' ' . $units[$pos];
}

$files = array();
foreach (scandir($dir) as $name) {
    $path = $dir . '/' . $name;
    if ($name === '.' || $name === '..' || !is_file($path)) continue;
    $files[] = array(
        'name'  => $name,
        'size'  => filesize($path),
        'mtime' => filemtime($path),
    );
}
usort($files, function($a, $b) { return $b['mtime'] - $a['mtime']; });
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>文件列表</title>
<style>
body { font-family: monospace; max-width: 760px; margin: 40px auto; padding: 0 16px; color: #111; background: #fff; }
h2 { border-bottom: 1px solid #ccc; padding-bottom: 6px; margin-bottom: 4px; }
.topbar { margin-bottom: 16px; font-size: 13px; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
th, td { text-align: left; padding: 5px 10px; border-bottom: 1px solid #ddd; }
th { background: #f0f0f0; }
td.size  { white-space: nowrap; width: 80px; color: #555; }
td.mtime { white-space: nowrap; width: 220px; color: #555; }
.abs { color: #aaa; font-size: 11px; }
td.name  { word-break: break-all; }
a { color: #06c; }
.empty { color: #999; padding: 12px 0; }
</style>
</head>
<body>
<h2>文件列表</h2>
<div class="topbar"><a href="upload.php">&uarr; 上传文件</a></div>
<table>
<tr><th>文件名</th><th class="mtime">修改时间</th><th class="size">大小</th></tr>
<?php if (empty($files)) { ?>
<tr><td colspan="3" class="empty">暂无文件</td></tr>
<?php } else { foreach ($files as $f) { ?>
<tr>
    <td class="name"><a href="files/<?php echo rawurlencode($f['name']); ?>" download><?php echo htmlspecialchars($f['name']); ?></a></td>
    <td class="mtime"><?php echo reltime($f['mtime']); ?>  <span class="abs"><?php echo date('Y-m-d H:i:s', $f['mtime']); ?></span></td>
    <td class="size"><?php echo byteformat($f['size']); ?></td>
</tr>
<?php } } ?>
</table>
</body>
</html>
