---
title: Linux astuces
description: Linux astuces en tout genre
date: 2023-08-23T10:00:00-05:00
draft: true
tags:
- linux
categories:
  - logiciel
---

# Linux astuces

## Debian/Ubuntu/Mint

* Désactiver/activer login automatique

  ```shell
  sudo geany /etc/lightdm/lightdm.conf 
  ```

  ```conf
  [SeatDefaults]  
  greeter-session=unity-greeter  
  user-session=ubuntu  
  autologin-user=username
  ```