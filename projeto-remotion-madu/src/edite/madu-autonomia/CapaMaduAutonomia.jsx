// Capa do Reel "Autonomia" (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo.
// Gancho = frase inteira dita no vídeo ("Querer que seu filho durma com autonomia não é falta de amor"); em cima, mãe e filha
// (as mesmas imagens do vídeo); degradê branco atrás da frase; Madu embaixo com o fundo real. Opções para a Sarah escolher vendo.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduAutonomia.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9308-2.0': 662, '9307-5.0': 651, '9303-27.0': 687};
const ROSTO_Y = 1150;  // Sarah 20/10: Madu mais baixa
const GANCHO_Y = 680;
const GANCHOS = {
  amor: [['Querer que seu filho', 'durma com autonomia', 'não é'], 'falta de amor'],
};

// imagem de cima (Sarah 20/10: nada de mulher de olho fechado; mãe acordada com o filho de madrugada)
const TOPOS = {
  '4347500': {img: 'foto-4347500.jpg', left: -90, top: 20, width: 1400, height: 934},    // bebê deitado no berço, calmo (foto Pexels)
  '7938218': {img: 'foto-7938218.jpg', left: 0, top: 60, width: 1080, height: 1620},     // criança em pé no berço, luz de noite (foto Pexels)
};

export const CapaMaduAutonomia = ({madu = '9308-2.0', gancho = 'amor', topo = '4347500'}) => {
  const maduY = ROSTO_Y - QUADROS[madu];
  const [linhas, destaque] = GANCHOS[gancho];
  const mascara = 'linear-gradient(180deg, #000 0px, #000 700px, transparent 900px)';
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        {/* fundo da própria foto, desfocado: a foto menor que a tela nunca deixa faixa vazia */}
        <Img src={staticFile(A(`assets/capa/${TOPOS[topo].img}`))} style={{position: 'absolute', left: 0, top: 0, width: 1080, height: 1100, objectFit: 'cover', filter: 'blur(40px)', transform: 'scale(1.2)'}} />
        <Img src={staticFile(A(`assets/capa/${TOPOS[topo].img}`))} style={{position: 'absolute', left: TOPOS[topo].left, top: TOPOS[topo].top, width: TOPOS[topo].width, height: TOPOS[topo].height}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 520, height: 720,
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
