#!/usr/bin/env sh
# AUTHOR: gotbletu (@gmail|twitter|youtube|github|lbry)
#         https://www.youtube.com/user/gotbletu
# DESC:   generate a script for your last w3m session then you can run script to restore all urls in new tabs
# DEMO:   https://youtu.be/qYhNJ3itqWw
# DEPEND: coreutils sed gawk
# CLOG:   2021-04-17 first draft, no option to jump to tab 1 at the moment
# REQD:   1. Allow executable permissions and put script in ~/.w3m/cgi-bin/restore_session.cgi 
#
#         2. Add binding to ~/.w3m/keymap
#               keymap  Q       COMMAND     "EXTERN 'echo %s > ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; NEXT_TAB ; EXTERN 'echo %s >> ~/.w3m/RestoreSession.txt' ; READ_SHELL ~/.w3m/cgi-bin/restore_session.cgi ; ABORT"
#
#         3. Add to ~/.bashrc or ~/.zshrc $PATH variable
#               [ -d "$HOME/.w3m/bin" ] && PATH="$HOME/.w3m/bin:$PATH"
#
#         4. To load w3m with the last session
#               $ w3mlastsession

## ---------------------------------------------
mkdir -p "$HOME/.w3m/bin"
# location of generated script of last session
RESTORE_SESSSION="$HOME/.w3m/bin/w3mlastsession"
# add shell header
echo "#!/usr/bin/env sh" > "$RESTORE_SESSSION"
echo "w3m \\" >> "$RESTORE_SESSSION"
# remove dupes without sorting, add -N flag at beginning and append trailing slash to each url
awk '!x[$0]++' "$HOME/.w3m/RestoreSession.txt" | while read -r line ; do echo "-N '"$line"' \\" >> "$RESTORE_SESSSION" ; done
# delete last trailing slash at the last line
sed -i '$ s-.$--' "$RESTORE_SESSSION"
chmod +x "$RESTORE_SESSSION"

## OUTPUT SCRIPT FILE EXAMPLE ~/.w3m/bin/w3mlastsession
## --------------------------------------------------
##  #!/usr/bin/env sh
##  w3m \
##  -N 'https://www.reddit.com/r/w3m/.mobile' \
##  -N 'https://www.reddit.com/r/commandline/.mobile' \
##  -N 'https://www.reddit.com/r/linux/.mobile' \
##  -N 'http://lite.cnn.com/en' \
##  -N 'https://raw.githubusercontent.com/tats/w3m/master/ChangeLog' \
##  -N 'https://github.com/gotbletu/shownotes' 
## --------------------------------------------------
