# python_learning
```bash
conda env list # conda kornyezetek listazasa

# conda environment letrehozasa
conda create --name playground python=3.10 -y 

# conda environmentbe belepes - beaktivalas
conda activate playground

pip install pip-tools
pip-compile requirements.in

pip install -r requirements.txt
#pip install numpy pandas matplotlib scikit-learn jupyter ipywidgets ipykernel

conda deactivate
```