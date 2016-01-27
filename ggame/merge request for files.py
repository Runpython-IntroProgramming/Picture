git remote add -f ggame https://github.com/BrythonServer/ggame.git
git merge -s ours --no-commit ggame/minimal
mkdir ggame
git read-tree --prefix=ggame/ -u ggame/minimal
git commit -m "Merge ggame project as our subdirectory"
