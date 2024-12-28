Invoke-RestMethod -Uri "http://127.0.0.1:5000/convert" -Method Post -Form @{'file' = Get-Item -Path "test/moves.csv" }
