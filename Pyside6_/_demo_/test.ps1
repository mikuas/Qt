param (
    [string]$arg1,
    [string]$arg2,
    [array]$array
)

Write-Host "arg1: $arg1, arg2: $arg2, switch: $bool"

Write-Host "array"

if ($arg1) {
    Write-Host true
}

for ($i = 0; $i -lt $array.Count; $i++) {
    Write-Host $array[$i]
    <# Action that will repeat until the condition is met #>
}