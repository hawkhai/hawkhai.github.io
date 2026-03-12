<?php
$dir = dirname(__FILE__) . '/files';
if (!is_dir($dir)) {
    mkdir($dir, 0755, true);
}

$msg = '';
$msgType = '';

// 处理删除请求
if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['action']) && $_POST['action'] === 'delete') {
    $pwd = isset($_POST['pwd']) ? $_POST['pwd'] : '';
    if (md5($pwd) !== 'b2f8ad91addf53d67d02e1a5ba6cea88') {
        $msg = '密码错误，删除失败';
        $msgType = 'error';
    } else {
        $filesToDelete = isset($_POST['files']) ? $_POST['files'] : array();
        if (empty($filesToDelete)) {
            $msg = '未选择任何文件';
            $msgType = 'error';
        } else {
            $deleted = 0;
            $failed = 0;
            foreach ($filesToDelete as $filename) {
                $filename = basename($filename); // 安全处理
                $filepath = $dir . '/' . $filename;
                if (file_exists($filepath) && is_file($filepath)) {
                    if (unlink($filepath)) {
                        $deleted++;
                    } else {
                        $failed++;
                    }
                } else {
                    $failed++;
                }
            }
            if ($failed === 0) {
                $msg = "成功删除 {$deleted} 个文件";
                $msgType = 'ok';
            } else {
                $msg = "删除 {$deleted} 个文件，失败 {$failed} 个";
                $msgType = 'warning';
            }
        }
    }
    
    // POST-Redirect-GET 模式：删除后重定向，避免刷新重复提交和缓存问题
    session_start();
    $_SESSION['delete_msg'] = $msg;
    $_SESSION['delete_msg_type'] = $msgType;
    header('Location: ' . $_SERVER['PHP_SELF']);
    exit;
}

