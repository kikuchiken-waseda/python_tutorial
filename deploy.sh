set -e
cd ./build/html
git init
git add -A
git commit -m 'deploy-page'
git push -f git@github.com:kikuchiken-waseda/python_tutorial.git master:gh-pages
cd -
