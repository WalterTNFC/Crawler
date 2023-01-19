from pymongo import MongoClient
import requests
from parsel import Selector

# Entrando manualmente com o nome da empresa
company_name = "vivodigital"
company_page = f"https://{company_name}.gupy.io/"

# Requisição do tipo GET
response = requests.get(company_page)
selector = Selector(text=response.text)

# Criando seletor de vagas
select_job = selector.css("li.sc-7dc8e42e-2 div.sc-7dc8e42e-4::text").getall()

# Inicializando a conexão com o mongo:
client = MongoClient()
db = client.crawlerProcessos

# Interando na lista de vagas abertas
for i in range(len(select_job)-1):
    job = {
        "title": select_job[i],
    }
    job_id = db.processos.insert_one(job).inserted_id
    print(job_id)

client.close()