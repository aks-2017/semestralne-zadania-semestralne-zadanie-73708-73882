# Mininet-WiFi: Emulating Software-Deﬁned Wireless Networks 

# Martin Gembec, Martin Dieška 
Cvičiaci: Ing. Tomáš Boros, Utorok - 19:00
------------------------------------------------------------------------

# Analýza
## Mininet
Mininet je sieťový emulátor SDN sietí. Pomocou tohto emulátora dokážeme vygenerovať virtuálnu sieť. Mininet je emulátor určený pre učenie sa princípu fungovania SDN sietí, experimentovanie s rôznymi topológiami sietí, ale aj pre jednoduché testovanie a vývoj OpenFlow aplikácií.

Používateľ má možnosť jednoducho pridávať hostov, switche, routre a prepojenia medzi nimi, čo zabezpečuje flexibilitu pri vytváraní požadovanej topológie (môžeme vytvoriť topológiu s jedným switchom alebo komplexnú topológiu, napr. dátové centrum). Hostovia sa správajú rovnako, ako na skutočnom stroji; je možné testovať komunikáciu medzi jednotlivými hostami alebo spúšťať vlastné programy, ktoré budú odosielať pakety rovnako, ako keby boli spustené na skutočnom Ethernet rozhraní[3].

## Mininet-Wifi
Mininet-Wifi môžeme definovať ako rozšírenie už existujúceho Mininet emulátora pre SDN siete o virtualizované prístupové body a stanice, ktoré zabezpečujú bezdrôtové pripojenie. V takto upravenom emulátore je stále možné používať funkcionalitu klasického SDN emulátora, avšak je pridaná aj nová funkcionalita, ako napríklad určenie pozície a pohybu stanice relatívne ku prístupovému bodu[1].

### Architektúra Mininet-Wifi
![architecture](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xdieska-xgembec/blob/master/images/architecture.png "Architektura")

Pomocou Mininet-Wifi vieme nasimulovať akúkoľvek topológiu siete, a následne ju zreplikovať aj v reálnom svete. Pre simuláciu sú k dispozícií dva modely: Mobility model a Propagations model[2].

Aktuálne Mobility modely podporované s Mininet-Wifi sú: Random-Walk, Truncated-Levy Walk, Random- Direction, Random-Waypoint, Gauss-Markov, Reference-Point and Time-Variant Community. Nie sú to však jediné modely, pretože používateľ si vie sám zadefinovať, ktorými bodmi uzol prejde, v akom čase a akou rýchlosťou. Vďaka tomu má používateľ totálnu kontrolu nad uzlami a ich pohybom[2].

V súčasnosti podporuje Mininet-Wifi model tieto Propagations modely: Free-Space, Log-Distance, Two-Ray Ground, and International Telecommunication Union (ITU). Úlohou takýchto modelov je výpočet signálu, ktorý prijme stanica a konverzia týchto hodnôt do reálnych vlastností siete, ako napríklad očakávaná strata paketov a podobne[2].

### VANET
VANET je skratka pre Vehicle Ad Hoc Network. Táto sieť zabezpečuje komunikáciu medzi vozidlami a má slúžiť hlavne na zvýšenie bezpečnosti vozidiel, ktoré navzájom komunikujú v sieti a v prípade kolízie si posielajú varovné signály. Vďaka Mininet-Wifi by mohla byť táto komunikácia spoľahlivejšia a rýchlejšia.[4]
![vanet](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xdieska-xgembec/blob/master/images/vanet.png "vanet example")
Prehľad programovateľnosti OpenFlow s použitím VANET a architektúry automobilových uzlov, ako staníc v službe Mininet-WiFi[4]

### Porovnanie emulátorov
![emulators](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xdieska-xgembec/blob/master/images/emulator_compare.png "Porovnanie emulatorov")

# Návrh
V našej práci budeme overovať predchádzajúcu prácu[1], ktorá sa zaoberala témou Mininet-Wifi. Autori v článku podrobne rozpisovali SDN siete a Mininet – emulátor pre vytváranie takýchto sieti. Následne predstavujú Mininet-Wifi; spojenie Mininetu a prístupových bodov a staníc, ktoré zabezpečujú bezdrôtové pripojenie. V článku je opísaný postup, ako si vytvoriť vlastnú topológiu spolu s príkladmi komunikácie medzi jednotlivými hostami pomocou tejto bezdrôtovej siete. Nakoniec boli uvedené softvérové a hardvérové experimenty, ktoré ukázali výhody a slabiny Mininet-Wifi emulátora.

Našim cieľom bude vytvoriť topológiu mininet-wifi siete, ktorú bude definovať používateľ pomocou webového rozhrania. Webové rozhranie bude poskytovať používateľovi príjemné a jednoduché používateľské rozhranienie a bude mať viacero použití: 

 - vytvorenie sieťovej topológie zadaním parametrov
 - zobrazenie vytvorenej topológie na webe
 - zisťovanie konektivity jednotlivých zariadení v sieti
 - poskytnúť log o pripojeniach v sieti

Vytvorením sieťovej topológie sa myslí vytovrenie zadaného počtu staníc a prístupových bodov v určitej vziadelenosti od seba, keďže sa jedná o Wifi sieť, kde je vziadelnosť najpodstatnejšia.
  
  Topológiu, ktorú sme vytvorili bude môcť používateľ zobraziť v podobe grafu priamo na webe.
  
  Používateľ bude mať možnosť overiť konektivitu zvolenej stanice na inú stanicu, alebo na prístupový bod. Taktiež bude môcť overiť dostupnosť staníc z pohľadu prístupového bodu.
  
  Overené pripojenia z predchádzajúceho bodu sa budú dať zobraziť ako textová informácia na webe.
  
  Architektúra aplikácie bude postavená na základe Server-Client komunikácie. Bude pozostávať zo serveru, ktorý bude pracovať s Mininet-Wifi a zároveň bude poskytovať RESTové rozhranie zabezpečujúce komunikáciu s klientom. Klient bude následne využívať RESTové rozhranie na vykonávanie požiadaviek od používateľa a prijímanie dát, ktoré zobrazí následne na webe.

## Mockup návrh webovej aplikácie
![webapp-mockup](https://github.com/aks-2017/semestralne-zadania-semestralne-zadanie-xdieska-xgembec/blob/master/images/webapp-mockup.PNG "Mockup")
   
# Použitá literatúra
1. http://ieeexplore.ieee.org/document/7367387/

2. Ramon dos Reis Fontes and Mohamed Mahfoudi and Walid Dabbous and Thierry Turletti and Chris- tian Rothenberg. How Far Can We Go? Towards Realistic Software-Defined Wireless Networking Experiments, Oxford University Press (OUP), DOI: 10.1093/comjnl/bxx023.

3. Kreutz, D., Ramos, F. M. V., Ver´ıssimo, P., Rothenberg, C. E., Azodolmolky, S., and Uhlig, S. (2014) Software-defined networking: A comprehensive survey. CoRR, abs/1406.0440.

4. Fontes, R. R. and Rothenberg, C. E, From Theory to Experimental Evaluation: Resource Management in Software-Defined Vehicular Networks, University of Campinas (UNICAMP), Feb 23, 2017

