# Mininet-WiFi: Emulating Software-Deﬁned Wireless Networks 

# Martin Gembec, Martin Dieška 
Cvičiaci: Ing. Tomáš Boros, Utorok - 19:00
------------------------------------------------------------------------

## Analýza
### Mininet
Mininet je sieťový emulátor SDN sietí. Pomocou tohto emulátora dokážeme vygenerovať virtuálnu sieť. Mininet je emulátor určený pre učenie sa princípu fungovania SDN sietí, experimentovanie s rôznymi topológiami sietí, ale aj pre jednoduché testovanie a vývoj OpenFlow aplikácií.

Používateľ má možnosť jednoducho pridávať hostov, switche, routre a prepojenia medzi nimi, čo zabezpečuje flexibilitu pri vytváraní požadovanej topológie (môžeme vytvoriť topológiu s jedným switchom alebo komplexnú topológiu, napr. dátové centrum). Hostovia sa správajú rovnako, ako na skutočnom stroji; je možné testovať komunikáciu medzi jednotlivými hostami alebo spúšťať vlastné programy, ktoré budú odosielať pakety rovnako, ako keby boli spustené na skutočnom Ethernet rozhraní.

### Mininet-Wifi
Mininet-Wifi môžeme definovať ako rozšírenie už existujúceho Mininet emulátora pre SDN siete o virtualizované prístupové body a stanice, ktoré zabezpečujú bezdrôtové pripojenie. V takto upravenom emulátore je stále možné používať funkcionalitu klasického SDN emulátora, avšak je pridaná aj nová funkcionalita, ako napríklad určenie pozície a pohybu stanice relatívne ku prístupovému bodu.


## Návrh
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
   
  


