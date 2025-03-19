---
layout: post
title: "开发环境 -- Ubuntu 新 SSD 硬盘使用指南 & ftp config"
author:
location: "珠海"
categories: ["开发环境"]
tags: ["开发环境", "ftp"]
toc: true
toclistyle:
comments:
visibility:
mathjax:
mermaid:
glslcanvas:
codeprint:
---


## 在 Ubuntu 中使用新加的 SSD 硬盘


### 1. 检查硬盘是否被识别

首先，确认系统是否识别了新硬盘。

```bash
sudo fdisk -l
```

这将列出所有硬盘，找到新 SSD 的设备名（如 `/dev/sdb` ）。

* 1.0 TB Disk `/dev/nvme0n1p4`
* 4.0 TB Hard Disk `/dev/sda1`
* 2.0 TB Disk `/dev/sdb`


### 2. 格式化硬盘（如果需要）

如果硬盘未格式化或需要重新格式化，可以使用以下命令：

```bash
sudo mkfs.ext4 /dev/sdb
```

假设你要格式化为 `ext4` 文件系统，且分区为 `/dev/sdb` 。

* sudo mkfs.ext4 /dev/sdb


### 3. 创建挂载点

选择一个目录作为挂载点，例如 `/mnt/ssd` ：

```bash
sudo mkdir /mnt/ssd
```


### 4. 挂载硬盘

将硬盘挂载到刚创建的目录：

```bash
sudo mount /dev/sdb /mnt/ssd
```


### 5. 设置开机自动挂载

编辑 `/etc/fstab` 文件，添加以下内容：

```bash
/dev/sdb /mnt/ssd ext4 defaults 0 2
```

保存并退出。
sudo cp '/home/yqh/ 桌面 /fstab' /etc/fstab


### 6. 检查挂载

使用以下命令确认挂载成功：

```bash
df -h
```

你应该能看到 `/dev/sdb` 挂载在 `/mnt/ssd` 。


### 7. 使用硬盘

现在，你可以通过 `/mnt/ssd` 访问和使用新硬盘。


### 总结

- **设备名** ：如 `/dev/sdb`
- **挂载点** ：如 `/mnt/ssd`
- **格式化** ：根据需要选择是否格式化

完成这些步骤后，新 SSD 就可以正常使用了。


## 在 Ubuntu 上创建 FTP 服务并指定根目录为 `/mnt/ssd/ftp` ，同时支持开机自启动，可以使用 `vsftpd` （Very Secure FTP Daemon）


### 1. 安装 `vsftpd`

打开终端，运行以下命令安装 `vsftpd` ：

```bash
sudo apt update
sudo apt install vsftpd
```


### 2. 配置 `vsftpd`

编辑 `vsftpd` 的配置文件：

```bash
sudo nano /etc/vsftpd.conf
```

在文件中找到或添加以下配置：

```bash
# 禁止匿名登录
anonymous_enable=NO

# 允许本地用户登录
local_enable=YES

# 允许写入
write_enable=YES

# 设置本地用户的根目录
chroot_local_user=YES

# 指定根目录
local_root=/mnt/ssd/ftp

# 限制用户只能访问其根目录
allow_writeable_chroot=YES

# 启用被动模式（如果需要）
pasv_enable=YES
pasv_min_port=10000
pasv_max_port=10100
```

保存并退出编辑器（ `Ctrl+O` 保存， `Ctrl+X` 退出）。


### 3. 创建 FTP 根目录

创建 `/mnt/ssd/ftp` 目录，并设置权限：

```bash
sudo mkdir -p /mnt/ssd/ftp
sudo chown -R ftp:ftp /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp
```


### 4. 重启 `vsftpd` 服务

应用配置并重启服务：

```bash
sudo systemctl restart vsftpd
```


### 5. 设置开机自启动

确保 `vsftpd` 服务已启用开机自启动：

```bash
sudo systemctl enable vsftpd
```


### 6. 配置防火墙（如果需要）

如果启用了防火墙（如 `ufw` ），需要允许 FTP 端口：

```bash
sudo ufw allow 20/tcp
sudo ufw allow 21/tcp
sudo ufw allow 10000:10100/tcp
sudo ufw reload
```


### 7. 测试 FTP 服务

使用 FTP 客户端（如 `FileZilla` ）或命令行工具测试连接：

