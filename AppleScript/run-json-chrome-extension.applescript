tell application "Google Chrome"
    activate
    open location "chrome-extension://pkgccpejnmalmdinmhkkfafefagiiiad/json-format/index.html"
end tell

delay 0.5

tell application "System Events"
    keystroke "v" using {command down}
end tell
