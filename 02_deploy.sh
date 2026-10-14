#!/usr/bin/env bash
# VIM PRACTICE 2: Shell script
# Exercises:
#  1. Rename variable "srv" to "server" everywhere: :%s/\<srv\>/server/g
#  2. Go to line 40 with 40G, then back to the top with gg
#  3. Use % on each { and ( to jump to its match
#  4. Change the word "staging" to "production" on one line with ciw
#  5. Use A to append "  # needs sudo" to the systemctl line
#  6. Use O to add a blank line + comment above the rsync line
#  7. Delete the whole log_info function with d} or V}d
#  8. Indent the body of the for loop with >} or visual mode and >
#  9. Undo with u, redo with Ctrl-r
# 10. Record a macro: qa I# <Esc> j q  then 4@a to comment four lines

set -euo pipefail

srv="staging.example.com"
user="deploy"
app_dir="/var/www/myapp"
release="$(date +%Y%m%d%H%M%S)"

log_info() {
echo "[INFO] $(date '+%H:%M:%S') $*"
}

log_error() {
echo "[ERROR] $(date '+%H:%M:%S') $*" >&2
}

check_host() {
if ping -c 1 "$srv" > /dev/null 2>&1; then
log_info "Host $srv is reachable"
else
log_error "Host $srv is unreachable"
exit 1
fi
}

check_host

log_info "Syncing files to $srv"
rsync -az --delete ./build/ "$user@$srv:$app_dir/releases/$release/"

for service in web worker scheduler queue; do
log_info "Restarting $service"
ssh "$user@$srv" systemctl restart "myapp-$service"
sleep 2
done

log_info "Linking current release"
ssh "$user@$srv" ln -sfn "$app_dir/releases/$release" "$app_dir/current"
log_info "Deploy finished"
