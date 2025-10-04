/**
 * 英语音标播放器 - 防内存泄露版本
 * 支持多版本音频文件自动切换播放
 */

class PhoneticPlayer {
    constructor(config = {}) {
        // 配置参数
        this.config = {
            playCount: config.playCount || 4,           // 播放次数
            playInterval: config.playInterval || 300,   // 播放间隔(ms)
            toastDuration: config.toastDuration || 2000, // 提示显示时长(ms)
            maxConcurrentAudio: config.maxConcurrentAudio || 5, // 最大并发音频数
            ...config
        };

        // 播放完成回调
        this.onPlayComplete = null;

        // 播放状态
        this.currentAudio = null;  // 当前播放的音频对象
        this.isPlaying = false;
        this.playTimeouts = [];    // 存储所有setTimeout ID

        // 音频对象池 - 防止创建过多Audio对象
        this.audioPool = new Map();
        this.audioPoolSize = 0;

        // 音标到数字ID的映射表
        this.phoneticToId = {
            'iː': '001', 'ɜː': '002', 'ɑː': '003', 'ɔː': '004', 'uː': '005',
            'ɪ': '006', 'e': '007', 'æ': '008', 'ə': '009', 'ʌ': '010',
            'ɒ': '011', 'ʊ': '012', 'eɪ': '013', 'aɪ': '014', 'ɔɪ': '015',
            'əʊ': '016', 'aʊ': '017', 'ɪə': '018', 'eə': '019', 'ʊə': '020',
            'p': '021', 't': '022', 'k': '023', 'f': '024', 'θ': '025',
            's': '026', '∫': '027', 'ʃ': '051', 'h': '028', 't∫': '029', 'tʃ': '050', 'ts': '030',
            'tr': '031', 'b': '032', 'd': '033', 'g': '034', 'v': '035',
            'ð': '036', 'z': '037', 'ʒ': '038', 'r': '039', 'dʒ': '040',
            'dz': '041', 'dr': '042', 'm': '043', 'n': '044', 'ŋ': '045',
            'l': '046', 'j': '047', 'w': '048', 'ks': '049'
        };

        // 初始化
        this.init();
    }

    /**
     * 初始化播放器
     */
    init() {
        // 绑定音标卡片点击事件
        this.bindCardEvents();

        // 添加移动端触摸反馈
        this.addTouchFeedback();

        // 页面卸载时清理资源
        window.addEventListener('beforeunload', () => {
            this.cleanup();
        });
    }

    /**
     * 清理所有资源 - 防止内存泄露
     */
    cleanup() {
        // 停止当前播放
        this.stopAllAudio();

        // 清理所有定时器
        this.playTimeouts.forEach(timeoutId => {
            clearTimeout(timeoutId);
        });
        this.playTimeouts = [];

        // 清理音频对象池
        this.audioPool.forEach(audio => {
            if (audio) {
                audio.pause();
                audio.src = '';
                audio.load(); // 释放资源
            }
        });
        this.audioPool.clear();
        this.audioPoolSize = 0;
    }

    /**
     * 获取或创建音频对象
     */
    getAudioObject(url) {
        // 如果池中已有该URL的音频对象，复用它
        if (this.audioPool.has(url)) {
            const audio = this.audioPool.get(url);
            audio.currentTime = 0; // 重置播放位置
            return audio;
        }

        // 控制音频对象池大小，防止内存泄露
        if (this.audioPoolSize >= this.config.maxConcurrentAudio) {
            // 清理最旧的音频对象
            const firstKey = this.audioPool.keys().next().value;
            const oldAudio = this.audioPool.get(firstKey);
            if (oldAudio) {
                oldAudio.pause();
                oldAudio.src = '';
                oldAudio.load();
            }
            this.audioPool.delete(firstKey);
            this.audioPoolSize--;
        }

        // 创建新的音频对象
        const audio = new Audio();
        audio.preload = 'none'; // 不预加载，节省内存
        audio.src = url;

        // 添加错误处理
        audio.addEventListener('error', (e) => {
            console.warn(`音频加载失败: ${url}`, e);
        });

        this.audioPool.set(url, audio);
        this.audioPoolSize++;

        return audio;
    }