// 从 session 中读取消息（如果有）
session_start();
if (isset($_SESSION['delete_msg'])) {
    $msg = $_SESSION['delete_msg'];
    $msgType = $_SESSION['delete_msg_type'];
    unset($_SESSION['delete_msg']);
    unset($_SESSION['delete_msg_type']);
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
body { font-family: monospace; max-width: 860px; margin: 40px auto; padding: 0 16px; color: #111; background: #fff; }
h2 { border-bottom: 1px solid #ccc; padding-bottom: 6px; margin-bottom: 4px; }
.topbar { margin-bottom: 16px; font-size: 13px; display: flex; justify-content: space-between; align-items: center; }
.msg { border: 1px solid #ccc; padding: 8px 12px; margin-bottom: 12px; font-size: 13px; border-radius: 3px; }
.msg.ok { border-color: #6a6; background: #efe; color: #363; }
.msg.error { border-color: #c66; background: #fee; color: #633; }
.msg.warning { border-color: #da6; background: #ffc; color: #630; }
.delete-panel { display: none; padding: 10px; background: #f9f9f9; border: 1px solid #ddd; border-radius: 3px; margin-bottom: 12px; }
.delete-panel.show { display: block; }
.delete-panel input[type=password] { padding: 4px 8px; font-size: 13px; margin-right: 8px; width: 120px; }
.delete-panel button { padding: 4px 12px; font-size: 13px; cursor: pointer; margin-right: 6px; }
.delete-panel .btn-delete { background: #c33; color: #fff; border: 1px solid #a22; }
.delete-panel .btn-delete:hover { background: #d44; }
.delete-panel .btn-cancel { background: #eee; border: 1px solid #ccc; }
.delete-panel .btn-cancel:hover { background: #ddd; }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
th, td { text-align: left; padding: 5px 10px; border-bottom: 1px solid #ddd; }
th { background: #f0f0f0; }
th.check, td.check { width: 30px; text-align: center; }
td.size  { white-space: nowrap; width: 80px; color: #555; }
td.mtime { white-space: nowrap; width: 220px; color: #555; }
td.actions { white-space: nowrap; width: 60px; text-align: center; }
.abs { color: #aaa; font-size: 11px; }
td.name  { word-break: break-all; }
a { color: #06c; text-decoration: none; }
a:hover { text-decoration: underline; }
.empty { color: #999; padding: 12px 0; }
.btn-del-single { color: #c33; cursor: pointer; font-size: 12px; }
.btn-del-single:hover { color: #f44; text-decoration: underline; }
.toolbar { font-size: 13px; }
.toolbar a { margin-right: 12px; }
.toolbar .btn-batch-delete { color: #c33; cursor: pointer; }
.toolbar .btn-batch-delete:hover { text-decoration: underline; }
.toolbar .selected-count { color: #666; margin-left: 8px; }
</style>
</head>
<body>
<h2>文件列表</h2>
<div class="topbar">
    <div class="toolbar">
        <a href="upload.php">&uarr; 上传文件</a>
        <?php if (!empty($files)) { ?>
        <a href="#" class="btn-batch-delete" onclick="showDeletePanel(); return false;">批量删除</a>
        <span class="selected-count" id="selectedCount"></span>
        <?php } ?>
    </div>
</div>

<?php if ($msg !== '') { ?>
<div class="msg <?php echo $msgType; ?>"><?php echo htmlspecialchars($msg); ?></div>
<?php } ?>

<div class="delete-panel" id="deletePanel">
    <span id="deleteHint">确认删除选中的文件？</span>
    <input type="password" id="deletePwd" placeholder="删除密码" required>
    <button type="button" class="btn-delete" onclick="submitBatchDelete();">确认删除</button>
    <button type="button" class="btn-cancel" onclick="hideDeletePanel();">取消</button>
</div>

<form method="POST" id="fileListForm">
<input type="hidden" name="action" value="delete" id="deleteAction" disabled>
<input type="hidden" name="pwd" id="deletePwdHidden" disabled>
<table>
<tr>
    <th class="check"><?php if (!empty($files)) { ?><input type="checkbox" id="checkAll" onchange="toggleAll(this);"><?php } ?></th>
    <th>文件名</th>
    <th class="mtime">修改时间</th>
    <th class="size">大小</th>
    <th class="actions">操作</th>
</tr>
<?php if (empty($files)) { ?>
<tr><td colspan="5" class="empty">暂无文件</td></tr>
<?php } else { foreach ($files as $f) { ?>
<tr>
    <td class="check"><input type="checkbox" class="file-check" name="files[]" value="<?php echo htmlspecialchars($f['name']); ?>" onchange="updateCount();"></td>
    <td class="name"><a href="files/<?php echo rawurlencode($f['name']); ?>" download><?php echo htmlspecialchars($f['name']); ?></a></td>
    <td class="mtime"><?php echo reltime($f['mtime']); ?>  <span class="abs"><?php echo date('Y-m-d H:i:s', $f['mtime']); ?></span></td>
    <td class="size"><?php echo byteformat($f['size']); ?></td>
    <td class="actions"><a href="#" class="btn-del-single" onclick="deleteSingle('<?php echo htmlspecialchars($f['name'], ENT_QUOTES); ?>'); return false;">删除</a></td>
</tr>
<?php } } ?>
</table>
</form>

<script>
function toggleAll(checkbox) {
    const checks = document.querySelectorAll('.file-check');
    checks.forEach(c => c.checked = checkbox.checked);
    updateCount();
}

function updateCount() {
    const checked = document.querySelectorAll('.file-check:checked').length;
    const countEl = document.getElementById('selectedCount');
    if (checked > 0) {
        countEl.textContent = `(已选 ${checked} 个)`;
    } else {
        countEl.textContent = '';
    }
}

function showDeletePanel() {
    const checked = document.querySelectorAll('.file-check:checked').length;
    if (checked === 0) {
        alert('请先选择要删除的文件');
        return;
    }
    document.getElementById('deleteHint').textContent = `确认删除选中的 ${checked} 个文件？`;
    document.getElementById('deletePanel').classList.add('show');
}

function hideDeletePanel() {
    document.getElementById('deletePanel').classList.remove('show');
}

function submitBatchDelete() {
    const pwd = document.getElementById('deletePwd').value;
    if (!pwd) {
        alert('请输入删除密码');
        return;
    }
    
    const checked = document.querySelectorAll('.file-check:checked');
    if (checked.length === 0) {
        alert('请选择要删除的文件');
        return;
    }
    
    // 启用隐藏字段并设置值
    document.getElementById('deleteAction').disabled = false;
    document.getElementById('deletePwdHidden').disabled = false;
    document.getElementById('deletePwdHidden').value = pwd;
    
    // 提交表单
    document.getElementById('fileListForm').submit();
}

function deleteSingle(filename) {
    const pwd = prompt('请输入删除密码：');
    if (pwd === null) return;
    
    const form = document.createElement('form');
    form.method = 'POST';
    form.innerHTML = `
        <input type="hidden" name="action" value="delete">
        <input type="hidden" name="pwd" value="${pwd}">
        <input type="hidden" name="files[]" value="${filename}">
    `;
    document.body.appendChild(form);
    form.submit();
}
</script>
</body>
</html>
