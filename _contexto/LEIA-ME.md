# Madu Drummond · Mentoria Individual Scale Business

> Projeto iniciado em 26/08/2026 · **6 meses · 12 encontros, todos quinzenais** · quartas às 10h30, no Zoom.
> Régua a partir do E03 (16/09): 30/09 · 14/10 · 28/10 · 11/11 · 25/11 · 09/12 · **recesso: sem encontros de 15/12 a janeiro** · retomada 03/02 · 17/02 · 03/03/2027.
> E01 Diagnóstico · E02 Briefing do Projeto · E03 Planejamento Estratégico · E04 a E12 com tema a definir ao longo do caminho.

## Arquivos

| Arquivo | O que é |
|---|---|
| `02-mapa-do-cliente-luxo.md` | **Mapa do Cliente Luxo** — 15 campos, a 6ª camada, perfis a priorizar e a arquitetura do ecossistema. |
| `03-mapa-do-metodo.md` | **Mapa do Método Sleepy** — PUV, mecanismo dos 4 Pilares, narrativa, as 8 etapas e o posicionamento central. |
| `04-briefing-do-projeto.md` | **Briefing do Projeto** (10 blocos do padrão SB) — o contrato de trabalho dos 6 meses. |
| `05-esteira-de-produtos.md` | **Esteira de Produtos** — a esteira com preços, o papel de cada solução, a jornada da cliente e a ficha de cada produto. |
| `07-analise-de-vendas.md` | **Análise de Vendas** — 308 vendas desde 2024: faturamento real, sazonalidade, mix, ticket e a base da projeção. |
| `06-guia-de-posicionamento.md` | **Guia de Posicionamento** — posição estratégica, território, o inimigo da marca, manual de marca, manual de comunicação, frases, objeções, bio e ganchos. |
| `08-calendario-de-conteudo.md` | **Calendário de Conteúdo** — snapshot do Instagram, 2 semanas de conteúdo real (Pilar Ritmo Sereno, Afeto e Emoções, Teste Sleepy) e ações estratégicas. Preparado para o Encontro 03. |
| `09-isca-teste-sleepy.md` | **Isca — Teste Sleepy** — as 12 perguntas, a pontuação e os 5 resultados, formatados a partir do `Iscas_.docx` da Madu. Pronto para construir. |
| `Encontros individuais/Encontro 3 - Planejamento/` | **Os 17 documentos do Planejamento Estratégico (E03 · 16/09)** — documentos `10` a `24`: estratégia de vendas, voz da audiência, Calendário BASE D1-D7, pesquisa de mercado, banco de ganchos, pesquisas de Google/TikTok/YouTube, narrativa do método, análises de concorrentes, comandos de extração e as decisões da sessão. |
| `dash/index.html` | **Dash da mentorada**, instanciado do padrão (dash-referência: Rosa Formiga). |
| `dash/sincronizar-dash.py` | Injeta nos slots do dash os documentos-base **02 a 09** (só esses — não lê a pasta do Planejamento Estratégico). **Os `.md` são a fonte da verdade** — edite neles e rode o script de dentro de `dash/`. |
| `transcricoes/` | Transcrição do Encontro 01 (89 min, Gemini 2.5 Flash). |
| `_insumos-briefing/` | Extração da call com timestamps · inventário dos materiais dela · resumo da sessão de 01/05/2026 · textos extraídos dos PDFs e DOCX. |
| `iscas/teste-sleepy/` | **Teste Sleepy com página de captura (30/09)**, no Playbook Visual oficial. `index.html` = captura (nome, WhatsApp, e-mail, idade do bebê) · `teste.html` = as 12 perguntas, só abre com cadastro (`?previa=resultado-rotina` etc. abre sem) · `planilha/` = script da planilha Google da Madu que recebe os leads · `_fonte/` = template e build da captura (`python3 _fonte/captura-build.py`) · `_historico/` = teste de 16/09. Prévia em `http://localhost:8784` (config `isca-teste-sleepy-8784`) · **não publicado**. |
| `iscas/quiz-sleepy/` | **Quiz Sleepy** (2ª isca, por idade · 30/09 · CONSTRUÍDO, não publicado): `index.html` = o quiz (gerado de `_fonte/quiz-template.html` por `_fonte/quiz-build.py` — nunca editar o index à mão) · `guias/` = Guia Sleepy por faixa em PDF (gerado por `_fonte/build-por-faixa.py`, WhatsApp com `[origem: quiz-sleepy]`) · `01-proposta` (APROVADA) · `02-roteiro` (fonte do conteúdo; itens [PEDIR/VALIDAR COM A MADU] entraram PROVISÓRIOS, 19 marcas no template) · `_referencia/` · prévia em `http://localhost:8785` (config `quiz-sleepy-8785`; `?previa=7-9m-varios` etc.). Leads na mesma planilha do Teste (`teste-sleepy/planilha/`, agora "Leads · Sleepy"). |

## Senhas do dash

As senhas são definidas no topo do `<script>` do `dash/index.html` (`SENHA_ALUNA` / `SENHA_ADMIN`).
Peça as senhas diretamente para a Sarah.

## O que já está no dash

- **Encontro 01 completo:** transcrição integral (576 falas, marcas de tempo), 6 insights do diagnóstico e o Plano de Ação liberado com 11 ações.
- **Briefing do Projeto** renderizado em Markdown, em Documentos › Material de trabalho.
- **Os 4 documentos estratégicos completos** — Mapa do Cliente Luxo, Mapa do Método Sleepy, Esteira de Produtos e Guia de Posicionamento, entregues no Encontro 02.
- **Diagnóstico** com as 20 perguntas do banco oficial (`plataforma-sb/lib/diagnostico-checkin.js`).
- Encontros 02 a 12 criados, prontos para receber gravação, transcrição, insights e plano.

## Deploy

```
rsync -az dash/ sb:/var/www/scalebusinessa.com.br/mentoradas/madu-drummond/
```

⚠️ **Sem aprovação da Sarah, não subir.**

## Pendências

- Temas dos encontros 04 a 12 ficam a definir ao longo do caminho (decisão da Sarah, 16/09).
- A pauta dos encontros 03 em diante é previsão de trabalho, não decisão fechada.
- Materiais que a Madu ainda deve enviar: preço da Sonequinha · arquivo de fechamento do 3º encontro · gravação de um encontro real · explicação por voz de como monta o plano de sono.
- **Grafia do método a travar: Sleepy (materiais dela) × Sleep (conversas)** e Aplicativo Sleepy × Aplicativo do Método Sleepy.
- **"Ciclo do Improviso Noturno"** — nome proposto para o inimigo da marca, aguardando aprovação.
- **Tempo de experiência — RESOLVIDO.** Não havia contradição: o Manual é de dez/2024 ("sete anos") e o deck é de ago/2026 ("quase 10 anos"). Início da atuação em **2017**, hoje 9 anos. Usar "quase 10 anos" ou "desde 2017". Falta a Madu confirmar o ano.

## Preços travados (02/09)

| Produto | Preço |
|---|---|
| Aplicativo Sleepy | R$39,90/mês · R$299,90/ano |
| Call Consulta | R$495 |
| Consultoria Sleepy | R$3.497 à vista · 12x R$374 |
| Renovação | R$997 (30 dias + 1 encontro) · R$698 (30 dias) |
| Comunidade Sleepy | a definir · lançamento em novembro ou fevereiro |
| Sonequinha | a definir |