```bash
ftp localhost
```

输入本地用户的用户名和密码，确认可以访问 `/mnt/ssd/ftp` 目录。


### 总结

- **FTP 根目录** ：`/mnt/ssd/ftp`
- **配置文件** ：`/etc/vsftpd.conf`
- **开机自启动** ：已通过 `systemctl enable vsftpd` 启用
- **测试** ：使用 FTP 客户端或命令行工具连接测试

完成以上步骤后，FTP 服务即可正常运行并支持开机自启动。


## 在 Ubuntu 上使用 `vsftpd` 创建两个 FTP 账号，一个只读账号，一个支持读写的账号，可以按照以下步骤操作：


### 1. 安装 `vsftpd`

如果尚未安装 `vsftpd` ，先安装：

```bash
sudo apt update
sudo apt install vsftpd
```


### 2. 创建两个用户

创建两个用户，例如 `ftp_readonly` （只读）和 `ftp_readwrite` （读写）：

```bash
sudo adduser ftp_readonly # 35218764
sudo adduser ftp_readwrite # 54219863
```

按照提示设置密码和其他信息。


### 3. 设置用户根目录

将两个用户的根目录设置为 `/mnt/ssd/ftp` ：

```bash
sudo usermod -d /mnt/ssd/ftp ftp_readonly
sudo usermod -d /mnt/ssd/ftp ftp_readwrite
```


### 4. 配置 `vsftpd`

编辑 `vsftpd` 的配置文件：

```bash
sudo nano /etc/vsftpd.conf
```

确保以下配置已启用或添加：

```bash
# 禁止匿名登录
anonymous_enable=NO

# 允许本地用户登录
local_enable=YES

# 允许写入
write_enable=YES

# 设置本地用户的根目录
chroot_local_user=YES

# 允许可写根目录
allow_writeable_chroot=YES

# 启用被动模式（如果需要）
pasv_enable=YES
pasv_min_port=10000
pasv_max_port=10100
```

保存并退出编辑器。
```
sudo cp '/home/yqh/ 桌面 /vsftpd.conf' /etc/vsftpd.conf
```


### 5. 配置用户权限

#### 只读用户 ( `ftp_readonly` )

将 `/mnt/ssd/ftp` 目录的权限设置为只读：

```bash
sudo chown ftp_readonly:ftp_readonly /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp
```

#### 读写用户 ( `ftp_readwrite` )

将 `/mnt/ssd/ftp` 目录的权限设置为读写：

```bash
sudo chown ftp_readwrite:ftp_readwrite /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp
```


### 6. 限制只读用户的写权限

为了确保只读用户无法写入，可以通过 `vsftpd` 的配置文件限制其权限。
编辑 `/etc/vsftpd.conf` ，添加以下内容：

```bash
# 限制只读用户
user_config_dir=/etc/vsftpd/user_conf
```

然后创建用户配置文件目录：

```bash
sudo mkdir /etc/vsftpd
sudo mkdir /etc/vsftpd/user_conf
```

为只读用户 `ftp_readonly` 创建配置文件：

```bash
sudo nano /etc/vsftpd/user_conf/ftp_readonly
```

添加以下内容：

```bash
write_enable=NO
```

保存并退出。


### 7. 重启 `vsftpd` 服务

应用配置并重启服务：

```bash
sudo systemctl restart vsftpd
```


### 8. 测试 FTP 服务

使用 FTP 客户端（如 `FileZilla` ）或命令行工具测试连接：

- **只读用户** ：`ftp_readonly`
  - 应该只能读取文件，无法写入或删除。
- **读写用户** ：`ftp_readwrite`
  - 应该可以读取、写入和删除文件。


### 9. 设置开机自启动

确保 `vsftpd` 服务已启用开机自启动：

```bash
sudo systemctl enable vsftpd
```


### 总结

- **只读用户** ：`ftp_readonly` ，只能读取文件。
- **读写用户** ：`ftp_readwrite` ，可以读取和写入文件。
- **FTP 根目录** ：`/mnt/ssd/ftp`
- **配置文件** ：`/etc/vsftpd.conf` 和 `/etc/vsftpd/user_conf/ftp_readonly`
- **开机自启动** ：已通过 `systemctl enable vsftpd` 启用

