#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '

alias grep='grep --color=auto'
alias ls='ls --group-directories-first --file-type -N --color=auto'
alias lsa='ls --group-directories-first --file-type -NA --color=auto'
alias rm='rm -i'
alias reload='. ~/.bashrc'
alias findh='find ~ -name'
alias findr='sudo find / -name'
alias install='sudo pacman -S'
alias update='sudo pacman -Syu'
alias remove='sudo pacman -Rs'

alias steamapps='cd ~/.steam/steam/steamapps/common'
alias sshe='ssh esg2@esg2.host.cs.st-andrews.ac.uk'
alias hang='journalctl --grep=HANG:'

alias ms=mousepad
alias weather='curl wttr.in'
alias groffdoc='python3 ~/Programs/myPrograms/mdToGroff.py'
alias dgg='surf https://destiny.gg/embed/chat'
alias nerdcubed='mpv https://www.twitch.tv/nerdcubed'
alias yt-dgg='yt-dlp youtube.com/@destiny/live'
alias log='python3 ~/Programs/myPrograms/log.py'
alias inting='python3 ~/Programs/myPrograms/emote.py'
alias pastinting='cat ~/Programs/log/angery.txt'

HISTSIZE=20000
HISTFILESIZE=20000

export PATH=$PATH:~/.local/bin




