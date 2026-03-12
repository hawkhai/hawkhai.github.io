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
* { margin: 0; padding: 0; box-sizing: border-box; }
body { 
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans SC', sans-serif;
    max-width: 900px; 
    margin: 0 auto; 
    padding: 24px; 
    color: #1a1a1a; 
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
}
.container {
    background: #fff;
    border-radius: 12px;
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    padding: 32px;
}
h2 { 
    font-size: 28px;
    font-weight: 600;
    color: #1a1a1a;
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 2px solid #e5e7eb;
}
.topbar { 
    margin-bottom: 20px; 
    display: flex; 
    justify-content: space-between; 
    align-items: center; 
}
.msg { 
    padding: 12px 16px; 
    margin-bottom: 20px; 
    font-size: 14px; 
    border-radius: 8px;
    border-left: 4px solid;
    animation: slideIn 0.3s ease;
}
@keyframes slideIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
.msg.ok { border-color: #10b981; background: #d1fae5; color: #065f46; }
.msg.error { border-color: #ef4444; background: #fee2e2; color: #991b1b; }
.msg.warning { border-color: #f59e0b; background: #fef3c7; color: #92400e; }
.delete-panel { 
    display: none; 
    padding: 16px; 
    background: #fef2f2; 
    border: 1px solid #fecaca; 
    border-radius: 8px; 
    margin-bottom: 20px;
    animation: slideIn 0.3s ease;
}
.delete-panel.show { display: block; }
.delete-panel input[type=password] { 
    padding: 8px 12px; 
    font-size: 14px; 
    margin-right: 10px; 
    width: 160px;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    outline: none;
    transition: all 0.2s;
}
.delete-panel input[type=password]:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}
.delete-panel button { 
    padding: 8px 16px; 
    font-size: 14px; 
    cursor: pointer; 
    margin-right: 8px;
    border-radius: 6px;
    border: none;
    font-weight: 500;
    transition: all 0.2s;
}
.delete-panel .btn-delete { 
    background: #ef4444; 
    color: #fff;
}
.delete-panel .btn-delete:hover { 
    background: #dc2626;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
}
.delete-panel .btn-cancel { 
    background: #f3f4f6; 
    color: #374151;
}
.delete-panel .btn-cancel:hover { 
    background: #e5e7eb;
}
table { 
    width: 100%; 
    border-collapse: separate;
    border-spacing: 0;
    font-size: 14px;
    overflow: hidden;
    border-radius: 8px;
    border: 1px solid #e5e7eb;
}
th, td { 
    text-align: left; 
    padding: 12px 16px;
}
th { 
    background: linear-gradient(to bottom, #f9fafb, #f3f4f6);
    font-weight: 600;
    color: #374151;
    border-bottom: 2px solid #e5e7eb;
}
td {
    border-bottom: 1px solid #f3f4f6;
    transition: background 0.2s;
}
tr:hover td {
    background: #f9fafb;
}
tr:last-child td {
    border-bottom: none;
}
th.check, td.check { width: 40px; text-align: center; }
td.size { white-space: nowrap; width: 100px; color: #6b7280; }
td.mtime { white-space: nowrap; width: 240px; color: #6b7280; }
td.actions { white-space: nowrap; width: 70px; text-align: center; }
.abs { color: #9ca3af; font-size: 12px; margin-left: 8px; }
td.name { word-break: break-all; }
a { 
    color: #667eea; 
    text-decoration: none;
    transition: color 0.2s;
}
a:hover { 
    color: #764ba2;
    text-decoration: underline;
}
.empty { 
    color: #9ca3af; 
    padding: 40px 0; 
    text-align: center;
    font-size: 14px;
}
.btn-del-single { 
    color: #ef4444; 
    cursor: pointer; 
    font-size: 13px;
    font-weight: 500;
}
.btn-del-single:hover { 
    color: #dc2626;
    text-decoration: underline;
}
.toolbar { 
    font-size: 14px;
    display: flex;
    align-items: center;
}
.toolbar a { 
    margin-right: 16px;
    padding: 8px 16px;
    border-radius: 6px;
    transition: all 0.2s;
    font-weight: 500;
}
.toolbar a:first-child {
    background: #667eea;
    color: #fff;
}
.toolbar a:first-child:hover {
    background: #5568d3;
    text-decoration: none;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}
.toolbar .btn-batch-delete { 
    color: #ef4444;
    cursor: pointer;
}
.toolbar .btn-batch-delete:hover { 
    color: #dc2626;
}
.toolbar .selected-count { 
    color: #6b7280; 
    margin-left: 8px;
    font-size: 13px;
}
input[type=checkbox] {
    width: 16px;
    height: 16px;
    cursor: pointer;
    accent-color: #667eea;
}
</style>
</head>
<body>
<div class="container">
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
</div>
</body>
</html>
