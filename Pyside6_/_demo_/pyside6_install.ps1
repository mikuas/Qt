param (
    [string]$pyFile,
    [string]$fileName = "demo",
    [string]$iconPath,
    [string]$outputDir = "/bin",
    [string]$images
)

if ($images) {
    nuitka `
        --standalone `
        --enable-plugin=pyside6 `
        --assume-yes-for-downloads `
        --windows-console-mode=disable `
        --output-dir=$outputDir `
        --remove-output `
        --nofollow-import-to="tkinter,turtle,test,unittest" `
        --windows-icon-from-ico=$iconPath `
        --lto=yes `
        --jobs=8 `
        --output-filename=$fileName `
        --include-data-dir=images=$images `
        $pyFile
}
else {
    nuitka `
        --standalone `
        --enable-plugin=pyside6 `
        --assume-yes-for-downloads `
        --windows-console-mode=disable `
        --output-dir=$outputDir `
        --remove-output `
        --nofollow-import-to="tkinter,turtle,test,unittest" `
        --windows-icon-from-ico=$iconPath `
        --lto=yes `
        --jobs=8 `
        --output-filename=$fileName `
        $pyFile
}