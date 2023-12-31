import app.get_files as get_files
import app.empresa as empresa
import app.estabelecimentos as estabelecimentos
import app.socios as socios
import app.simples as simples
import app.cnae as cnae
import app.moti as moti
import app.munic as munic
import app.natju as natju
import app.pais as pais
import app.quals as quals

from app.utils import initialize

def run():
    initialize()

    get_files.run()
    empresa.run()
    estabelecimentos.run()
    socios.run()
    simples.run()
    cnae.run()
    moti.run()
    munic.run()
    natju.run()
    pais.run()
    quals.run()

    print("""Processo 100% finalizado! Você já pode usar seus dados no BD!
        - Desenvolvido por: JunioDBL
        - Contribua com esse projeto aqui: https://github.com/xpto
    """)

if __name__ == "__main__":
    run()