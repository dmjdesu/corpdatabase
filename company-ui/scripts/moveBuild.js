const shell = require('shelljs');
const path = require('path');

// ビルドディレクトリと移動先ディレクトリのパスを取得
const buildDir = path.join(__dirname, '../build');
const staticDir = path.join(buildDir, 'static');
const targetDir = path.join(__dirname, '../../staticfiles');

// 既に移動先ディレクトリが存在する場合は削除
if (shell.test('-e', targetDir)) {
  shell.rm('-rf', targetDir);
}

// staticディレクトリを移動先ディレクトリにコピー
shell.cp('-R', staticDir, targetDir);

console.log(`Static files moved to ${targetDir}`);
