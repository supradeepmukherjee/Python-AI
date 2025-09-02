import threading,requests,time

def download(url):
    print('Starting download from ',url)
    res=requests.get(url)
    print(f'Finished downloading file of size {len(res.content)}bytes')

urls=[
    'https://httpbin.org/image/jpeg',
    'https://httpbin.org/image/png',
    'https://httpbin.org/image/svg',
]

start=time.time()
threads=[]

for url in urls:
    t=threading.Thread(target=download,args=(url,))
    t.start()
    threads.append(t)

for thread in threads:thread.join()

end=time.time()
print(f'{start},{end},{end-start:.2f}sec')