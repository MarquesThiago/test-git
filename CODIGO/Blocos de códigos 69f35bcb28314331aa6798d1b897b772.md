# Blocos de códigos

Created: March 13, 2022 4:38 AM

No markdown temos forma de inserir código. de forma que criamos blocos, esses texto são considerados de mono-espaçados, e como já e bem comum existem duas formas de realizar a inserção de código no markdown, a primeira considera só como um bloco de código, e não a especificação  da linguagem e utilizamos  crase para abrir e fechar esse blocos:

```markdown
codigo python

```
def claer_text(text):
	return " ".join([letter for letter in re.sub("\s", " ", text) if not letter in string.ponctual])  

```

```

Resultado

![Untitled](Blocos%20de%20co%CC%81digos%2069f35bcb28314331aa6798d1b897b772/Untitled.png)

Agora se passarmos depois da crase o nome da linguagem com o mesmo código 

```markdown
codigo python

```python
def claer_text(text):
	return " ".join([letter for letter in re.sub("\s", " ", text) if not letter in string.ponctual])  

```
```

Resultado:

![Untitled](Blocos%20de%20co%CC%81digos%2069f35bcb28314331aa6798d1b897b772/Untitled%201.png)

podemos notar que ele colocar uma coloração respeitando a linguagem

também podemos utilizar o ~ ao invés da ` é o mesmo resultado.