param (
    [String]$filePath
)

if ($filePath)
{
    Write-Host "filePath: $filePath"
    C:\Users\Administrator\Downloads\upx-5.0.1-win64\upx-5.0.1-win64\upx.exe --best --lzma $filePath
}