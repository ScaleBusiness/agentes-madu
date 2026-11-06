// Capa do Reel "Dormir no peito" (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo.
// Gancho = frase inteira dita no vídeo ("Nenhuma dessas ajudas é um hábito ruim"); em cima, mãe amamentando no colo
// (as mesmas imagens do vídeo); degradê branco atrás da frase; Madu embaixo com o fundo real. Opções para a Sarah escolher vendo.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduPeito.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9295-2.5': 631, '9296-3.5': 649, '9299-24.0': 666};
const ROSTO_Y = 1150;  // Sarah 20/10: Madu mais baixa
const GANCHO_Y = 760;
const GANCHOS = {
  habito: [['Nenhuma dessas ajudas', 'é um'], 'hábito ruim'],
};

// imagem de cima (Sarah 20/10: nada de mulher de olho fechado; mãe acordada com o filho de madrugada)
const TOPOS = {
  // a mesma mãe do vídeo (Sarah 21/10: "pode usar essa imagem que está no vídeo"): quadro alto, então a frase e a Madu descem
  '7508616': {img: 'topo-7508616.jpg', left: 0, top: -380, width: 1080, height: 1920, ganchoY: 800, rostoY: 1180, mascara: [770, 950], degrade: 680},  // testa da mãe em y 292 (dentro do 4:5); bebê inteiro acima da frase; frase acima da testa da Madu
  '27175921': {img: 'foto-27175921.jpg', left: 0, top: 60, width: 1150, height: 767},   // mãe amamentando, rosto dela e do bebê inteiros (foto Pexels)
  '10956985': {img: 'foto-10956985.jpg', left: 0, top: 40, width: 1080, height: 1620},   // close do bebê mamando (foto Pexels)
};

export const CapaMaduPeito = ({madu = '9295-2.5', gancho = 'habito', topo = '27175921'}) => {
  const T = TOPOS[topo];
  const maduY = (T.rostoY || ROSTO_Y) - QUADROS[madu];
  const [linhas, destaque] = GANCHOS[gancho];
  const [m0, m1] = T.mascara || [700, 900];
  const mascara = `linear-gradient(180deg, #000 0px, #000 ${m0}px, transparent ${m1}px)`;
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        {/* fundo da própria foto, desfocado: a foto menor que a tela nunca deixa faixa vazia */}
        <Img src={staticFile(A(`assets/capa/${TOPOS[topo].img}`))} style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1100, objectFit: 'cover', filter: 'blur(40px)', transform: 'scale(1.2)'}} />
        <Img src={staticFile(A(`assets/capa/${TOPOS[topo].img}`))} style={{position: 'absolute', left: TOPOS[topo].left, top: TOPOS[topo].top, width: TOPOS[topo].width, height: TOPOS[topo].height}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: T.degrade || 640, height: 560,
        background: 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.93) 28%, rgba(255,255,255,.93) 72%, rgba(255,255,255,0) 100%)'}} />
      <div style={{position: 'absolute', left: 108, right: 108, top: T.ganchoY || GANCHO_Y, textAlign: 'center'}}>
        {linhas.map((l) => (
          <div key={l} style={{fontFamily: INTER, fontWeight: 800, fontSize: 74, lineHeight: 1.1, letterSpacing: '-0.02em', color: COR.noite}}>{l}</div>
        ))}
        <div style={{display: 'inline-block', marginTop: 12, fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: destaque.length > 14 ? 84 : 100, lineHeight: 1.1, whiteSpace: 'nowrap',
          color: COR.noite, background: COR.pessego, padding: '0 .2em .06em', borderRadius: 12, transform: 'rotate(-1.2deg)'}}>
          {destaque}</div>
      </div>
    </AbsoluteFill>
  );
};
