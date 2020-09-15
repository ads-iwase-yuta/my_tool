@echo off
echo STEP1/3: make files
pyinstaller ../main.py --onefile --noconsole --icon=../resources/logo.ico -n SSI
echo STEP2/3: replace spec file
python replace_spec.py
echo STEP3/3: build
pyinstaller SSI.spec