// Capa do Reel "Dia de soneca ruim" (Madu · Edite Pro, lote 20/10/2026). Arquivo à parte, nunca o 1º quadro do vídeo (playbook da Madu).
// Modelo aprovado: capa do "Acolher o choro" (14/10). Gancho com a frase inteira dita no vídeo; criança coerente com o gancho
// (cansada e chorando, Pexels 6264268, aprovado pela Sarah em 20/10); degradê branco atrás da frase (contraste); a frase longe da testa da Madu;
// quadro da Madu em opções (`madu`), a Sarah escolhe vendo. Imagem do tema em cima, a Madu embaixo com o fundo real.
import React from 'react';
import {AbsoluteFill, Img, staticFile} from 'remotion';
import {COR, INTER, PLAYFAIR, A} from './MaduSoneca.jsx';

// quadros da Madu (take-tempo): topo do rosto no bruto (Vision) → a Madu desce até o rosto começar em ROSTO_Y
// (o queixo fica dentro do recorte 4:5 do perfil, y 285–1635; o cabelo, abaixo da frase)
const QUADROS = {'9269-3.2': 711, '9269-19.0': 703, '9313-10.4': 603, '9313-2.6': 599};
const ROSTO_Y = 1060;
const GANCHO_Y = 560;
const GANCHOS = {
  cansaco: [['Mais cansaço', 'não significa'], 'mais sono'],
  sonecas: [['Seu filho dormiu mal'], 'as sonecas?'],
};

export const CapaMaduSoneca = ({madu = '9313-10.4', gancho = 'cansaco'}) => { // Sarah 20/10: opção 3 (quadro 9313 · 10,4 s)
  const maduY = ROSTO_Y - QUADROS[madu];
  const [linhas, destaque] = GANCHOS[gancho];
  const mascara = 'linear-gradient(180deg, #000 0px, #000 560px, transparent 760px)';
  return (
    <AbsoluteFill style={{background: COR.branco}}>
      <Img src={staticFile(A(`assets/capa/madu-${madu}.png`))} style={{position: 'absolute', left: 0, top: maduY, width: 1080, height: 1920}} />
      <AbsoluteFill style={{WebkitMaskImage: mascara, maskImage: mascara}}>
        {/* criança cansada chorando: rosto em x 380–701, y 199–521 nesta escala (olhos dentro do recorte 4:5, que começa em y 285) */}
        <Img src={staticFile(A('assets/capa/crianca-cansada.jpg'))} style={{position: 'absolute', left: -103, top: 0, width: 1300, height: 731}} />
      </AbsoluteFill>
      {/* degradê branco longo atrás da frase (sem borda, sem faixa dura) */}
      <div style={{position: 'absolute', left: 0, right: 0, top: 440, height: 560,
        background: 'linear-gradient(180deg, rgba(255,255,255,0) 0%, rgba(255,255,255,.93) 28%, rgba(255,255,255,.93) 72%, rgba(255,255,255,0) 100%)'}} />
      <div style={{position: 'absolute', left: 108, right: 108, top: GANCHO_Y, textAlign: 'center'}}>
        {linhas.map((l) => (
          <div key={l} style={{fontFamily: INTER, fontWeight: 800, fontSize: 74, lineHeight: 1.1, letterSpacing: '-0.02em', color: COR.noite}}>{l}</div>
        ))}
        <div style={{display: 'inline-block', marginTop: 12, fontFamily: PLAYFAIR, fontStyle: 'italic', fontWeight: 400, fontSize: 100, lineHeight: 1.1,
          color: COR.noite, background: COR.pessego, padding: '0 .2em .06em', borderRadius: 12, transform: 'rotate(-1.2deg)'}}>
          {destaque}</div>
      </div>
    </AbsoluteFill>
  );
};
