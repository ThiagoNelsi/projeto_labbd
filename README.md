# Como rodar o projeto

## Iniciar o banco de dados:

Na pasta raiz do projeto, execute o seguinte comando para iniciar o container MySQL.
Isso criará uma instância MySQL, inicializará o banco de dados e executará o script setup.sql
que cria as tabelas e views e importa os dados:

```bash
sudo docker run --name labbd-mysql \
  -e MYSQL_ROOT_PASSWORD=123 \
  -e MYSQL_DATABASE=labbd \
  -p 3306:3306 \
  -v $(pwd)/data:/var/lib/mysql-files \
  -v $(pwd)/setup.sql:/docker-entrypoint-initdb.d/setup.sql \
  -d mysql:latest
```

### Iniciar a aplicação web:

Navegue até a pasta `src` instale as dependências e inicie o streamlit:

```bash
cd src
pip install -r ./requirements.txt
streamlit run app.py
```

Por fim, acesse http://localhost:8501/
