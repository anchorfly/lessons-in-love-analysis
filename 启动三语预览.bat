@echo off
chcp 65001 >nul
cd /d "%~dp0"
title LIL 三语预览服务器 (8899)
set "PY=C:\Users\anke\.workbuddy\binaries\python\versions\3.13.12\python.exe"
set "URL=http://127.0.0.1:8899/guide_i18n.html"

echo ============================================
echo   LIL 三语导航本地预览
echo   根目录: %CD%
echo   地址:   %URL%
echo ============================================
echo.

if not exist "%PY%" (
  echo [错误] 找不到 Python，请检查路径：
  echo   %PY%
  echo.
  pause
  exit /b 1
)

netstat -ano | findstr ":8899 " | findstr /i LISTENING >nul
if not errorlevel 1 (
  echo 端口 8899 已在监听，服务器应该已经在跑了。
  echo 直接打开浏览器。
  echo.
  start "" "%URL%"
  pause
  exit /b 0
)

echo 正在启动服务器（先监听端口，再自动打开浏览器）...
echo 关闭本窗口即停止服务器。
echo.
"%PY%" -c "import http.server,webbrowser; s=http.server.ThreadingHTTPServer(('127.0.0.1',8899),http.server.SimpleHTTPRequestHandler); print('server ready: http://127.0.0.1:8899'); webbrowser.open('http://127.0.0.1:8899/guide_i18n.html'); s.serve_forever()"

echo.
echo 服务器已停止。
pause
