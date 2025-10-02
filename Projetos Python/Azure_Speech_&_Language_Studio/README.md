# 🚗 Desafio DIO - Azure Speech & Language Studio com Avaliações de Veículos

Este repositório documenta minha experiência prática com ferramentas de inteligência artificial da Microsoft — **Azure Speech Studio** e **Azure Language Studio** — aplicadas ao contexto de **avaliações de veículos por usuários**. O objetivo foi explorar recursos de fala e linguagem natural, simulando aplicações reais para análise de opiniões em áudio e texto sobre carros.

---

## 🛠️ Ferramentas Utilizadas

- **Azure Speech Studio**
  - Speech to Text (STT)
  - Text to Speech (TTS)

- **Azure Language Studio**
  - Análise de Sentimentos
  - Extração de Entidades Nomeadas
  - Classificação de Texto

- **GitHub + Markdown**
  - Para documentação técnica

---

## 🗣️ Speech Studio - Experimentos

### 🎯 Experimento 1: Fala para Texto (Speech to Text)

**Contexto:** Simulei o envio de feedback por voz de um cliente após test drive.

**Entrada (áudio em português):**  
> "Achei o consumo do carro excelente, mas o espaço interno poderia ser melhor."

**Resultado do STT:**  
> "Achei o consumo do carro excelente, mas o espaço interno poderia ser melhor."

**Observações:**
- A transcrição foi precisa.
- A pontuação foi automaticamente aplicada.
- A ferramenta detectou corretamente o idioma (pt-BR).

---

### 🎯 Experimento 2: Texto para Fala (Text to Speech)

**Texto convertido:**  
> "Este carro oferece excelente custo-benefício e um bom desempenho em estrada."

**Configurações:**
- Voz: FranciscaNeural
- Idioma: pt-BR
- Emoção: neutra

**Resultado:** A voz gerada foi clara e natural, com ótima entonação para aplicações como:
- Leitura de reviews em aplicativos automotivos
- Acessibilidade para usuários com deficiência visual

---

## 📚 Language Studio - Experimentos

### 🎯 Experimento 3: Análise de Sentimentos

**Entrada:**  
> "O motor é muito silencioso e responde bem, mas o acabamento deixa a desejar."

**Resultado:**
- **Sentimento geral:** Neutro
- **Análise detalhada:**
  - Positivo: "motor é muito silencioso", "responde bem"
  - Negativo: "acabamento deixa a desejar"

**Aplicação prática:** Ideal para analisar reviews de clientes e gerar relatórios automáticos sobre pontos fortes e fracos de um modelo.

---

### 🎯 Experimento 4: Extração de Entidades

**Texto analisado:**  
> "Comprei um Honda Civic 2022 em Belo Horizonte no mês passado e estou satisfeito."

**Entidades extraídas:**
- Produto: *Honda Civic 2022*
- Local: *Belo Horizonte*
- Data relativa: *mês passado*
- Sentimento implícito: *positivo*

**Usos possíveis:** Mapear dados de localização, modelo e data em grandes volumes de avaliações.

---

### 🎯 Experimento 5: Classificação de Texto

**Texto:**  
> "O desempenho do câmbio automático surpreendeu, principalmente em retomadas."

**Categoria atribuída:**  
- *Desempenho / Transmissão*

**Utilidade:** Permite organizar automaticamente comentários em categorias como:
- Consumo
- Desempenho
- Conforto
- Acabamento
- Tecnologia

---

## 📌 Aprendizados

- O **Speech Studio** é simples e funcional, ótimo para prototipagem de apps que envolvem entrada por voz.
- O **Language Studio** mostrou-se extremamente útil para analisar textos de forma automática e com boa precisão.
- Essas ferramentas são ideais para cenários de análise de opinião de usuários, especialmente em plataformas de reviews automotivos.
- Documentar com clareza os testes feitos permite replicar e escalar soluções com facilidade.

---

## 🔄 Como Reproduzir os Testes

1. Acesse o portal da Microsoft: [https://portal.azure.com](https://portal.azure.com)
2. No **Azure Speech Studio**:
   - Use a função “Speech to Text” e grave frases como feedbacks de clientes.
   - Experimente o “Text to Speech” com frases de avaliações.
3. No **Azure Language Studio**:
   - Use a ferramenta de “Análise de Sentimentos” com textos de avaliações reais.
   - Extraia entidades e experimente a classificação de texto por categorias.
4. Teste com diferentes tipos de avaliações (positivas, neutras, negativas).

---

## 📚 Referências

- [Azure Speech Studio - Microsoft Docs](https://learn.microsoft.com/pt-br/azure/cognitive-services/speech-service/)
- [Azure Language Studio - Microsoft Docs](https://learn.microsoft.com/pt-br/azure/ai-services/language-service/)
- [Guia Markdown no GitHub](https://guides.github.com/features/mastering-markdown/)

---

## 👤 Autor

**Lucas Siqueira de Souza**  

---

---

