name=$(pwd | rev | cut -d '/' -f 2 | rev)

git add -A;
git commit -m $1;
echo "code-Cells"
echo $gitkey
git push origin main
pip3 install -e git+https://github.com/code-Cells/$name@$2

