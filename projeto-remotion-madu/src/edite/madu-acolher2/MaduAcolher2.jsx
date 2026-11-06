// Edite Pro · Reel da Madu Drummond · "Acolher o choro · regravação (takes 9285 + 9291 + 9288)" · lote 20/10/2026
// Modelo aprovado: Reel "Acolher o choro" (14/10, skill /edite-pro-madu). Identidade = Playbook da Madu, seção 10:
// legenda Inter 800 68 px Azul Noite + marca-texto Pêssego + Playfair itálico 88 px no destaque, brilho branco difuso.
// Nesta gravação a Madu está mais perto e segura o microfone no queixo: rosto em y 553–1253 no bruto (Vision, preparar.py),
// por isso a legenda da tela cheia desce para o busto abaixo do microfone e a Madu desce menos na dividida.
// Sem névoa e sem efeito sonoro nos cortes (Sarah 14/10); piano baixo só na mixagem final. CTA: palavra-chave do Guia.
import React from 'react';
import {
  AbsoluteFill, Audio, Easing, Img, OffthreadVideo, Sequence, interpolate, staticFile,
  useCurrentFrame, useVideoConfig,
} from 'remotion';
import {loadFont as loadInter} from '@remotion/google-fonts/Inter';
import {loadFont as loadPlayfair} from '@remotion/google-fonts/PlayfairDisplay';

const {fontFamily: INTER} = loadInter('normal', {weights: ['500', '800'], subsets: ['latin', 'latin-ext']});
const {fontFamily: PLAYFAIR} = loadPlayfair('italic', {weights: ['400'], subsets: ['latin', 'latin-ext']});

// Paleta Madu (playbook)
const COR = {noite: '#1F4B7A', pessego: '#FFDBD5', nevoa: '#EEF6FB', ceu: '#AEDDED', branco: '#FFFFFF'};
const noite = (a) => `rgba(31,75,122,${a})`;
const nevoa = (a) => `rgba(238,246,251,${a})`;
const BRILHO = '0 0 18px rgba(255,255,255,.95), 0 0 34px rgba(255,255,255,.8), 0 0 60px rgba(255,255,255,.55)';
const SOMBRA = '0 26px 60px rgba(31,75,122,0.28), 0 3px 8px rgba(31,75,122,0.12)';

const JUNCAO = 880;          // fim do apoio na tela dividida (mescla sem faixa)
const VIDEO_Y_DIV = 470;     // na dividida a Madu desce: o alto do cabelo (rosto a partir de y 553–691 no bruto) fica abaixo da legenda
const LEGENDA_DIV_BASE = 872; // na dividida a legenda fica presa por baixo na junção, sempre acima do cabelo (Sarah 14/10: nunca no rosto)
const LEGENDA_CHEIA = 1180;  // tela cheia: no peito, abaixo do queixo (≤ 1253), do microfone e da mão que o segura (conferência 20/10)
const TRANS = 0.34;
const A = (n) => `madu-acolher2/${n}`;

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'};
const suave = Easing.bezier(0.16, 1, 0.3, 1);
const norm = (s) => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, '');

const criaG = (dados) => (texto, n = 1) => {
  const alvo = norm(texto);
  const achados = dados.grupos.filter((g) => norm(g.palavras.map((p) => p.texto).join(' ')).startsWith(alvo));
  if (!achados[n - 1]) throw new Error(`Grupo não encontrado: ${texto} (${n})`);
  return achados[n - 1].inicio;
};
const criaQ = (dados) => {
  const lista = dados.grupos.flatMap((g) => g.palavras);
  return (texto, n = 1) => {
    const achadas = lista.filter((p) => norm(p.texto) === norm(texto));
    if (!achadas[n - 1]) throw new Error(`Palavra não encontrada: ${texto} (${n})`);
    return achadas[n - 1];
  };
};

const useTempo = () => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const ease = (a, b) => interpolate(t, [a, b], [0, 1], {...clamp, easing: suave});
  return {frame, fps, t, ease};
};

