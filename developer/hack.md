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

## Sécurité we

* Burp Suite (pour intercepter des requêtes web) https://portswigger.net/burp/communitydownload
* CyberChef (un outil web base pour décoder toutes sortes de données) [https://gchq.github.io/CyberChef/](https://gchq.github.io/CyberChef/)
  * Rotate 13 est une facon classique de rotation des characteres car sur warmup on avait SYNT au lieu de flag
* Nmap pour scanner les ports ouverts (https://nmap.org/) 
* SQLMap pour automatiser des injections SQL (https://sqlmap.org/)
* Decodage [www.dcode.fr](www.dcode.fr)

## Reverse engineering
* Ghidra https://ghidra-sre.org/
* IDA Free https://hex-rays.com/ida-free/
* X64dbg sur windows
* GDB avec le plugin GEF sur Linux https://github.com/hugsy/gef

* Recherche de chaines dans un fichier
  * strings -n 7 kitty.jpeg
  * identify -verbose kitty.jpeg
* base64 decode en ligne de commande dans linux
  * base64 -d

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

## CTF

* Des histoires (et du code) de CTF précédent:
  * https://github.com/UnitedCTF/UnitedCTF-2020
  * https://github.com/UnitedCTF/UnitedCTF-2021