完成以上步骤后，两个 FTP 账号即可正常运行，分别支持只读和读写权限。

要查看当前 `vsftpd` 服务中有哪些 FTP 账户，以及是否屏蔽了匿名登录，可以按照以下步骤操作：


### 1. 查看当前 FTP 账户

`vsftpd` 本身没有直接列出所有 FTP 账户的命令，但可以通过以下方法间接查看：

#### 方法 1：查看系统用户

`vsftpd` 默认允许本地系统用户登录。可以通过查看 `/etc/passwd` 文件来列出所有系统用户：

```bash
cat /etc/passwd
```

如果只想查看可能用于 FTP 的用户，可以过滤出普通用户（UID ≥ 1000）：

```bash
awk -F: '$3 >= 1000 {print $1}' /etc/passwd
```

#### 方法 2：查看 `vsftpd` 用户列表文件（如果配置了）

如果配置了 `userlist_file` 或 `userlist_enable` ，可以通过以下命令查看允许或禁止登录的用户：

```bash
cat /etc/vsftpd/user_list
```


### 2. 检查是否屏蔽了匿名登录

打开 `vsftpd` 的配置文件 `/etc/vsftpd.conf` ，查看以下配置项：

```bash
sudo nano /etc/vsftpd.conf
```

找到以下行：

```bash
anonymous_enable=NO
```

- 如果 `anonymous_enable=NO` ，则表示匿名登录已被禁用。
- 如果 `anonymous_enable=YES` ，则表示匿名登录已启用。

保存并退出编辑器。


### 3. 检查 `vsftpd` 的运行状态

可以通过以下命令查看 `vsftpd` 的运行状态，确认配置是否已生效：

```bash
sudo systemctl status vsftpd
```


### 4. 测试匿名登录（可选）

如果仍然不确定匿名登录是否被禁用，可以尝试使用匿名账户登录 FTP 服务器：

```bash
ftp localhost
```

输入用户名 `anonymous` ，密码可以为空或任意邮箱地址。如果登录失败，说明匿名登录已被禁用。


### 总结

- **查看 FTP 账户** ：通过 `/etc/passwd` 或 `/etc/vsftpd/user_list` 查看。
- **检查匿名登录** ：查看 `/etc/vsftpd.conf` 中的 `anonymous_enable` 配置。
- **测试匿名登录** ：使用 `ftp localhost` 尝试匿名登录。

通过这些步骤，你可以确认当前 FTP 服务的账户列表以及匿名登录是否被禁用。


## 要为 FTP 的读写账户分配文件创建权限，需要确保该账户对目标目录具有写权限


### 1. 确认读写账户

假设读写账户为 `ftp_readwrite` ，目标目录为 `/mnt/ssd/ftp` 。


### 2. 检查目录权限

确保 `/mnt/ssd/ftp` 目录的权限允许 `ftp_readwrite` 用户写入：

```bash
ls -ld /mnt/ssd/ftp
```

输出示例：

```bash
drwxr-xr-x 2 ftp_readwrite ftp_readwrite 4096 Oct 10 12:34 /mnt/ssd/ftp
```

- **所有者** ：`ftp_readwrite`
- **权限** ：`drwxr-xr-x` （所有者有读写执行权限，其他用户只有读和执行权限）

如果权限不正确，可以使用以下命令修复：

```bash
sudo chown ftp_readwrite:ftp_readwrite /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp

sudo chown ftp_readonly:ftp_readonly /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp
```


### 3. 确保 `vsftpd` 配置允许写入

编辑 `vsftpd` 的配置文件 `/etc/vsftpd.conf` ，确保以下配置已启用：

```bash
write_enable=YES
```

保存并退出编辑器，然后重启 `vsftpd` 服务：

```bash
sudo systemctl restart vsftpd
```


### 总结

- **目录权限** ：确保 `/mnt/ssd/ftp` 的所有者为 `ftp_readwrite` ，权限为 `755` 。
- ** `vsftpd` 配置** ：确保 `write_enable=YES` 。
- **测试** ：使用 FTP 客户端或命令行工具测试文件创建权限。
- **SELinux/AppArmor** ：如果启用，确保策略允许 FTP 写入。

完成以上步骤后， `ftp_readwrite` 账户应具备文件创建权限。


