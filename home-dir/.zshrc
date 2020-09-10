echo "
 ██████╗ █████╗ ██████╗ ████████╗ █████╗ ███╗   ███╗██████╗ ██████╗ ██╗ ██████╗ █████╗
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗████╗ ████║╚════██╗██╔══██╗██║██╔════╝██╔══██╗
██║     ███████║██████╔╝   ██║   ███████║██╔████╔██║ █████╔╝██████╔╝██║██║     ███████║
██║     ██╔══██║██╔═══╝    ██║   ██╔══██║██║╚██╔╝██║ ╚═══██╗██╔══██╗██║██║     ██╔══██║
╚██████╗██║  ██║██║        ██║   ██║  ██║██║ ╚═╝ ██║██████╔╝██║  ██║██║╚██████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝        ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═
"

echo ""
echo "Be strong and of great courage,
be not afraid or dismayed for the Lord
your God is wich you wherever you go.
 - Joshua 1:9"

echo ""
date
uptime
echo ""
who
echo ""

alias ls='ls -G  -F'
alias ll='ls -la'
alias grep='grep --color'
alias bitwarden='bw'
alias gitgoing='git add * && git commit -m "Updates added" && git push'
alias gotoicloud='cd /Users/captam3rica/Library/Mobile\ Documents/com~apple~CloudDocs'

export PROMPT='%m%#: '
export EDITOR="/usr/bin/vim"
export HISTFILESIZE=10
export HISTSIZE=10
export HISTCONTROL=$HISTCONTROL${HISTCONTROL+,}ignoredups
export HISTIGNORE='&:clear:ls:cd:[bf]g:exit:[ t\]*'
export EMACS="*term*"

bindkey -e

autoload -U compinit && compinit

# pyenv stuff
if command -v pyenv 1>/dev/null 2>&1; then
	eval "$(pyenv init -)"
fi

# pyenv-virtualenv
eval "$(pyenv virtualenv-init -)"
