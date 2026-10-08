# Esporta i 4 Word di riassunti in PDF (per leggerli dal telefono) in OneDrive\UNI-PDF, che si sincronizza da solo.
# Usa Word in sola lettura e invisibile: non modifica i documenti. Se Word e' aperto con altri file lo lascia stare.
# Uso: powershell -ExecutionPolicy Bypass -File esporta_pdf.ps1
$ErrorActionPreference = "Stop"
$uni  = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
$dest = Join-Path $env:USERPROFILE "OneDrive\UNI-PDF"
New-Item -ItemType Directory -Force -Path $dest | Out-Null
$docs = @{
  "Algebra lineare"     = "Riassunto Algebra lineare.docx"
  "Matematica discreta" = "Appunti matematica discreta.docx"
  "Fondamenti Info"     = "Fondamenti Informatica.docx"
  "Programmazione"      = "Riassunto Programmazione.docx"
}
$word = New-Object -ComObject Word.Application
$word.Visible = $false
$word.DisplayAlerts = 0
try {
  foreach ($m in $docs.Keys) {
    $src = Join-Path $uni (Join-Path $m $docs[$m])
    $pdf = Join-Path $dest ("$m.pdf")
    if ((Test-Path $pdf) -and ((Get-Item $pdf).LastWriteTime -ge (Get-Item $src).LastWriteTime)) { Write-Host "gia' aggiornato: $m"; continue }
    $doc = $word.Documents.Open($src, $false, $true, $false)   # ConfirmConversions=false, ReadOnly=true, AddToRecentFiles=false
    $doc.ExportAsFixedFormat($pdf, 17, $false, 0, 0, 0, 0, 0, $true)   # 17 = wdExportFormatPDF; segnalibri dai titoli
    $doc.Close($false)
    Write-Host ("PDF creato: {0} ({1:N0} KB)" -f $pdf, ((Get-Item $pdf).Length / 1KB))
  }
} finally {
  $word.Quit()
}
