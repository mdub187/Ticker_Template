import config, manage
import server.__init__
import client.__init__
import myproject
# parent_dir = "./"
# from config import API_KEY
# credentials = {
#     "firstName": "marc",
#     "lastName": "dub",
#     "email": "maweeks.91@gmail.com",
#     "API_KEY": "2f2d48ebac0ff1195cb9b3ec9cc16293",  # type: ignore
#     "x-rapidapi-pair_key": "2f2d48ebac0ff1195cb9b3ec9cc16293",
#     "x-apisports-key": "2f2d48ebac0ff1195cb9b3ec9cc16293",
#     "x-rapidapi-host": "2f2d48ebac0ff1195cb9b3ec9cc16293",
#}
if __name__ == 'server' or __name__ == 'client':
    print(client.__init__.__name__)
    print(server.__init__.__name__)
elif __name__ == '__main__':
    print(myproject, manage, config)