    /**
     * 绑定音标卡片点击事件
     */
    bindCardEvents() {
        document.addEventListener('DOMContentLoaded', () => {
            const cards = document.querySelectorAll('.phonetic-card');

            cards.forEach(card => {
                card.addEventListener('click', (e) => {
                    const sound = card.getAttribute('data-sound');
                    const symbol = card.querySelector('.phonetic-symbol')?.textContent || sound;

                    this.playPhonetic(sound, symbol);

                    // 添加点击动画效果
                    this.addClickAnimation(card);
                });
            });
        });
    }

    /**
     * 添加点击动画效果
     */
    addClickAnimation(element) {
        element.style.transform = 'scale(0.95)';
        const timeoutId = setTimeout(() => {
            element.style.transform = '';
        }, 150);
        this.playTimeouts.push(timeoutId);
    }

    /**
     * 添加移动端触摸反馈
     */
    addTouchFeedback() {
        if ('ontouchstart' in window) {
            document.addEventListener('DOMContentLoaded', () => {
                document.querySelectorAll('.phonetic-card').forEach(card => {
                    card.addEventListener('touchstart', function() {
                        this.style.backgroundColor = 'rgba(102, 126, 234, 0.1)';
                    });

                    card.addEventListener('touchend', function() {
                        const timeoutId = setTimeout(() => {
                            this.style.backgroundColor = '';
                        }, 200);
                        // 注意：这里不添加到playTimeouts，因为是UI效果，不是播放相关
                    });
                });
            });
        }
    }

    /**
     * 停止所有正在播放的音频
     */
    stopAllAudio() {
        // 停止当前音频
        if (this.currentAudio && !this.currentAudio.paused) {
            this.currentAudio.pause();
            this.currentAudio.currentTime = 0;
        }
        this.currentAudio = null;
        this.isPlaying = false;

        // 清理所有播放相关的定时器
        this.playTimeouts.forEach(timeoutId => {
            clearTimeout(timeoutId);
        });
        this.playTimeouts = [];

        // 清理回调
        this.onPlayComplete = null;
    }

    /**
     * 根据数字ID获取音频序列
     */
    getAudioSequence(numericId) {
        const sequences = [];

        // 按优先级添加可用的音频文件
        const folders = [
            { name: 'yp', ext: '.mp3' },
            { name: 'xdf', ext: '.mp3' },
            //{ name: 'tingclass', ext: '.mp3' },
            { name: 'mp3', ext: '.mp3' }
        ];

        folders.forEach(folder => {
            sequences.push(`./${folder.name}/${numericId}${folder.ext}`);
        });

        return sequences;
    }

    /**
     * 播放音标发音
     */
    playPhonetic(soundFile, symbol, onComplete = null) {
        try {
            // 强制停止之前的播放
            this.stopAllAudio();

            // 设置播放状态
            this.isPlaying = true;
            this.onPlayComplete = onComplete;

            // 获取数字ID
            const numericId = this.phoneticToId[soundFile];
            if (!numericId) {
                console.error(`未找到音标 ${soundFile} 的数字ID映射`);
                this.showToast(`❌ 未找到映射: ${symbol}`);
                this.isPlaying = false;
                if (onComplete) onComplete();
                return;
            }

            // 获取音频序列
            const audioSequence = this.getAudioSequence(numericId);

            if (audioSequence.length === 0) {
                console.error(`未找到音标 ${soundFile} 的音频文件`);
                this.showToast(`❌ 未找到音频: ${symbol}`);
                this.isPlaying = false;
                if (onComplete) onComplete();
                return;
            }

            this.showToast(`🔊 ${symbol} (播放${this.config.playCount}遍)`);
            this.playAudioSequence(audioSequence, 0, symbol);

        } catch (error) {
            console.log('音频加载失败:', error);
            this.showToast(`❌ 音频加载失败: ${symbol}`);
            this.isPlaying = false;
            if (onComplete) onComplete();
        }
    }

