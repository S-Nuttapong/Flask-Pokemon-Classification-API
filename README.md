# Flask-Pokemon-Classification-API
API endpoint for Pokémon's image classification

![GIF](/pokenet_model/assets/poke_illustration.gif)

## Project setup

### Creating Virtualenv
Create a python virtual environment with venv, name it as you wish, for example ```Pokemon_Backend``` Replace the path /PATH/TO to your desired virtualenv accordingly, for example ```virpython``` .
```
pip3 install virtualenv

mkdir virpython <<<< </PATH/TO>

cd <PATH/TO/virpython

virtualenv -p python3.7 Pokemon_Backend <<<<<<<< <VENV NAME>
```
#### Activate Virtual environment
```
source <PATH/TO/virpython/Pokemon_Backend/bin/activate>
```

### Installing all dependency for the project. Run the following command:
```
cd </PATH/TO/WORK_DIR>

# From WORK_DIR/
pip install -r requirements.txt
``` 

## Running and Testing API

### Starting endpoint for service
```
# From WORK_DIR/
python predict_app.py
```
### Frontend
For frontend, kindly head to  https://s-nuttapong.github.io/Pokemon-webapp/


In addition, you can test API directly from this Github page https://s-nuttapong.github.io/Pokemon-webapp/Pokemon-webapp.html
