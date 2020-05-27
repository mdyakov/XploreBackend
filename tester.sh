username="testScript"
password="testScript1234"
username2="testScript2"
gameName="portal"
gameID=4200
gameURL="https://media.rawg.io/media/games/328/3283617cb7d75d67257fc58339188742.jpg"


http post https://xplore-backend-staging.herokuapp.com/users/ username=$username password=$password
echo
http post https://xplore-backend-staging.herokuapp.com/users/login/ username=$username password=$password
echo
# read

http get https://xplore-backend-staging.herokuapp.com/users/$username/favorites/ 
echo
http get https://xplore-backend-staging.herokuapp.com/users/$username/wishlist/ 
echo

read -p 'Token: ' token
echo $token

http post https://xplore-backend-staging.herokuapp.com/users/$username/wishlist/ id=$gameID name=$gameName poster_url=$gameURL "Authorization: Token ${token}"
echo 
http get https://xplore-backend-staging.herokuapp.com/users/$username/wishlist/ "Authorization: Token ${token}"
echo
http delete https://xplore-backend-staging.herokuapp.com/users/$username/wishlist/ id=$gameID "Authorization: Token ${token}"
echo
read

http post https://xplore-backend-staging.herokuapp.com/users/$username/favorites/ id=$gameID name=$gameName poster_url=$gameURL "Authorization: Token ${token}"
echo
http get https://xplore-backend-staging.herokuapp.com/users/$username/favorites/ "Authorization: Token ${token}"
echo
http delete https://xplore-backend-staging.herokuapp.com/users/$username/favorites/ id=$gameID "Authorization: Token ${token}"
echo

# read

http post https://xplore-backend-staging.herokuapp.com/users/$username/friends/ username=admin "Authorization: Token ${token}"
echo
http get https://xplore-backend-staging.herokuapp.com/users/$username/friends/ "Authorization: Token ${token}"
echo
http delete https://xplore-backend-staging.herokuapp.com/users/$username/friends/ username=admin "Authorization: Token ${token}"
echo
http post https://xplore-backend-staging.herokuapp.com/users/ username=$username2 password=$password
echo 
http post https://xplore-backend-staging.herokuapp.com/users/$username/friends/ username=$username2 "Authorization: Token ${token}"
echo
http get https://xplore-backend-staging.herokuapp.com/users/$username2/wishlist/ "Authorization: Token ${token}"
echo



read



rm testResult