// ---------- Material da Madu (página inteira, na proporção dela) ----------
const ASP_DOC = 1521 / 1076;
const Doc = ({src, cx, cy, h, p = 1, sai = 0, rot = 0}) => {
  const w = h / ASP_DOC;
  return (
    <div style={{position: 'absolute', left: cx - w / 2, top: cy - h / 2, width: w, height: h, borderRadius: 14, overflow: 'hidden',
      background: '#fff', boxShadow: SOMBRA, opacity: Math.min(p * 1.6, 1) * (1 - sai),
      filter: p < 0.99 || sai > 0.01 ? `blur(${(1 - p) * 14 + sai * 10}px)` : undefined,
      transform: `translateY(${(1 - p) * 80 - sai * 90}px) rotate(${rot}deg) scale(${0.9 + 0.1 * p})`}}>
      <Img src={staticFile(A(`assets/${src}`))} style={{width: w, height: h, display: 'block'}} />
    </div>
  );
};

// ---------- Apoio da tela dividida: vídeo novo em largura total OU páginas da Madu sobre a névoa ----------
// em = quando entra · desce = quanto o vídeo sobe (px na largura 1080) para o assunto ficar acima da junção · de = ponto do clipe
const Apoio = ({lista}) => {
  const {t, fps, ease} = useTempo();
  const k = lista.reduce((acc, it, i) => (t >= it.em ? i : acc), -1);
  if (k < 0) return null;
  const camada = (it, i, entra) => {
    const fim = lista[i + 1] ? lista[i + 1].em : it.em + 30;
    const kb = interpolate(t, [it.em, fim + 0.4], [0, 1], clamp); // aproximação lenta
    const estilo = {position: 'absolute', inset: 0, opacity: entra, filter: entra < 0.99 ? `blur(${(1 - entra) * 12}px)` : undefined};
    if (it.video) {
      const h = it.alt || 1920;
      return (
        <div key={`ap${i}`} style={estilo}>
          <Sequence from={Math.round(it.em * fps) - 8} layout="none" premountFor={Math.round(1.5 * fps)}>
            <OffthreadVideo src={staticFile(A(`apoios/${it.video}`))} muted trimBefore={Math.round((it.de || 0) * fps)}
              style={{position: 'absolute', left: 0, top: -it.desce, width: 1080, height: h,
                transform: `scale(${1.02 + 0.05 * kb + 0.05 * (1 - entra)})`, transformOrigin: `540px ${it.desce + 440}px`}} />
          </Sequence>
        </div>
      );
    }
    // páginas: a primeira entra, a seguinte chega pela direita e fica na frente (cada página inteira)
    const docs = it.docs;
    return (
      <div key={`ap${i}`} style={{...estilo, background: `radial-gradient(120% 90% at 30% 20%, #FFFFFF 0%, ${COR.nevoa} 55%, #DCEBF5 100%)`}}>
        {docs.map((d, j) => {
          const p = ease(d.em, d.em + 0.5);
          const n = docs.length;
          const cx = n === 1 ? 540 : 540 + (j - (n - 1) / 2) * 300;
          return <Doc key={j} src={d.src} cx={cx} cy={405} h={n === 1 ? 640 : 590} p={p} rot={n === 1 ? 0 : (j - (n - 1) / 2) * 3.5} />;
        })}
      </div>
    );
  };
  const atual = lista[k];
  const entra = k === 0 ? 1 : ease(atual.em - 0.05, atual.em + 0.35);
  return <>
    {k > 0 && entra < 1 && camada(lista[k - 1], k - 1, 1)}
    {camada(atual, k, entra)}
  </>;
};

