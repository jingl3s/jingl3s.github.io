---
title: Hack
description: Hack logiciel responsable
date: 2022-04-03T10:00:00-05:00
draft: true
tags:
- hack
- securite
categories:
  - hack
  - logiciel
---
# Hack logiciel

## Sécurité

* Burp Suite (pour intercepter des requêtes web) https://portswigger.net/burp/communitydownload
* CyberChef (un outil web base pour décoder toutes sortes de données) [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)
  * Rotate 13 est une facon classique de rotation des characteres car sur warmup on avait SYNT au lieu de flag
* Nmap pour scanner les ports ouverts (https://nmap.org/) 
* SQLMap pour automatiser des injections SQL (https://sqlmap.org/)
* Decodage [www.dcode.fr](www.dcode.fr)

## Reverse engineering

### Outils reverse engenering

* Ghidra https://ghidra-sre.org/
* IDA Free https://hex-rays.com/ida-free/
* X64dbg sur windows
* GDB avec le plugin GEF sur Linux https://github.com/hugsy/gef

* Recherche de chaines dans un fichier
  * strings -n 7 kitty.jpeg
  * identify -verbose kitty.jpeg
* base64 decode en ligne de commande dans linux
  * base64 -d

### Emulation jeux videos

#### N64
* Emulateur avec fonction de debug est Project 64
  * [https://hack64.net/docs/pj64d/](https://hack64.net/docs/pj64d/)
  * [https://www.retroreversing.com/n64-decompiling](https://www.retroreversing.com/n64-decompiling)
  * Ne pas oublier d'utiliser la sauvegarde et restauration d'etat pour accelerer les debug
* Ghidra permet de faire une analyse de code si fichier elf dispo sinon Rom car il permet de decompiler avec une vue en langage C
* Un plugin ghidra permet de decompiler une rom N64
  * [https://github.com/zeroKilo/N64LoaderWV](https://github.com/zeroKilo/N64LoaderWV)
* CTF NorthSec 2022 [https://github.com/wernerburat/ctf-writeups/blob/main/_2022/NorthSec%202022/The%20Legend%20of%20Shiitakoin%20Early%20Access/writeup.md](https://github.com/wernerburat/ctf-writeups/blob/main/_2022/NorthSec%202022/The%20Legend%20of%20Shiitakoin%20Early%20Access/writeup.md)

## Circuits logiques

* Pulseview logic analyseur
  * Choose channels
  * Use a decoder like UART and setup the channels
  * Dans l'icone en haut a gauche il est possible de choisir binaire et ensuite d'exporter le decodage 
* Autre outil d'analyseur logique
  * https://www.saleae.com/downloads/
  * Permet de choisir le mode de decoage et les vitesses
* Default Baudrate for serial
  * Standard baud rates include 110, 300, 600, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200, 128000 and 256000
* Convert hexa to text
  * xxd -r -p dump.hex

## Pratiquer légalement

* https://ringzer0ctf.com/home (en particulier les challenges web & injections SQL)
* https://www.root-me.org/ (pour pratiquer le reverse engineering et autre)

## Autres

* Stéganographie
  * https://0xrick.github.io/lists/stego/
  * Crack le mot de passe https://github.com/RickdeJager/stegseek
  * Example https://ctftime.org/writeup/25391
  * Cacher une image dans une image [https://www.avestura.dev/blog/hide-a-photo-inside-another-photo](https://www.avestura.dev/blog/hide-a-photo-inside-another-photo)

* outils étranges
 * Identification automatique mais pas encore utilisé https://github.com/bee-san/pyWhat
* Astuces lignes de commande pour conversion https://github.com/alirezaomidi/ctf/tree/master/ringzer0team/steganography/hidden-in-plain-sight


* Liste d'outils https://blog.lumen.com/8-ways-to-succeed-in-your-first-capture-the-flag-ctf/


## CTF

* Des histoires (et du code) de CTF précédent:
  * https://github.com/UnitedCTF/UnitedCTF-2020
  * https://github.com/UnitedCTF/UnitedCTF-2021
