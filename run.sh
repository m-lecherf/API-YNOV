heroku container:login

heroku create api-ynov-mathis

# Création de l'image docker
docker build . -t api-ynov-mathis

docker tag api-ynov-mathis registry.heroku.com/api-ynov-mathis/web


docker push registry.heroku.com/api-ynov-mathis/web

heroku container:release web -a api-ynov-mathis

heroku open
# Start un container    
# docker run -p 5000:8000 -e PORT=5000 -v "$(pwd):/home/app" -it api-ynov-mathis