## 要为 `ftp_readonly` 用户分配文件夹列举权限，需要确保该用户对目标目录具有 **读取** 和 **执行** 权限


### 1. 检查目录权限

确保 `/mnt/ssd/ftp` 目录的权限允许 `ftp_readonly` 用户读取和列举文件。

运行以下命令检查目录权限：

```bash
ls -ld /mnt/ssd/ftp
```

输出示例：

```bash
drwxr-xr-x 2 ftp_readwrite ftp_readwrite 4096 Oct 10 12:34 /mnt/ssd/ftp
```

- **所有者** ：`ftp_readwrite`
- **权限** ：`drwxr-xr-x` （所有者有读写执行权限，其他用户只有读和执行权限）

如果权限不正确，可以使用以下命令修复：

```bash
sudo chmod 755 /mnt/ssd/ftp

sudo chown ftp_readonly:ftp_readonly /mnt/ssd/ftp
sudo chmod 755 /mnt/ssd/ftp
```


### 2. 确保 `vsftpd` 配置允许读取

编辑 `vsftpd` 的配置文件 `/etc/vsftpd.conf` ，确保以下配置已启用：

sudo nano /etc/vsftpd.conf

```bash
local_enable=YES
write_enable=YES
```

- `local_enable=YES` ：允许本地用户登录。
- `write_enable=YES` ：允许写入（即使只读用户不需要写入权限，此选项也需要启用以支持其他功能）。

保存并退出编辑器，然后重启 `vsftpd` 服务：

```bash
sudo systemctl restart vsftpd
```


### 3. 配置只读用户的权限

为了确保 `ftp_readonly` 用户只能读取文件而不能写入，可以通过 `vsftpd` 的用户配置文件限制其权限。

#### 创建用户配置文件

编辑 `ftp_readonly` 的用户配置文件：

```bash
sudo nano /etc/vsftpd/user_conf/ftp_readonly
```

添加以下内容：

```bash
write_enable=NO
```

保存并退出。

```
sudo cp '/home/yqh/ 桌面 /vsftpd_readonly.conf' /etc/vsftpd/user_conf/ftp_readonly
```

#### 确保 `vsftpd` 使用用户配置文件

编辑 `/etc/vsftpd.conf` ，确保以下配置已启用：

```bash
user_config_dir=/etc/vsftpd/user_conf
```

sudo nano /etc/vsftpd.conf

保存并退出，然后重启 `vsftpd` 服务：

```bash
sudo systemctl restart vsftpd
```


### 总结

- **目录权限** ：确保 `/mnt/ssd/ftp` 的权限为 `755` 。
- ** `vsftpd` 配置** ：确保 `local_enable=YES` 和 `write_enable=YES` 。
- **只读用户配置** ：通过用户配置文件限制 `ftp_readonly` 的写入权限。
- **测试** ：使用 FTP 客户端或命令行工具测试文件夹列举权限。
- **SELinux/AppArmor** ：如果启用，确保策略允许 FTP 读取。

完成以上步骤后， `ftp_readonly` 用户应具备文件夹列举权限，但无法写入文件。


## 要创建一个新 FTP 账号，使其具备 **除了创建文件和写入文件之外的所有权限** （包括文件夹列举、文件读取等），可以按照以下步骤操作：


### 3. 检查目录权限

确保 `/mnt/ssd/ftp` 目录的权限允许 `ftp_readonly` 读取和列举文件。

运行以下命令检查目录权限：

```bash
ls -ld /mnt/ssd/ftp
```

输出示例：

```bash
drwxr-xr-x 2 ftp_readwrite ftp_readwrite 4096 Oct 10 12:34 /mnt/ssd/ftp
```

- **权限** ：`drwxr-xr-x` （所有者有读写执行权限，其他用户只有读和执行权限）

如果权限不正确，可以使用以下命令修复：

```bash
sudo chmod 755 /mnt/ssd/ftp
```


### 4. 配置 `vsftpd`

编辑 `vsftpd` 的配置文件 `/etc/vsftpd.conf` ，确保以下配置已启用：

```bash
local_enable=YES
write_enable=YES
chroot_local_user=YES
allow_writeable_chroot=YES
```

