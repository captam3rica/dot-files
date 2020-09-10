[ -n "$PYENV_DEBUG" ] && set -x
export PYENV_ROOT="/Users/captam3rica/.pyenv"
program="$("/usr/local/Cellar/pyenv/1.2.16/libexec/pyenv" which "${BASH_SOURCE##*/}")"
if [ -e "${program}" ]; then
  . "${program}" "$@"
fi
