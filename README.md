# db
0- ligar o docker da sua máquina caso não esteja ligado. `Caso esteja no windows`
        
        sudo service docker start

1- Criar um novo arquivo com o nome ".env"

2- Copiar o conteudo de .env.dev (que já está no projeto) para esse novo .env criado

3- Instalar o pip3 

        sudo apt install python3-pip


4- `Se for a primeira vez que você estiver abrindo o projeto`, rodar o comando:

        make prepare_network
        
Esse comando irá criar uma docker network nova. Só precisa ter uma docker dessa funcionando na sua máquina, portanto, `não precisa executar esse comando novamente`.

5- Rodar o comando:
        
        make start-dev

Esse comando sempre deve ser executado quando quiser iniciar o container do banco de dados.

6- Por ultimo, após o container do banco de dados inciar, abra um novo terminal em paralelo (zsh) (não feche o terminal do docker) e rode o comando:
        
        setup_db

7- Para testar se os dados foram carregadaos corretamente, rode o comando:
                                
        make test_db

O resultado esperado é mostrar (print) o nome dos primeiros deputados cadastrados.