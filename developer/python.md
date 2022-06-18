# Python

Choses importantes pour Python

## VS Code

### Organizer les import python à la sauvegarde

source : https://www.techiediaries.com/vscode-automatically-organize-python-imports/

* Installer la lib isort
* Ctrl+Shift+P
* Preferences: Configure Language Specific Settings

```json
"[python]": {
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
}
```


## Avancé

### Gestion mémoire

* Méthodes python https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba
* Navigateur moniteur mémoire https://developer.chrome.com/docs/devtools/memory-problems/

### Debug à distance

* [https://www.codementor.io/@jorgecolon/remote-debugging-in-python-v1cbnej91](https://www.codementor.io/@jorgecolon/remote-debugging-in-python-v1cbnej91)


#### Example reglage VSCode

* launch.config
```json
        {
            // Example of attaching to local debug server
            "name": "Python: Attach Local",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "localhost",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ],
        },
        {
            // Example of attaching to my production server
            "name": "Python: Attach Remote",
            "type": "python",
            "request": "attach",
            "port": 5678,
            "host": "192.168.254.196",
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "/CHEMIN_COMPLET"
                }
            ],
        }
```

* Ajouter dans le code

```python
import ptvsd
debugger_helper.attach_vscode(lambda host, port: ptvsd.enable_attach(address=(host, port), redirect_output=True))

```


#### Example reglage VSCode

Cette méthode est plus utile avec un container

[https://github.com/microsoft/debugpy](https://github.com/microsoft/debugpy)

```shell
python -m pip install debugpy

python -m debugpy --listen localhost:5678 mon_fichier.py

```



## Regles codage

### Linter

https://code.visualstudio.com/docs/python/linting
https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html

## Podcasts ##

  * [Python en anglais](https://ayushirawat.com/best-podcasts-for-python)
