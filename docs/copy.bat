set TM=%TIME:~0,2%%TIME:~3,2%
mkdir E:\Developer_07\Copies\%date%_%TM%\Open_Basics
set folder=E:\Developer_07\Copies\%date%_%TM%\Open_Basics
xcopy /y /s "C:\Users\Gaming PC\Documents\GitHub\Open_Basics" %folder%