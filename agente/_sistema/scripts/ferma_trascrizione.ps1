# Ferma le trascrizioni in corso (script di coda e processo Whisper), senza fermare se stesso.
# Uso: powershell -NoProfile -File ferma_trascrizione.ps1
Get-CimInstance Win32_Process |
  Where-Object { $_.ProcessId -ne $PID -and $_.CommandLine -and ($_.CommandLine -match 'catena\.sh' -or $_.CommandLine -match 'trascrivi\.py') } |
  ForEach-Object { Write-Host ("fermo PID {0}" -f $_.ProcessId); Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue }
