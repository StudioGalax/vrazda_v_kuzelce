# mapa.py
# Databáze místností a lokací pro hru Vražda v Kuželce

MISTNOSTI = {
    "vchod": {
        "nazev": "Vchod / Výčep",
        "popis": "Hlavní vchod do hospody Kuželka.",
        "sousedni": ["chodba"],
        "obrazek": "obrazky/vchod.png"
    },
    "chodba": {
        "nazev": "Chodba",
        "popis": "Spojovací chodba. Odtud vede cesta k výčepu, na záchody nebo do restaurace.",
        "sousedni": ["vchod", "pisoary", "retaurace"],
        "obrazek": "obrazky/chodba.png"
    },
    "pisoary": {
        "nazev": "Pisoary",
        "popis": "Pánské záchody.",
        "sousedni": ["chodba", "wc_kabinka"],
        "obrazek": "obrazky/pisoary.png"
    },
    "wc_kabinka": {
        "nazev": "Kabinka WC",
        "popis": "Zavřená kabinka, kde se dají najít stopy.",
        "sousedni": ["pisoary"],
        "obrazek": "obrazky/wc_kabinka.png"
    },
    "retaurace": {
        "nazev": "Hlavní restaurace",
        "popis": "Hlavní sál plný štamgastů. Můžeš odtud k baru nebo prozkoumat stoly.",
        "sousedni": ["chodba", "bar"],
        "obrazek": "obrazky/retaurace.png",
        "stoly": {
            "jena": {
                "nazev": "Stůl s Jeňou",
                "popis": "Jeňa u notebooku a vyřezané srdíčko na stole.",
                "obrazek": "obrazky/detail_stolu_jena.png"
            },
            "drsoni": {
                "nazev": "Stůl štamgastů (Drsňáci)",
                "popis": "Drsná parta u piva a podezřelého sáčku.",
                "obrazek": "obrazky/detail_stolu_drsoni.png"
            },
            "cns": {
                "nazev": "Stůl Člověče, nezlob se",
                "popis": "Hráči u deskovky a zápisníku.",
                "obrazek": "obrazky/detail_stolu_CnS.png"
            }
        }
    },
    "bar": {
        "nazev": "Barový pult",
        "popis": "Výčep. Odtud se dá pokračovat dál do skladu.",
        "sousedni": ["retaurace", "sklad"],
        "obrazek": "obrazky/bar.png"
    },
    "sklad": {
        "nazev": "Sklad",
        "popis": "Sklad sudů. Odtud vede cesta do zadní chodby.",
        "sousedni": ["bar", "zadni_chodba_leva"],
        "obrazek": "obrazky/sklad.png"
    },
    "zadni_chodba_leva": {
        "nazev": "Zadní chodba (levá část)",
        "popis": "Chodba v zázemí.",
        "sousedni": ["sklad", "zadni_chodba_prava"],
        "obrazek": "obrazky/zadni_chodba_leva.png"
    },
    "zadni_chodba_prava": {
        "nazev": "Zadní chodba (pravá část)",
        "popis": "Pokračování chodby k zadnímu východu.",
        "sousedni": ["zadni_chodba_leva", "zadni_vchod"],
        "obrazek": "obrazky/zadni_chodba_prava.png"
    },
    "zadni_vchod": {
        "nazev": "Zadní vchod",
        "popis": "Východ ven do tmy.",
        "sousedni": ["zadni_chodba_prava", "zatceni"],
        "obrazek": "obrazky/zadni_vchod.png"
    },
    "zatceni": {
        "nazev": "Zatčení",
        "popis": "Finále případu.",
        "sousedni": [],
        "obrazek": "obrazky/zatceni.png"
    }
}
