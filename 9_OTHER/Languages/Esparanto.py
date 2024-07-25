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

# Agordo de protokolado
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
            os.makedirs(elira_dosierujo, exist_ok=True)
            nova_dosierindiko = os.path.join(elira_dosierujo, f"{os.path.basename(dosierindiko)[:-3]}_eo.py")
        else:
            nova_dosierindiko = f"{os.path.splitext(dosierindiko)[0]}_eo{os.path.splitext(dosierindiko)[1]}"

        with open(nova_dosierindiko, 'w', encoding='utf-8') as dosiero:
            dosiero.write(tradukita_enhavo)

        logger.info(f"Dosiero sukcese tradukita kaj konservita: {nova_dosierindiko}")
        return dosierindiko, nova_dosierindiko
    except Exception as e:
        logger.error(f"Eraro dum tradukado de dosiero {dosierindiko}: {str(e)}")
        return dosierindiko, None

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
    python_dosieroj = []
    for dosierindiko, dosierujoj, dosieroj in os.walk(radika_dosierujo):
        for dosiero in dosieroj:
            if dosiero.endswith('.py'):
                python_dosieroj.append(os.path.join(dosierindiko, dosiero))

    rezultoj = {}
    with concurrent.futures.ProcessPoolExecutor(max_workers=maksimumaj_laboristoj) as plenumanto:
        estonteco_al_dosiero = {plenumanto.submit(traduki_dosieron, dosierindiko, elira_dosierujo): dosierindiko for dosierindiko in python_dosieroj}
        
        with tqdm(total=len(python_dosieroj), desc="Tradukado de dosieroj") as pbar:
            for estonteco in concurrent.futures.as_completed(estonteco_al_dosiero):
                dosierindiko = estonteco_al_dosiero[estonteco]
                try:
                    originala, tradukita = estonteco.result()
                    rezultoj[originala] = tradukita
                except Exception as e:
                    logger.error(f"Eraro dum traktado de dosiero {dosierindiko}: {str(e)}")
                    rezultoj[dosierindiko] = None
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
    if vorto.endswith(('o', 'a')):
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
        tempo (str): La dezirата tempo ('as' por prezenco, 'is' por preterito, 'os' por futuro).
    
    Returns:
        str: La konjugaciita verbo.
    """
    if verbo.endswith('i'):
        radiko = verbo[:-1]
        return radiko + tempo
    return verbo

def main():
    parser = argparse.ArgumentParser(description="Tradukado de komentoj en Python-kodo al Esperanto.")
    parser.add_argument("radika_dosierujo", help="Radika dosierujo de la kodbazaro")
    parser.add_argument("--eliro", help="Dosierujo por konservi la tradukitajn dosierojn")
    parser.add_argument("--maksimumaj-laboristoj", type=int, default=5, help="Maksimuma nombro da paralelaj procezoj")
    args = parser.parse_args()

    komenco_tempo = time.time()
    rezultoj = traduki_kodbazaron(args.radika_dosierujo, args.eliro, args.maksimumaj_laboristoj)
    fino_tempo = time.time()

    sukcesaj_tradukoj = sum(1 for tradukita in rezultoj.values() if tradukita is not None)
    logger.info(f"Tradukado de la kodbazaro al Esperanto finiĝis.")
    logger.info(f"Sukcese tradukitaj dosieroj: {sukcesaj_tradukoj}/{len(rezultoj)}")
    logger.info(f"Plenumtempo: {fino_tempo - komenco_tempo:.2f} sekundoj")

if __name__ == "__main__":
    main()
