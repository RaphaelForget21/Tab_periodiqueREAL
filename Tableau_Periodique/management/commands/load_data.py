# Tableau_Periodique/management/commands/load_data.py
from django.core.management.base import BaseCommand
from Tab_periodiqueREAL.Tableau_Periodique.models import models  # Replace with your actual model name
from decimal import Decimal

class Command(BaseCommand):
    help = 'Load data into the database'

    def handle(self, *args, **kwargs):
        data = [
            {
                "numero": 1,
                "symbole": "H",
                "nom": "Hydrogène",
                "masse": "1,008",
                "categorie": "hydrogene",
                "position": {"row": 1, "col": 1}
            },
            {
                "numero": 2,
                "symbole": "He",
                "nom": "Hélium",
                "masse": "4,0026",
                "categorie": "gazNoble",
                "position": {"row": 1, "col": 18}
            },
            {
                "numero": 3,
                "symbole": "Li",
                "nom": "Lithium",
                "masse": "6,94",
                "categorie": "alcalin",
                "position": {"row": 2, "col": 1}
            },
            {
                "numero": 4,
                "symbole": "Be",
                "nom": "Béryllium",
                "masse": "9,0122",
                "categorie": "alcalino",
                "position": {"row": 2, "col": 2}
            },
            {
                "numero": 5,
                "symbole": "B",
                "nom": "Bore",
                "masse": "10,81",
                "categorie": "metalloide",
                "position": {"row": 2, "col": 13}
            },
            {
                "numero": 6,
                "symbole": "C",
                "nom": "Carbone",
                "masse": "12,011",
                "categorie": "nonMetal",
                "position": {"row": 2, "col": 14}
            },
            {
                "numero": 7,
                "symbole": "N",
                "nom": "Azote",
                "masse": "14,007",
                "categorie": "nonMetal",
                "position": {"row": 2, "col": 15}
            },
            {
                "numero": 8,
                "symbole": "O",
                "nom": "Oxygène",
                "masse": "15,999",
                "categorie": "nonMetal",
                "position": {"row": 2, "col": 16}
            },
            {
                "numero": 9,
                "symbole": "F",
                "nom": "Fluor",
                "masse": "18,998",
                "categorie": "nonMetal",
                "position": {"row": 2, "col": 17}
            },
            {
                "numero": 10,
                "symbole": "Ne",
                "nom": "Néon",
                "masse": "20,180",
                "categorie": "gazNoble",
                "position": {"row": 2, "col": 18}
            },
            {
                "numero": 11,
                "symbole": "Na",
                "nom": "Sodium",
                "masse": "22,990",
                "categorie": "alcalin",
                "position": {"row": 3, "col": 1}
            },
            {
                "numero": 12,
                "symbole": "Mg",
                "nom": "Magnésium",
                "masse": "24,305",
                "categorie": "alcalino",
                "position": {"row": 3, "col": 2}
            },
            {
                "numero": 13,
                "symbole": "Al",
                "nom": "Aluminium",
                "masse": "26,982",
                "categorie": "metalPauvre",
                "position": {"row": 3, "col": 13}
            },
            {
                "numero": 14,
                "symbole": "Si",
                "nom": "Silicium",
                "masse": "28,085",
                "categorie": "metalloide",
                "position": {"row": 3, "col": 14}
            },
            {
                "numero": 15,
                "symbole": "P",
                "nom": "Phosphore",
                "masse": "30,974",
                "categorie": "nonMetal",
                "position": {"row": 3, "col": 15}
            },
            {
                "numero": 16,
                "symbole": "S",
                "nom": "Soufre",
                "masse": "32,06",
                "categorie": "nonMetal",
                "position": {"row": 3, "col": 16}
            },
            {
                "numero": 17,
                "symbole": "Cl",
                "nom": "Chlore",
                "masse": "35,45",
                "categorie": "nonMetal",
                "position": {"row": 3, "col": 17}
            },
            {
                "numero": 18,
                "symbole": "Ar",
                "nom": "Argon",
                "masse": "39,948",
                "categorie": "gazNoble",
                "position": {"row": 3, "col": 18}
            },
            {
                "numero": 19,
                "symbole": "K",
                "nom": "Potassium",
                "masse": "39,098",
                "categorie": "alcalin",
                "position": {"row": 4, "col": 1}
            },
            {
                "numero": 20,
                "symbole": "Ca",
                "nom": "Calcium",
                "masse": "40,078",
                "categorie": "alcalino",
                "position": {"row": 4, "col": 2}
            },
            {
                "numero": 21,
                "symbole": "Sc",
                "nom": "Scandium",
                "masse": "44,956",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 3}
            },
            {
                "numero": 22,
                "symbole": "Ti",
                "nom": "Titane",
                "masse": "47,867",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 4}
            },
            {
                "numero": 23,
                "symbole": "V",
                "nom": "Vanadium",
                "masse": "50,942",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 5}
            },
            {
                "numero": 24,
                "symbole": "Cr",
                "nom": "Chrome",
                "masse": "52,00",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 6}
            },
            {
                "numero": 25,
                "symbole": "Mn",
                "nom": "Manganèse",
                "masse": "54,938",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 7}
            },
            {
                "numero": 26,
                "symbole": "Fe",
                "nom": "Fer",
                "masse": "55,845",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 8}
            },
            {
                "numero": 27,
                "symbole": "Co",
                "nom": "Cobalt",
                "masse": "58,933",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 9}
            },
            {
                "numero": 28,
                "symbole": "Ni",
                "nom": "Nickel",
                "masse": "58,693",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 10}
            },
            {
                "numero": 29,
                "symbole": "Cu",
                "nom": "Cuivre",
                "masse": "63,546",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 11}
            },
            {
                "numero": 30,
                "symbole": "Zn",
                "nom": "Zinc",
                "masse": "65,38",
                "categorie": "metalTransition",
                "position": {"row": 4, "col": 12}
            },
            {
                "numero": 31,
                "symbole": "Ga",
                "nom": "Gallium",
                "masse": "69,723",
                "categorie": "metalPauvre",
                "position": {"row": 4, "col": 13}
            },
            {
                "numero": 32,
                "symbole": "Ge",
                "nom": "Germanium",
                "masse": "72,63",
                "categorie": "metalloide",
                "position": {"row": 4, "col": 14}
            },
            {
                "numero": 33,
                "symbole": "As",
                "nom": "Arsenic",
                "masse": "74,922",
                "categorie": "metalloide",
                "position": {"row": 4, "col": 15}
            },
            {
                "numero": 34,
                "symbole": "Se",
                "nom": "Sélénium",
                "masse": "78,971",
                "categorie": "nonMetal",
                "position": {"row": 4, "col": 16}
            },
            {
                "numero": 35,
                "symbole": "Br",
                "nom": "Brome",
                "masse": "79,904",
                "categorie": "nonMetal",
                "position": {"row": 4, "col": 17}
            },
            {
                "numero": 36,
                "symbole": "Kr",
                "nom": "Krypton",
                "masse": "83,798",
                "categorie": "gazNoble",
                "position": {"row": 4, "col": 18}
            },
            {
                "numero": 37,
                "symbole": "Rb",
                "nom": "Rubidium",
                "masse": "85,468",
                "categorie": "alcalin",
                "position": {"row": 5, "col": 1}
            },
            {
                "numero": 38,
                "symbole": "Sr",
                "nom": "Strontium",
                "masse": "87,62",
                "categorie": "alcalino",
                "position": {"row": 5, "col": 2}
            },
            {
                "numero": 39,
                "symbole": "Y",
                "nom": "Yttrium",
                "masse": "88,906",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 3}
            },
            {
                "numero": 40,
                "symbole": "Zr",
                "nom": "Zirconium",
                "masse": "91,224",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 4}
            },
            {
                "numero": 41,
                "symbole": "Nb",
                "nom": "Niobium",
                "masse": "92,906",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 5}
            },
            {
                "numero": 42,
                "symbole": "Mo",
                "nom": "Molybdène",
                "masse": "95,95",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 6}
            },
            {
                "numero": 43,
                "symbole": "Tc",
                "nom": "Technétium",
                "masse": "98,00",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 7}
            },
            {
                "numero": 44,
                "symbole": "Ru",
                "nom": "Ruthénium",
                "masse": "101,07",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 8}
            },
            {
                "numero": 45,
                "symbole": "Rh",
                "nom": "Rhodium",
                "masse": "102,91",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 9}
            },
            {
                "numero": 46,
                "symbole": "Pd",
                "nom": "Palladium",
                "masse": "106,42",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 10}
            },
            {
                "numero": 47,
                "symbole": "Ag",
                "nom": "Argent",
                "masse": "107,87",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 11}
            },
            {
                "numero": 48,
                "symbole": "Cd",
                "nom": "Cadmium",
                "masse": "112,41",
                "categorie": "metalTransition",
                "position": {"row": 5, "col": 12}
            },
            {
                "numero": 49,
                "symbole": "In",
                "nom": "Indium",
                "masse": "114,82",
                "categorie": "metalPauvre",
                "position": {"row": 5, "col": 13}
            },
            {
                "numero": 50,
                "symbole": "Sn",
                "nom": "Étain",
                "masse": "118,71",
                "categorie": "metalPauvre",
                "position": {"row": 5, "col": 14}
            },
            {
                "numero": 51,
                "symbole": "Sb",
                "nom": "Antimoine",
                "masse": "121,76",
                "categorie": "metalloide",
                "position": {"row": 5, "col": 15}
            },
            {
                "numero": 52,
                "symbole": "Te",
                "nom": "Tellure",
                "masse": "127,60",
                "categorie": "metalloide",
                "position": {"row": 5, "col": 16}
            },
            {
                "numero": 53,
                "symbole": "I",
                "nom": "Iode",
                "masse": "126,90",
                "categorie": "nonMetal",
                "position": {"row": 5, "col": 17}
            },
            {
                "numero": 54,
                "symbole": "Xe",
                "nom": "Xénon",
                "masse": "131,29",
                "categorie": "gazNoble",
                "position": {"row": 5, "col": 18}
            },
            {
                "numero": 55,
                "symbole": "Cs",
                "nom": "Césium",
                "masse": "132,91",
                "categorie": "alcalin",
                "position": {"row": 6, "col": 1}
            },
            {
                "numero": 56,
                "symbole": "Ba",
                "nom": "Baryum",
                "masse": "137,33",
                "categorie": "alcalino",
                "position": {"row": 6, "col": 2}
            },
            {
                "numero": 57,
                "symbole": "La",
                "nom": "Lanthane",
                "masse": "138,91",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 3}
            },
            {
                "numero": 58,
                "symbole": "Ce",
                "nom": "Cérium",
                "masse": "140,12",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 4}
            },
            {
                "numero": 59,
                "symbole": "Pr",
                "nom": "Praséodyme",
                "masse": "140,91",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 5}
            },
            {
                "numero": 60,
                "symbole": "Nd",
                "nom": "Néodyme",
                "masse": "144,24",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 6}
            },
            {
                "numero": 61,
                "symbole": "Pm",
                "nom": "Prométhium",
                "masse": "(145)",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 7}
            },
            {
                "numero": 62,
                "symbole": "Sm",
                "nom": "Samarium",
                "masse": "150,36",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 8}
            },
            {
                "numero": 63,
                "symbole": "Eu",
                "nom": "Europium",
                "masse": "151,96",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 9}
            },
            {
                "numero": 64,
                "symbole": "Gd",
                "nom": "Gadolinium",
                "masse": "157,25",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 10}
            },
            {
                "numero": 65,
                "symbole": "Tb",
                "nom": "Terbium",
                "masse": "158,93",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 11}
            },
            {
                "numero": 66,
                "symbole": "Dy",
                "nom": "Dysprosium",
                "masse": "162,50",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 12}
            },
            {
                "numero": 67,
                "symbole": "Ho",
                "nom": "Holmium",
                "masse": "164,93",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 13}
            },
            {
                "numero": 68,
                "symbole": "Er",
                "nom": "Erbium",
                "masse": "167,26",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 14}
            },
            {
                "numero": 69,
                "symbole": "Tm",
                "nom": "Thulium",
                "masse": "168,93",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 15}
            },
            {
                "numero": 70,
                "symbole": "Yb",
                "nom": "Ytterbium",
                "masse": "173,04",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 16}
            },
            {
                "numero": 71,
                "symbole": "Lu",
                "nom": "Lutécium",
                "masse": "174,97",
                "categorie": "lanthanide",
                "position": {"row": 9, "col": 17}
            },
            {
                "numero": 72,
                "symbole": "Hf",
                "nom": "Hafnium",
                "masse": "178,49",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 4}
            },
            {
                "numero": 73,
                "symbole": "Ta",
                "nom": "Tantale",
                "masse": "180,95",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 5}
            },
            {
                "numero": 74,
                "symbole": "W",
                "nom": "Tungstène",
                "masse": "183,84",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 6}
            },
            {
                "numero": 75,
                "symbole": "Re",
                "nom": "Rhénium",
                "masse": "186,21",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 7}
            },
            {
                "numero": 76,
                "symbole": "Os",
                "nom": "Osmium",
                "masse": "190,23",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 8}
            },
            {
                "numero": 77,
                "symbole": "Ir",
                "nom": "Iridium",
                "masse": "192,22",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 9}
            },
            {
                "numero": 78,
                "symbole": "Pt",
                "nom": "Platine",
                "masse": "195,08",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 10}
            },
            {
                "numero": 79,
                "symbole": "Au",
                "nom": "Or",
                "masse": "196,97",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 11}
            },
            {
                "numero": 80,
                "symbole": "Hg",
                "nom": "Mercure",
                "masse": "200,59",
                "categorie": "metalTransition",
                "position": {"row": 6, "col": 12}
            },
            {
                "numero": 81,
                "symbole": "Tl",
                "nom": "Thallium",
                "masse": "204,38",
                "categorie": "metalPauvre",
                "position": {"row": 6, "col": 13}
            },
            {
                "numero": 82,
                "symbole": "Pb",
                "nom": "Plomb",
                "masse": "207,2",
                "categorie": "metalPauvre",
                "position": {"row": 6, "col": 14}
            },
            {
                "numero": 83,
                "symbole": "Bi",
                "nom": "Bismuth",
                "masse": "208,98",
                "categorie": "metalPauvre",
                "position": {"row": 6, "col": 15}
            },
            {
                "numero": 84,
                "symbole": "Po",
                "nom": "Polonium",
                "masse": "(209)",
                "categorie": "metalPauvre",
                "position": {"row": 6, "col": 16}
            },
            {
                "numero": 85,
                "symbole": "At",
                "nom": "Astate",
                "masse": "(210)",
                "categorie": "metalloide",
                "position": {"row": 6, "col": 17}
            },
            {
                "numero": 86,
                "symbole": "Rn",
                "nom": "Radon",
                "masse": "(222)",
                "categorie": "gazNoble",
                "position": {"row": 6, "col": 18}
            },
            {
                "numero": 87,
                "symbole": "Fr",
                "nom": "Francium",
                "masse": "(223)",
                "categorie": "alcalin",
                "position": {"row": 7, "col": 1}
            },
            {
                "numero": 88,
                "symbole": "Ra",
                "nom": "Radium",
                "masse": "(226)",
                "categorie": "alcalino",
                "position": {"row": 7, "col": 2}
            },
            {
                "numero": 89,
                "symbole": "Ac",
                "nom": "Actinium",
                "masse": "(227)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 3}
            },
            {
                "numero": 90,
                "symbole": "Th",
                "nom": "Thorium",
                "masse": "232,04",
                "categorie": "actinides",
                "position": {"row": 10, "col": 4}
            },
            {
                "numero": 91,
                "symbole": "Pa",
                "nom": "Protactinium",
                "masse": "231,04",
                "categorie": "actinides",
                "position": {"row": 10, "col": 5}
            },
            {
                "numero": 92,
                "symbole": "U",
                "nom": "Uranium",
                "masse": "238,03",
                "categorie": "actinides",
                "position": {"row": 10, "col": 6}
            },
            {
                "numero": 93,
                "symbole": "Np",
                "nom": "Neptunium",
                "masse": "(237)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 7}
            },
            {
                "numero": 94,
                "symbole": "Pu",
                "nom": "Plutonium",
                "masse": "(244)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 8}
            },
            {
                "numero": 95,
                "symbole": "Am",
                "nom": "Américium",
                "masse": "(243)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 9}
            },
            {
                "numero": 96,
                "symbole": "Cm",
                "nom": "Curium",
                "masse": "(247)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 10}
            },
            {
                "numero": 97,
                "symbole": "Bk",
                "nom": "Berkélium",
                "masse": "(247)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 11}
            },
            {
                "numero": 98,
                "symbole": "Cf",
                "nom": "Californium",
                "masse": "(251)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 12}
            },
            {
                "numero": 99,
                "symbole": "Es",
                "nom": "Einsteinium",
                "masse": "(252)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 13}
            },
            {
                "numero": 100,
                "symbole": "Fm",
                "nom": "Fermium",
                "masse": "(257)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 14}
            },
            {
                "numero": 101,
                "symbole": "Md",
                "nom": "Mendelevium",
                "masse": "(258)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 15}
            },
            {
                "numero": 102,
                "symbole": "No",
                "nom": "Nobélium",
                "masse": "(259)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 16}
            },
            {
                "numero": 103,
                "symbole": "Lr",
                "nom": "Lawrencium",
                "masse": "(262)",
                "categorie": "actinides",
                "position": {"row": 10, "col": 17}
            },
            {
                "numero": 104,
                "symbole": "Rf",
                "nom": "Rutherfordium",
                "masse": "(267)",
                "categorie": "metalTransition",
                "position": {"row": 7, "col": 4}
            },
            {
                "numero": 105,
                "symbole": "Db",
                "nom": "Dubnium",
                "masse": "(270)",
                "categorie": "metalTransition",
                "position": {"row": 7, "col": 5}
            },
            {
                "numero": 106,
                "symbole": "Sg",
                "nom": "Seaborgium",
                "masse": "(271)",
                "categorie": "metalTransition",
                "position": {"row": 7, "col": 6}
            },
            {
                "numero": 107,
                "symbole": "Bh",
                "nom": "Bohrium",
                "masse": "(270)",
                "categorie": "metalTransition",
                "position": {"row": 7, "col": 7}
            },
            {
                "numero": 108,
                "symbole": "Hs",
                "nom": "Hassium",
                "masse": "(277)",
                "categorie": "metalTransition",
                "position": {"row": 7, "col": 8}
            },
            {
                "numero": 109,
                "symbole": "Mt",
                "nom": "Meitnérium",
                "masse": "(278)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 9}
            },
            {
                "numero": 110,
                "symbole": "Ds",
                "nom": "Darmstadtium",
                "masse": "(281)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 10}
            },
            {
                "numero": 111,
                "symbole": "Rg",
                "nom": "Roentgenium",
                "masse": "(282)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 11}
            },
            {
                "numero": 112,
                "symbole": "Cn",
                "nom": "Copernicium",
                "masse": "(285)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 12}
            },
            {
                "numero": 113,
                "symbole": "Nh",
                "nom": "Nihonium",
                "masse": "(286)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 13}
            },
            {
                "numero": 114,
                "symbole": "Fl",
                "nom": "Flérovium",
                "masse": "(289)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 14}
            },
            {
                "numero": 115,
                "symbole": "Mc",
                "nom": "Moscovium",
                "masse": "(290)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 15}
            },
            {
                "numero": 116,
                "symbole": "Lv",
                "nom": "Livermorium",
                "masse": "(293)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 16}
            },
            {
                "numero": 117,
                "symbole": "Ts",
                "nom": "Tennesse",
                "masse": "(294)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 17}
            },
            {
                "numero": 118,
                "symbole": "Og",
                "nom": "Oganesson",
                "masse": "(294)",
                "categorie": "inconnu",
                "position": {"row": 7, "col": 18}
            },
            {
                "numero": "",
                "symbole": "",
                "nom": "57-71",
                "masse": "Lanthanides",
                "categorie": "vide",
                "position": {"row": 6, "col": 3}
            },
            {
                "numero": "",
                "symbole": "",
                "nom": "89-103",
                "masse": "Actinides",
                "categorie": "vide",
                "position": {"row": 7, "col": 3}
            }
        ]

        for item in data:
            # Convert 'masse' to Decimal and replace commas with dots
            item['masse'] = Decimal(item['masse'].replace(',', '.')) if item['masse'] else None

            models.objects.update_or_create(
                numero=item['numero'],  # Replace 'numero' with your unique field
                defaults=item
            )

        self.stdout.write(self.style.SUCCESS('Data successfully loaded into the database'))

