# Python learning

## Conda environment
```bash
# Már meglévő conda environmentek listázása
conda env list

# Új conda environment létrehozása
conda create --name playground python=3.10 -y 

# conda environmentbe belépés
conda activate playground

# Csekkold, hogy a python megfelelő helyről lesz használ
which python

# pip-tools py package telepítése hogy tudjuk compile-olni a requirements.in file-t
python -m pip install pip-tools

# Lehetséges, hogy a pip-compile binárisának a teljes elérési útját kell megadni. Ezt onnan tudod, hogy amikor beírtad a 
# which python parancsot, akkor a pip-compile binárisa is ott lesz abban a mappában ahol a python binárisa van.
# Nálam pl: 
# which python --> /Users/rolandpinter/opt/anaconda3/envs/ervin/bin/python (én a conda envem nem playgroudnak, hanem ervinnek hívtam)
# pip-compile binárisa: /Users/rolandpinter/opt/anaconda3/envs/ervin/bin/pip-compile
pip-compile requirements.in

# A requirements.in file-t a pip-compile lefordítja requirements.txt file-ba, amit aztán a pip telepít
python -m pip install -r requirements.txt

# conda environmentből kilépés
conda deactivate
```