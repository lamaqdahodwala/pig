pip install -r requirements.txt
cd svelte
npm install 
cd ../battle
gunicorn battle.wsgi --bind 0.0.0.0:3000