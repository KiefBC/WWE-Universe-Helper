MONTHS = [
    ('01', 'January'),
    ('02', 'February'),
    ('03', 'March'),
    ('04', 'April'),
    ('05', 'May'),
    ('06', 'June'),
    ('07', 'July'),
    ('08', 'August'),
    ('09', 'September'),
    ('10', 'October'),
    ('11', 'November'),
    ('12', 'December')
]

WEIGHT_CLASSES = [
    ('HW', 'Heavyweight'),
    ('CW', 'Cruiserweight'),
    ('LHW', 'Light Heavyweight'),
    ('SHW', 'Super Heavyweight')
]

DAYS_OF_WEEK = [
    ('MON', 'Monday'),
    ('TUE', 'Tuesday'),
    ('WED', 'Wednesday'),
    ('THU', 'Thursday'),
    ('FRI', 'Friday'),
    ('SAT', 'Saturday'),
    ('SUN', 'Sunday')
]

# A dictionary of days from 1 to 31
DAYS_OF_MONTH = [(str(day), str(day)) for day in range(1, 32)]

# A dictionary of years From 1970 to 2030
YEARS = [(str(year), str(year)) for year in range(1, 50)]

# List of Wrestlers in WWE 2K23
WRESTLERS = {
    'AJ Styles': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Akira Tozawa': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Alba Fyre': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Alexa Bliss': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Aliyah': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Andre The Giant': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Angel': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Angelo Dawkins': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Apollo Crews': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Ashante "Thee" Adonis': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Asuka': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Austin Theory': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Axiom': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Batista': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Bayley': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Becky Lynch': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Beth Phoenix': {'weight_class': 'HW', 'show': None, 'gender': 'F'},
    'Bianca Belair': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Big Boss Man': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Big E': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Blair Davenport': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Bobbly Lashley': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Boogeyman': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Booker T': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Braun Strowman': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Bray Wyatt': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Bret "The Hitman" Heart': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Brie Bella': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'British Bulldog': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Brock Lesnar': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Bron Breaker': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Brutus Creed': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Butch': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Cactus Jack': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Cameron Grimes': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Candice LeRAE': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Carmella': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Carmelo Hayes': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Cedric Alexander': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Chad Gable': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Charlotte Flair': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Chyna': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Cody Rhodes': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Commander Azeez': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Cora Jade': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Cruz Del Toro': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Dakota Kai': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Damian Priest': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Dana Brooke': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Dexter Lumis': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Diesel': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Doink The Clown': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Dolph Ziggler': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Dominik Mysterio': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Doudrop': {'weight_class': 'HW', 'show': None, 'gender': 'F'},
    'Drew Gulak': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Drew Mcintyre': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Eddie Guerrero': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Eddie Guerrero \'97': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Edge': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Elias': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Elton Prince': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Eric Bischoff': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Erik': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Ezekiel': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Faarooq': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Finn Balor': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Gigi Dolin': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Giovanni Vinci': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Goldberg': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Grayson Waller': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Gunther': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Happy Corbin': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Harley Race': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Hollywood Hogan': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Hollywood Hogan \'02': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Humberto': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'The Hurricane': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Ilja Dragunov': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Indi Hartwell': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Ivar': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Ivy Nile': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Iyo Sky': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Jacy Jayne': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Jake "The Snake" Roberts': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'JBL': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'JD McDonagh': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Jean-Paul Levesque': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Jerry "The King" Lawler': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Jey USO': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Jim "The Anvil" Neidhart': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Jimmy USO': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Jinder Mahal': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Joaquin Wilde': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Joe Gacy': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'John Cena': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Johnny Gargano': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Julius Creed': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Kane': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Kane \'08': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Karl Anderson': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Karrion Kross': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Katana Chance': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Kayden Carter': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Kevin Nash': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Kevin Nash (nWo)': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Kevin Owns': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Kit Wilson': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Kofi Kingston': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'LA Knight': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Lacey Evans': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Lita': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Liv Morgan': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Logan Paul': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Ludwig Kaiser': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Luke Gallows': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Ma.ce': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    '"Macho Man" Randy Savage': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Madcap Moss': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Man.Soor': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Maryse': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Matt Riddle': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    '"Michin" Mia Yim': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'The Miz': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Montez Ford': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Mr. McMAHON': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Mustafa Ali': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'MVP': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Natalya': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Nikki A.S.H.': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Nikki Bella': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Nikkita Lyons': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Noam Dar': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Omos': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Otis': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Queen Zelina': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'R-Truth': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Randy Orton': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Raquel Rodriguez': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Razor Ramon': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Reggie': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Rey Mysterio': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Rey Mysterio Jr.': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Rhea Ripley': {'weight_class': 'HW', 'show': None, 'gender': 'F'},
    'Rick Boogs': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Rick Steiner': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Ricochet': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Ridge Holland': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Rikishi': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Robert Roode': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'The Rock': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Roman Reigns': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Ronda Rousey': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    '"Rowdy" Roddy Piper': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Roxanne Perez': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Sami Zayn': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Santos Escobar': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Scott Hall': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Scott Hall (nWo)': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Scott Steiner': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Seth "Freakin" Rollins': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Shane McMAHON': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Shanky': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Shawn Michaels': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Shawn Michaels \'05': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Shayna Baszler': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Sheamus': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Shelton Benjamin': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Shinsuke Nakamura': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Shotzi': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Solo Sikoa': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Sonya Deville': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Stacy Keibler': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Stephanie McMAHON': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    '"Stone Cold" Steve Austin': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Syxx': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'T-Bar': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Tamina': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Ted DiBIASE': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Tiffany Stratton': {'weight_class': 'LHW', 'show': None, 'gender': 'F'},
    'Titus O\'neil': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Tommaso Ciampa': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Tony D\'angelo': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Top Dolla': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Trick Williams': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Triple H': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Trish Stratus': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Tyler Bate': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Tyler Breeze': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Ultimate Warrior': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Umaga': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Uncle Howdy': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Undertaker': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Undertaker \'98': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Vader': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Valhalla': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Veer Mahaan': {'weight_class': 'HW', 'show': None, 'gender': 'M'},
    'Wendy Choo': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Wes Less': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'X-PAC': {'weight_class': 'LHW', 'show': None, 'gender': 'M'},
    'Xavier Woods': {'weight_class': 'CW', 'show': None, 'gender': 'M'},
    'Xia Li': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
    'Yokozuna': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Zeus': {'weight_class': 'SHW', 'show': None, 'gender': 'M'},
    'Zoey Stark': {'weight_class': 'CW', 'show': None, 'gender': 'F'},
}