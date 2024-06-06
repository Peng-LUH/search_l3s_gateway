# import psycopg2
# import os
# from dotenv import load_dotenv
# load_dotenv()


# host= os.getenv("POSTGRES_HOST")
# user=os.getenv("postgres")
# password= os.getenv("admin")
# database= os.getenv("SearchDB")
# port = os.getenv("POSTGRES_PORT")


# def is_database_connected():
#     try:
#         connection = psycopg2.connect(
#             host= host,
#             user= user,
#             password= password,
#             database=database,
#             port = port
#         )
#         connection.close()
#         return True
#     except Exception as e:
#         return False

# # Example usage
# if is_database_connected():
#     print("Database is connected")
# else:
#     print("Database connection failed")

# import json
# from src.l3s_gateway_api.util import mls_api
# r = mls_api.MLSConnection().get_task_by_id(task_id='111')
# print(r.status_code)
# # print(f'Status Code: {r[]}')

list = [(0, 1), (0, 2), (3, 1)]

for l in list:
    if not l[0] == 0:
        list.remove(l)
        
print(list)