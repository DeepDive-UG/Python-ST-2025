import pandas as pd
import numpy as np
import math

# Zadanie 1: Program wybierający grę o najniższej cenie
def wybor_gry_o_najnizszej_cenie():
    # Tworzymy przykładowy DataFrame z grami i cenami (zamiast wczytywać z xlsx)
    
    df_gry = pd.read_excel('ceny_gier.xlsx')
    
    # Znajdujemy grę o najniższej cenie
    najtansza_gra = df_gry.loc[df_gry['cena'].idxmin()]
    print(f"Najtańsza gra: {najtansza_gra['gra']} za {najtansza_gra['cena']} zł")
    

if __name__ == "__main__":
    print("=== TYDZIEŃ 6 - WSTĘP DO PROGRAMOWANIA OBIEKTOWEGO ===\n")
    
    # Zadanie 1
    print("Zadanie 1: Wybór gry o najniższej cenie")
    wybor_gry_o_najnizszej_cenie()
    print()