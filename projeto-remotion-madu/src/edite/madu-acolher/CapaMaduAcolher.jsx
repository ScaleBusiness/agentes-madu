// Capa do Reel "Acolher o choro" (Madu · Edite Pro, 14/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo (playbook da Madu).
// Sarah 14/10: gancho com a frase inteira ("Você não precisa deixar seu filho chorando"); criança chorando (foto Pexels 6849307,
// escolhida por ela); bebê mais alto; degradê branco no meio para destacar a frase (contraste); a frase nunca sobre a testa da Madu;
// outro quadro da Madu (opções em `madu`, ela escolhe vendo).
// Imagem do tema em cima, a Madu embaixo com o fundo real, o gancho na junção: Inter 800 + Playfair itálico sobre Pêssego.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduAcolher.jsx';

// quadros da Madu: topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em y 1090 (cabelo ~980, abaixo da frase)
const QUADROS = {'1.2': 407, '29.6': 353, '33': 338, '37.9': 391, '59': 409};
const ROSTO_Y = 1090;
const GANCHO_Y = 650;   // frase no degradê branco, entre o bebê (rosto em y 238–443) e o cabelo da Madu

export const CapaMaduAcolher = ({madu = '37.9'}) => { // Sarah 14/10: opção 3 (quadro 37,9 s)
  const maduY = ROSTO_Y - QUADROS[madu];
  const mascara = 'linear-gradient(180deg, #000 0px, #000 600px, transparent 780px)';
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        <Img src={staticFile(A('assets/capa/crianca-chorando.jpg'))} style={{position: 'absolute', left: -110, top: -130, width: 1440, height: 960}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 500, height: 520,
        background: 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.93) 30%, rgba(255,255,255,.93) 70%, rgba(255,255,255,0) 100%)'}} />
      <div style={{position: 'absolute', left: 108, right: 108, top: GANCHO_Y, textAlign: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 74, lineHeight: 1.1, letterSpacing: '-0.02em', color: COR.noite}}>
          Você não precisa deixar</div>
        <div style={{display: 'inline-block', marginTop: 12, fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: 100, lineHeight: 1.1,
          color: COR.noite, background: COR.pessego, padding: '0 .2em .06em', borderRadius: 12, transform: 'rotate(-1.2deg)'}}>
          seu filho chorando</div>
      </div>
    </AbsoluteFill>
  );
};
