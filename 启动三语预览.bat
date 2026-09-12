@echo off
chcp 65001 >nul
cd /d "%~dp0"
title LIL 三语预览服务器 (8899)
echo ============================================
echo   LIL 三语导航本地预览
echo   根目录: %CD%
echo   端口:   8899
echo ============================================
echo.
echo 正在启动服务器并打开浏览器...
echo (关闭本窗口即停止服务器)
echo.
start "" "http://127.0.0.1:8899/guide_i18n.html"
"C:\Users\anke\.workbuddy\binaries\python\versions\3.13.12\python.exe" -m http.server 8899 --bind 127.0.0.1
pause
