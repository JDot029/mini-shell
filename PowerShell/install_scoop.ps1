Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
scoop install git
scoop bucket add games
scoop bucket add java
scoop bucket add extras
scoop bucket add utils
scoop bucket add versions
exit