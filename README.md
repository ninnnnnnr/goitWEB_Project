# goitWEB_Project
WEB project on course GoIT

for start app:
  cd personal_assistance
  docker-compose up -d
  docker-compose exec web python manage.py makemigrations --noinput
  docker-compose exec web python manage.py migrate --noinput
  
  in web browser http://127.0.0.1:8000/