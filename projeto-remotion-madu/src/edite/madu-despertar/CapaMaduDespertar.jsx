// Capa do Reel "Nem todo despertar é fome" (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo.
// Modelo aprovado: capas do "Acolher o choro" (14/10) e do lote 20/10. Gancho = o tema do vídeo em frase inteira;
// imagem de cima = foto da filha da Madu no berço, enviada pela Sarah em 20/10 (antes: bebês do Pexels; Guia tirado da capa a pedido dela);
// Madu embaixo com o fundo real (quadro 9280 · 3,0 s, opção 1 escolhida por ela).
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduDespertar.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9280-3.0': 652, '9283-10.6': 624, '9279-55.0': 659};
const ROSTO_Y = 1150;  // Sarah 20/10: Madu mais baixa
const GANCHO_Y = 760;
const GANCHOS = {
  despertar: [['Nem todo despertar'], 'é fome'],
};

// imagem de cima (Sarah 20/10: nada de mulher de olho fechado; mãe acordada com o filho de madrugada)
const TOPOS = {
  // Sarah 20/10: sem o Guia na capa; em cima, um bebê menino chorando (rosto centrado, olhos abaixo de y 285, dentro do recorte 4:5)
  '20541804': {img: 'choro-20541804.jpg', left: 0, top: -417, width: 1080, height: 1620},
  '34456069': {img: 'choro-34456069.jpg', left: -38, top: -321, width: 1190, height: 1488},
  '7973656': {img: 'choro-7973656.jpg', left: -84, top: -237, width: 1333, height: 2000},
  '3845455': {img: 'choro-3845455.jpg', left: 0, top: -404, width: 1080, height: 1620},
  // Sarah 20/10: "seria a opção 03, mas esse bebê está muito pequeno" → bebês mais velhos, deitado/no berço
  '6392811': {img: 'choro-6392811.jpg', left: -586, top: -584, width: 1904, height: 2856},
  '7491215': {img: 'choro-7491215.jpg', left: -175, top: -640, width: 1442, height: 2163},
  '7938222': {img: 'choro-7938222.jpg', left: -6, top: -608, width: 1092, height: 1636},
  // Sarah 20/10: "coloque essa foto da filha da Madu (aproxime mais para ver o rostinho dela)" — foto enviada por ela, no berço
  'filha': {img: 'filha-madu-berco.jpg', left: -348, top: -755, width: 2208, height: 2944},  // ×2,3: rosto x 425–655, y 395–625
};

export const CapaMaduDespertar = ({madu = '9280-3.0', gancho = 'despertar', topo = 'filha'}) => { // Sarah 20/10: foto da filha da Madu
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
