# Tricks on development

## VS Code

* VS Code auto completion issue
    * [https://donjayamanne.github.io/pythonVSCodeDocs/docs/troubleshooting_intellisense/](https://donjayamanne.github.io/pythonVSCodeDocs/docs/troubleshooting_intellisense/)
* [Lecture Oximètre Nonin](https://github.com/jingl3s/NoninPulseOx)
* 'Debug' a distance de navigateurs
  * A distance Debug Firefox ne permet pas de previsualiser le résulat et ne permet pas l’access au JS
  * A distance debug Chrome
    * Lancer avec les parametres
        `chrome --remote-debugging-port=9222 --remote-debugging-address=0.0.0.0 --headless`
    * Lancer le chrome controller
    * Ouvrir chrome://inspect
    * Dans configure ajouter 192.168.254.196:9222 ou l'adresse IP du navigateur a controller
