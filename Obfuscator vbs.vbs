Option Explicit

Function vbs_obfuscator(n)
	Dim r, k
	r = Round(Rnd() * 10000) + 1
	k = Round(Rnd() * 2) + 1
	Select Case k
		Case 0
			vbs_obfuscator = "CLng(&H" & Hex(r + n) & ")-" & r
		Case 1
			vbs_obfuscator = (n - r) & "+CLng(&H" & Hex(r) & ")"
		Case Else
			vbs_obfuscator = (n * r) & "/CLng(&H" & Hex(r) & ")"
	End Select
End Function

Function Obfuscator(vbs)
	Dim length, s, i
	length = Len(vbs)
	s = ""
	For i = 1 To length
		s = s & "chr(" & vbs_obfuscator(Asc(Mid(vbs, i))) + ")&"
	Next
	s = s & "vbCrlf"
	Obfuscator = "Execute " & s
End Function

' If WScript.Arguments.Count = 0 Then
' 	WScript.Echo "Missing parameter(s): VBScript source file(s)"
' 	WScript.Quit
' End If 

Dim fso, i
Const ForReading = 1
Dim MyFile
Dim a

Set fso = CreateObject("Scripting.FileSystemObject")
Set MyFile = fso.OpenTextFile("./ini.vbs", ForReading)
Dim vbs
vbs = MyFile.ReadAll
set a = CreateObject("Scripting.FileSystemObject").CreateTextFile("./a.txt")
a.write Obfuscator(vbs)
a.Close
WScript.Echo Obfuscator(vbs)
' MyFile.Close

' For i = 0 To WScript.Arguments.Count - 1
' 	Dim FileName
' 	FileName = WScript.Arguments(i)
' 	Dim MyFile
' 	Set MyFile = fso.OpenTextFile(FileName, ForReading)
' 	Dim vbs
' 	vbs = MyFile.ReadAll
' 	WScript.Echo Obfuscator(vbs)
' 	MyFile.Close
' Next

Set fso = Nothing













' ////////////////////////////////Defuscator 
' Option Explicit

' Function Defuscator(vbs)
'     Dim t
'     t = InStr(1, vbs, "Execute", 1)
'     t = Mid(vbs, t + Len("Execute")) 
'     t = Eval(t)
'     Defuscator = t
' End Function

' Dim fso, i
' Const ForReading = 1
' Set fso = CreateObject("Scripting.FileSystemObject")
' For i = 0 To WScript.Arguments.Count - 1
'     Dim FileName
'     FileName = WScript.Arguments(i)
'     Dim MyFile
'     Set MyFile = fso.OpenTextFile(FileName, ForReading)
'     Dim vbs
'     vbs = MyFile.ReadAll    
'     WScript.Echo Defuscator(vbs)
'     MyFile.Close
' Next
' Set fso = Nothing