- `local_enable=YES` ：允许本地用户登录。
- `write_enable=YES` ：允许写入（即使只读用户不需要写入权限，此选项也需要启用以支持其他功能）。
- `chroot_local_user=YES` ：将用户限制在其根目录内。
- `allow_writeable_chroot=YES` ：允许可写根目录（即使只读用户不需要写入权限，此选项也需要启用）。

保存并退出编辑器。


### 5. 配置只读用户的权限

为了确保 `ftp_readonly` 用户只能读取文件而不能写入，可以通过 `vsftpd` 的用户配置文件限制其权限。

#### 创建用户配置文件

编辑 `ftp_readonly` 的用户配置文件：

```bash
sudo nano /etc/vsftpd/user_conf/ftp_readonly
```

添加以下内容：

```bash
write_enable=NO
```

保存并退出。

#### 确保 `vsftpd` 使用用户配置文件

编辑 `/etc/vsftpd.conf` ，确保以下配置已启用：

```bash
user_config_dir=/etc/vsftpd/user_conf
```

保存并退出，然后重启 `vsftpd` 服务：

```bash
sudo systemctl restart vsftpd
```


### 6. 测试只读权限

使用 `ftp_readonly` 账户登录 FTP 服务器，测试其权限：

#### 使用 FTP 客户端

1. 使用 FTP 客户端（如 FileZilla）登录。
2. 尝试列举 `/mnt/ssd/ftp` 目录中的文件和子目录。
3. 尝试上传文件或创建目录，确认操作被拒绝。

#### 使用命令行

使用 `ftp` 命令行工具测试：

```bash
ftp localhost
```

输入用户名 `ftp_readonly` 和密码，然后尝试列举目录：

```bash
ftp> ls
```

尝试上传文件：

```bash
ftp> put testfile.txt
```

如果文件上传失败并返回 `550 Permission denied` ，说明只读权限配置正确。


### 总结

- **新用户** ：`ftp_readonly` ，可以读取和列举目录，但不能写入或创建文件。
- **目录权限** ：确保 `/mnt/ssd/ftp` 的权限为 `755` 。
- ** `vsftpd` 配置** ：通过用户配置文件限制 `ftp_readonly` 的写入权限。
- **测试** ：使用 FTP 客户端或命令行工具测试权限。
- **SELinux/AppArmor** ：如果启用，确保策略允许 FTP 读取。

完成以上步骤后， `ftp_readonly` 用户将具备除了创建文件和写入文件之外的所有权限。
```bash
sudo chown ftp_readwrite:ftp_group /mnt/ssd/ftp/
sudo chmod 755 /mnt/ssd/ftp/

sudo systemctl restart vsftpd

sudo groupadd ftp_group
sudo usermod -aG ftp_group ftp_readwrite
sudo usermod -aG ftp_group ftp_readonly
sudo usermod -aG ftp_group ftp_readonly
sudo chown -R :ftp_group /mnt/ssd/ftp
sudo chmod -R 775 /mnt/ssd/ftp
sudo chmod g+s /mnt/ssd/ftp
ls -ld /mnt/ssd/ftp
```

(base) yqh@yqh-Z790-UD:~$ ls -ld /mnt/ssd/ftp
```
drwxrwsr-x 4 ftp_readonly ftp_group 4096  2 月 19 17:14 /mnt/ssd/ftp
```

```bash
ls -ld /mnt/ssd/ftp
ls -ld /mnt/ssd/ftp/gitremote
ls -ld /mnt/ssd/ftp/_md5dir
```

在 /etc/vsftpd.conf 中，设置 local_umask 来为文件和目录设置默认权限：
```bash
sudo nano /etc/vsftpd.conf
```
确保 umask 设置合适，确保文件和目录的权限对于组成员是可读写的。
```bash
local_umask=022

sudo chmod g+s /mnt/ssd/ftp

sudo setfacl -m g:ftp_group:rwx /mnt/ssd/ftp
sudo setfacl -d -m g:ftp_group:rwx /mnt/ssd/ftp

sudo chmod -R 775 /mnt/ssd/ftp
sudo chown -R :ftp_group /mnt/ssd/ftp
```



<hr class='reviewline'/>
<p class='reviewtip'><script type='text/javascript' src='{% include relref.html url="/assets/reviewjs/blogs/2025-02-19-Ubuntu-ssd-ftp.md.js" %}'></script></p>
