<?php
$dir = dirname(__FILE__) . '/files';
if (!is_dir($dir)) {
    mkdir($dir, 0755, true);
}

// 判断是否为 API 调用（?json=1 或 Accept: application/json）
$isApi = isset($_GET['json']) ||
    (isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false);

$msg = '';
$msgType = '';
$uploadedName = '';
$baseUrl = (isset($_SERVER['HTTPS']) && $_SERVER['HTTPS'] === 'on' ? 'https' : 'http')
        . '://' . $_SERVER['HTTP_HOST']
        . rtrim(dirname($_SERVER['SCRIPT_NAME']), '/');

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $pwd = isset($_POST['pwd']) ? $_POST['pwd'] : '';
    if (md5($pwd) !== 'b2f8ad91addf53d67d02e1a5ba6cea88') {
        $msg = ' 密码错误，文件未保存 ';
        $msgType = 'error';
    } else {
        $file = $_FILES['file'];
        if ($file['error'] !== UPLOAD_ERR_OK) {
            $errors = array(
                UPLOAD_ERR_INI_SIZE   => ' 文件超过服务器限制 ',
                UPLOAD_ERR_FORM_SIZE  => ' 文件超过表单限制 ',
                UPLOAD_ERR_PARTIAL    => ' 文件只上传了一部分 ',
                UPLOAD_ERR_NO_FILE    => ' 没有选择文件 ',
                UPLOAD_ERR_NO_TMP_DIR => ' 缺少临时目录 ',
                UPLOAD_ERR_CANT_WRITE => ' 写入磁盘失败 ',
            );
            $msg = isset($errors[$file['error']]) ? $errors[$file['error']] : ' 上传出错 (code=' . $file['error'] . ')';
            $msgType = 'error';
        } else {
            $name = basename($file['name']);
            $name = preg_replace('/[^\w\.\-\x{4e00}-\x{9fa5}]/u', '_', $name);
            $dest = $dir . '/' . $name;
            if (move_uploaded_file($file['tmp_name'], $dest)) {
                $msg = ' 上传成功：' . $name;
                $msgType = 'ok';
                $uploadedName = $name;
            } else {
                $msg = ' 移动文件失败，请检查目录权限 ';
                $msgType = 'error';
            }
        }
    }

    if ($isApi) {
        header('Content-Type: application/json; charset=utf-8');
        $resp = array('ok' => ($msgType === 'ok'), 'msg' => $msg);
        if ($uploadedName !== '') {
            $resp['filename'] = $uploadedName;
            $resp['url'] = $baseUrl . '/files/' . rawurlencode($uploadedName);
        }
        echo json_encode($resp, JSON_UNESCAPED_UNICODE);
        exit;
    }
}
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>文件上传</title>
<style>
body { font-family: monospace; max-width: 600px; margin: 40px auto; padding: 0 16px; color: #111; background: #fff; }
h2 { border-bottom: 1px solid #ccc; padding-bottom: 6px; }
pre.terms { background: #f6f6f6; border: 1px solid #ccc; padding: 14px 16px;
    font-family: monospace; font-size: 13px; line-height: 1.7;
    white-space: pre-wrap; word-break: break-all; margin-bottom: 12px; }
.agree { margin-bottom: 16px; font-size: 14px; }
.agree input { margin-right: 6px; }
fieldset { border: 1px solid #ccc; padding: 16px; margin: 0 0 12px; }
legend { font-weight: bold; padding: 0 6px; }
input[type=file] { display: block; margin-bottom: 12px; }
input[type=submit] { padding: 6px 20px; font-size: 14px; cursor: pointer; }
input[type=submit]:disabled { color: #999; cursor: not-allowed; }
.msg { border: 1px solid #ccc; padding: 8px 12px; margin-top: 12px; font-size: 13px; }
.ok    { border-color: #6a6; color: #363; }
.error { border-color: #c66; color: #633; }
a { color: #06c; }
</style>
</head>
<body>
<h2>文件上传</h2>

<div class="agree">
    <label>
    <input type="checkbox" id="agree"
        onchange="document.getElementById('btnSubmit').disabled=!this.checked;">
    我已阅读并同意以上协议
    </label>
</div>

<fieldset>
    <legend>选择文件</legend>
    <form method="POST" enctype="multipart/form-data">
    <input type="file" name="file">
    <input type="password" name="pwd" placeholder=" 上传密码" style="display:block;margin-bottom:12px;font-size:14px;">
    <input type="submit" id="btnSubmit" value=" 上传" disabled>
    </form>
<?php if ($msg !== '') { ?>
    <div class="msg <?php echo $msgType; ?>"><?php echo htmlspecialchars($msg); ?></div>
<?php } ?>
</fieldset>

<p><a href="index.php">&larr; 查看文件列表</a></p>


<pre class="terms">
========================================
    内部文件传输工具  —  使用协议
========================================

本工具供内部成员传递文本、配置、日志等小文件使用。

【使用规范】
1. 仅限内部成员使用，请勿对外公开本工具地址。
2. 上传的文件存储于公开目录，任何知晓链接的人均可
   直接访问和下载，请勿上传含密码、密钥、Token、
   个人隐私或任何敏感信息的文件。
3. 请勿上传可执行程序（.exe .bat .sh .php .py 等）
   及任何恶意文件。
4. 文件随时可能被清理，请勿依赖本服务做持久存储，
   重要文件请自行备份。
5. 使用即视为同意以上条款。

========================================
    API 文档
========================================

端点：  POST /blog/tools/upload.php
        POST /blog/tools/upload.php?json=1  （返回 JSON）

请求：  Content-Type: multipart/form-data
        字段名：file

--- 上传文件（curl 示例）---

# 浏览器表单方式（默认返回 HTML）
curl -F "file=@/path/to/yourfile.txt" \
    -F "pwd= 你的密码" \
    https://sunocean.life/blog/tools/upload.php

# JSON 模式（?json=1 或 Accept: application/json）
curl -F "file=@/path/to/yourfile.txt" \
    -F "pwd= 你的密码" \
    "https://sunocean.life/blog/tools/upload.php?json=1"

--- JSON 响应格式 ---

成功：
{
    "ok": true,
    "msg": "上传成功：yourfile.txt",
    "filename": "yourfile.txt",
    "url": "https://sunocean.life/blog/tools/files/yourfile.txt"
}

失败：
{
    "ok": false,
    "msg": "文件超过服务器限制"
}

--- 文件列表 ---

GET  /blog/tools/index.php          列表页面（HTML）

--- 文件下载 ---

GET  /blog/tools/files/{filename}   直接下载

========================================
    API 使用须知
========================================

1. API 无鉴权，任何能访问本域名的人均可调用，
   请在内网或可信环境下使用。
2. 文件名中非字母 / 数字 / 中文 /.-_ 的字符会被替换为
   下划线，请勿依赖特殊字符文件名。
3. 同名文件会被直接覆盖，无版本管理。
4. 上传大小受服务器 php.ini 限制（upload_max_filesize
   / post_max_size），超限返回错误。
5. 本 API 无速率限制，请合理使用，避免滥用。
</pre>
</body>
</html>
