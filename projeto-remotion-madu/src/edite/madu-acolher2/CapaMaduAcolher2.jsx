// Capa do Reel "Acolher o choro" regravado (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo.
// Gancho = frase inteira dita no vídeo ("Choro acolhido não é abandono"); em cima, criança chorando (aprovadas para este vídeo:
// Pexels 6391705 e 6623002); degradê branco atrás da frase; Madu embaixo com o fundo real. Opções para a Sarah escolher vendo.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduAcolher2.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9285-3.5': 673, '9288-62.0': 703, '9291-3.0': 715};
const ROSTO_Y = 1150;  // Sarah 20/10: Madu mais baixa
const GANCHO_Y = 760;
const GANCHOS = {
  acolhido: [['Choro acolhido'], 'não é abandono'],
};

// imagem de cima (Sarah 20/10: nada de mulher de olho fechado; mãe acordada com o filho de madrugada)
const TOPOS = {
  '6391705': {img: 'topo-6391705.jpg', left: 0, top: 0, width: 1080, height: 1920},       // criança chorando (rosto y ≈ 230–640, olhos dentro do 4:5)
  '6623002': {img: 'topo-6623002.jpg', left: -550, top: -1000, width: 1728, height: 3072}, // bebê chorando no chão (rosto y ≈ 350–650)
};

export const CapaMaduAcolher2 = ({madu = '9285-3.5', gancho = 'acolhido', topo = '6391705'}) => {
  const maduY = ROSTO_Y - QUADROS[madu];
  const [linhas, destaque] = GANCHOS[gancho];
  const mascara = 'linear-gradient(180deg, #000 0px, #000 700px, transparent 900px)';
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        <Img src={staticFile(A(`assets/capa/${TOPOS[topo].img}`))} style={{position: 'absolute', left: TOPOS[topo].left, top: TOPOS[topo].top, width: TOPOS[topo].width, height: TOPOS[topo].height}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 640, height: 560,
        background: 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.93) 28%, rgba(255,255,255,.93) 72%, rgba(255,255,255,0) 100%)'}} />
      <div style={{position: 'absolute', left: 108, right: 108, top: GANCHO_Y, textAlign: 'center'}}>
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
