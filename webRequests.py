from ntpath import join
import requests
from parsel import Selector
import csv

# Entrando manualmente com o nome da empresa
company_name = "vivodigital"
company_page = f"https://{company_name}.gupy.io/"
# Requisição do tipo GET
response = requests.get(company_page)
selector = Selector(text=response.text)

print(selector.css("li.sc-7dc8e42e-2 div.sc-7dc8e42e-4::text").get())
# Para imprimir todas as tags referentes as vagas abertas
# for job in selector.css("li.sc-7dc8e42e-2 ").getall():
#     print(job)

# Para imprimir todos os processos de uma página:
select_job = selector.css("li.sc-7dc8e42e-2 div.sc-7dc8e42e-4::text").getall()
# print(select_job)
# file = open('example.csv', 'w+', newline ='')
# with file:
#     write =csv.writer(file)
#     write.writerows(join(str(select_job)))
for job in select_job:
    print(job)
    with open('example.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(','.join(job))
# Para navegar até um processo
# job_page = selector.css("li.sc-7dc8e42e-2 a::attr(href)").get()
# job_page_link = f"{company_page}{job_page}"
# print(job_page_link)
# select_requirement = selector.css("div.sc-aa0b7872-1")
# select_requirement = selector.get(job_page_link)
# print(select_requirement)
# job_page_request = requests.get(f"https://vivo.gupy.io/{job_page}")
# print(job_page_request)
# job_page_selector(text=job_page_request)
# print(Selector)