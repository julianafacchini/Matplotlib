#!/usr/bin/env python
# coding: utf-8

# Vamos agora estudar a biblioteca de visualização chamada Matplotlib. Essa é uma ferramenta básica para os
# cientistas de dados. Os gráficos que ela fornece são simples e 'limpos'. Por isso, ela é usada para um
# conhecimento inicial dos dados. A documentação é bastante boa e deve ser usada sempre! Vamos conhecer algumas 
# ferramentas abaixo. Utilizarei dados que sejam bons para a visualização dos gráficos. Para isso, importaremos
# o dataset tips do seaborn.
# https://matplotlib.org/
# 
# Primeiro vamos importar as bibliotecas pandas e numpy para manipulação dos dados, carregamento de arquivos etc. Vamos importar a biblioteca matplotlib, sendo que utilizaremos a subpasta pyplot da mesma (import matplotlib.pyplot), vamos apelida-la de plt. Sempre coloco o comando: %matplotlib inline, para que os gráficos
# aparecem dentro do próprio notebook. Essa decisão é pessoal. Importaremos seaborn para obter o dataset tips.

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Carregando o dataset Tips
data = sns.load_dataset('tips')


# In[3]:


#Verificando as 5 primeiras linhas 
data.head()


# O gráfico de linhas é usado para observar variáveis quantitativas. Eles são compostos por um número muito grande
# de pontos, ligados uns com os outros com segmentos de retas.Eles são importantes para verificar o comportamento
# dos dados, se estão normalizados,etc

# In[4]:


graf = plt.plot(data.tip, color = 'red')
plt.xlabel('Quantidade de gorjeta')
plt.ylabel('Valores de Gorjeta')
plt.title('GRAFICO DE LINHAS')
plt.show()


# O gráfico de barras é bom para visualizar o balanceamento dos dados. Verificar se temos muita diferença
# na quantidade de cada variável. Se as variáveis target forem muito desbalanceadas, você poderá ter problemas
# no seu resultado final. O seu modelo poderá "aprender" mais um resultado do que o outro, levando a acurácia para
# valores baixos.

# In[5]:


graf2 = plt.bar(data.sex, data.tip, color = 'green')
plt.xlabel('Sexo')
plt.ylabel('Quantidade de Gorjeta')
plt.title('GRÁFICO DE COLUNAS')
plt.show()


# O gráfico de dispersão é bastante valioso para observar o comportamento da sua variável e também a relação
# dela com uma segunda variável. Por exemplo, um gráfico de dispersão pode mostrar nitidamente um comportamento
# de linearidade ou exponencialidade. No gráfico abaixo escolhi o marcador triângulo, mas há várias possibilidades.O
# default é círculo. O alpha muda a transparência dos marcadores, tornando-se, ao meu ver, mais facil a visualização. 

# In[6]:


graf3 = plt.scatter(data.tip, data.total_bill, marker = "v", alpha = 0.6)
plt.xlabel('Gorjeta')
plt.ylabel('Total')
plt.title('GRÁFICO DE DISPERSÃ')
plt.show()


# O box plot é um conhecido gráfico para verificação de outliers. Esses são dados "fora da curva", aqueles que
# estão fora do padrão dos demais. Na maioria das vezes esses valores são indesejáveis, eles acabam aumentando o erro do modelo, tornando-o menos confiável. No entanto, as vezes os outliers são exatamente aquilo que procuramos
# como, por exemplo, na busca por fraudes em cartões.

# In[7]:


graf4 = plt.boxplot(data.total_bill)
plt.title('GRÁFICO BOX PLOT')
plt.show()


# Os histogramas são muito usados para verificar se os dados estão normalizados. 

# In[8]:


graf5 = plt.hist(data.total_bill, color = 'purple',label= 'total de gorjeta')

plt.title('HISTOGRAMA')
plt.show()


# In[ ]:




