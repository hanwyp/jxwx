@echo off

if "%1" == "h" goto begin

mshtavbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit

:begin

REM

start python logMain.py
