#INFO: convertir de un epub a json para NPL

html_dir= 'cuentos_completos/'

import codecs
import os
import re
import json

R= {} #U: resultado titulo -> [parrafo*]

def limpiar(s):
    notags= re.sub('<[^>]*>','',s)
    spaceok= re.sub(r'\s+',' ',notags)
    return spaceok.strip()

def procesar_un_archivo(path):
    with codecs.open(archivo.path, 'r', encoding='utf-8', errors='ignore') as f:
        html= f.read().replace('\n', '')
        m= re.search('blockquote class="calibre_6">(.*)</blockquote>(.*)<div',html)
        if m!=None: #A: es un cuento
            t_h= m.group(1) #A: el titulo
            b= m.group(2) #A: el "cuerpo"
            parrafos_h= re.findall('p[^>]*>(.*?)</p',b)
            if parrafos_h!=None and len(parrafos_h)>0:
                R[limpiar(t_h)]= list(filter(lambda x: x!='', map(limpiar,parrafos_h)))

with os.scandir(html_dir) as archivos:
    for archivo in archivos:
        if archivo.is_file():
            procesar_un_archivo(archivo.path)
            

print(json.dumps(R,indent=2, ensure_ascii=False))
