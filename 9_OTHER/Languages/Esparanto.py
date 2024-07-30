import os
import re
import requests
from typing import Dict, List, Any, Optional, Tuple
from googletrans import Translator
from tqdm import tqdm
import argparse
import logging
import concurrent.futures
import time
import json
from pathlib import Path
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk

# Agordo de protokolado
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ensure NLTK resources are downloaded
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

# Initialize Esperanto stopwords (if available)
try:
    esperanto_stopwords = set(stopwords.words('esperanto'))
except:
    esperanto_stopwords = set()

def traduki_al_esperanto(teksto: str, provoj: int = 3, prokrasto: float = 1.0) -> Optional[str]:
    """
    Tradukas tekston al Esperanto uzante la bibliotekon googletrans.
    
    Args:
        teksto (str): Origina teksto por traduki.
        provoj (int): Nombro da provoj por traduki kaze de eraro.
        prokrasto (float): Prokrasto inter provoj en sekundoj.
    
    Returns:
        Optional[str]: Tradukita teksto aŭ None kaze de eraro.
    """
    tradukisto = Translator()
    for provo in range(provoj):
        try:
            return tradukisto.translate(teksto, dest='eo').text
        except Exception as e:
            logger.warning(f"Eraro dum tradukado (provo {provo + 1}/{provoj}): {str(e)}")
            if provo < provoj - 1:
                time.sleep(prokrasto)
            else:
                logger.error(f"Ne eblis traduki la tekston post {provoj} provoj.")
                return None

def traduki_komentojn(kodo: str) -> str:
    """
    Tradukas komentojn en kodo al Esperanto.
    
    Args:
        kodo (str): Origina kodo kun komentoj.
    
    Returns:
        str: Kodo kun tradukitaj komentoj.
    """
    def traduki_komenton(kongruo):
        komento = kongruo.group(0)
        tradukita = traduki_al_esperanto(komento[1:].strip())
        return f"# {tradukita}" if tradukita else komento

    # Traduki unuliniajn komentojn
    kodo = re.sub(r'#.*', traduki_komenton, kodo)

    # Traduki plurliniajn komentojn
    def traduki_plurlinian_komenton(kongruo):
        komento = kongruo.group(1)
        tradukita = traduki_al_esperanto(komento)
        return f'"""{tradukita}"""' if tradukita else kongruo.group(0)

    kodo = re.sub(r'"""([\s\S]*?)"""', traduki_plurlinian_komenton, kodo)

    return kodo

def traduki_dosieron(dosierindiko: str, elira_dosierujo: Optional[str] = None) -> Tuple[str, Optional[str]]:
    """
    Tradukas la enhavon de dosiero al Esperanto.
    
    Args:
        dosierindiko (str): Indiko al la origina dosiero.
        elira_dosierujo (Optional[str]): Dosierujo por konservi la tradukitan dosieron.
    
    Returns:
        Tuple[str, Optional[str]]: Paro de la origina dosierindiko kaj la tradukita dosierindiko (aŭ None kaze de eraro).
    """
    try:
        with open(dosierindiko, 'r', encoding='utf-8') as dosiero:
            enhavo = dosiero.read()

        tradukita_enhavo = traduki_komentojn(enhavo)

        # Krei novan dosieron kun tradukita enhavo
        if elira_dosierujo:
            elira_dosierujo = Path(elira_dosierujo)
            elira_dosierujo.mkdir(parents=True, exist_ok=True)
            nova_dosierindiko = elira_dosierujo / f"{Path(dosierindiko).stem}_eo.py"
        else:
            nova_dosierindiko = Path(dosierindiko).with_stem(f"{Path(dosierindiko).stem}_eo")

        with open(nova_dosierindiko, 'w', encoding='utf-8') as dosiero:
            dosiero.write(tradukita_enhavo)

        logger.info(f"Dosiero sukcese tradukita kaj konservita: {nova_dosierindiko}")
        return str(dosierindiko), str(nova_dosierindiko)
    except Exception as e:
        logger.error(f"Eraro dum tradukado de dosiero {dosierindiko}: {str(e)}")
        return str(dosierindiko), None

def traduki_kodbazaron(radika_dosierujo: str, elira_dosierujo: Optional[str] = None, maksimumaj_laboristoj: int = 5) -> Dict[str, Optional[str]]:
    """
    Tradukas ĉiujn Python-dosierojn en la specifita dosierujo kaj ĝiaj subdosierujoj.
    
    Args:
        radika_dosierujo (str): Radika dosierujo de la kodbazaro.
        elira_dosierujo (Optional[str]): Dosierujo por konservi la tradukitajn dosierojn.
        maksimumaj_laboristoj (int): Maksimuma nombro da paralelaj procezoj.
    
    Returns:
        Dict[str, Optional[str]]: Vortaro kun indikoj al originalaj dosieroj kaj respondaj tradukitaj dosieroj.
    """
    radika_dosierujo = Path(radika_dosierujo)
    python_dosieroj = list(radika_dosierujo.rglob('*.py'))

    rezultoj = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=maksimumaj_laboristoj) as plenumanto:
        estonteco_al_dosiero = {plenumanto.submit(traduki_dosieron, str(dosierindiko), elira_dosierujo): dosierindiko for dosierindiko in python_dosieroj}
        
        with tqdm(total=len(python_dosieroj), desc="Tradukado de dosieroj") as pbar:
            for estonteco in concurrent.futures.as_completed(estonteco_al_dosiero):
                dosierindiko = estonteco_al_dosiero[estonteco]
                try:
                    originala, tradukita = estonteco.result()
                    rezultoj[originala] = tradukita
                except Exception as e:
                    logger.error(f"Eraro dum traktado de dosiero {dosierindiko}: {str(e)}")
                    rezultoj[str(dosierindiko)] = None
                pbar.update(1)

    return rezultoj

