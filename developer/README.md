# Tricks on development

## VS Code

* VS Code auto completion issue
  * [https://donjayamanne.github.io/pythonVSCodeDocs/docs/troubleshooting_intellisense/](https://donjayamanne.github.io/pythonVSCodeDocs/docs/troubleshooting_intellisense/)
* VS Code en tant que serveur <https://dev.to/babak/how-to-run-vs-code-on-the-server-3c7h>

##

* [Lecture Oximètre Nonin](https://github.com/jingl3s/NoninPulseOx)
* 'Debug' a distance de navigateurs
  * A distance Debug Firefox ne permet pas de prévisualiser le résultat et ne permet pas l’access au JS
    * Extension pour faire du debug a distance dans Firefox <https://marketplace.visualstudio.com/items?itemName=firefox-devtools.vscode-firefox-debug>
  * A distance debug Chrome
    * Lancer avec les paramètres
        `chrome --remote-debugging-port=9222 --remote-debugging-address=0.0.0.0 --headless`
    * Lancer le chrome controller
    * Ouvrir chrome://inspect
    * Dans configure ajouter 192.168.254.196:9222 ou l'adresse IP du navigateur a controller
  * VSCode remote
    * [https://github.com/microsoft/vscode-js-debug](https://github.com/microsoft/vscode-js-debug)
      * Permet également de formatter du code minifié "Pretty print minified"
    * ms-vscode.js-debug-companion
      * Permet de prendre la main sur le navigateur

* Firefox formatter du code JS dans la console <https://firefox-source-docs.mozilla.org/devtools-user/debugger/how_to/pretty-print_a_minified_file/index.html>

## Infonuagique / Cloud Computing

### General

* Infonuagique / Cloud computing
  * [5 good reasons not to get AWS certified](https://cloudonaut.io/5-good-reasons-not-to-get-aws-certified/)
  * Stay away from the race to the bottom
  * Showcase your skills with your work instead of a certificate
  * Be unique, define your own curriculum
  * Learning by doing is much more effective than memorizing answers
  * Avoid marketing nonsense by learning from independents

### AWS

#### Flux RSS

    https://aws.amazon.com/blogs/aws/feed/
    https://cloudonaut.io/feed/rss.xml

#### Podcasts

    https://aws.amazon.com/fr/podcasts/aws-podcast/?podcast-list.sort-by=item.additionalFields.EpisodeNum&podcast-list.sort-order=desc&awsf.episode-type=*all&awsf.tech-category-filter=*all&awsf.product-filter=*all&awsf.industry-filter=*all
    https://aws.amazon.com/fr/podcasts/aws-techchat/

## Sous sections

* [Numérique responsable](./numerique_responsable/README.md)
* [Python](./python.md)
* [Hacks](./hack_ctf/hack.md)
* [CTF analyses](./hack_ctf/README.md)

* Bureau debout
  * Système étagère à poser sur bureau <https://nickjanetakis.com/blog/build-a-home-made-standing-desk-for-50-dollars-in-10-easy-steps>
*

## Android

* [Android AmazFit Band 5 automatisation sync](./20220408_android_amazfit_automatisation.md)

* Afficher l'écran sur l'ordinateur <https://github.com/Genymobile/scrcpy>
* Faire un VPN en utilisant l'ordinateur en tant que pont pour la connexion internet plutôt que le Wifi <https://github.com/Genymobile/gnirehtet>

## Astuces

* RSS YouTube
  <https://www.ghacks.net/2022/08/01/how-to-subscribe-to-youtube-rss-feeds-without-third-party-services/>
  URL a utiliser <https://www.youtube.com/feeds/videos.xml?channel_id=CHANNELID>
