`echo %~1 |clip`

* `%~1` retorna o caminho do primeiro argumento sem as aspas
* `|clip` copia para o clipboard


1. Criar o arquivo Batch
2. Criar um atalho para o arquivo
3. Configurar em Propriedades para executar de forma minimizada: isso serve para não mostrar a tela preta ao ser executado
4. Mover para a pasta do SendTo (`C:\Users\...\AppData\Roaming\Microsoft\Windows\SendTo`)
