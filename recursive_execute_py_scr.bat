cd "C:\\Sourcecode"
for /r %%i in (*.c) do (
	python C:\Sourcecode\lineread_delete_ifdef.py "%%i"
	del %%i
)

for /r %%i in (*.h) do (
	python C:\Sourcecode\lineread_delete_ifdef.py "%%i"
	del %%i
)

for /r /d %%i in (*) do (
	cd %%i
	ren *.ctemp *.c
	ren *.htemp *.h
)
