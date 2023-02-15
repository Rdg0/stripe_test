### stripe_test

Создаем платежные формы с помощью Django и Stripe.  

Стек:  
Django 3.2
stripe 5.0




### Запуск проекта с помощью docker
В директории stripe_test/shop/shop создайте файл .env и внесите все необходимые переменные окружения:

STRIPE_PUBLIC_KEY - публичный ключ stripe  
STRIPE_SECRET_KEY - секретный ключ stripe  
DOMAIN - адрес вашего домена  

Запуск проекта производится из директории stripe_test командой:  
docker-compose up -d --build  

Затем необходимо произвести подготовку данных проекта, выполнив следующие команды:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --no-input
docker-compose exec web python manage.py createsuperuser

Далее через панель администратора добавить необходимые товары.


Опубликован тут:  
http://194.87.210.36/



