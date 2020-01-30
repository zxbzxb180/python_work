#coding=gbk
import requests

#ִ��API���ò��洢��Ӧ
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code)

#��API��Ӧ�洢��һ��������
response_dict = r.json()

print("Total repositories:",response_dict['total_count'])

repo_dicts = response_dict['items']

print("Repositories returned:",len(repo_dicts))

repo_dict = repo_dicts[0]
print("\nKeys:",len(repo_dict))

for key in sorted(repo_dict.key()):
	print(key)
