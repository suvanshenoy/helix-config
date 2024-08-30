# rm -rvf .git
git init
git add .
git branch -m main
git commit -m "[create:add|create|impl] create helix config"
git remote add origin git@github.com:suvanshenoy/helix-config
# git remote set-url origin $2
# git remote get-url origin
git push -u origin -f main
# rm -rvf .git
