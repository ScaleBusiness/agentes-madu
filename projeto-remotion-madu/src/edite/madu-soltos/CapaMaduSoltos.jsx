// Capa do Reel "Por dentro da Consultoria" (Madu · bastidor gravado em 29/09, editado em 21/10). Arquivo à parte, nunca o 1º quadro do vídeo.
// Sarah 21/10: no estilo do próprio vídeo — a Madu inteira na mesa (fundo real), "Por dentro da Consultoria Sleepy" no alto
// e o título com "plano de sono" em destaque. Tudo dentro do recorte 4:5 do perfil (y 285–1635). Opções de quadro da Madu.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduSoltos.jsx';

const nevoa = (a) => `rgba(238,246,251,${a})`;
const BRILHO = '0 0 18px rgba(255,255,255,.95), 0 0 34px rgba(255,255,255,.8), 0 0 60px rgba(255,255,255,.55)';
// quadros da Madu (take-tempo) → topo do rosto no bruto (Vision); a Madu desce até o rosto começar em ROSTO_Y
const QUADROS = {'8872-35.0': 627, '8872-66.0': 661, '8875-15.5': 653};
const ROSTO_Y = 820;

const Marca = ({children, tam}) => (
  <div style={{display: 'inline-block', fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: tam, lineHeight: 1.08, whiteSpace: 'nowrap',
    color: COR.noite, background: COR.pessego, padding: '0 .2em .07em', borderRadius: 12, transform: 'rotate(-1.2deg)'}}>{children}</div>
);

export const CapaMaduSoltos = ({madu = '8872-35.0'}) => {
  const desce = ROSTO_Y - QUADROS[madu];
  return (
    <AbsoluteFill style={{background: COR.nevoa}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: desce, width: 1080, height: 1920}} />
      {/* névoa clara no alto: o mesmo letreiro do vídeo, sem faixa dura */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 0, height: desce + 560,
        background: `linear-gradient(180deg, ${nevoa(1)} 0px, ${nevoa(1)} ${desce}px, ${nevoa(0.9)} ${desce + 160}px, ${nevoa(0.5)} ${desce + 380}px, ${nevoa(0)} ${desce + 560}px)`}} />
      <div style={{position: 'absolute', left: 90, right: 90, top: 330, textAlign: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 70, letterSpacing: '-0.02em', color: COR.noite, lineHeight: 1.1}}>Por dentro da</div>
        <div style={{marginTop: 12}}><Marca tam={92}>Consultoria Sleepy</Marca></div>
      </div>
      {/* título sobre o peito/mesa, abaixo do queixo, com "plano de sono" em destaque */}
      <div style={{position: 'absolute', left: 90, right: 90, top: 1290, textAlign: 'center'}}>
        <div style={{fontFamily: INTER, fontWeight: 800, fontSize: 76, letterSpacing: '-0.02em', color: COR.noite, lineHeight: 1.1, textShadow: BRILHO}}>Seu primeiro</div>
        <div style={{marginTop: 14}}><Marca tam={104}>plano de sono</Marca></div>
      </div>
    </AbsoluteFill>
  );
};