// ---------- Letreiro na tela cheia (Inter 800 + Playfair itálico), sobre véu névoa no alto ----------
// sem letreiro na tela cheia: o rosto da Madu ocupa o alto da tela e o letreiro caía sobre ele (conferência 14/10)
const LETTERING = (G) => [];
const Lettering = ({itens}) => {
  const {t, ease} = useTempo();
  const atual = itens.filter((l) => t >= l.a - 0.05 && t < l.b + 0.25).pop();
  if (!atual) return null;
  const e = ease(atual.a, atual.a + 0.35), s = ease(atual.b - 0.05, atual.b + 0.2);
  const v = e * (1 - s);
  return <>
    <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: 700, opacity: v,
      background: `linear-gradient(180deg, ${nevoa(0.94)} 0px, ${nevoa(0.86)} 300px, ${nevoa(0.45)} 500px, ${nevoa(0)} 700px)`}} />
    <div style={{position: 'absolute', left: 108, right: 108, top: 170, textAlign: 'center', opacity: v,
      filter: `blur(${(1 - e) * 10 + s * 8}px)`, transform: `scale(${0.95 + 0.05 * e + 0.03 * ease(atual.a, atual.b)}) translateY(${-s * 30}px)`}}>
      {atual.linhas.map(([txt, tipo], i) => (tipo === 'inter'
        ? <div key={i} style={{fontFamily: INTER, fontWeight: 800, fontSize: 74, letterSpacing: '-0.02em', color: COR.noite, lineHeight: 1.1}}>{txt}</div>
        : <div key={i} style={{display: 'inline-block', marginTop: 10, fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: 112,
            lineHeight: 1.05, color: COR.noite, background: COR.pessego, padding: '0 .2em .08em', borderRadius: 10, transform: 'rotate(-1.2deg)'}}>{txt}</div>
      ))}
    </div>
  </>;
};
const repete = (grupo, item) => {
  if (!item || !item.linhas) return false;
  const chaves = new Set(item.linhas.flatMap(([txt]) => txt.split(' ').map(norm)));
  return grupo.palavras.some((p) => norm(p.texto).length >= 4 && chaves.has(norm(p.texto)));
};

// ---------- Madu ----------
const Pessoa = ({cortes, duracao, modo, cta}) => {
  const {fps} = useVideoConfig();
  const inicios = cortes.map((c) => Math.round(c.saida * fps));
  return cortes.map((c, i) => {
    const de = inicios[i];
    const ate = i + 1 < cortes.length ? inicios[i + 1] : Math.round(duracao * fps);
    return (
      <Sequence key={i} from={de} durationInFrames={ate - de} premountFor={i ? Math.round(1.5 * fps) : 0}>
        <PessoaCorte corte={c} indice={i} dur={ate - de} modo={modo} cta={cta} />
      </Sequence>
    );
  });
};
const PessoaCorte = ({corte, indice, dur, modo, cta}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = corte.saida + frame / fps;
  const m = modo(t);
  const cheia = (indice % 2 === 0 ? 1.04 : 1.1) + interpolate(frame, [0, dur], [0, 0.03], clamp);
  // chamada final: Madu ampliada (playbook)
  const amplia = interpolate(t, [cta, cta + 0.4], [0, 0.12], {...clamp, easing: suave});
  const z = cheia + (1.0 - cheia) * m + amplia;
  const entra = indice ? interpolate(frame, [0, 6], [1, 0], {...clamp, easing: Easing.out(Easing.cubic)}) : 0;
  return (
    <OffthreadVideo
      src={staticFile(corte.video)}
      trimBefore={Math.round(corte.de * fps)}
      volume={(f) => interpolate(f, [dur - 1, dur], [1, 0], clamp)}
      style={{position: 'absolute', left: 0, top: VIDEO_Y_DIV * m, width: 1080, height: 1920,
        transform: `scale(${z * (1 + 0.05 * entra)})`, transformOrigin: '540px 1100px', filter: entra > 0.01 ? `blur(${entra * 4}px)` : undefined}}
    />
  );
};