def apliki_akuzativon(vorto: str) -> str:
    """
    Aldonas la akuzativan finaĵon '-n' al substantivo aŭ adjektivo.
    
    Args:
        vorto (str): La vorto por transformi.
    
    Returns:
        str: La vorto kun la akuzativa finaĵo.
    """
    if vorto.endswith(('o', 'a', 'oj', 'aj')):
        return vorto + 'n'
    return vorto

def krei_pluralon(vorto: str) -> str:
    """
    Kreas la pluralon de substantivo aŭ adjektivo.
    
    Args:
        vorto (str): La vorto por transformi.
    
    Returns:
        str: La plurala formo de la vorto.
    """
    if vorto.endswith('o'):
        return vorto[:-1] + 'oj'
    elif vorto.endswith('a'):
        return vorto[:-1] + 'aj'
    return vorto

def konjugacii_verbon(verbo: str, tempo: str) -> str:
    """
    Konjugacias verbon laŭ la specifita tempo.
    
    Args:
        verbo (str): La verbo en la infinitiva formo.
        tempo (str): La dezirата tempo ('as' por prezenco, 'is' por preterito, 'os' por futuro, 'us' por kondicionalo, 'u' por volitivo).
    
    Returns:
        str: La konjugaciita verbo.
    """
    if verbo.endswith('i'):
        radiko = verbo[:-1]
        return radiko + tempo
    return verbo

def konservi_rezultojn(rezultoj: Dict[str, Optional[str]], elira_dosiero: str):
    """
    Konservas la rezultojn de la tradukado en JSON-dosiero.
    
    Args:
        rezultoj (Dict[str, Optional[str]]): Vortaro kun indikoj al originalaj dosieroj kaj respondaj tradukitaj dosieroj.
        elira_dosiero (str): Dosierindiko por konservi la rezultojn.
    """
    with open(elira_dosiero, 'w', encoding='utf-8') as dosiero:
        json.dump(rezultoj, dosiero, ensure_ascii=False, indent=2)
    logger.info(f"Rezultoj konservitaj en: {elira_dosiero}")

def analizi_tekston(teksto: str) -> Dict[str, Any]:
    """
    Analizas la donitan tekston kaj provizas bazajn statistikojn.
    
    Args:
        teksto (str): La teksto por analizi.
    
    Returns:
        Dict[str, Any]: Vortaro kun bazaj statistikoj pri la teksto.
    """
    vortoj = word_tokenize(teksto.lower())
    signifaj_vortoj = [vorto for vorto in vortoj if vorto not in esperanto_stopwords]
    
    return {
        "nombro_da_vortoj": len(vortoj),
        "nombro_da_signifaj_vortoj": len(signifaj_vortoj),
        "unikaj_vortoj": len(set(vortoj)),
        "plej_oftaj_vortoj": Counter(signifaj_vortoj).most_common(10)
    }

def main():
    parser = argparse.ArgumentParser(description="Tradukado de komentoj en Python-kodo al Esperanto.")
    parser.add_argument("radika_dosierujo", help="Radika dosierujo de la kodbazaro")
    parser.add_argument("--eliro", help="Dosierujo por konservi la tradukitajn dosierojn")
    parser.add_argument("--maksimumaj-laboristoj", type=int, default=5, help="Maksimuma nombro da paralelaj procezoj")
    parser.add_argument("--rezultoj-dosiero", default="traduko_rezultoj.json", help="Dosiero por konservi la rezultojn de la tradukado")
    args = parser.parse_args()

    komenco_tempo = time.time()
    rezultoj = traduki_kodbazaron(args.radika_dosierujo, args.eliro, args.maksimumaj_laboristoj)
    fino_tempo = time.time()

    sukcesaj_tradukoj = sum(1 for tradukita in rezultoj.values() if tradukita is not None)
    logger.info(f"Tradukado de la kodbazaro al Esperanto finiĝis.")
    logger.info(f"Sukcese tradukitaj dosieroj: {sukcesaj_tradukoj}/{len(rezultoj)}")
    logger.info(f"Plenumtempo: {fino_tempo - komenco_tempo:.2f} sekundoj")

    konservi_rezultojn(rezultoj, args.rezultoj_dosiero)

if __name__ == "__main__":
    main()
