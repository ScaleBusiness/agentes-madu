// Capa do Reel "Ajuda às 3h" (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo (playbook da Madu).
// Modelo aprovado: capa do "Acolher o choro" (14/10) e do "Dia de soneca ruim" (20/10). Gancho com a frase inteira dita no vídeo;
// imagem coerente com o gancho (mãe acordada de madrugada com o filho; a do despertador foi reprovada: olho fechado); degradê branco atrás da frase; a frase longe da testa da Madu;
// quadro da Madu em opções (`madu`), a Sarah escolhe vendo. Imagem do tema em cima, a Madu embaixo com o fundo real.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduAjuda3h.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9273-2.2': 766, '9273-5.6': 778, '9273-22.4': 787, '9278-17.2': 809};
const ROSTO_Y = 1150;  // Sarah 20/10: Madu mais baixa
const GANCHO_Y = 730;
const GANCHOS = {
  revezamento: [['Às 3 da manhã', 'não tem'], 'revezamento'],
  levanta: [['Às 3 da manhã,'], 'quem levanta é você'],
};

// imagem de cima (Sarah 20/10: nada de mulher de olho fechado; mãe acordada com o filho de madrugada)
const TOPOS = {
  '33321456': {left: -40, top: -80, width: 1120, height: 1680},    // mãe com o bebê bocejando no quarto escuro
  '7938237': {left: 0, top: -600, width: 1080, height: 1618},    // mãe no berço com o filho, luzinhas da noite
};

export const CapaMaduAjuda3h = ({madu = '9273-2.2', gancho = 'levanta', topo = '33321456'}) => { // Sarah 20/10: opção 3 (bebê bocejando + "quem levanta é você")
  const maduY = ROSTO_Y - QUADROS[madu];
  const [linhas, destaque] = GANCHOS[gancho];
  const mascara = 'linear-gradient(180deg, #000 0px, #000 700px, transparent 900px)';
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        <Img src={staticFile(A(`assets/capa/noite-${topo}.jpg`))} style={{position: 'absolute', ...TOPOS[topo]}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 610, height: 560,
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