// ---------- Legenda (playbook da Madu) ----------
// quebra o grupo em no máximo 2 linhas (~18 caracteres por linha)
const linhas = (palavras) => {
  const total = palavras.reduce((s, p) => s + p.texto.length + 1, 0);
  if (total <= 20) return [palavras];
  let acc = 0, k = 0;
  for (; k < palavras.length - 1; k++) { acc += palavras[k].texto.length + 1; if (acc >= total / 2) break; }
  return [palavras.slice(0, k + 1), palavras.slice(k + 1)];
};
const Legenda = ({grupos, modo, oculta, lettering}) => {
  const frame = useCurrentFrame();
  const {fps} = useVideoConfig();
  const t = frame / fps;
  const i = grupos.findIndex((g, k) => {
    const prox = grupos[k + 1];
    const fim = prox ? Math.min(prox.inicio, g.fim + 0.6) : g.fim + 0.8;
    return t >= g.inicio && t < fim;
  });
  if (i < 0 || oculta(t)) return null;
  const letreiro = lettering.find((l) => t >= l.a - 0.05 && t < l.b + 0.25);
  if (repete(grupos[i], letreiro)) return null;
  // em transição a legenda nunca fica no rosto: some enquanto a tela troca
  const m = modo(t);
  const ls = linhas(grupos[i].palavras);
  const y = m >= 0.5 ? LEGENDA_DIV_BASE - ls.length * 100 : LEGENDA_CHEIA;
  const vis = interpolate(m, [0, 0.12, 0.88, 1], [1, 0, 0, 1], clamp);
  if (vis <= 0.01) return null;
  const g = grupos[i];
  const f0 = frame - Math.round(g.inicio * fps);
  const cresce = interpolate(f0, [0, 5], [0.9, 1], {...clamp, easing: suave});
  return (
    <div style={{position: 'absolute', left: 70, right: 70, top: y, textAlign: 'center', opacity: vis,
      transform: `scale(${cresce})`, transformOrigin: '50% 0%'}}>
      {ls.map((ln, li) => (
        <div key={li} style={{fontFamily: INTER, fontWeight: 800, fontSize: 68, lineHeight: '100px', letterSpacing: '-1.6px',
          color: COR.noite, textShadow: BRILHO, whiteSpace: 'nowrap'}}>
          {ln.map((p, k) => {
            const falada = t >= p.inicio - 0.02 && t < Math.max(p.fim, p.inicio + 0.18);
            const ult = k === ln.length - 1;
            const base = {display: 'inline-block', marginRight: ult ? 0 : '0.26em', position: 'relative'};
            const txt = p.destaque
              ? <span style={{fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: 88, letterSpacing: 0}}>{p.texto}</span>
              : p.texto;
            return (
              <span key={k} style={base}>
                {/* marca-texto Pêssego acompanha a voz, palavra a palavra, levemente inclinado */}
                <span style={{position: 'absolute', left: '-0.12em', right: '-0.12em', top: '22%', bottom: '14%', background: COR.pessego,
                  borderRadius: 8, transform: 'rotate(-1.5deg)', opacity: falada ? 1 : 0, zIndex: -1, boxShadow: 'none'}} />
                <span style={{position: 'relative', textShadow: falada ? 'none' : BRILHO}}>{txt}</span>
              </span>
            );
          })}
        </div>
      ))}
    </div>
  );
};

// ---------- Chamada final (tela cheia, sobre o busto) e palavra-chave sozinha ----------
const Chamada = ({inicio, fim}) => {
  const {t, ease} = useTempo();
  if (t < inicio - 0.1 || t > fim + 0.3) return null;
  const e = ease(inicio, inicio + 0.4), s = ease(fim - 0.05, fim + 0.25);
  return (
    <div style={{position: 'absolute', left: 108, right: 108, top: 1130, textAlign: 'center', opacity: e * (1 - s),
      transform: `translateY(${(1 - e) * 30}px)`, zIndex: 12}}>
      <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 76, color: COR.noite, textShadow: BRILHO, letterSpacing: '-0.02em'}}>Comente</div>
      <div style={{display: 'inline-block', margin: '8px 0 10px', fontFamily: PLAYFAIR, fontStyle: 'italic', fontSize: 104, color: COR.noite,
        background: COR.pessego, padding: '0 .22em .06em', borderRadius: 10, transform: 'rotate(-1.2deg)'}}>QUERO</div>
      <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 50, lineHeight: 1.2, color: COR.noite, textShadow: BRILHO}}>que eu te explico como conduzo<br />isso na Consultoria Sleepy</div>
    </div>
  );
};
const Fechamento = ({inicio}) => {
  const {t, ease} = useTempo();
  if (t < inicio) return null;
  const e = ease(inicio, inicio + 0.4), cresce = ease(inicio + 0.1, inicio + 0.8);
  return (
    <AbsoluteFill style={{zIndex: 20, opacity: e, background: `radial-gradient(120% 80% at 50% 30%, #FFFFFF 0%, ${COR.nevoa} 60%, #DCEBF5 100%)`}}>
      <Img src={staticFile(A('assets/logo-madu-drummond-escura.png'))} style={{position: 'absolute', left: 540 - 150, top: 230, width: 300, opacity: 0.95}} />
      <div style={{position: 'absolute', left: 0, right: 0, top: 960, textAlign: 'center', transform: `translateY(-50%) scale(${0.92 + 0.14 * cresce})`}}>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 78, color: COR.noite, letterSpacing: '-0.02em'}}>Comente</div>
        <div style={{display: 'inline-block', marginTop: 16, fontFamily: PLAYFAIR, fontStyle: 'italic', fontSize: 132, color: COR.noite,
          background: COR.pessego, padding: '0 .22em .06em', borderRadius: 12, transform: 'rotate(-1.2deg)'}}>QUERO</div>
        <div style={{fontFamily: INTER, fontWeight: 500, fontSize: 46, color: COR.noite, marginTop: 26}}>e eu te explico como conduzo isso<br />na Consultoria Sleepy</div>
      </div>
    </AbsoluteFill>
  );
};

