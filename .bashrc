#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --group-directories-first --file-type -N --color=auto'
alias grep='grep --color=auto'
PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '
alias groffdoc='python3 ~/Programs/My-Programs/mdToGroff.py'
alias rm='rm -i'
alias install='sudo pacman -S'
alias update='sudo pacman -Syu'
alias dgg='surf https://destiny.gg/embed/chat'
alias ms=mousepad
alias hang='journalctl --grep=HANG:'
alias reload='. ~/.bashrc'
alias lsa='ls --group-directories-first --file-type -NA --color=auto'
alias remove='sudo pacman -Rs'
alias findr='sudo find / -name'
alias log='python3 ~/Programs/My-Programs/log.py'
alias weather='curl wttr.in'
alias steamapps='cd ~/.steam/steam/steamapps/common'
HISTSIZE=20000
HISTFILESIZE=20000
alias findh='find ~ -name'
export PATH=$PATH:~/.local/bin
alias goff='python3 ~/Programs/My-Programs/emote.py'
alias goffread='cat ~/Programs/log/angery.txt'
