git config --global user.email "private_email"
git rebase -i
git commit --amend --reset-author
git rebase --continue
git push