    /**
     * 顺序播放音频序列 - 防内存泄露版本
     */
    playAudioSequence(audioFiles, index, symbol) {
        // 检查是否被中断
        if (!this.isPlaying) {
            return;
        }

        if (index >= audioFiles.length) {
            this.showToast(`✅ ${symbol} 播放完成 (共${this.config.playCount}遍)`);
            this.isPlaying = false;
            this.currentAudio = null;

            // 调用完成回调
            if (this.onPlayComplete) {
                this.onPlayComplete();
                this.onPlayComplete = null;
            }
            return;
        }

        const audioUrl = audioFiles[index];
        const audio = this.getAudioObject(audioUrl);
        this.currentAudio = audio;

        // 设置事件监听器 - 使用一次性监听器防止重复绑定
        const onEnded = () => {
            audio.removeEventListener('ended', onEnded);
            audio.removeEventListener('error', onError);

            if (this.isPlaying) {
                const timeoutId = setTimeout(() => {
                    this.playAudioSequence(audioFiles, index + 1, symbol);
                }, this.config.playInterval);
                this.playTimeouts.push(timeoutId);
            }
        };

        const onError = () => {
            audio.removeEventListener('ended', onEnded);
            audio.removeEventListener('error', onError);

            console.log(`音频文件不存在: ${audioUrl}`);

            if (this.isPlaying) {
                const timeoutId = setTimeout(() => {
                    this.playAudioSequence(audioFiles, index + 1, symbol);
                }, this.config.playInterval);
                this.playTimeouts.push(timeoutId);
            }
        };

        audio.addEventListener('ended', onEnded, { once: true });
        audio.addEventListener('error', onError, { once: true });

        // 播放音频
        audio.play().then(() => {
            console.log(`播放第${index + 1}遍: ${audioUrl}`);
        }).catch(error => {
            console.log(`音频播放失败 (第${index + 1}遍):`, error);
            // 如果播放失败，触发错误处理
            onError();
        });
    }

    /**
     * 显示提示消息
     */
    showToast(message) {
        // 移除现有的 toast
        const existingToast = document.querySelector('.toast');
        if (existingToast) {
            existingToast.remove();
        }

        // 创建新的 toast
        const toast = document.createElement('div');
        toast.className = 'toast';
        toast.textContent = message;
        document.body.appendChild(toast);

        // 显示 toast
        const showTimeoutId = setTimeout(() => {
            toast.classList.add('show');
        }, 100);
        this.playTimeouts.push(showTimeoutId);

        // 自动隐藏 toast
        const hideTimeoutId = setTimeout(() => {
            toast.classList.remove('show');
            const removeTimeoutId = setTimeout(() => {
                if (toast.parentNode) {
                    toast.parentNode.removeChild(toast);
                }
            }, 300);
            this.playTimeouts.push(removeTimeoutId);
        }, this.config.toastDuration);
        this.playTimeouts.push(hideTimeoutId);
    }

    /**
     * 自动学习模式 - 顺序播放所有音标
     */
    startAutoLearn(phoneticList, options = {}) {
        const config = {
            interval: options.interval || 3000,  // 音标间隔时间
            repeat: options.repeat || 1,         // 每个音标重复次数
            onProgress: options.onProgress || null,  // 进度回调
            onComplete: options.onComplete || null   // 完成回调
        };

        let currentIndex = 0;

        const playNext = () => {
            if (currentIndex >= phoneticList.length) {
                if (config.onComplete) {
                    config.onComplete();
                }
                return;
            }

            const phonetic = phoneticList[currentIndex];

            if (config.onProgress) {
                config.onProgress(currentIndex, phonetic, phoneticList.length);
            }

            this.playPhonetic(phonetic.sound, phonetic.symbol);

            currentIndex++;
            const timeoutId = setTimeout(playNext, config.interval);
            this.playTimeouts.push(timeoutId);
        };

        playNext();
    }

    /**
     * 更新音标映射
     */
    updatePhoneticMapping(newMapping) {
        this.phoneticToId = { ...this.phoneticToId, ...newMapping };
    }
}

// 全局实例
window.phoneticPlayer = new PhoneticPlayer();

// 兼容性函数 - 保持向后兼容
window.playSound = function(soundFile, symbol, onComplete) {
    window.phoneticPlayer.playPhonetic(soundFile, symbol, onComplete);
};

window.stopAllAudio = function() {
    window.phoneticPlayer.stopAllAudio();
};

window.showToast = function(message) {
    window.phoneticPlayer.showToast(message);
};
