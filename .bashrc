#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls -G  -F'
alias grep='grep --color'
alias bitwarden='bw'

export EDITOR="/usr/bin/vim"
export HISTFILESIZE=10
export HISTSIZE=10

PS1='[\u@\h \W]\$ '

# >>> BEGIN ADDED BY CNCHI INSTALLER
# <<< END ADDED BY CNCHI INSTALLER

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
