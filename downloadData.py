import urllib
url = 'http://dados.prefeitura.sp.gov.br/dataset/32cced28-ba1c-4037-ad5d-5e861a1ec1a2/resource/cdf768ea-1319-4085-91bc-181fc2362f1c/download/politicadistribuicaodividendos.pdf'
fileobj = urllib.urlopen(url)
a= open(r'C:\..\Informacoes.pdf', 'wb')
a.write(fileobj.read())
a.close()