export const MaduAcolher2 = ({dados}) => {
  const G = criaG(dados), Q = criaQ(dados);
  const {t} = useTempo();
  const fimFala = dados.duracao;
  // trechos em tela dividida (o resto é tela cheia). A Madu segura uma boneca em pé no peito: legenda e CTA da tela cheia descem
  const DIVIDIDA = [
    [0, G('Se o medo')],   // calar o choro · acolher no berço · protestar · choro acolhido
  ].map(([a, b], i) => [i === 0 ? -1 : a - TRANS, b - TRANS - 0.05]);
  const modo = (s) => Math.max(0, ...DIVIDIDA.map(([a, b]) =>
    interpolate(s, [a, a + TRANS, b, b + TRANS], [0, 1, 1, 0], {...clamp, easing: Easing.inOut(Easing.cubic)})));
  const m = modo(t);
  const cta = G('Comente');
  const fechamento = Math.min(Q('Sleepy.').fim + 0.25, fimFala - 0.1);
  // Sarah 20/10: só bebês chorando; a mãe no berço (7884188) e os bebês chorando do Reel de 14/10 reaproveitados com a liberação dela
  const APOIO = [
    {em: 0, video: 'pexels-6391705.mp4', desce: -15, de: 0.5},                                 // calar o choro: criança chorando
    {em: G('Acolher') - 0.1, video: 'pexels-7884188.mp4', desce: 700, de: 1},              // acolher: mão no filho, no berço
    {em: G('Ele pode') - 0.1, video: 'foto-6849307.mp4', desce: 80, alt: 1100, de: 0},     // protestar diante da mudança: chorando no berço
    {em: G('Choro acolhido') - 0.1, video: 'pexels-6623002.mp4', desce: 500, de: 1},       // choro acolhido: adulto ao lado do bebê que chora
  ];
  const mascara = `linear-gradient(180deg, #000 0px, #000 ${JUNCAO - 70}px, transparent ${JUNCAO + 120}px)`;
  return (
    <AbsoluteFill style={{background: COR.nevoa}}>
      <Pessoa cortes={dados.cortes} duracao={fimFala} modo={modo} cta={cta} />
      {/* alto da tela dividida: desce como cortina e some por transparência sobre a Madu (sem faixa, sem linha) */}
      <AbsoluteFill style={{transform: `translateY(${-(1 - m) * 1080}px)`, WebkitMaskImage: mascara, maskImage: mascara}}>
        {m > 0.01 && <Apoio lista={APOIO} />}
      </AbsoluteFill>
      <Legenda grupos={dados.grupos} modo={modo} lettering={LETTERING(G)} oculta={(s) => s >= cta - 0.05} />
      <Chamada inicio={cta - 0.05} fim={fechamento} />
      <Fechamento inicio={fechamento} />
    </AbsoluteFill>
  );
};

export const DURACAO_MADU_ACOLHER2 = (dados) => dados.duracao + 1.2;
export {COR, INTER, PLAYFAIR, JUNCAO, VIDEO_Y_DIV, A};
