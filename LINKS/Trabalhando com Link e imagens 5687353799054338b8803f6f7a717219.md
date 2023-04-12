# Trabalhando com Link e imagens

Created: March 13, 2022 4:34 AM

## Adicionando hiperlink

OS vamos hiperlinks, são os link comum, nos queremos em caminhar uma usuário para uma pagina  podemos utilizar, endereções de e-mail também sã o tipo de hiperlinks e podemos fazer simples:

temos duas forma de fazer na primeria temos a seguinte estrutura temos a chave e dentro dela temos o nome que vai aparecer do link, colado nas chaves temos um parenteses com o link e se depois do link e dentro dos parentes e dermos, espaço entre aspas podemos colocar uma descrição para o link. Ex.:  [nome do link](www.link... “espaço descrição do que é o link”)

```markdown
[google](www.google.com.br "site de pesquisa - isso é descrição do link e é bom para acessibidade")

[nome_email](email_aleatorio@galeatorio.com "emails aleatorio")
```

resultado:

 

![Untitled](Trabalhando%20com%20Link%20e%20imagens%205687353799054338b8803f6f7a717219/Untitled.png)

temos outra forma mas nela só aparece o link sem nome:

```markdown
<https:www.google.com.br>

<emailaleatorio@aleatorio.com.br>
```

no caos de link de site essas coisa precisa de https: ou http: antes do link 

Resultado 

![Untitled](Trabalhando%20com%20Link%20e%20imagens%205687353799054338b8803f6f7a717219/Untitled%201.png)

## Adicionando Imagens:

Idêntica a forma de utilização de link com a diferença que temos o ! no inicio e só temos uma única forma de fazer diferente da maneira de inserir link que tínhamos duas 

```markdown
![nome_da_image](https://img.freepik.com/fotos-gratis/imagem-aproximada-em-tons-de-cinza-de-uma-aguia-careca-americana-em-um-fundo-escuro_181624-31795.jpg?t=st=1647156475~exp=1647157075~hmac=9c9b505b27bf0d9bed6c9193ee620b1ae78fa9c2d934ad8d3dd026c513b42a62&w=1380 "imagem aleatoria da internet")
```

resultado:

![Untitled](Trabalhando%20com%20Link%20e%20imagens%205687353799054338b8803f6f7a717219/Untitled%202.png)

## Criando variáveis

São link que podemos podemos utilizar de maneiras mais fácil sem tem que ficar rescrevendo o link toda vez que for utilizar, eu faço a chamada do link pela variável  

```markdown

criando variaveis 

[nome_variavel]:https://img.freepik.com/fotos-gratis/imagem-aproximada-em-tons-de-cinza-de-uma-aguia-careca-americana-em-um-fundo-escuro_181624-31795.jpg?t=st=1647156475~exp=1647157075~hmac=9c9b505b27bf0d9bed6c9193ee620b1ae78fa9c2d934ad8d3dd026c513b42a62&w=1380

[google]:www.google.com.br "descrição"

utllizando variaveis 

[google_link][google]

![variavel][nome_variavel]
```

Resultado:

![Untitled](Trabalhando%20com%20Link%20e%20imagens%205687353799054338b8803f6f7a717219/Untitled%203.png)