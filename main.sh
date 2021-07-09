pip install -r requirements.txt
cd svelte
npm install
npm run build
cd ../battle
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn battle.wsgi --bind 0.0.0.0:3000