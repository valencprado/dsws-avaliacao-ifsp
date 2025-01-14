# Desenvolvimento Web Servidor: API's com Flask
Códigos da matéria de "Desenvolvimento Web: Servidor" do Instituto Federal de São Paulo - Campus Pirituba

## Libs instaladas
- flask-bootstrap
- flask-moment
- flask-wtforms
- flask-sqlalchemy
- flask-migrate
- requests
- flask-mail

## Executar projeto
1. Criar ambiente virtual
```bash

python -m venv venv

```

2. Executar ambiente 
- (no Windows Powershell)

    ```bash

    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

    ```

    ```bash

    /env/Scripts/activate

    ```

- No Linux:

    Criar:

    ```bash
    mkvirtualenv myvirtualenv 
    ```

    Reexecutar:

    ```bash
    workon myvirtualenv
    ```

    Desativar:

    ```bash
    deactivate
    ```


3. Instalar dependências

```bash
pip install -r requirements.txt
```

4. Rodar a aplicação

```bash

flask --app hello run --debug

```
